"""GrokBotClient — Connect-RPC transport + service accessors."""
from __future__ import annotations

import json
import struct
import uuid
from collections.abc import AsyncIterator
from typing import Any

import httpx
from google.protobuf import message_factory
from google.protobuf.message import Message

from grokbot import auth as auth_mod
from grokbot.constants import (
    CLIENT_TYPE,
    CLIENT_VERSION,
    DEFAULT_BACKEND,
    USER_AGENT,
)
from grokbot.errors import AuthError, GrokBotError, NotFoundError, StreamError, UnauthorizedError

FLAG_TRAILER = 0x02


def encode_frame(payload: bytes, flags: int = 0) -> bytes:
    return bytes([flags & 0xFF]) + struct.pack(">I", len(payload)) + payload


class FrameDecoder:
    """Incremental Connect envelope decoder (flags + 4-byte BE length + payload)."""

    def __init__(self) -> None:
        self.buf = b""

    def feed(self, chunk: bytes) -> list[tuple[int, bytes]]:
        self.buf += chunk
        out: list[tuple[int, bytes]] = []
        while len(self.buf) >= 5:
            flags = self.buf[0]
            length = struct.unpack(">I", self.buf[1:5])[0]
            if len(self.buf) < 5 + length:
                break
            body = self.buf[5 : 5 + length]
            self.buf = self.buf[5 + length :]
            out.append((flags, body))
        return out


def _parse_connect_error(resp: httpx.Response) -> tuple[str | None, str]:
    text = resp.text or ""
    try:
        data = resp.json()
    except Exception:
        return None, text[:500]
    if not isinstance(data, dict):
        return None, text[:500]
    err = data.get("error") if isinstance(data.get("error"), dict) else data
    if not isinstance(err, dict):
        return None, text[:500]
    code = err.get("code")
    msg = err.get("message") or err.get("msg") or text[:500]
    return (str(code) if code else None), str(msg)


def _raise_for_status(resp: httpx.Response, rpc: str) -> None:
    if resp.status_code == 200:
        return
    code, msg = _parse_connect_error(resp)
    detail = f"{rpc} -> HTTP {resp.status_code}" + (f" [{code}]" if code else "") + f": {msg}"
    if resp.status_code == 401 or code == "unauthenticated":
        raise UnauthorizedError(detail, code=code or "unauthenticated")
    if resp.status_code == 404 or code == "not_found":
        raise NotFoundError(detail, code=code or "not_found")
    raise GrokBotError(detail, code=code)


def _service_name(service_desc: Any) -> str:
    return service_desc.full_name


class GrokBotClient:
    """Async client for the Grok Bot backend (Connect-RPC, protobuf payloads).

    Usage::

        async with GrokBotClient() as client:
            me = await client.get_me()
    """

    def __init__(
        self,
        auth: auth_mod.AuthStrategy | None = None,
        base_url: str = DEFAULT_BACKEND,
        timeout: float = 30.0,
        client_version: str = CLIENT_VERSION,
        ghost_mode: bool = True,
        http: httpx.AsyncClient | None = None,
    ) -> None:
        self.auth = auth if auth is not None else auth_mod.auto()
        self.base_url = base_url.rstrip("/")
        self.client_version = client_version
        self.ghost_mode = ghost_mode
        self._own_http = http is None
        self._http = http or httpx.AsyncClient(timeout=httpx.Timeout(timeout, read=120.0))
        self._agents = None
        self._widgets = None
        self._secrets = None

    async def __aenter__(self) -> GrokBotClient:
        return self

    async def __aexit__(self, *exc: object) -> None:
        await self.close()

    async def close(self) -> None:
        if self._own_http:
            await self._http.aclose()

    def _headers(
        self, token: str, streaming: bool, request_id: str | None = None
    ) -> dict[str, str]:
        return {
            "authorization": f"Bearer {token}",
            "connect-protocol-version": "1",
            "content-type": "application/connect+proto" if streaming else "application/proto",
            "user-agent": USER_AGENT,
            "x-cursor-client-type": CLIENT_TYPE,
            "x-cursor-client-source": CLIENT_TYPE,
            "x-cursor-client-version": self.client_version,
            "x-ghost-mode": "true" if self.ghost_mode else "false",
            "x-request-id": request_id or str(uuid.uuid4()),
        }

    async def unary(self, service_desc: Any, method: str, request: Message) -> Message:
        """Call a unary RPC. `service_desc` is a protobuf ServiceDescriptor."""
        return await self._unary_with_retry(service_desc, method, request)

    async def _unary_with_retry(self, service_desc: Any, method: str, request: Message) -> Message:
        svc = _service_name(service_desc)
        rpc = f"{svc}/{method}"
        url = f"{self.base_url}/{rpc}"
        method_desc = service_desc.methods_by_name[method]
        last_unauth: UnauthorizedError | None = None
        for attempt in (0, 1):
            token = await self.auth.token()
            resp = await self._http.post(
                url,
                headers=self._headers(token, streaming=False),
                content=request.SerializeToString(),
            )
            try:
                _raise_for_status(resp, rpc)
            except UnauthorizedError as exc:
                last_unauth = exc
                if attempt == 0:
                    try:
                        await self.auth.on_unauthorized()
                    except AuthError:
                        raise UnauthorizedError(str(exc), code=exc.code) from exc
                    continue
                raise
            out = message_factory.GetMessageClass(method_desc.output_type)()
            out.ParseFromString(resp.content)
            return out
        assert last_unauth is not None
        raise last_unauth

    async def server_stream(
        self, service_desc: Any, method: str, request: Message
    ) -> AsyncIterator[Message]:
        """Call a server-streaming RPC; yields decoded response messages."""
        svc = _service_name(service_desc)
        rpc = f"{svc}/{method}"
        url = f"{self.base_url}/{rpc}"
        method_desc = service_desc.methods_by_name[method]
        payload = request.SerializeToString()
        frame = encode_frame(payload, 0)
        retried = False
        while True:
            token = await self.auth.token()
            async with self._http.stream(
                "POST", url, headers=self._headers(token, streaming=True), content=frame
            ) as resp:
                if resp.status_code != 200:
                    await resp.aread()
                    try:
                        _raise_for_status(resp, rpc)
                    except UnauthorizedError:
                        if not retried:
                            try:
                                await self.auth.on_unauthorized()
                            except AuthError as exc:
                                raise UnauthorizedError(str(exc), code="unauthenticated") from exc
                            retried = True
                            continue
                        raise
                decoder = FrameDecoder()
                async for chunk in resp.aiter_bytes():
                    for flags, body in decoder.feed(chunk):
                        if flags & FLAG_TRAILER:
                            trailer = json.loads(body or b"{}")
                            err = trailer.get("error") if isinstance(trailer, dict) else None
                            if err:
                                code = err.get("code") if isinstance(err, dict) else None
                                msg = err.get("message") if isinstance(err, dict) else str(err)
                                raise StreamError(
                                    f"{rpc} trailer error: {msg}",
                                    code=str(code) if code else None,
                                )
                            return
                        msg = message_factory.GetMessageClass(method_desc.output_type)()
                        msg.ParseFromString(body)
                        yield msg
                return

    # ── accessors ──────────────────────────────────────────────────────────

    @property
    def agents(self):
        from grokbot.agents import AgentAPI

        if self._agents is None:
            self._agents = AgentAPI(self)
        return self._agents

    def chat(self, agent_id: str, session_id: str | None = None):
        from grokbot.chat import ChatSession

        return ChatSession(self, agent_id, session_id=session_id)

    @property
    def widgets(self):
        from grokbot.widgets import WidgetAPI

        if self._widgets is None:
            self._widgets = WidgetAPI(self)
        return self._widgets

    @property
    def secrets(self):
        from grokbot.secrets import SecretsAPI

        if self._secrets is None:
            self._secrets = SecretsAPI(self)
        return self._secrets

    async def desktop(self, *, wake: bool = False):
        from grokbot.desktop import DesktopSession

        return await DesktopSession.ensure(self, wake=wake)

    async def end_handoff(
        self, agent_id: str, request_id: str, *, trigger: str = "DISMISSED"
    ) -> bool:
        from grokbot.desktop import end_box_handoff

        return await end_box_handoff(self, agent_id, request_id, trigger=trigger)

    def watch(self, *, include_unlisted_agents: bool = True, inline_body_max_bytes: int = 65536):
        from grokbot.transcripts import TranscriptWatcher

        return TranscriptWatcher(
            self,
            include_unlisted_agents=include_unlisted_agents,
            inline_body_max_bytes=inline_body_max_bytes,
        )

    async def get_me(self):
        from grokbot._proto.aiserver.v1 import DashboardService_pb2 as dash
        from grokbot._proto.aiserver.v1 import types_pb2 as t
        from grokbot.models import Account

        svc = dash.DESCRIPTOR.services_by_name["DashboardService"]
        resp = await self.unary(svc, "GetMe", t.GetMeRequest())
        return Account.from_pb2(resp)
