"""GrokBotClient — transport + service access. See docs/API.md."""
from __future__ import annotations

from grokbot.auth import AuthStrategy


class GrokBotClient:
    """Async client for the Grok Bot backend (Connect-RPC, protobuf payloads).

    Usage:
        async with GrokBotClient() as client:
            agents = await client.agents.list()
    """

    def __init__(
        self,
        auth: AuthStrategy | None = None,
        base_url: str = "https://api2.cursor.sh",
        timeout: float = 30.0,
        client_version: str = "0.51.0",
        ghost_mode: bool = True,
    ) -> None:
        raise NotImplementedError

    @property
    def agents(self):  # -> AgentAPI
        raise NotImplementedError

    def chat(self, agent_id: str):  # -> ChatSession
        raise NotImplementedError

    @property
    def widgets(self):  # -> WidgetAPI
        raise NotImplementedError

    async def desktop(self, agent_id: str):  # -> DesktopSession
        raise NotImplementedError

    def watch(self, *, include_unlisted: bool = True, inline_body_max_bytes: int = 65536):
        # -> TranscriptWatcher
        raise NotImplementedError

    async def get_me(self):  # -> Account
        raise NotImplementedError

    async def close(self) -> None:
        raise NotImplementedError
