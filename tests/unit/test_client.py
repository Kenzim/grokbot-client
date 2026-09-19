import httpx
import pytest
from grokbot._svc import t
from grokbot.auth import AuthStrategy, Static
from grokbot.client import GrokBotClient, encode_frame
from grokbot.errors import NotFoundError, StreamError


class CountingAuth(AuthStrategy):
    def __init__(self) -> None:
        self.tokens = 0
        self.unauths = 0

    async def token(self) -> str:
        self.tokens += 1
        return "tok"

    async def on_unauthorized(self) -> None:
        self.unauths += 1


@pytest.mark.asyncio
async def test_get_me_unary():
    def handler(request: httpx.Request) -> httpx.Response:
        assert request.url.path.endswith("/aiserver.v1.DashboardService/GetMe")
        assert request.headers["x-cursor-client-type"] == "sand-desktop"
        body = t.GetMeResponse(user_id=42, email="a@b.c", first_name="Ada").SerializeToString()
        return httpx.Response(200, content=body)

    http = httpx.AsyncClient(transport=httpx.MockTransport(handler))
    async with GrokBotClient(auth=Static("t"), http=http) as client:
        me = await client.get_me()
    assert me.user_id == 42
    assert me.email == "a@b.c"


@pytest.mark.asyncio
async def test_unary_401_retries_once():
    calls = {"n": 0}

    def handler(request: httpx.Request) -> httpx.Response:
        calls["n"] += 1
        if calls["n"] == 1:
            return httpx.Response(401, json={"code": "unauthenticated", "message": "nope"})
        body = t.GetMeResponse(user_id=1, email="ok@x").SerializeToString()
        return httpx.Response(200, content=body)

    auth = CountingAuth()
    http = httpx.AsyncClient(transport=httpx.MockTransport(handler))
    async with GrokBotClient(auth=auth, http=http) as client:
        me = await client.get_me()
    assert me.user_id == 1
    assert auth.unauths == 1
    assert calls["n"] == 2


@pytest.mark.asyncio
async def test_unary_not_found():
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(404, json={"code": "not_found", "message": "gone"})

    http = httpx.AsyncClient(transport=httpx.MockTransport(handler))
    async with GrokBotClient(auth=Static("t"), http=http) as client:
        with pytest.raises(NotFoundError):
            await client.get_me()


@pytest.mark.asyncio
async def test_server_stream_frames_and_trailer():
    hb = t.GrokBotTranscriptWatchFrame()
    hb.heartbeat.server_time_ms = 99
    payload = encode_frame(hb.SerializeToString()) + encode_frame(b"{}", flags=0x02)

    def handler(request: httpx.Request) -> httpx.Response:
        assert "application/connect+proto" in request.headers["content-type"]
        return httpx.Response(200, content=payload)

    http = httpx.AsyncClient(transport=httpx.MockTransport(handler))
    from grokbot._svc import GB

    async with GrokBotClient(auth=Static("t"), http=http) as client:
        frames = [
            f
            async for f in client.server_stream(
                GB, "WatchGrokBotTranscripts", t.WatchGrokBotTranscriptsRequest()
            )
        ]
    assert len(frames) == 1
    assert frames[0].WhichOneof("frame") == "heartbeat"


@pytest.mark.asyncio
async def test_server_stream_trailer_error():
    trailer = encode_frame(b'{"error":{"code":"internal","message":"boom"}}', flags=0x02)

    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(200, content=trailer)

    http = httpx.AsyncClient(transport=httpx.MockTransport(handler))
    from grokbot._svc import GB

    async with GrokBotClient(auth=Static("t"), http=http) as client:
        with pytest.raises(StreamError, match="boom"):
            async for _ in client.server_stream(
                GB, "WatchGrokBotTranscripts", t.WatchGrokBotTranscriptsRequest()
            ):
                pass


@pytest.mark.asyncio
async def test_chat_draft_requires_one_payload():
    http = httpx.AsyncClient(transport=httpx.MockTransport(lambda r: httpx.Response(500)))
    async with GrokBotClient(auth=Static("t"), http=http) as client:
        chat = client.chat("agent-1", session_id="")
        with pytest.raises(ValueError, match="exactly one"):
            await chat.draft("e1")
        with pytest.raises(ValueError, match="exactly one"):
            await chat.draft("e1", email={"body": "x"}, slack={"target": "c", "body": "y"})


@pytest.mark.asyncio
async def test_end_handoff_unary():
    def handler(request: httpx.Request) -> httpx.Response:
        assert request.url.path.endswith("/aiserver.v1.GrokBotService/EndGrokBotBoxHandoff")
        body = t.EndGrokBotBoxHandoffResponse(dispatched=True).SerializeToString()
        return httpx.Response(200, content=body)

    http = httpx.AsyncClient(transport=httpx.MockTransport(handler))
    async with GrokBotClient(auth=Static("t"), http=http) as client:
        assert await client.end_handoff("agent-1", "req-9") is True


@pytest.mark.asyncio
async def test_chat_draft_email():
    def handler(request: httpx.Request) -> httpx.Response:
        assert request.url.path.endswith("/SendGrokBotDraft")
        body = t.SendGrokBotDraftResponse(accepted=True).SerializeToString()
        return httpx.Response(200, content=body)

    http = httpx.AsyncClient(transport=httpx.MockTransport(handler))
    async with GrokBotClient(auth=Static("t"), http=http) as client:
        chat = client.chat("agent-1", session_id="")
        assert await chat.draft("e1", email={"to": ["a@b.c"], "subject": "hi", "body": "n"})
