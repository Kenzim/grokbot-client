# grokbot-client

Unofficial async Python client for **Grok Bot** cloud agents. It talks
Connect-RPC + protobuf to `https://api2.cursor.sh` (`aiserver.v1`) using a
normal **Cursor account**. Import name is `grokbot`.

Not affiliated with Cursor or xAI. The API is undocumented and can change
when the desktop app updates. Bundled schemas match grok-bot **0.51.0**
(`grokbot.SCHEMA_VERSION`). MIT licensed.

## Install

Python 3.10+. Runtime: `httpx`, `protobuf>=5.29,<6`.

```bash
pip install grokbot-client
# from this repo:
pip install -e ".[dev]"
```

## Authentication

Default `GrokBotClient()` uses `grokbot.auth.auto()`:

1. Cursor CLI files, first hit wins:
   `~/.config/cursor/auth.json`, `~/.cursor/auth.json`,
   `~/.cursor/cli-config.json` (`accessToken` / `authInfo.accessToken`)
2. else `$GROKBOT_TOKEN` (raw JWT)

Expired JWTs are rejected. Re-login with the Cursor app or `agent login`.
The Grok Bot Electron app stores sealed secrets that this library does
**not** read.

| Strategy | When to use |
|----------|-------------|
| `auth.auto()` | default |
| `auth.HostFiles()` | CLI files only; re-reads each call |
| `auth.ApiKey(key)` | dashboard key via `POST /auth/exchange_user_api_key` |
| `auth.Static(jwt)` | explicit access token, no refresh |
| `auth.RefreshToken(token)` | experimental `POST /oauth/token` (often 404; prefer HostFiles or ApiKey) |

Custom providers: subclass `AuthStrategy` and implement `async token()` and
`async on_unauthorized()`. The client retries a call once after
`on_unauthorized`.

Never commit tokens, `auth.json`, or `GROKBOT_TOKEN`.

## Quickstart

```python
import asyncio
import grokbot

async def main():
    async with grokbot.GrokBotClient() as client:
        me = await client.get_me()
        print(me.email, me.user_id)
        for agent in await client.agents.list():
            print(agent.name, agent.harness, agent.agent_id)

asyncio.run(main())
```

## What you can do

Grok Bot agents run in Cursor’s cloud. `box` harnesses share one **account**
sandbox (VNC desktop). `temporal` harnesses are workflows with no desktop.

This library covers:

- account identity (`get_me`)
- agent list / get / create / update / delete, capabilities, sessions, todos
- send, interrupt, history, drafts, reactions
- account-wide transcript watch (typed events, resume cursors)
- widgets: respond, dismiss, forms, secrets, approvals
- desktop coordinates for an external noVNC/RFB client (`wake=True` may
  start a hibernated sandbox)

Out of scope: a VNC widget, `InferenceService`, Slack/marketplace/1Password
wrappers, sandbox admin RPCs (schemas are in `proto/` only).

`grokbot._proto` is private generated code. Public types keep a `.raw`
protobuf handle when you need a field we have not mapped.

## Chat

`client.chat(agent_id)` lazily uses the agent’s `MAIN` session. On 0.51.0
`ListGrokBotAgentSessions` is often empty; the client then uses
`session_id=""`. Pass an explicit `session_id` for DMs / groups / Slack.

`send()` mints a UUID `message_id` (idempotent) and sets
`source=DESKTOP`. Delivery is `ACCEPTED_BOX`, `ACCEPTED_TEMPORAL`,
`DUPLICATE`, or `REFUSED`. `REFUSED` and harness refusals raise
`RefusalError`.

```python
async with grokbot.GrokBotClient() as client:
    chat = client.chat(agent_id)
    receipt = await chat.send("summarise my open PRs")
    print(receipt.message_id, receipt.delivery)

    status = await chat.status(receipt.message_id)
    print(status.state)

    page = await chat.history(limit=50)
    for entry in page.entries:
        print(entry.seq, entry.entry_kind, entry.body)

    await chat.interrupt()          # stop the current run if any
    await chat.react(entry_id, "👍")
```

Drafts need **exactly one** of `email=` or `slack=`:

```python
await chat.draft(entry_id, email={"to": ["a@b"], "subject": "Hi", "body": "..."})
await chat.discard_draft(entry_id)
```

Create / delete (mutating; costs a cloud agent):

```python
agent = await client.agents.create(name="scratch", harness="box")
await client.agents.delete(agent.agent_id)
```

`update()` takes `name`, `description`, `title`, `avatar_shape`,
`avatar_color`. `get()` matches UUID `agent_id` or numeric `id`.

## Live events

`client.watch()` opens `WatchGrokBotTranscripts` for the whole account.
Iterate it, or `watcher.on(Type, callback)` then `await watcher.run()`.

Persist `watcher.cursors` (keyed by `(agent_id, session_id)`) and pass them
to `start(cursors=...)` to resume. On `cursor_too_old` the watcher resyncs
via history and emits `StreamReset`. Large bodies omitted from the stream
are fetched from the sandbox store.

Reconnect happens before `connected.absolute_lifetime_ms` expires.
Presence heartbeats are not required on 0.51.0.

```python
async with grokbot.GrokBotClient() as client:
    watcher = client.watch()
    async for event in watcher:
        match event:
            case grokbot.Message(text=text, role=role):
                print(role, text)
            case grokbot.HandoffRequested() as h:
                desktop = await client.desktop(wake=True)
                # hand desktop.connect_url() + websocket_headers() to noVNC
                print(h.instruction, desktop.connect_url())
            case grokbot.WidgetRequest() as w:
                await client.widgets.respond(w, "done")
            case grokbot.TurnFailed(reason=r, code=c):
                print("failed", c, r)
            case grokbot.AgentStateUpdate(is_running=running):
                print("running", running)
```

| Event | Meaning |
|-------|---------|
| `Message` | transcript row (`text`, `role`, `entry_kind`, `body`) |
| `WidgetRequest` | captcha / form / secret / approval |
| `HandoffRequested` | agent wants a human on the cloud desktop |
| `AgentStateUpdate` | `is_running` / `is_composing` |
| `ComputerActions` | computer-use actions |
| `TurnFailed` | `code` is a `GrokBotTurnFailureCode` name |
| `RosterChanged` | agent added/removed |
| `BoxStateChanged` | sandbox `run_state` |
| `StreamReset` | cleared stream or expired cursor (already resynced) |

Entry bodies are UTF-8 JSON when they start with `{`/`[`, otherwise text.

## Widgets and approvals

```python
await client.widgets.respond(widget, "solved")
await client.widgets.dismiss(widget)
await client.widgets.submit_form(widget, {"field": "value"})
await client.widgets.submit_secret(widget, "secret")
await client.widgets.resolve_approval(widget, approved=True)
```

`resolve_approval` picks virtual-card / local-tool-permission / auto-review
from `widget.kind`. A `refusal` on the RPC raises `RefusalError`.

## Desktop (account sandbox)

Not per-agent. `temporal` agents have no desktop. `wake=True` may boot a
hibernated box (billable).

```python
desktop = await client.desktop(wake=False)
print(desktop.run_state)
url = desktop.connect_url()          # wss websockify URL with network_token
headers = desktop.websocket_headers()  # x-anyrun-network-token, optional Bearer
await desktop.window(0)
await desktop.refresh(wake=False)
```

Pass `url` + `headers` to noVNC (or any RFB websocket client). This package
does not speak RFB.

## Client constructor

```python
GrokBotClient(
    auth=None,                          # default auth.auto()
    base_url="https://api2.cursor.sh",
    timeout=30.0,                       # connect; read timeout is 120s
    client_version="0.51.0",
    ghost_mode=True,
    http=None,                          # inject httpx.AsyncClient (tests)
)
```

`await client.close()` or use `async with`. Low-level `client.unary(...)`
and `client.server_stream(...)` exist if you have a protobuf request
message; prefer the typed helpers.

Wire format: unary is raw protobuf POST (`content-type: application/proto`);
streaming uses Connect frames (`flags` + 4-byte BE length + payload,
trailer `flags & 0x02`). Client headers mimic the desktop app
(`x-cursor-client-type: sand-desktop`, `connect-es/1.6.1`).

## Errors

`GrokBotError` → `AuthError`, `UnauthorizedError`, `RefusalError`,
`StreamError`, `CursorTooOldError`, `NotFoundError`.

`RefusalError.failure_code` is the harness/refusal code when present.

## Tests

```bash
pytest tests/unit tests/contract
GROKBOT_LIVE=1 pytest tests/live -m live                 # GetMe, list, watch, EnsureSandBox(wake=False)
GROKBOT_LIVE_MUTATE=1 pytest tests/live -m live_mutate   # create/send/delete a throwaway agent
```

Live tests need a Cursor login on the machine. They are skipped unless the
env var is set.

After copying newer `.proto` files into `proto/`:

```bash
tools/regen.sh    # uses .venv/bin/python, or PYTHON=python3
```

Forgejo Actions (same runner pattern as dcim: LAN git checkout, no
`actions/checkout`):

- `ci.yml` — regen drift, ruff, unit + contract
- `sonarqube.yml` — coverage + scanner + quality gate (`SONAR_HOST_URL`,
  `SONAR_TOKEN` repo secrets; project key `kenzim_grokbot-client`)
- `owasp.yml` — Dependency-Check JSON on the runner (not imported into Sonar)

## Layout

| Path | What |
|------|------|
| `grokbot/` | public package |
| `proto/` | owned `aiserver.v1` / `agent.v1` schemas |
| `grokbot/_proto/` | generated `*_pb2` (do not edit) |
| `tools/regen.sh` | regenerate `_proto` from `proto/` |
| `tests/` | unit, contract, optional live |
