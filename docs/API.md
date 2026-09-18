# `grokbot` API reference (planned)

This is the public surface of the `grokbot` package. Everything here is
async. Only names documented here are public; `grokbot._proto` is private.

## `grokbot.GrokBotClient`

```python
GrokBotClient(
    auth: AuthStrategy | None = None,          # default: auth.auto()
    base_url: str = "https://api2.cursor.sh",
    timeout: float = 30.0,
    client_version: str = "0.51.0",            # x-cursor-client-version
    ghost_mode: bool = True,
)
```

| Attribute / method | Returns | Description |
|--------------------|---------|-------------|
| `client.agents` | `AgentAPI` | agent CRUD + state |
| `client.chat(agent_id)` | `ChatSession` | messaging interface to one agent |
| `client.widgets` | `WidgetAPI` | respond/dismiss widgets & approvals |
| `client.desktop(agent_id)` | `DesktopSession` | provision desktop stream coordinates |
| `client.watch(*, include_unlisted=True, inline_body_max_bytes=65536)` | `TranscriptWatcher` | account-wide event stream |
| `await client.get_me()` | `Account` | identity sanity check |
| `await client.close()` | `None` | close underlying httpx client |
| async context manager | | `async with GrokBotClient() as c:` |

## `grokbot.auth`

```python
auth.auto() -> AuthStrategy                 # HostFiles → GROKBOT_TOKEN env
auth.HostFiles(paths: list[Path] | None)    # Cursor CLI files, refresh via /oauth/token
auth.RefreshToken(token: str)               # stored refresh token
auth.ApiKey(key: str)                       # dashboard key, /auth/exchange_user_api_key
auth.Static(token: str)                     # raw JWT, no refresh
```

Custom strategies: subclass `AuthStrategy` and implement
`async token() -> str` and `async on_unauthorized() -> None`.

## `AgentAPI` (`client.agents`)

| Method | Returns | Wraps |
|--------|---------|-------|
| `list(*, include_team=False, role=None)` | `list[Agent]` | `ListGrokBotAgents` |
| `get(agent_id)` | `Agent` | `ListGrokBotAgents` + filter |
| `create(*, name, description="", harness="box", ...)` | `Agent` | `CreateGrokBotAgent` |
| `update(agent_id, **fields)` | `Agent` | `UpdateGrokBotAgent` |
| `delete(agent_id)` | `None` | `DeleteGrokBotAgent` |
| `capabilities()` | `RuntimeCapabilities` | `GetGrokBotRuntimeCapabilities` |
| `sessions(agent_id)` | `list[Session]` | `ListGrokBotAgentSessions` |
| `todos(agent_id)` | `list[Todo]` | `ListGrokBotAgentTodos` |

## `ChatSession` (`client.chat(agent_id)`)

| Method | Returns | Wraps |
|--------|---------|-------|
| `send(text, *, rich_text=None, reply_to_id=None, attachments=None, fork=False)` | `SendReceipt` | `SendGrokBotUserMessage` (UUID `message_id` for idempotency) |
| `status(message_id)` | `SendStatus` | `GetGrokBotSendStatus` |
| `interrupt()` | `None` | `InterruptGrokBotAgentRun` |
| `draft(text)` / `discard_draft()` | `None` | `SendGrokBotDraft` / `DiscardGrokBotDraft` |
| `react(entry_id, emoji)` | `None` | `ReactToGrokBotMessage` |
| `history(*, cursor=None, limit=...)` | `TranscriptPage` | `ListGrokBotTranscriptEntries` |

## `TranscriptWatcher` (`client.watch()`)

Async iterator + callback hybrid:

```python
async for event in watcher: ...
# or
watcher.on(WidgetRequest, lambda e: ...)
await watcher.run()  # blocks; watcher.stop() from elsewhere
```

| Member | Description |
|--------|-------------|
| `watcher.cursor` | last `GrokBotTranscriptCursor` (persist to resume across restarts) |
| `watcher.last_seen` | monotonic ts of last frame/heartbeat |
| `watcher.start(cursor=None)` | start (optionally from a saved cursor) |
| `watcher.stop()` | graceful stop |

### Event types (`grokbot.events`)

| Event | Emitted for | Key fields |
|-------|-------------|------------|
| `Message` | transcript entry of kind message | `agent_id, entry_id, seq, text, role, ts` |
| `WidgetRequest` | widget entries (captcha, form, credential, approval) | `agent_id, entry_id, session_id, kind, prompt` |
| `AgentStateUpdate` | `agent_state` / `agent_state_changed` frames | `agent_id, live_state` |
| `ComputerActions` | `computer_actions` frames | `agent_id, actions` |
| `TurnFailed` | `turn_failed` | `agent_id, reason` |
| `RosterChanged` | agents added/removed | — |
| `BoxStateChanged` | `box_state` | `agent_id, run_state` |
| `StreamReset` | `cleared` / `cursor_too_old` (after resync) | — |

## `WidgetAPI` (`client.widgets`)

| Method | Wraps |
|--------|-------|
| `respond(widget, value)` | `RespondGrokBotWidget` |
| `dismiss(widget)` | `DismissGrokBotWidget` |
| `submit_form(widget, values)` | `SubmitGrokBotUserForm` |
| `submit_secret(widget, value)` | `SubmitGrokBotSecret` |
| `resolve_approval(widget, approved)` | `ResolveGrokBotAutoReviewApproval` / `ResolveGrokBotLocalToolPermission` / `ResolveGrokBotVirtualCardApproval` |

## `DesktopSession`

```python
session = await client.desktop(agent_id)   # EnsureSandBox under the hood
session.vnc_url          # websockify WSS endpoint for the RFB stream
session.gateway_url      # in-box Sand gateway
session.gateway_token
session.network_token
session.exec_daemon_url  # exec daemon (terminal/FS in the sandbox)
session.exec_daemon_auth_token
session.run_state        # SandBoxRunState
session.websocket_headers() -> dict[str, str]   # auth headers for the WSS upgrade
session.fork_url(window_index) -> str           # fork desktop base URL
await session.refresh()  # re-ensure (tokens rotate with sandbox restarts)
```

## `grokbot.models`

Typed dataclasses decoupling callers from pb2: `Account`, `Agent`,
`Session`, `Todo`, `SendReceipt`, `SendStatus`, `TranscriptPage`,
`TranscriptEntry`, `RuntimeCapabilities`. All have `.raw` holding the
underlying protobuf message for fields we didn't map yet.

## `grokbot.errors`

`GrokBotError` · `AuthError` · `UnauthorizedError` · `RefusalError` ·
`StreamError` · `CursorTooOldError` · `NotFoundError`

## Constants

`grokbot.SCHEMA_VERSION` — app version the bundled protos were extracted
from (`"0.51.0"`). `grokbot.__version__` — library version.
