"""Widget / approval helpers — captcha, forms, secrets, approvals."""
from __future__ import annotations

from typing import TYPE_CHECKING

from grokbot._svc import GB, t
from grokbot.errors import RefusalError
from grokbot.events import WidgetRequest

if TYPE_CHECKING:
    from grokbot.client import GrokBotClient


def _raise_refusal(resp) -> None:
    if hasattr(resp, "HasField") and resp.HasField("refusal"):
        ref = resp.refusal
        if ref.failure_code or ref.message:
            raise RefusalError(ref.message or "widget refused", failure_code=ref.failure_code)


class WidgetAPI:
    """Accessed via `client.widgets`."""

    def __init__(self, client: GrokBotClient) -> None:
        self._client = client

    async def respond(self, widget: WidgetRequest, value: str) -> None:
        resp = await self._client.unary(
            GB,
            "RespondGrokBotWidget",
            t.RespondGrokBotWidgetRequest(
                agent_id=widget.agent_id,
                entry_id=widget.entry_id,
                value=value,
                session_id=widget.session_id,
            ),
        )
        _raise_refusal(resp)

    async def dismiss(self, widget: WidgetRequest) -> None:
        resp = await self._client.unary(
            GB,
            "DismissGrokBotWidget",
            t.DismissGrokBotWidgetRequest(
                agent_id=widget.agent_id,
                entry_id=widget.entry_id,
                session_id=widget.session_id,
            ),
        )
        _raise_refusal(resp)

    async def submit_form(self, widget: WidgetRequest, values: dict[str, str]) -> None:
        req = t.SubmitGrokBotUserFormRequest(
            agent_id=widget.agent_id,
            entry_id=widget.entry_id,
            session_id=widget.session_id,
            platform=t.GROK_BOT_USER_FORM_CLIENT_PLATFORM_DESKTOP,
        )
        req.values.update(values)
        resp = await self._client.unary(GB, "SubmitGrokBotUserForm", req)
        _raise_refusal(resp)

    async def submit_secret(self, widget: WidgetRequest, value: str) -> None:
        resp = await self._client.unary(
            GB,
            "SubmitGrokBotSecret",
            t.SubmitGrokBotSecretRequest(
                agent_id=widget.agent_id,
                entry_id=widget.entry_id,
                value=value,
                session_id=widget.session_id,
            ),
        )
        _raise_refusal(resp)

    async def resolve_approval(self, widget: WidgetRequest, approved: bool) -> None:
        kind = (widget.kind or "").lower()
        request_id = widget.request_id or widget.entry_id
        if "virtual_card" in kind or "card" in kind:
            resolution = (
                t.GROK_BOT_VIRTUAL_CARD_RESOLUTION_APPROVED
                if approved
                else t.GROK_BOT_VIRTUAL_CARD_RESOLUTION_DENIED
            )
            resp = await self._client.unary(
                GB,
                "ResolveGrokBotVirtualCardApproval",
                t.ResolveGrokBotVirtualCardApprovalRequest(
                    agent_id=widget.agent_id,
                    entry_id=widget.entry_id,
                    request_id=request_id,
                    resolution=resolution,
                ),
            )
            _raise_refusal(resp)
            return
        if "permission" in kind or "local_tool" in kind:
            resolution = (
                t.GROK_BOT_LOCAL_TOOL_PERMISSION_CARD_RESOLUTION_ALLOW_ONCE
                if approved
                else t.GROK_BOT_LOCAL_TOOL_PERMISSION_CARD_RESOLUTION_DENY
            )
            resp = await self._client.unary(
                GB,
                "ResolveGrokBotLocalToolPermission",
                t.ResolveGrokBotLocalToolPermissionRequest(
                    agent_id=widget.agent_id,
                    entry_id=widget.entry_id,
                    request_id=request_id,
                    resolution=resolution,
                    session_id=widget.session_id,
                ),
            )
            _raise_refusal(resp)
            return
        resolution = (
            t.GROK_BOT_AUTO_REVIEW_APPROVAL_RESOLUTION_APPROVED
            if approved
            else t.GROK_BOT_AUTO_REVIEW_APPROVAL_RESOLUTION_DENIED
        )
        await self._client.unary(
            GB,
            "ResolveGrokBotAutoReviewApproval",
            t.ResolveGrokBotAutoReviewApprovalRequest(
                agent_id=widget.agent_id,
                request_id=request_id,
                resolution=resolution,
                approval_platform="desktop",
                session_id=widget.session_id,
            ),
        )
