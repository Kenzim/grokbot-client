"""Typed models decoupling callers from protobuf. Each keeps `.raw`."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass
class Account:
    user_id: int
    email: str
    first_name: str
    raw: Any = None


@dataclass
class Agent:
    agent_id: str
    name: str
    description: str
    harness: str  # "box" | "temporal"
    kind: str
    created_at_ms: int
    raw: Any = None


@dataclass
class Session:
    session_id: str
    agent_id: str
    raw: Any = None


@dataclass
class Todo:
    text: str
    status: str
    raw: Any = None


@dataclass
class SendReceipt:
    message_id: str
    raw: Any = None


@dataclass
class SendStatus:
    message_id: str
    state: str
    raw: Any = None


@dataclass
class TranscriptPage:
    entries: list[Any]
    cursor: bytes | None
    raw: Any = None
