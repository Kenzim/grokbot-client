from grokbot.auth import Static


def client_with(handler, **kw):
    import httpx
    from grokbot.client import GrokBotClient

    transport = httpx.MockTransport(handler)
    http = httpx.AsyncClient(transport=transport)
    return GrokBotClient(auth=kw.get("auth") or Static("test-token"), http=http)
