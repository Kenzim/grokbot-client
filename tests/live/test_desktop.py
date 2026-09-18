import os

import pytest
from grokbot import GrokBotClient
from grokbot.auth import auto
from grokbot.desktop import derive_vnc_connect_url

pytestmark = pytest.mark.skipif(
    os.environ.get("GROKBOT_LIVE") != "1", reason="GROKBOT_LIVE!=1"
)


@pytest.mark.live
@pytest.mark.asyncio
async def test_live_ensure_sandbox_no_wake():
    async with GrokBotClient(auth=auto()) as client:
        desktop = await client.desktop(wake=False)
    assert desktop.run_state in {"ABSENT", "HIBERNATED", "RUNNING", "STARTING", "UNSPECIFIED"}
    if desktop.vnc_url:
        url = desktop.connect_url()
        assert url.startswith("ws")
        assert derive_vnc_connect_url(desktop.vnc_url, desktop.network_token) == url


@pytest.mark.skipif(
    os.environ.get("GROKBOT_LIVE_MUTATE") != "1", reason="GROKBOT_LIVE_MUTATE!=1"
)
@pytest.mark.live_mutate
@pytest.mark.asyncio
async def test_live_vnc_handshake():
    """WSS handshake against vnc_url. May wake a hibernated sandbox."""
    import ssl

    import httpx

    async with GrokBotClient(auth=auto()) as client:
        desktop = await client.desktop(wake=True)
    if not desktop.vnc_url:
        pytest.skip("EnsureSandBox returned empty vnc_url")
    url = desktop.connect_url()
    headers = desktop.websocket_headers()
    try:
        async with httpx.AsyncClient(timeout=15.0) as http:
            async with http.stream("GET", url, headers={**headers, "upgrade": "websocket"}) as resp:
                # A 400/401/426 still proves the endpoint is reachable.
                assert resp.status_code < 500
    except (httpx.ConnectError, ssl.SSLError) as exc:
        pytest.fail(f"vnc handshake connect failed: {exc}")
