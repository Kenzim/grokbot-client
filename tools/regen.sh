#!/usr/bin/env bash
# Regenerate grokbot/_proto from proto/. Requires grpcio-tools + protobuf 5.29.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

if [[ -z "${PYTHON:-}" ]]; then
  if [[ -x "$ROOT/.venv/bin/python" ]]; then
    PYTHON="$ROOT/.venv/bin/python"
  elif command -v python3 >/dev/null 2>&1; then
    PYTHON="$(command -v python3)"
  else
    PYTHON="$(command -v python)"
  fi
fi

STAGE="$ROOT/grokbot/_proto"
rm -rf "$STAGE"
mkdir -p "$STAGE/aiserver/v1" "$STAGE/agent/v1"

rewrite() {
  local src="$1" dest="$2"
  sed -E \
    -e 's#import "aiserver/v1/#import "grokbot/_proto/aiserver/v1/#g' \
    -e 's#import "agent/v1/#import "grokbot/_proto/agent/v1/#g' \
    "$src" > "$dest"
}

for f in proto/aiserver/v1/*.proto; do
  rewrite "$f" "$STAGE/aiserver/v1/$(basename "$f")"
done
for f in proto/agent/v1/*.proto; do
  rewrite "$f" "$STAGE/agent/v1/$(basename "$f")"
done

"$PYTHON" -m grpc_tools.protoc \
  -I . \
  --python_out=. \
  --pyi_out=. \
  grokbot/_proto/aiserver/v1/*.proto \
  grokbot/_proto/agent/v1/*.proto

# Keep generated Python only; proto/ is the source of truth.
find "$STAGE" -name '*.proto' -delete

# Namespace packages so `grokbot._proto.aiserver.v1` imports.
for d in \
  grokbot/_proto \
  grokbot/_proto/aiserver \
  grokbot/_proto/aiserver/v1 \
  grokbot/_proto/agent \
  grokbot/_proto/agent/v1
do
  : > "$d/__init__.py"
done

echo "regenerated grokbot/_proto"
