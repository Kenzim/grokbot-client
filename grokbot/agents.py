"""Agent resource API: CRUD, capabilities, sessions, todos."""
from __future__ import annotations

import uuid
from typing import TYPE_CHECKING

from grokbot._svc import GB, t
from grokbot.errors import NotFoundError
from grokbot.models import Agent, RuntimeCapabilities, Session, Todo

if TYPE_CHECKING:
    from grokbot.client import GrokBotClient

_HARNESS = {
    "box": t.GROK_BOT_AGENT_HARNESS_KIND_BOX,
    "temporal": t.GROK_BOT_AGENT_HARNESS_KIND_TEMPORAL,
}


class AgentAPI:
    """Accessed via `client.agents`."""

    def __init__(self, client: GrokBotClient) -> None:
        self._client = client

    async def list(self, *, include_team: bool = False, role: str | None = None) -> list[Agent]:
        req = t.ListGrokBotAgentsRequest(include_team_agents=include_team)
        if role:
            req.role = role
        resp = await self._client.unary(GB, "ListGrokBotAgents", req)
        return [Agent.from_pb2(a) for a in resp.agents]

    async def get(self, agent_id: str) -> Agent:
        for agent in await self.list(include_team=True):
            if agent.agent_id == agent_id or agent.id == agent_id:
                return agent
        raise NotFoundError(f"agent not found: {agent_id}")

    async def create(
        self,
        *,
        name: str,
        description: str = "",
        harness: str = "box",
        agent_id: str | None = None,
        **kw,
    ) -> Agent:
        hid = str(agent_id or uuid.uuid4())
        kind = _HARNESS.get(harness.lower())
        if kind is None:
            raise ValueError(f"unknown harness {harness!r}; expected box|temporal")
        req = t.CreateGrokBotAgentRequest(
            name=name,
            description=description,
            title=kw.get("title", ""),
            avatar_shape=kw.get("avatar_shape", ""),
            avatar_color=kw.get("avatar_color", ""),
            agent_id=hid,
            legacy_agent_id=kw.get("legacy_agent_id", hid),
            harness=kind,
        )
        if kw.get("purpose"):
            req.purpose = kw["purpose"]
        method = (
            "CreateGrokBotTemporalAgent" if harness.lower() == "temporal" else "CreateGrokBotAgent"
        )
        resp = await self._client.unary(GB, method, req)
        return Agent.from_pb2(resp.agent)

    async def update(self, agent_id: str, **fields) -> Agent:
        agent = await self.get(agent_id)
        req = t.UpdateGrokBotAgentRequest(
            id=agent.id,
            name=fields.get("name", agent.name),
            description=fields.get("description", agent.description),
            title=fields.get("title", agent.title),
            avatar_shape=fields.get("avatar_shape", ""),
            avatar_color=fields.get("avatar_color", ""),
        )
        resp = await self._client.unary(GB, "UpdateGrokBotAgent", req)
        return Agent.from_pb2(resp.agent)

    async def delete(self, agent_id: str) -> None:
        agent = await self.get(agent_id)
        await self._client.unary(GB, "DeleteGrokBotAgent", t.DeleteGrokBotAgentRequest(id=agent.id))

    async def capabilities(self) -> RuntimeCapabilities:
        resp = await self._client.unary(
            GB, "GetGrokBotRuntimeCapabilities", t.GetGrokBotRuntimeCapabilitiesRequest()
        )
        return RuntimeCapabilities.from_pb2(resp)

    async def sessions(self, agent_id: str) -> list[Session]:
        resp = await self._client.unary(
            GB, "ListGrokBotAgentSessions", t.ListGrokBotAgentSessionsRequest(agent_id=agent_id)
        )
        return [Session.from_pb2(s) for s in resp.sessions]

    async def todos(self, agent_id: str) -> list[Todo]:
        resp = await self._client.unary(
            GB, "ListGrokBotAgentTodos", t.ListGrokBotAgentTodosRequest(agent_id=agent_id)
        )
        return [Todo.from_pb2(item) for item in resp.todos]
