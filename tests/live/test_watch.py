import asyncio
import os

import pytest
from grokbot import GrokBotClient
from grokbot.auth import auto

pytestmark = pytest.mark.skipif(os.environ.get("GROKBOT_LIVE") != "1", reason="GROKBOT_LIVE!=1")


@pytest.mark.live
@pytest.mark.asyncio
async def test_live_watch_connects():
    async with GrokBotClient(auth=auto()) as client:
        watcher = client.watch()
        watcher.start()
        got = False
        try:
            async def _consume():
                nonlocal got
                async for _event in watcher:
                    got = True
                    break

            await asyncio.wait_for(_consume(), timeout=15)
        except TimeoutError:
            # A silent heartbeat-only stream still counts as connected if last_seen moved.
            pass
        finally:
            await watcher.stop()
        assert watcher.last_seen > 0 or got
