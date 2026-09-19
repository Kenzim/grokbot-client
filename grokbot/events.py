"""Typed watcher events."""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class Message:
    """A transcript message entry (agent or user)."""

    agent_id: str
    session_id: str
    entry_id: str
    seq: int
    text: str
    role: str
    ts: float = 0.0
    entry_kind: str = ""
    body: Any = None


@dataclass
class WidgetRequest:
    """An interactive widget: captcha, form, credential request, or approval."""

    agent_id: str
    session_id: str
    entry_id: str
    kind: str
    prompt: str
    request_id: str = ""
    body: Any = None
    ts: float = 0.0


@dataclass
class HandoffRequested:
    """The agent wants a human to take over the cloud desktop (captcha / login)."""

    agent_id: str
    session_id: str
    request_id: str
    instruction: str
    reason: str = ""
    tab_id: str = ""
    since_ms: int = 0
    updated_at_ms: int = 0


@dataclass
class AgentStateUpdate:
    agent_id: str
    session_id: str
    is_running: bool
    is_composing: bool
    live_state: Any = None


@dataclass
class ComputerActions:
    agent_id: str
    actions: list[Any] = field(default_factory=list)


@dataclass
class TurnFailed:
    agent_id: str
    session_id: str
    reason: str
    code: str = ""
    turn_id: str = ""


@dataclass
class RosterChanged:
    kind: str
    agent_id: str


@dataclass
class BoxStateChanged:
    run_state: str
    raw: Any = None


@dataclass
class StreamReset:
    """Stream was cleared or the cursor expired; a resync already happened."""

    agent_id: str
    session_id: str
    reason: str = ""
