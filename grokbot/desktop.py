"""DesktopSession — account-level sandbox coordinates for VNC streaming.

The sandbox is per Cursor account, not per agent. `box`-harness agents run
inside it; `temporal` agents are cloud workflows and have no desktop.

`vnc_url` from EnsureSandBox is an HTTPS URL. The RFB websocket is derived
the same way the desktop app does (`iVt`): path query (default `/websockify`),
https→wss, copy `network_token` / `port_token`. The network token is also sent
as header `x-anyrun-network-token`.
"""
from __future__ import annotations

from typing import TYPE_CHECKING
from urllib.parse import parse_qs, urlparse, urlunparse

from grokbot._svc import GB, t
from grokbot.constants import NETWORK_TOKEN_HEADER
from grokbot.models import enum_suffix

if TYPE_CHECKING:
    from grokbot.client import GrokBotClient


def derive_vnc_connect_url(vnc_url: str, network_token: str = "") -> str:
    """HTTPS vnc_url → WSS websockify URL with token query params."""
    parsed = urlparse(vnc_url)
    qs = parse_qs(parsed.query)
    path = (qs.get("path") or ["websockify"])[0]
    if not path.startswith("/"):
        path = "/" + path
    scheme = "wss" if parsed.scheme == "https" else "ws"
    parts: list[str] = []
    for key in ("network_token", "port_token"):
        vals = qs.get(key)
        if vals:
            parts.append(f"{key}={vals[0]}")
        elif key == "network_token" and network_token:
            parts.append(f"network_token={network_token}")
    return urlunparse((scheme, parsed.netloc, path, "", "&".join(parts), ""))


class DesktopSession:
    """Obtained via `await client.desktop(wake=False)`."""

    def __init__(self, client: GrokBotClient, resp) -> None:
        self._client = client
        self._apply(resp)

    def _apply(self, resp) -> None:
        self.cluster = resp.cluster
        self.tenant_id = resp.tenant_id
        self.pod_id = resp.pod_id
        self.vnc_url = resp.vnc_url
        self.gateway_url = resp.gateway_url
        self.gateway_token = resp.gateway_token
        self.network_token = resp.network_token
        self.exec_daemon_url = resp.exec_daemon_url
        self.exec_daemon_auth_token = resp.exec_daemon_auth_token
        self.fork_vnc_base_url = resp.fork_vnc_base_url
        self.terminals_folder = resp.terminals_folder
        self.run_state = enum_suffix(
            t.SandBoxRunState, resp.run_state, "SAND_BOX_RUN_STATE_"
        )
        self.raw = resp

    @classmethod
    async def ensure(cls, client: GrokBotClient, *, wake: bool = False) -> DesktopSession:
        req = t.EnsureSandBoxRequest()
        if wake:
            req.wake = True
        resp = await client.unary(GB, "EnsureSandBox", req)
        return cls(client, resp)

    def connect_url(self) -> str:
        """WSS URL the RFB/noVNC client should open."""
        return derive_vnc_connect_url(self.vnc_url, self.network_token)

    def websocket_headers(self) -> dict[str, str]:
        headers: dict[str, str] = {}
        if self.network_token:
            headers[NETWORK_TOKEN_HEADER] = self.network_token
        if self.gateway_token:
            headers["authorization"] = f"Bearer {self.gateway_token}"
        return headers

    def fork_url(self, window_index: int) -> str:
        base = self.fork_vnc_base_url.rstrip("/")
        return f"{base}/{window_index}"

    async def window(self, index: int) -> DesktopSession:
        resp = await self._client.unary(
            GB, "EnsureSandBoxWindow", t.EnsureSandBoxWindowRequest(window_index=index)
        )
        self._apply(resp)
        return self

    async def refresh(self, *, wake: bool = False) -> None:
        req = t.EnsureSandBoxRequest()
        if wake:
            req.wake = True
        resp = await self._client.unary(GB, "EnsureSandBox", req)
        self._apply(resp)
