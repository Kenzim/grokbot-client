import json
import struct

from grokbot.client import FLAG_TRAILER, FrameDecoder, encode_frame


def test_encode_frame_roundtrip():
    payload = b"hello"
    raw = encode_frame(payload, 0)
    assert raw[0] == 0
    assert struct.unpack(">I", raw[1:5])[0] == 5
    assert raw[5:] == payload
    dec = FrameDecoder()
    frames = dec.feed(raw)
    assert frames == [(0, payload)]


def test_decoder_splits_across_chunks():
    payload = b"abcdef"
    raw = encode_frame(payload)
    dec = FrameDecoder()
    assert dec.feed(raw[:3]) == []
    assert dec.feed(raw[3:]) == [(0, payload)]


def test_trailer_flag():
    body = json.dumps({"error": None}).encode()
    raw = encode_frame(body, FLAG_TRAILER)
    flags, payload = FrameDecoder().feed(raw)[0]
    assert flags & FLAG_TRAILER
    assert json.loads(payload)["error"] is None
