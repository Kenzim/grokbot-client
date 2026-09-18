import json
from pathlib import Path

from grokbot.desktop import derive_vnc_connect_url
from grokbot.models import TranscriptEntry, decode_body
from grokbot.transcripts import events_from_entry


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
