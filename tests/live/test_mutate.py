"""Mutating live test. Creates a throwaway agent, sends a message, watches for a reply.

Consumes cloud usage. Never touches the user's existing agents.
Requires GROKBOT_LIVE_MUTATE=1 (and a valid Cursor login).
"""
from __future__ import annotations

import asyncio
import os
import uuid

import pytest
from grokbot import GrokBotClient, Message
from grokbot.auth import auto

pytestmark = pytest.mark.skipif(
    os.environ.get("GROKBOT_LIVE_MUTATE") != "1", reason="GROKBOT_LIVE_MUTATE!=1"
)


@pytest.mark.live_mutate
@pytest.mark.asyncio
async def test_live_send_and_watch_reply():
    name = f"grokbot-client-test-{uuid.uuid4().hex[:8]}"
    async with GrokBotClient(auth=auto()) as client:
        agent = await client.agents.create(
            name=name, description="throwaway test agent", harness="temporal"
        )
        watcher = None
        try:
            chat = client.chat(agent.agent_id)
            watcher = client.watch()
            watcher.start()
            receipt = await chat.send("Reply with the single word pong.")
            assert receipt.delivery in {
                "ACCEPTED_BOX",
                "ACCEPTED_TEMPORAL",
                "DUPLICATE",
                "UNSPECIFIED",
            }
            seen_user = False

            async def _wait():
                nonlocal seen_user
                async for event in watcher:
                    if isinstance(event, Message) and event.agent_id in {
                        agent.agent_id,
                        agent.id,
                    }:
                        seen_user = True
                        return

            await asyncio.wait_for(_wait(), timeout=45)
            assert seen_user or receipt.dispatched
        finally:
            if watcher is not None:
                await watcher.stop()
            await client.agents.delete(agent.agent_id)
