"""Widget / approval helpers — the "solve this captcha" loop.

Widgets arrive as transcript entries and surface through the watcher as
`events.WidgetRequest`. Answers go back via:

- RespondGrokBotWidget(agent_id, entry_id, value, session_id)
- DismissGrokBotWidget
- SubmitGrokBotUserForm / SubmitGrokBotSecret
- ResolveGrokBotAutoReviewApproval / ResolveGrokBotLocalToolPermission /
  ResolveGrokBotVirtualCardApproval
"""
from __future__ import annotations


class WidgetAPI:
    """Accessed via `client.widgets`. See docs/API.md#widgetapi."""

    async def respond(self, widget, value: str) -> None: ...
    async def dismiss(self, widget) -> None: ...
    async def submit_form(self, widget, values: dict[str, str]) -> None: ...
    async def submit_secret(self, widget, value: str) -> None: ...
    async def resolve_approval(self, widget, approved: bool) -> None: ...
