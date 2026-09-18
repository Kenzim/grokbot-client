"""DesktopSession — coordinates for streaming an agent's cloud desktop.

The library stops at provisioning: `EnsureSandBox` returns everything a
VNC/noVNC stack needs (vnc_url, gateway_url + token, network_token,
exec_daemon_url + auth token, fork_vnc_base_url). The host app (Forge)
renders the stream; this module just keeps the coordinates fresh.
"""
from __future__ import annotations


class DesktopSession:
    """Obtained via `await client.desktop(agent_id)`. See docs/API.md#desktopsession."""

    vnc_url: str
    gateway_url: str
    gateway_token: str
    network_token: str
    exec_daemon_url: str
    exec_daemon_auth_token: str
    run_state: object  # SandBoxRunState enum value

    def websocket_headers(self) -> dict[str, str]:
        """Auth headers for the WSS upgrade against vnc_url."""
        raise NotImplementedError

    def fork_url(self, window_index: int) -> str:
        """Base URL for a fork-desktop window."""
        raise NotImplementedError

    async def refresh(self) -> None:
        """Re-ensure the sandbox; tokens rotate on sandbox restarts."""
        raise NotImplementedError
