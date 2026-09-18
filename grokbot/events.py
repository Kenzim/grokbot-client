"""Typed watcher events. See docs/API.md#event-types."""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class Message:
    """A transcript message entry (agent or user)."""
    agent_id: str
    entry_id: str
    seq: int
    text: str
    role: str
    ts: float


@dataclass
class WidgetRequest:
    """An interactive widget: captcha, form, credential request, or approval."""
    agent_id: str
    entry_id: str
    session_id: str
    kind: str
    prompt: str


@dataclass
class AgentStateUpdate:
    agent_id: str
    live_state: Any


@dataclass
class ComputerActions:
    agent_id: str
    actions: list[Any] = field(default_factory=list)


@dataclass
class TurnFailed:
    agent_id: str
    reason: str


@dataclass
class RosterChanged:
    pass


@dataclass
class BoxStateChanged:
    agent_id: str
    run_state: Any


@dataclass
class StreamReset:
    """Stream was cleared or the cursor expired; a resync already happened."""
