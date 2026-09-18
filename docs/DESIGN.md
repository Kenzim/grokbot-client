# `grokbot` — library design

A standalone, publishable Python client for the Grok Bot cloud-agent backend
(`aiserver.v1` on `api2.cursor.sh`). This document is the plan we implement
against; it doubles as the architecture section of the published docs.

- **Package name (PyPI):** `grokbot-client`
- **Import name:** `grokbot`
- **Python:** ≥3.10
- **Runtime deps:** `httpx`, `protobuf` (nothing else)
- **License:** MIT — unofficial client, not affiliated with Cursor/xAI

## Scope

| In scope | Out of scope |
|----------|--------------|
| Auth (token files, refresh token, API-key exchange) | A full VNC/RFB client (we hand connection descriptors to the host app) |
| Agent CRUD + capabilities | Any UI |
| Chat: send, interrupt, drafts, reactions, attachments | Model inference (`InferenceService` — cloud-side, separate token) |
| Transcript streaming with resume | SandBox admin RPCs (present in protos, not wrapped) |
| Widgets / approvals / captcha prompts | Slack/marketplace/1Password wrappers (protos only) |
| Desktop connection provisioning (`EnsureSandBox` → VNC/gateway creds) | |

## Backend facts the design relies on

- Connect-RPC: unary = raw protobuf POST; streaming = Connect envelope frames
  (see TRANSPORT.md in the sibling `grokbot-api` repo).
- Auth: Cursor account JWT; month-long `accessToken` + `refreshToken`
  (`offline_access`) in `~/.config/cursor/auth.json`; API-key exchange at
  `POST /auth/exchange_user_api_key`; refresh at `POST /oauth/token`.
- `EnsureSandBox` returns `vnc_url`, `gateway_url` + `gateway_token`,
  `network_token`, `exec_daemon_url` + `exec_daemon_auth_token`,
  `fork_vnc_base_url` — everything a desktop stream needs.
- `WatchGrokBotTranscripts` frames: `connected | rows | cleared |
  cursor_too_old | heartbeat | agent_state | computer_actions |
  agent_state_changed | turn_failed | roster_changed | box_state`.
- Transcript entries are seq-ordered; large bodies are offloaded to the
  sandbox store (`blob_hash` + `body_omitted`, fetched via
  `PresignSandBoxStoreReads`).
- Widgets/approvals are transcript entries answered with
  `RespondGrokBotWidget(agent_id, entry_id, value, session_id)` /
  `DismissGrokBotWidget`.

## Package layout

```
grokbot/
├── __init__.py          # public API re-exports, __version__
├── client.py            # GrokBotClient — transport + service stubs
├── auth.py              # auth strategies (see below)
├── agents.py            # Agent resource (CRUD, capabilities, state)
├── chat.py              # ChatSession — send/interrupt/drafts/reactions
├── transcripts.py       # TranscriptWatcher — resilient stream + decoding
├── widgets.py           # Widget/Approval models, respond/dismiss helpers
├── desktop.py           # DesktopSession — sandbox ensure + VNC coordinates
├── store.py             # sandbox-store blob fetch (presigned reads)
├── models.py            # typed dataclasses wrapping the pb2 messages
├── errors.py            # error hierarchy
├── _proto/              # vendored generated *_pb2 (built from ../proto)
└── py.typed
```

## Public API shape

```python
import grokbot

client = grokbot.GrokBotClient(auth=grokbot.auth.auto())   # async

agents = await client.agents.list()
agent  = await client.agents.get(agent_id)                 # or create(...)

chat = client.chat(agent.id)
await chat.send("find me 5 senior python roles in Berlin") # idempotent UUID message_id
await chat.interrupt()

async for event in client.watch():          # TranscriptWatcher, auto-resume
    match event:
        case grokbot.Message(agent_id=_, text=text):      ...
        case grokbot.WidgetRequest() as w:                 # captcha / form / approval
            desktop = await client.desktop(w.agent_id)     # ensure sandbox
            show_user(desktop.vnc_url, desktop.gateway_token)
            await client.widgets.respond(w, value="solved")
        case grokbot.TurnFailed(agent_id=_, reason=r):     ...
```

### Auth strategies (`grokbot.auth`)

| Strategy | Source | Refresh |
|----------|--------|---------|
| `auth.auto()` | first working of the below | — |
| `auth.HostFiles()` | `~/.config/cursor/auth.json` etc. | re-read per call; uses `refreshToken` via `/oauth/token` when expired |
| `auth.RefreshToken(token)` | stored by host app (Forge settings) | `/oauth/token` |
| `auth.ApiKey(key)` | dashboard key | `/auth/exchange_user_api_key` per expiry |
| `auth.Static(token)` | explicit JWT | none (caller manages) |

All strategies implement `async def token(self) -> str` and
`async def on_unauthorized(self) -> None` (drop cache, re-acquire). The client
retries a call once after `on_unauthorized`.

### TranscriptWatcher

- Holds `WatchGrokBotTranscripts` open; yields decoded, typed events.
- Resumes with the last `GrokBotTranscriptCursor` on reconnect; on
  `cursor_too_old` it resyncs via `ListGrokBotTranscriptEntries`.
- Fetches offloaded bodies (`blob_hash`) transparently via `store.py`.
- Backpressure: internal `asyncio.Queue` (bounded); heartbeats update a
  `last_seen` timestamp for liveness monitoring by the host.

### DesktopSession

`await client.desktop(agent_id)` → `DesktopSession(vnc_url, gateway_url,
gateway_token, network_token, exec_daemon_url, exec_daemon_auth_token,
fork_vnc_base_url, run_state)`.

The library deliberately stops at provisioning: the host application (Forge)
already has a noVNC/RFB proxy; it consumes these coordinates. A small
`desktop.websocket_headers()` helper returns the auth headers the websockify
endpoint expects, and `desktop.fork_url(n)` builds fork-desktop URLs.

### Captcha / widget flow (the "solve this for me" loop)

1. Agent posts a transcript entry whose body is a widget (captcha, form,
   credential request, approval).
2. `TranscriptWatcher` emits `WidgetRequest` (parsed kind, prompt, entry_id,
   session_id).
3. Host UI shows a button → opens the desktop stream (`client.desktop`).
4. User solves in the desktop; host calls `widgets.respond(w, "solved")` or
   `widgets.dismiss(w)`.
5. Watcher emits the follow-up `Message` when the agent continues.

### Errors

```
GrokBotError
├── AuthError            # no credential / refresh failed (re-login needed)
├── UnauthorizedError    # 401 after retry — triggers on_unauthorized path
├── RefusalError         # GrokBotHarnessRefusal returned by the backend
├── StreamError          # connect trailer error / malformed frame
├── CursorTooOldError    # internal: triggers watcher resync
└── NotFoundError        # agent/session/entry gone
```

## Testing

- **Unit:** fake Connect server (httpx `MockTransport`) replaying captured
  frames; auth strategy expiry/refresh logic; cursor/resume logic.
- **Contract:** `protoc --descriptor_set_out` must compile clean in CI;
  generated pb2 are byte-stable for a pinned app version.
- **Live (opt-in, `GROKBOT_LIVE=1`):** `GetMe`, `ListGrokBotAgents`, watch
  connect — same as today's `poc/`.

## Versioning & publishing

- SemVer. The **backend schema version** (app version the protos were
  extracted from, e.g. `0.51.0`) is recorded in `grokbot.SCHEMA_VERSION` and
  the changelog; the library's own version is independent.
- Regenerate flow: `tools/gen_proto.js` → `proto/` → `protoc` →
  `grokbot/_proto/`; CI fails if `proto/` and `_proto/` drift.
- Publish: PyPI via `hatchling`, tag-driven GitHub Action.

## Relationship to Forge

Forge depends on `grokbot-client` and adds only app-level glue:
a `backend/capabilities/grokbot.py` (watcher → chat wake, bindings),
`grokbot_mcp.py` (chat tools), and noVNC panes fed by `DesktopSession`.
Nothing Forge-specific lives in the library.
