"""Authentication strategies. See docs/AUTH.md and docs/API.md#grokbotauth.

Strategy protocol:

    async def token(self) -> str: ...            # current Bearer token
    async def on_unauthorized(self) -> None: ... # drop cache, re-acquire

`auto()` picks the first working strategy: HostFiles, then $GROKBOT_TOKEN.
"""
from __future__ import annotations

from pathlib import Path


class AuthStrategy:
    """Base class for credential providers."""

    async def token(self) -> str:
        raise NotImplementedError

    async def on_unauthorized(self) -> None:
        raise NotImplementedError


class HostFiles(AuthStrategy):
    """Cursor CLI credential files; refreshes via POST /oauth/token."""

    def __init__(self, paths: list[Path] | None = None) -> None: ...


class RefreshToken(AuthStrategy):
    """A stored refresh token (e.g. from Forge settings); /oauth/token."""

    def __init__(self, token: str) -> None: ...


class ApiKey(AuthStrategy):
    """Cursor dashboard API key; exchanged via /auth/exchange_user_api_key."""

    def __init__(self, key: str) -> None: ...


class Static(AuthStrategy):
    """A raw access JWT. No refresh; caller manages expiry."""

    def __init__(self, token: str) -> None: ...


def auto() -> AuthStrategy:
    """First working strategy: HostFiles, then $GROKBOT_TOKEN."""
    raise NotImplementedError
