"""grokbot — unofficial async Python client for the Grok Bot cloud-agent backend."""

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
from grokbot.events import (
    AgentStateUpdate,
    BoxStateChanged,
    ComputerActions,
    HandoffRequested,
    Message,
    RosterChanged,
    StreamReset,
    TurnFailed,
    WidgetRequest,
)
from grokbot.models import Account, Agent, SendReceipt, Session, Todo, TranscriptCursor

__version__ = "0.1.0"
SCHEMA_VERSION = "0.51.0"

__all__ = [
    "Account",
    "Agent",
    "AgentStateUpdate",
    "AuthError",
    "BoxStateChanged",
    "ComputerActions",
    "CursorTooOldError",
    "GrokBotClient",
    "GrokBotError",
    "HandoffRequested",
    "Message",
    "NotFoundError",
    "RefusalError",
    "RosterChanged",
    "SCHEMA_VERSION",
    "SendReceipt",
    "Session",
    "StreamError",
    "StreamReset",
    "Todo",
    "TranscriptCursor",
    "TurnFailed",
    "UnauthorizedError",
    "WidgetRequest",
    "__version__",
    "auth",
    "events",
]
