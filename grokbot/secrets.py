"""Agent secret store: list / put / delete. Values are write-only.

`ListGrokBotSecrets` / `PutGrokBotSecret` require Team Bot secrets. Personal
accounts often return ``permission_denied``; the Apply-box captcha key then
lives in the sandbox object store at ``secrets/TWOCAPTCHA_API_KEY``.
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from grokbot._svc import GB, t
from grokbot.models import Secret

if TYPE_CHECKING:
    from grokbot.client import GrokBotClient


class SecretsAPI:
    """Accessed via `client.secrets`."""

    def __init__(self, client: GrokBotClient) -> None:
        self._client = client

    async def list(self, agent_id: str) -> list[Secret]:
        resp = await self._client.unary(
            GB, "ListGrokBotSecrets", t.ListGrokBotSecretsRequest(id=agent_id)
        )
        return [Secret.from_pb2(s) for s in resp.secrets]

    async def put(
        self,
        agent_id: str,
        name: str,
        value: str,
        *,
        description: str = "",
    ) -> Secret:
        name = (name or "").strip()
        if not name:
            raise ValueError("secret name required")
        if not (value or "").strip():
            raise ValueError("secret value required")
        resp = await self._client.unary(
            GB,
            "PutGrokBotSecret",
            t.PutGrokBotSecretRequest(
                id=agent_id,
                name=name,
                description=description,
                value=value,
            ),
        )
        return Secret.from_pb2(resp.secret)

    async def delete(self, agent_id: str, name: str) -> None:
        name = (name or "").strip()
        if not name:
            raise ValueError("secret name required")
        await self._client.unary(
            GB,
            "DeleteGrokBotSecret",
            t.DeleteGrokBotSecretRequest(id=agent_id, name=name),
        )
