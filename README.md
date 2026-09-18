# grokbot-client

Unofficial async Python client for the **Grok Bot** cloud-agent backend
(`aiserver.v1` over Connect-RPC on `api2.cursor.sh`). Authenticates with a
normal Cursor account.

> Status: **planned / skeleton**. The architecture and API are fully
> specified — see [docs/DESIGN.md](docs/DESIGN.md) and
> [docs/API.md](docs/API.md). Implementation starts from the verified PoC in
> the sibling repo [`grokbot-api`](../grokbot-api) (backend reverse
> engineering: protos, transport, auth, live-tested scripts).

## What it does

- **Auth** — Cursor host credential files, stored refresh token, or dashboard
  API key (auto-refresh built in)
- **Agents** — create / list / update / delete cloud agents
- **Chat** — send messages (idempotent), interrupt, drafts, history
- **Watch** — resilient account-wide transcript stream (auto-resume, resync)
- **Widgets** — captcha / form / approval prompts your users answer in-app
- **Desktop** — provisions VNC/websocket coordinates for an agent's cloud
  desktop so your app can stream it (RFB rendering stays in your app)

```python
import grokbot

async with grokbot.GrokBotClient(auth=grokbot.auth.auto()) as client:
    agents = await client.agents.list()
    chat = client.chat(agents[0].agent_id)
    await chat.send("hello from grokbot-client")
    async for event in client.watch():
        print(event)
```

## Layout

- `grokbot/` — the package (skeleton with full signatures + docstrings)
- `docs/DESIGN.md` — architecture, scope, testing, versioning, publishing
- `docs/API.md` — planned public API reference

## Relationship to `grokbot-api`

[`grokbot-api`](../grokbot-api) documents and proves the backend API
(regenerated `.proto` files, transport/auth analysis, live PoCs). This repo
is the maintained, publishable library built on top of it. Proto schemas are
vendored from `grokbot-api` at build time (`grokbot/_proto/`).

Not affiliated with Cursor or xAI. MIT licensed.
