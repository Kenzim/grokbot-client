"""Error hierarchy."""

from __future__ import annotations


class GrokBotError(Exception):
    """Base class for all grokbot errors."""

    def __init__(self, message: str = "", *, code: str | None = None) -> None:
        super().__init__(message)
        self.code = code


class AuthError(GrokBotError):
    """No usable credential, or refresh/exchange failed. Re-login required."""


class UnauthorizedError(GrokBotError):
    """Backend returned 401 / unauthenticated even after one credential retry."""


class RefusalError(GrokBotError):
    """The backend returned a GrokBotHarnessRefusal for the request."""

    def __init__(
        self, message: str = "", *, code: str | None = None, failure_code: str | None = None
    ) -> None:
        super().__init__(message, code=code)
        self.failure_code = failure_code


class StreamError(GrokBotError):
    """Connect stream trailer error or malformed frame."""


class CursorTooOldError(GrokBotError):
    """Watch cursor expired; the watcher resyncs via ListGrokBotTranscriptEntries."""


class NotFoundError(GrokBotError):
    """Agent / session / transcript entry no longer exists."""
