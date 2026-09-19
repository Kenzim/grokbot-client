import httpx
import pytest
from grokbot._svc import t
from grokbot.auth import Static
from grokbot.client import GrokBotClient


def _ok(msg) -> httpx.Response:
    return httpx.Response(200, content=msg.SerializeToString())


@pytest.mark.asyncio
async def test_secrets_list_put_delete():
    seen: list[str] = []

    def handler(request: httpx.Request) -> httpx.Response:
        path = request.url.path
        seen.append(path.rsplit("/", 1)[-1])
        if path.endswith("/ListGrokBotSecrets"):
            req = t.ListGrokBotSecretsRequest()
            req.ParseFromString(request.content)
            assert req.id == "agent-1"
            return _ok(
                t.ListGrokBotSecretsResponse(
                    secrets=[t.GrokBotSecret(name="TWOCAPTCHA_API_KEY", description="solver")]
                )
            )
        if path.endswith("/PutGrokBotSecret"):
            req = t.PutGrokBotSecretRequest()
            req.ParseFromString(request.content)
            assert req.id == "agent-1"
            assert req.name == "TWOCAPTCHA_API_KEY"
            assert req.value == "fake-key"
            return _ok(
                t.PutGrokBotSecretResponse(
                    secret=t.GrokBotSecret(name=req.name, description=req.description)
                )
            )
        if path.endswith("/DeleteGrokBotSecret"):
            req = t.DeleteGrokBotSecretRequest()
            req.ParseFromString(request.content)
            assert req.id == "agent-1"
            assert req.name == "TWOCAPTCHA_API_KEY"
            return _ok(t.DeleteGrokBotSecretResponse())
        return httpx.Response(500, content=b"unexpected")

    http = httpx.AsyncClient(transport=httpx.MockTransport(handler))
    async with GrokBotClient(auth=Static("t"), http=http) as client:
        listed = await client.secrets.list("agent-1")
        assert [s.name for s in listed] == ["TWOCAPTCHA_API_KEY"]
        assert all(not hasattr(s, "value") or getattr(s, "value", None) in (None, "") for s in listed)
        put = await client.secrets.put(
            "agent-1", "TWOCAPTCHA_API_KEY", "fake-key", description="solver"
        )
        assert put.name == "TWOCAPTCHA_API_KEY"
        await client.secrets.delete("agent-1", "TWOCAPTCHA_API_KEY")
    assert seen == ["ListGrokBotSecrets", "PutGrokBotSecret", "DeleteGrokBotSecret"]


@pytest.mark.asyncio
async def test_secrets_put_requires_name_and_value():
    http = httpx.AsyncClient(transport=httpx.MockTransport(lambda r: httpx.Response(500)))
    async with GrokBotClient(auth=Static("t"), http=http) as client:
        with pytest.raises(ValueError, match="name"):
            await client.secrets.put("agent-1", "", "x")
        with pytest.raises(ValueError, match="value"):
            await client.secrets.put("agent-1", "TWOCAPTCHA_API_KEY", "  ")
