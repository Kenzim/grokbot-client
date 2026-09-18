import os

import pytest
from grokbot import GrokBotClient
from grokbot.auth import auto

pytestmark = pytest.mark.skipif(os.environ.get("GROKBOT_LIVE") != "1", reason="GROKBOT_LIVE!=1")


@pytest.mark.live
@pytest.mark.asyncio
async def test_live_get_me():
    async with GrokBotClient(auth=auto()) as client:
        me = await client.get_me()
    assert me.user_id
    assert me.email
