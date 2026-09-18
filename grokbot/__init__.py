"""grokbot — unofficial async Python client for the Grok Bot cloud-agent backend.

See docs/DESIGN.md for architecture and docs/API.md for the full reference.
"""

from grokbot import auth, events
from grokbot.client import GrokBotClient
from grokbot.errors import (
    AuthError,
    CursorTooOldError,
    GrokBotError,
    NotFoundError,
    RefusalError,
    StreamError,
    UnauthorizedError,
)
from grokbot.models import Account, Agent, SendReceipt, Session, Todo

__version__ = "0.1.0"

# Version of the grok-bot desktop app the bundled protos were extracted from.
SCHEMA_VERSION = "0.51.0"

__all__ = [
    "Account",
    "Agent",
    "AuthError",
    "CursorTooOldError",
    "GrokBotClient",
    "GrokBotError",
    "NotFoundError",
    "RefusalError",
    "SCHEMA_VERSION",
    "SendReceipt",
    "Session",
    "StreamError",
    "Todo",
    "UnauthorizedError",
    "__version__",
    "auth",
    "events",
]
