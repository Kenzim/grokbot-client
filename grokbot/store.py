"""Sandbox-store blob fetch via PresignSandBoxStoreReads."""
from __future__ import annotations

from typing import TYPE_CHECKING

from grokbot._svc import GB, t

if TYPE_CHECKING:
    from grokbot.client import GrokBotClient


async def fetch_blobs(client: GrokBotClient, rel_paths: list[str]) -> dict[str, bytes]:
    """Download omitted transcript bodies from the sandbox object store."""
    if not rel_paths:
        return {}
    resp = await client.unary(
        GB, "PresignSandBoxStoreReads", t.PresignSandBoxStoreReadsRequest(rel_paths=rel_paths)
    )
    out: dict[str, bytes] = {}
    for inst in resp.instructions:
        r = await client._http.get(inst.url)
        r.raise_for_status()
        out[inst.rel_path] = r.content
    return out
