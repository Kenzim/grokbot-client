"""ChatSession — messaging interface to one agent + session."""
from __future__ import annotations

import time
import uuid
from typing import TYPE_CHECKING, Any

from grokbot._svc import GB, t
from grokbot.errors import RefusalError
from grokbot.models import SendReceipt, SendStatus, TranscriptPage

if TYPE_CHECKING:
    from grokbot.client import GrokBotClient


class ChatSession:
    """Obtained via `client.chat(agent_id, session_id=None)`.

    If `session_id` is omitted it is lazily resolved to the agent's MAIN session.
    """

    def __init__(
        self, client: GrokBotClient, agent_id: str, session_id: str | None = None
    ) -> None:
        self._client = client
        self.agent_id = agent_id
        self.session_id = session_id

    async def _ensure_session(self) -> str:
        if self.session_id is not None:
            return self.session_id
        sessions = await self._client.agents.sessions(self.agent_id)
        main = next((s for s in sessions if s.kind == "MAIN"), None)
        chosen = main or (sessions[0] if sessions else None)
        # Live 0.51.0: ListGrokBotAgentSessions is often empty; the default
        # transcript is the empty session_id string.
        self.session_id = chosen.session_id if chosen else ""
        return self.session_id

    async def send(
        self,
        text: str,
        *,
        rich_text: str | None = None,
        reply_to_id: str | None = None,
        attachments: list[str] | None = None,
        fork: bool = False,
        message_id: str | None = None,
    ) -> SendReceipt:
        sid = await self._ensure_session()
        mid = message_id or str(uuid.uuid4())
        now = int(time.time() * 1000)
        req = t.SendGrokBotUserMessageRequest(
            agent_id=self.agent_id,
            message_id=mid,
            text=text,
            sent_at_ms=now,
            is_fork=fork,
            source=t.GROK_BOT_CLIENT_SURFACE_DESKTOP,
            session_id=sid,
        )
        if rich_text:
            req.rich_text = rich_text
        if reply_to_id:
            req.reply_to_id = reply_to_id
        if attachments:
            req.attachment_paths.extend(attachments)
            req.attachment_names.extend(attachments)
        resp = await self._client.unary(GB, "SendGrokBotUserMessage", req)
        if resp.HasField("refusal") and (resp.refusal.failure_code or resp.refusal.message):
            raise RefusalError(
                resp.refusal.message or "send refused",
                failure_code=resp.refusal.failure_code,
            )
        receipt = SendReceipt.from_pb2(mid, resp)
        if receipt.delivery == "REFUSED":
            raise RefusalError("send refused", failure_code="REFUSED")
        return receipt

    async def status(self, message_id: str) -> SendStatus:
        sid = await self._ensure_session()
        resp = await self._client.unary(
            GB,
            "GetGrokBotSendStatus",
            t.GetGrokBotSendStatusRequest(
                agent_id=self.agent_id, message_id=message_id, session_id=sid
            ),
        )
        return SendStatus.from_pb2(message_id, resp)

    async def interrupt(self, reason: str = "user") -> bool:
        sid = await self._ensure_session()
        resp = await self._client.unary(
            GB,
            "InterruptGrokBotAgentRun",
            t.InterruptGrokBotAgentRunRequest(
                agent_id=self.agent_id, reason=reason, session_id=sid
            ),
        )
        return bool(resp.had_active_run)

    async def draft(
        self,
        entry_id: str,
        *,
        email: dict[str, Any] | None = None,
        slack: dict[str, Any] | None = None,
    ) -> bool:
        """Send an email or Slack draft (`SendGrokBotDraft`). Exactly one of `email`/`slack`."""
        if bool(email) == bool(slack):
            raise ValueError("draft() requires exactly one of email= or slack=")
        sid = await self._ensure_session()
        req = t.SendGrokBotDraftRequest(
            agent_id=self.agent_id, entry_id=entry_id, session_id=sid
        )
        if email:
            msg = t.GrokBotEmailDraft(
                to=list(email.get("to") or []),
                cc=list(email.get("cc") or []),
                subject=email.get("subject") or "",
                body=email.get("body") or "",
            )
            sender = email.get("from")
            if sender:
                setattr(msg, "from", sender)
            req.email.CopyFrom(msg)
        else:
            assert slack is not None
            msg = t.GrokBotSlackDraft(
                target=slack.get("target") or "",
                body=slack.get("body") or "",
            )
            if slack.get("workspace"):
                msg.workspace = slack["workspace"]
            if slack.get("thread"):
                msg.thread = slack["thread"]
            req.slack.CopyFrom(msg)
        resp = await self._client.unary(GB, "SendGrokBotDraft", req)
        _raise_refusal(resp)
        return bool(resp.accepted)

    async def discard_draft(self, entry_id: str) -> None:
        sid = await self._ensure_session()
        resp = await self._client.unary(
            GB,
            "DiscardGrokBotDraft",
            t.DiscardGrokBotDraftRequest(
                agent_id=self.agent_id, entry_id=entry_id, session_id=sid
            ),
        )
        _raise_refusal(resp)

    async def react(self, entry_id: str, emoji: str) -> None:
        sid = await self._ensure_session()
        resp = await self._client.unary(
            GB,
            "ReactToGrokBotMessage",
            t.ReactToGrokBotMessageRequest(
                agent_id=self.agent_id, entry_id=entry_id, emoji=emoji, session_id=sid
            ),
        )
        _raise_refusal(resp)

    async def history(
        self, *, before_seq: int | None = None, limit: int = 100, generation: int | None = None
    ) -> TranscriptPage:
        sid = await self._ensure_session()
        req = t.ListGrokBotTranscriptEntriesRequest(
            agent_id=self.agent_id, session_id=sid, limit=limit
        )
        if before_seq is not None:
            req.before_seq = before_seq
        if generation is not None:
            req.generation = generation
        resp = await self._client.unary(GB, "ListGrokBotTranscriptEntries", req)
        return TranscriptPage.from_pb2(resp)


def _raise_refusal(resp) -> None:
    if resp.HasField("refusal") and (resp.refusal.failure_code or resp.refusal.message):
        raise RefusalError(
            resp.refusal.message or "refused", failure_code=resp.refusal.failure_code
        )
