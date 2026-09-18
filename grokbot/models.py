"""Typed models decoupling callers from protobuf. Each keeps `.raw`."""
from __future__ import annotations

import json
from dataclasses import dataclass, field
from typing import Any

from grokbot._svc import t


def enum_suffix(enum_cls, value: int, prefix: str) -> str:
    try:
        name = enum_cls.Name(value)
    except ValueError:
        return str(value)
    if name.startswith(prefix):
        return name[len(prefix) :]
    return name


def decode_body(raw: bytes | None) -> Any:
    """Decode a transcript entry body: JSON if possible, else UTF-8 text, else bytes."""
    if not raw:
        return None
    data = bytes(raw)
    try:
        text = data.decode("utf-8")
    except UnicodeDecodeError:
        return data
    text = text.strip()
    if not text:
        return None
    if text[0] in "{[":
        try:
            return json.loads(text)
        except json.JSONDecodeError:
            return text
    return text


@dataclass
class Account:
    user_id: int
    email: str
    first_name: str
    auth_id: str = ""
    raw: Any = None

    @classmethod
    def from_pb2(cls, msg) -> Account:
        return cls(
            user_id=int(msg.user_id),
            email=msg.email or "",
            first_name=msg.first_name or "",
            auth_id=msg.auth_id or "",
            raw=msg,
        )


@dataclass
class Agent:
    id: str
    agent_id: str
    name: str
    description: str
    harness: str
    kind: str
    created_at_ms: int
    viewer_session_id: str = ""
    title: str = ""
    raw: Any = None

    @classmethod
    def from_pb2(cls, msg) -> Agent:
        kind = enum_suffix(t.GrokBotAgentKind, msg.kind, "GROK_BOT_AGENT_KIND_")
        return cls(
            id=msg.id,
            agent_id=msg.agent_id or msg.legacy_agent_id or msg.id,
            name=msg.name,
            description=msg.description,
            harness=msg.harness or "",
            kind=kind,
            created_at_ms=int(msg.created_at_ms),
            viewer_session_id=msg.viewer_session_id or "",
            title=msg.title or "",
            raw=msg,
        )


@dataclass
class Session:
    session_id: str
    agent_id: str
    kind: str
    created_at_ms: int = 0
    raw: Any = None

    @classmethod
    def from_pb2(cls, msg) -> Session:
        kind = enum_suffix(
            t.GrokBotAgentSessionKind, msg.kind, "GROK_BOT_AGENT_SESSION_KIND_"
        )
        return cls(
            session_id=msg.session_id,
            agent_id=msg.agent_id,
            kind=kind,
            created_at_ms=int(msg.created_at_ms),
            raw=msg,
        )


@dataclass
class Todo:
    id: str
    text: str
    status: str
    raw: Any = None

    @classmethod
    def from_pb2(cls, msg) -> Todo:
        from grokbot._proto.agent.v1 import types_pb2 as at

        status = enum_suffix(at.TodoStatus, msg.status, "TODO_STATUS_")
        return cls(id=msg.id, text=msg.content, status=status, raw=msg)


@dataclass
class SendReceipt:
    message_id: str
    dispatched: bool
    delivery: str
    workflow_id: str | None = None
    raw: Any = None

    @classmethod
    def from_pb2(cls, message_id: str, msg) -> SendReceipt:
        delivery = enum_suffix(
            t.GrokBotUserMessageDelivery, msg.delivery, "GROK_BOT_USER_MESSAGE_DELIVERY_"
        )
        return cls(
            message_id=message_id,
            dispatched=bool(msg.dispatched),
            delivery=delivery,
            workflow_id=msg.workflow_id or None,
            raw=msg,
        )


@dataclass
class SendStatus:
    message_id: str
    state: str
    echo_entry_id: str | None = None
    rejection_code: str | None = None
    accepted_at_ms: int | None = None
    raw: Any = None

    @classmethod
    def from_pb2(cls, message_id: str, msg) -> SendStatus:
        state = enum_suffix(t.GrokBotSendStatus, msg.status, "GROK_BOT_SEND_STATUS_")
        return cls(
            message_id=message_id,
            state=state,
            echo_entry_id=msg.echo_entry_id or None,
            rejection_code=msg.rejection_code or None,
            accepted_at_ms=msg.accepted_at_ms or None,
            raw=msg,
        )


@dataclass
class RuntimeCapabilities:
    durable_identity_enabled: bool = False
    durable_identity_writes_enabled: bool = False
    temporal_creation_enabled: bool = False
    agent_messaging_enabled: bool = False
    server_rooms_enabled: bool = False
    raw: Any = None

    @classmethod
    def from_pb2(cls, msg) -> RuntimeCapabilities:
        cap = msg.capabilities
        return cls(
            durable_identity_enabled=cap.durable_identity_enabled,
            durable_identity_writes_enabled=cap.durable_identity_writes_enabled,
            temporal_creation_enabled=cap.temporal_creation_enabled,
            agent_messaging_enabled=cap.agent_messaging_enabled,
            server_rooms_enabled=cap.server_rooms_enabled,
            raw=msg,
        )


@dataclass
class TranscriptCursor:
    agent_id: str
    session_id: str
    generation: int = 0
    after_updated_seq: int = 0

    def to_pb2(self):
        return t.GrokBotTranscriptCursor(
            agent_id=self.agent_id,
            session_id=self.session_id,
            generation=self.generation,
            after_updated_seq=self.after_updated_seq,
        )

    @classmethod
    def from_pb2(cls, msg) -> TranscriptCursor:
        return cls(
            agent_id=msg.agent_id,
            session_id=msg.session_id,
            generation=int(msg.generation),
            after_updated_seq=int(msg.after_updated_seq),
        )

    @property
    def key(self) -> tuple[str, str]:
        return (self.agent_id, self.session_id)


@dataclass
class TranscriptEntry:
    seq: int
    entry_kind: str
    entry_id: str | None
    body: Any
    body_raw: bytes | None
    blob_hash: str | None
    body_omitted: bool
    updated_seq: int
    raw: Any = None

    @classmethod
    def from_pb2(cls, msg) -> TranscriptEntry:
        raw = bytes(msg.body) if msg.body else None
        return cls(
            seq=int(msg.seq),
            entry_kind=msg.entry_kind,
            entry_id=msg.entry_id or None,
            body=decode_body(raw),
            body_raw=raw,
            blob_hash=msg.blob_hash or None,
            body_omitted=bool(msg.body_omitted),
            updated_seq=int(msg.updated_seq),
            raw=msg,
        )


@dataclass
class TranscriptPage:
    entries: list[TranscriptEntry] = field(default_factory=list)
    generation: int = 0
    raw: Any = None

    @classmethod
    def from_pb2(cls, msg) -> TranscriptPage:
        return cls(
            entries=[TranscriptEntry.from_pb2(e) for e in msg.entries],
            generation=int(msg.generation),
            raw=msg,
        )
