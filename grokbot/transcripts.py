"""TranscriptWatcher — resilient account-wide event stream.

Wraps GrokBotService/WatchGrokBotTranscripts (server-streaming).

- Reconnects with the last GrokBotTranscriptCursor; on
  `cursor_too_old` resyncs via ListGrokBotTranscriptEntries.
- Fetches offloaded entry bodies (blob_hash / body_omitted) via store.py.
- Bounded internal asyncio.Queue for backpressure; heartbeats update
  `last_seen` for host-side liveness checks.
"""
from __future__ import annotations


class TranscriptWatcher:
    """Obtained via `client.watch()`. See docs/API.md#transcriptwatcher."""

    cursor: bytes | None
    last_seen: float

    async def start(self, cursor: bytes | None = None) -> None: ...
    async def stop(self) -> None: ...
    def on(self, event_type: type, callback) -> None: ...
    def __aiter__(self): ...
