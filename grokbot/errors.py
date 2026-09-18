"""Error hierarchy for grokbot. See docs/API.md#grokboterrors."""


class GrokBotError(Exception):
    """Base class for all grokbot errors."""


class AuthError(GrokBotError):
    """No usable credential, or refresh/exchange failed. Re-login required."""


class UnauthorizedError(GrokBotError):
    """Backend returned 401 even after one credential refresh retry."""


class RefusalError(GrokBotError):
    """The backend returned a GrokBotHarnessRefusal for the request."""


class StreamError(GrokBotError):
    """Connect stream trailer error or malformed frame."""


class CursorTooOldError(GrokBotError):
    """Watch cursor expired; the watcher resyncs via ListGrokBotTranscriptEntries."""


class NotFoundError(GrokBotError):
    """Agent / session / transcript entry no longer exists."""
