import json
from pathlib import Path
from types import SimpleNamespace

import pytest

from grokbot.desktop import derive_vnc_connect_url
from grokbot.events import HandoffRequested, WidgetRequest
from grokbot.models import TranscriptEntry, decode_body
from grokbot.transcripts import TranscriptWatcher, events_from_entry


def test_decode_json_body():
    assert decode_body(b'{"text":"hi","role":"user"}') == {"text": "hi", "role": "user"}
    assert decode_body(b"plain") == "plain"
    assert decode_body(None) is None


def test_events_from_message_entry():
    entry = TranscriptEntry(
        seq=1,
        entry_kind="user_message",
        entry_id="e1",
        body={"text": "hello", "role": "user"},
        body_raw=None,
        blob_hash=None,
        body_omitted=False,
        updated_seq=1,
    )
    evs = events_from_entry("agent-1", "sess-1", entry)
    assert len(evs) == 1
    assert evs[0].text == "hello"
    assert evs[0].role == "user"


def test_events_from_send_message_text():
    entry = TranscriptEntry(
        seq=3,
        entry_kind="send-message",
        entry_id="t3s12",
        body={
            "kind": "send-message",
            "id": "t3s12",
            "message": {"type": "text", "content": "hello from the bot"},
            "timestampMs": 1788028250883,
        },
        body_raw=None,
        blob_hash=None,
        body_omitted=False,
        updated_seq=3,
    )
    evs = events_from_entry("a", "", entry)
    assert evs[0].text == "hello from the bot"
    assert evs[0].role == "assistant"


def test_widget_event_includes_timestamp():
    entry = TranscriptEntry(
        seq=4,
        entry_kind="captcha",
        entry_id="cap1",
        body={"prompt": "Solve this", "timestampMs": 1_700_000_000_000},
        body_raw=None,
        blob_hash=None,
        body_omitted=False,
        updated_seq=4,
    )
    evs = events_from_entry("a", "", entry)
    assert isinstance(evs[0], WidgetRequest)
    assert evs[0].ts == 1_700_000_000.0


@pytest.mark.asyncio
async def test_agent_state_handoff_emits_once_per_request_id():
    watcher = TranscriptWatcher(SimpleNamespace())
    emitted: list[object] = []

    async def capture(event):
        emitted.append(event)

    watcher._emit = capture  # type: ignore[method-assign]

    awaiting_state = SimpleNamespace(reason="captcha", tab_id="t1", since_ms=1_700_000_000_000)

    class Live:
        agent_id = "agent-1"
        session_id = "s1"
        is_running = True
        is_composing_message = False
        box_handoff_request_id = "h-old"
        box_handoff_instruction = "Solve the captcha"
        updated_at_ms = 1_700_000_000_000
        awaiting = awaiting_state

        def HasField(self, name: str) -> bool:
            return name == "awaiting"

    state = SimpleNamespace(live=[Live()])
    await watcher._handle_agent_state(state)
    await watcher._handle_agent_state(state)
    handoffs = [e for e in emitted if isinstance(e, HandoffRequested)]
    assert len(handoffs) == 1
    assert handoffs[0].request_id == "h-old"
    assert handoffs[0].reason == "captcha"
    assert handoffs[0].since_ms == 1_700_000_000_000

    live2 = Live()
    live2.box_handoff_request_id = ""
    await watcher._handle_agent_state(SimpleNamespace(live=[live2]))
    live3 = Live()
    live3.box_handoff_request_id = "h-new"
    await watcher._handle_agent_state(SimpleNamespace(live=[live3]))
    handoffs = [e for e in emitted if isinstance(e, HandoffRequested)]
    assert [h.request_id for h in handoffs] == ["h-old", "h-new"]


def test_events_from_nested_widget():
    entry = TranscriptEntry(
        seq=4,
        entry_kind="send-message",
        entry_id="t3s11",
        body={
            "kind": "send-message",
            "message": {
                "type": "widget",
                "widget": {"prompt": "Which of these should I apply to?", "helpText": "tick"},
            },
        },
        body_raw=None,
        blob_hash=None,
        body_omitted=False,
        updated_seq=4,
    )
    evs = events_from_entry("a", "", entry)
    assert evs[0].prompt.startswith("Which of these")


def test_vnc_connect_url_copies_tokens():
    url = "https://box.example:8443/vnc.html?path=websockify&network_token=abc&port_token=xyz"
    got = derive_vnc_connect_url(url)
    assert got.startswith("wss://box.example:8443/websockify")
    assert "network_token=abc" in got
    assert "port_token=xyz" in got


def test_fixture_catalogues_live_entry_kinds():
    data = json.loads(
        (Path(__file__).resolve().parents[1] / "fixtures" / "transcript_sample.json").read_text()
    )
    kinds: set[str] = set()
    for page in data["pages"].values():
        kinds.update(page["entry_kinds"])
    assert {"message", "send-message", "spend-initiation"} <= kinds
