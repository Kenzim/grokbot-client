"""ChatSession — messaging interface to one agent.

Wraps GrokBotService: SendGrokBotUserMessage (client-generated UUID
message_id makes sends idempotent), GetGrokBotSendStatus,
InterruptGrokBotAgentRun, SendGrokBotDraft, DiscardGrokBotDraft,
ReactToGrokBotMessage, ListGrokBotTranscriptEntries.
"""
from __future__ import annotations


class ChatSession:
    """Obtained via `client.chat(agent_id)`. See docs/API.md#chatsession."""

    def __init__(self, agent_id: str) -> None:
        self.agent_id = agent_id

    async def send(
        self,
        text: str,
        *,
        rich_text: str | None = None,
        reply_to_id: str | None = None,
        attachments: list[str] | None = None,
        fork: bool = False,
    ): ...  # -> SendReceipt

    async def status(self, message_id: str): ...  # -> SendStatus
    async def interrupt(self) -> None: ...
    async def draft(self, text: str) -> None: ...
    async def discard_draft(self) -> None: ...
    async def react(self, entry_id: str, emoji: str) -> None: ...
    async def history(self, *, cursor=None, limit: int = 100): ...  # -> TranscriptPage
