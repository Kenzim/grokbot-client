"""TranscriptWatcher — resilient account-wide event stream."""
from __future__ import annotations

import asyncio
import logging
import time
from collections.abc import AsyncIterator, Callable
from typing import TYPE_CHECKING, Any

from grokbot import events as ev
from grokbot._svc import GB, t
from grokbot.models import (
    TranscriptCursor,
    TranscriptEntry,
    decode_body,
    enum_suffix,
)
from grokbot.store import fetch_blobs

if TYPE_CHECKING:
    from grokbot.client import GrokBotClient

log = logging.getLogger(__name__)


async def _iter_until(stream: Any, deadline_fn: Callable[[], float | None]) -> AsyncIterator[Any]:
    """Yield frames, returning when `deadline_fn()` (monotonic ts) is reached."""
    aiter = stream.__aiter__()
    while True:
        deadline = deadline_fn()
        timeout = None
        if deadline is not None:
            timeout = deadline - time.monotonic()
            if timeout <= 0:
                return
        try:
            frame = await asyncio.wait_for(aiter.__anext__(), timeout=timeout)
        except StopAsyncIteration:
            return
        except asyncio.TimeoutError:
            return
        yield frame


WIDGET_HINTS = (
    "widget",
    "form",
    "captcha",
    "credential",
    "approval",
    "secret",
    "permission",
    "user_form",
)


def _is_widget(kind: str, body: Any) -> bool:
    k = (kind or "").lower()
    if any(h in k for h in WIDGET_HINTS) and k != "send-message":
        return True
    if isinstance(body, dict):
        typ = str(body.get("type") or body.get("kind") or "").lower()
        if any(h in typ for h in WIDGET_HINTS):
            return True
        msg = body.get("message")
        if isinstance(msg, dict) and str(msg.get("type") or "").lower() == "widget":
            return True
    return False


def _extract_text_role(body: Any, kind: str) -> tuple[str, str, float]:
    role = "unknown"
    text = ""
    ts = 0.0
    if isinstance(body, dict):
        msg = body.get("message")
        if isinstance(msg, dict) and msg.get("type") == "text":
            text = str(msg.get("content") or "")
            role = "assistant"
        else:
            text = str(body.get("content") or body.get("text") or body.get("prompt") or "")
            role = str(body.get("role") or body.get("author") or body.get("from") or role)
        for key in ("timestampMs", "ts", "timestamp", "created_at_ms", "sent_at_ms"):
            if key in body:
                try:
                    ts = float(body[key])
                    if ts > 1e12:
                        ts = ts / 1000.0
                except (TypeError, ValueError):
                    pass
                break
    elif isinstance(body, str):
        text = body
    if not role or role == "unknown":
        lk = kind.lower()
        if lk == "message" or "user" in lk:
            role = "user"
        elif lk == "send-message" or "assistant" in lk or "agent" in lk:
            role = "assistant"
    return text, role, ts


def events_from_entry(
    agent_id: str, session_id: str, entry: TranscriptEntry
) -> list[Any]:
    body = entry.body
    kind = entry.entry_kind or ""
    eid = entry.entry_id or str(entry.seq)
    if _is_widget(kind, body):
        prompt = ""
        request_id = ""
        wkind = kind or "widget"
        widget_obj: Any = None
        if isinstance(body, dict):
            msg = body.get("message")
            if isinstance(msg, dict) and isinstance(msg.get("widget"), dict):
                widget_obj = msg["widget"]
                prompt = str(widget_obj.get("prompt") or widget_obj.get("helpText") or "")
                wkind = str(widget_obj.get("type") or msg.get("type") or wkind)
            else:
                prompt = str(body.get("prompt") or body.get("text") or body.get("content") or "")
                wkind = str(body.get("type") or body.get("kind") or wkind)
            request_id = str(
                body.get("requestId") or body.get("request_id") or body.get("id") or ""
            )
        return [
            ev.WidgetRequest(
                agent_id=agent_id,
                session_id=session_id,
                entry_id=eid,
                kind=wkind,
                prompt=prompt,
                request_id=request_id,
                body=widget_obj if widget_obj is not None else body,
            )
        ]
    text, role, ts = _extract_text_role(body, kind)
    return [
        ev.Message(
            agent_id=agent_id,
            session_id=session_id,
            entry_id=eid,
            seq=entry.seq,
            text=text,
            role=role,
            ts=ts,
            entry_kind=kind,
            body=body,
        )
    ]


class TranscriptWatcher:
    """Obtained via `client.watch()`. Async iterator over typed events."""

    def __init__(
        self,
        client: GrokBotClient,
        *,
        include_unlisted_agents: bool = True,
        inline_body_max_bytes: int = 65536,
    ) -> None:
        self._client = client
        self.include_unlisted_agents = include_unlisted_agents
        self.inline_body_max_bytes = inline_body_max_bytes
        self.cursors: dict[tuple[str, str], TranscriptCursor] = {}
        self.last_seen: float = 0.0
        self._queue: asyncio.Queue[Any] = asyncio.Queue(maxsize=256)
        self._task: asyncio.Task[None] | None = None
        self._stop = asyncio.Event()
        self._callbacks: list[tuple[type, Callable]] = []

    def on(self, event_type: type, callback: Callable) -> None:
        self._callbacks.append((event_type, callback))

    def start(
        self, cursors: dict[tuple[str, str], TranscriptCursor] | None = None
    ) -> TranscriptWatcher:
        if cursors:
            self.cursors = dict(cursors)
        if self._task is None or self._task.done():
            self._stop.clear()
            self._task = asyncio.create_task(self._run_loop(), name="grokbot-watch")
        return self

    async def stop(self) -> None:
        self._stop.set()
        task = self._task
        self._task = None
        if task is not None:
            task.cancel()
            try:
                await task
            except (asyncio.CancelledError, Exception):
                pass

    async def run(self) -> None:
        async for event in self:
            for typ, cb in self._callbacks:
                if isinstance(event, typ):
                    result = cb(event)
                    if asyncio.iscoroutine(result):
                        await result

    def __aiter__(self) -> AsyncIterator[Any]:
        if self._task is None:
            self.start()
        return self._iter()

    async def _iter(self) -> AsyncIterator[Any]:
        while True:
            if self._stop.is_set() and self._queue.empty():
                return
            try:
                item = await asyncio.wait_for(self._queue.get(), timeout=0.4)
            except asyncio.TimeoutError:
                if self._task is not None and self._task.done() and self._queue.empty():
                    exc = self._task.exception() if not self._task.cancelled() else None
                    if exc:
                        raise exc
                    return
                continue
            yield item

    async def _emit(self, event: Any) -> None:
        await self._queue.put(event)

    async def _run_loop(self) -> None:
        while not self._stop.is_set():
            try:
                await self._one_stream()
            except asyncio.CancelledError:
                raise
            except Exception:
                log.exception("watch stream dropped; reconnecting")
                await asyncio.sleep(1.0)

    async def _one_stream(self) -> None:
        req = t.WatchGrokBotTranscriptsRequest(
            include_unlisted_agents=self.include_unlisted_agents,
            inline_body_max_bytes=self.inline_body_max_bytes,
        )
        req.cursors.extend(c.to_pb2() for c in self.cursors.values())
        stream = self._client.server_stream(GB, "WatchGrokBotTranscripts", req)
        deadline: float | None = None
        try:
            async for frame in _iter_until(stream, lambda: deadline):
                if self._stop.is_set():
                    return
                self.last_seen = time.monotonic()
                which = frame.WhichOneof("frame")
                if which == "connected":
                    ms = int(frame.connected.absolute_lifetime_ms or 0)
                    if ms > 0:
                        slack_ms = min(5_000, max(500, ms // 10))
                        deadline = time.monotonic() + max(1.0, (ms - slack_ms) / 1000.0)
                    continue
                if which == "heartbeat":
                    continue
                if which == "rows":
                    await self._handle_rows(frame.rows)
                elif which == "cleared":
                    c = frame.cleared
                    key = (c.agent_id, c.session_id)
                    self.cursors[key] = TranscriptCursor(
                        agent_id=c.agent_id,
                        session_id=c.session_id,
                        generation=int(c.new_generation),
                        after_updated_seq=0,
                    )
                    await self._emit(ev.StreamReset(c.agent_id, c.session_id, reason="cleared"))
                elif which == "cursor_too_old":
                    c = frame.cursor_too_old
                    await self._resync(c.agent_id, c.session_id)
                    await self._emit(
                        ev.StreamReset(c.agent_id, c.session_id, reason="cursor_too_old")
                    )
                elif which == "agent_state":
                    await self._handle_agent_state(frame.agent_state)
                elif which == "agent_state_changed":
                    ch = frame.agent_state_changed
                    await self._emit(
                        ev.AgentStateUpdate(
                            agent_id=ch.agent_id,
                            session_id="",
                            is_running=False,
                            is_composing=False,
                        )
                    )
                elif which == "computer_actions":
                    actions = list(frame.computer_actions.actions)
                    agent_id = actions[0].agent_id if actions else ""
                    await self._emit(ev.ComputerActions(agent_id=agent_id, actions=actions))
                elif which == "turn_failed":
                    f = frame.turn_failed
                    code = enum_suffix(
                        t.GrokBotTurnFailureCode, f.code, "GROK_BOT_TURN_FAILURE_CODE_"
                    )
                    await self._emit(
                        ev.TurnFailed(
                            agent_id=f.agent_id,
                            session_id=f.session_id,
                            reason=f.summary,
                            code=code,
                            turn_id=f.turn_id,
                        )
                    )
                elif which == "roster_changed":
                    r = frame.roster_changed
                    kind = enum_suffix(
                        t.GrokBotRosterChangeKind, r.kind, "GROK_BOT_ROSTER_CHANGE_KIND_"
                    )
                    await self._emit(ev.RosterChanged(kind=kind, agent_id=r.agent_id))
                    if r.agent and r.agent.agent_id:
                        # New agent: seed an empty cursor so subsequent reconnects include them.
                        sid = r.agent.viewer_session_id or ""
                        if sid:
                            key = (r.agent.agent_id, sid)
                            self.cursors.setdefault(
                                key,
                                TranscriptCursor(agent_id=r.agent.agent_id, session_id=sid),
                            )
                elif which == "box_state":
                    st = frame.box_state.state
                    run = enum_suffix(t.SandBoxRunState, st.run_state, "SAND_BOX_RUN_STATE_")
                    await self._emit(ev.BoxStateChanged(run_state=run, raw=frame.box_state))
        finally:
            aclose = getattr(stream, "aclose", None)
            if aclose is not None:
                await aclose()

    async def _handle_rows(self, rows) -> None:
        key = (rows.agent_id, rows.session_id)
        cur = self.cursors.get(key) or TranscriptCursor(
            agent_id=rows.agent_id, session_id=rows.session_id, generation=int(rows.generation)
        )
        cur.generation = int(rows.generation)
        omitted: list[str] = []
        parsed: list[TranscriptEntry] = []
        for raw in rows.entries:
            entry = TranscriptEntry.from_pb2(raw)
            if entry.body_omitted and entry.blob_hash:
                omitted.append(entry.blob_hash)
            parsed.append(entry)
            if entry.updated_seq > cur.after_updated_seq:
                cur.after_updated_seq = entry.updated_seq
        for d in rows.deletes:
            if int(d.updated_seq) > cur.after_updated_seq:
                cur.after_updated_seq = int(d.updated_seq)
        self.cursors[key] = cur
        blobs: dict[str, bytes] = {}
        if omitted:
            try:
                blobs = await fetch_blobs(self._client, omitted)
            except Exception:
                log.exception("failed to fetch omitted transcript blobs")
        for entry in parsed:
            if entry.body_omitted and entry.blob_hash and entry.blob_hash in blobs:
                entry.body_raw = blobs[entry.blob_hash]
                entry.body = decode_body(entry.body_raw)
                entry.body_omitted = False
            for event in events_from_entry(rows.agent_id, rows.session_id, entry):
                await self._emit(event)

    async def _resync(self, agent_id: str, session_id: str) -> None:
        req = t.ListGrokBotTranscriptEntriesRequest(
            agent_id=agent_id, session_id=session_id, limit=100
        )
        resp = await self._client.unary(GB, "ListGrokBotTranscriptEntries", req)
        key = (agent_id, session_id)
        cur = TranscriptCursor(
            agent_id=agent_id, session_id=session_id, generation=int(resp.generation)
        )
        for raw in resp.entries:
            entry = TranscriptEntry.from_pb2(raw)
            if entry.updated_seq > cur.after_updated_seq:
                cur.after_updated_seq = entry.updated_seq
            for event in events_from_entry(agent_id, session_id, entry):
                await self._emit(event)
        self.cursors[key] = cur

    async def _handle_agent_state(self, state) -> None:
        for live in state.live:
            await self._emit(
                ev.AgentStateUpdate(
                    agent_id=live.agent_id,
                    session_id=live.session_id,
                    is_running=bool(live.is_running),
                    is_composing=bool(live.is_composing_message),
                    live_state=live,
                )
            )
            if live.box_handoff_request_id:
                reason = live.awaiting.reason if live.HasField("awaiting") else ""
                tab = live.awaiting.tab_id if live.HasField("awaiting") else ""
                await self._emit(
                    ev.HandoffRequested(
                        agent_id=live.agent_id,
                        session_id=live.session_id,
                        request_id=live.box_handoff_request_id,
                        instruction=live.box_handoff_instruction or "",
                        reason=reason,
                        tab_id=tab,
                    )
                )
