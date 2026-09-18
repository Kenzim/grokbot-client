import json
from pathlib import Path

import httpx
import pytest
from grokbot.auth import ApiKey, AuthError, HostFiles, RefreshToken, Static, auto
from grokbot.constants import API_KEY_EXCHANGE_PATH, OAUTH_TOKEN_PATH


def test_static_rejects_empty():
    with pytest.raises(AuthError):
        Static("")


def test_hostfiles_reads_access_token(tmp_path: Path):
    p = tmp_path / "auth.json"
    p.write_text(json.dumps({"accessToken": "abc123"}))
    hf = HostFiles(paths=[p])
    assert hf.read_access_token() == "abc123"


def test_hostfiles_missing(tmp_path: Path):
    hf = HostFiles(paths=[tmp_path / "nope.json"])
    with pytest.raises(AuthError, match="no Cursor access token"):
        hf.read_access_token()


@pytest.mark.asyncio
async def test_api_key_exchange():
    def handler(request: httpx.Request) -> httpx.Response:
        assert request.url.path == API_KEY_EXCHANGE_PATH
        assert request.headers["authorization"] == "Bearer k_live"
        return httpx.Response(200, json={"accessToken": "exchanged-jwt"})

    http = httpx.AsyncClient(transport=httpx.MockTransport(handler))
    strat = ApiKey("k_live", http=http)
    assert await strat.token() == "exchanged-jwt"
    await http.aclose()


@pytest.mark.asyncio
async def test_refresh_token_grant():
    def handler(request: httpx.Request) -> httpx.Response:
        assert request.url.path == OAUTH_TOKEN_PATH
        return httpx.Response(200, json={"access_token": "new-access", "refresh_token": "rot"})

    http = httpx.AsyncClient(transport=httpx.MockTransport(handler))
    strat = RefreshToken("old-refresh", http=http)
    assert await strat.token() == "new-access"
    assert strat.refresh_token == "rot"
    await http.aclose()


def test_auto_falls_back_to_env(monkeypatch, tmp_path: Path):
    monkeypatch.setenv("GROKBOT_TOKEN", "env-tok")
    monkeypatch.setattr("grokbot.auth.AUTH_CANDIDATES", [tmp_path / "missing.json"])
    # HostFiles() in auto() uses AUTH_CANDIDATES
    from grokbot import auth as auth_mod

    monkeypatch.setattr(auth_mod, "AUTH_CANDIDATES", [tmp_path / "missing.json"])
    strat = auto()
    assert isinstance(strat, Static)
