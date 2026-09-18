"""Authentication strategies.

Strategy protocol:

    async def token(self) -> str
    async def on_unauthorized(self) -> None   # drop cache / re-acquire

`auto()` uses HostFiles when a Cursor credential file is present, otherwise
`$GROKBOT_TOKEN` as a static JWT.

Refresh discovery (Phase 2): the Cursor CLI bundle (2026.06.04) contains
`/auth/poll` and `/auth/exchange_user_api_key` but **not** `/oauth/token`.
`HostFiles` therefore only re-reads the on-disk file (the CLI keeps it
fresh). `RefreshToken` still attempts `POST /oauth/token` as a best-effort
OIDC grant — prefer `ApiKey` for a host with no CLI babysitting the file.
"""
from __future__ import annotations

import base64
import json
import os
import time
from pathlib import Path

import httpx

from grokbot.constants import API_KEY_EXCHANGE_PATH, DEFAULT_BACKEND, OAUTH_TOKEN_PATH
from grokbot.errors import AuthError

AUTH_CANDIDATES = [
    Path.home() / ".config" / "cursor" / "auth.json",
    Path.home() / ".cursor" / "auth.json",
    Path.home() / ".cursor" / "cli-config.json",
]


def jwt_payload(token: str) -> dict:
    parts = token.split(".")
    if len(parts) != 3:
        return {}
    try:
        seg = parts[1] + "=" * (-len(parts[1]) % 4)
        payload = json.loads(base64.urlsafe_b64decode(seg))
    except Exception:
        return {}
    return payload if isinstance(payload, dict) else {}


def jwt_exp(token: str) -> float | None:
    exp = jwt_payload(token).get("exp")
    try:
        return float(exp) if exp is not None else None
    except (TypeError, ValueError):
        return None


def _token_from_mapping(data: dict) -> str | None:
    for key in ("accessToken", "access_token"):
        val = data.get(key)
        if isinstance(val, str) and val.strip():
            return val.strip()
    info = data.get("authInfo")
    if isinstance(info, dict):
        for key in ("accessToken", "access_token"):
            val = info.get(key)
            if isinstance(val, str) and val.strip():
                return val.strip()
    return None


def _refresh_from_mapping(data: dict) -> str | None:
    for key in ("refreshToken", "refresh_token"):
        val = data.get(key)
        if isinstance(val, str) and val.strip():
            return val.strip()
    info = data.get("authInfo")
    if isinstance(info, dict):
        return _refresh_from_mapping(info)
    return None


class AuthStrategy:
    """Base class for credential providers."""

    async def token(self) -> str:
        raise NotImplementedError

    async def on_unauthorized(self) -> None:
        raise NotImplementedError


class Static(AuthStrategy):
    """A raw access JWT. No refresh; caller manages expiry."""

    def __init__(self, token: str) -> None:
        self._token = token.strip()
        if not self._token:
            raise AuthError("empty static token")

    async def token(self) -> str:
        return self._token

    async def on_unauthorized(self) -> None:
        raise AuthError("static token was rejected (401); no refresh available")


class HostFiles(AuthStrategy):
    """Cursor CLI credential files. Re-reads per call; does not call a refresh grant.

    The CLI (or desktop app) is what keeps `accessToken` fresh in these files.
    """

    def __init__(self, paths: list[Path] | None = None, margin_sec: float = 30.0) -> None:
        self.paths = list(paths) if paths is not None else list(AUTH_CANDIDATES)
        self.margin_sec = margin_sec

    def read_access_token(self) -> str:
        tried: list[str] = []
        last_expired: str | None = None
        for path in self.paths:
            if not path.exists():
                continue
            tried.append(str(path))
            try:
                data = json.loads(path.read_text())
            except (OSError, json.JSONDecodeError) as exc:
                raise AuthError(f"{path} unreadable: {exc}") from exc
            if not isinstance(data, dict):
                continue
            token = _token_from_mapping(data)
            if not token:
                continue
            exp = jwt_exp(token)
            if exp is not None and exp <= time.time() + self.margin_sec:
                last_expired = str(path)
                continue
            return token
        if last_expired:
            raise AuthError(
                f"Cursor token in {last_expired} is expired; "
                "re-login with the Cursor app / `agent login`"
            )
        raise AuthError(
            "no Cursor access token found (tried: "
            + (", ".join(tried) or "none of the known paths")
            + "). Log in with the Cursor app or `agent login`, or set GROKBOT_TOKEN."
        )

    def read_refresh_token(self) -> str | None:
        for path in self.paths:
            if not path.exists():
                continue
            try:
                data = json.loads(path.read_text())
            except (OSError, json.JSONDecodeError):
                continue
            if isinstance(data, dict):
                tok = _refresh_from_mapping(data)
                if tok:
                    return tok
        return None

    async def token(self) -> str:
        return self.read_access_token()

    async def on_unauthorized(self) -> None:
        return None


class ApiKey(AuthStrategy):
    """Cursor dashboard API key; exchanged via POST /auth/exchange_user_api_key."""

    def __init__(
        self,
        key: str,
        *,
        base_url: str = DEFAULT_BACKEND,
        http: httpx.AsyncClient | None = None,
        margin_sec: float = 60.0,
    ) -> None:
        self.key = key.strip()
        if not self.key:
            raise AuthError("empty API key")
        self.base_url = base_url.rstrip("/")
        self._http = http
        self.margin_sec = margin_sec
        self._access: str | None = None
        self._exp: float | None = None

    async def token(self) -> str:
        if self._access and (self._exp is None or self._exp > time.time() + self.margin_sec):
            return self._access
        await self._exchange()
        assert self._access is not None
        return self._access

    async def _exchange(self) -> None:
        own = self._http is None
        client = self._http or httpx.AsyncClient(timeout=20.0)
        try:
            resp = await client.post(
                f"{self.base_url}{API_KEY_EXCHANGE_PATH}",
                headers={
                    "authorization": f"Bearer {self.key}",
                    "accept": "application/json",
                    "content-type": "application/json",
                },
                json={},
            )
        finally:
            if own:
                await client.aclose()
        if resp.status_code != 200:
            raise AuthError(
                f"API key exchange failed HTTP {resp.status_code}: {resp.text[:300]}"
            )
        try:
            data = resp.json()
        except Exception as exc:
            raise AuthError(f"API key exchange returned non-JSON: {resp.text[:200]}") from exc
        token = None
        if isinstance(data, dict):
            token = data.get("accessToken") or data.get("access_token") or data.get("token")
        if not isinstance(token, str) or not token.strip():
            raise AuthError("API key exchange returned no access token")
        self._access = token.strip()
        self._exp = jwt_exp(self._access)

    async def on_unauthorized(self) -> None:
        self._access = None
        self._exp = None


class RefreshToken(AuthStrategy):
    """Best-effort OIDC refresh grant against POST /oauth/token.

    The Cursor CLI binary we inspected does not reference this path, so this
    strategy may 404 in production. Prefer HostFiles or ApiKey.
    """

    def __init__(
        self,
        token: str,
        *,
        base_url: str = DEFAULT_BACKEND,
        http: httpx.AsyncClient | None = None,
        margin_sec: float = 60.0,
    ) -> None:
        self.refresh_token = token.strip()
        if not self.refresh_token:
            raise AuthError("empty refresh token")
        self.base_url = base_url.rstrip("/")
        self._http = http
        self.margin_sec = margin_sec
        self._access: str | None = None
        self._exp: float | None = None

    async def token(self) -> str:
        if self._access and (self._exp is None or self._exp > time.time() + self.margin_sec):
            return self._access
        await self._refresh()
        assert self._access is not None
        return self._access

    async def _refresh(self) -> None:
        own = self._http is None
        client = self._http or httpx.AsyncClient(timeout=20.0)
        try:
            resp = await client.post(
                f"{self.base_url}{OAUTH_TOKEN_PATH}",
                headers={
                    "accept": "application/json",
                    "content-type": "application/x-www-form-urlencoded",
                },
                data={"grant_type": "refresh_token", "refresh_token": self.refresh_token},
            )
        finally:
            if own:
                await client.aclose()
        if resp.status_code != 200:
            raise AuthError(
                f"refresh grant failed HTTP {resp.status_code} at {OAUTH_TOKEN_PATH} "
                f"(unconfirmed in Cursor CLI; use HostFiles or ApiKey). {resp.text[:300]}"
            )
        try:
            data = resp.json()
        except Exception as exc:
            raise AuthError(f"refresh grant returned non-JSON: {resp.text[:200]}") from exc
        token = None
        if isinstance(data, dict):
            token = data.get("access_token") or data.get("accessToken")
            nxt = data.get("refresh_token") or data.get("refreshToken")
            if isinstance(nxt, str) and nxt.strip():
                self.refresh_token = nxt.strip()
        if not isinstance(token, str) or not token.strip():
            raise AuthError("refresh grant returned no access_token")
        self._access = token.strip()
        self._exp = jwt_exp(self._access)

    async def on_unauthorized(self) -> None:
        self._access = None
        self._exp = None


def auto() -> AuthStrategy:
    """HostFiles if a credential file exists, else `$GROKBOT_TOKEN`."""
    env = (os.environ.get("GROKBOT_TOKEN") or "").strip()
    files = HostFiles()
    try:
        files.read_access_token()
        return files
    except AuthError:
        if env:
            return Static(env)
        raise
