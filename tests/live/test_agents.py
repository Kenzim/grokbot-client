import os

import pytest
from grokbot import GrokBotClient
from grokbot.auth import auto

pytestmark = pytest.mark.skipif(os.environ.get("GROKBOT_LIVE") != "1", reason="GROKBOT_LIVE!=1")


@pytest.mark.live
@pytest.mark.asyncio
async def test_live_list_agents_sessions_history():
    async with GrokBotClient(auth=auto()) as client:
        agents = await client.agents.list(include_team=True)
        assert agents, "expected at least one grok bot agent on this account"
        pages = {}
        for agent in agents:
            sessions = await client.agents.sessions(agent.agent_id)
            sid = next((s.session_id for s in sessions if s.kind == "MAIN"), "")
            if sessions and not sid:
                sid = sessions[0].session_id
            chat = client.chat(agent.agent_id, session_id=sid)
            page = await chat.history(limit=20)
            assert page.entries or page.generation >= 0
            pages[agent.agent_id] = page.generation
        assert pages
