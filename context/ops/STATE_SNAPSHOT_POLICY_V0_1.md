# STATE SNAPSHOT POLICY V0.1

## Goal
Keep remote state snapshots recoverable without turning the backup set into a high-sensitivity memory dump.

## Default mode
Safety-first remote backup profile.

## Include by default
- `USER.md`
- `IDENTITY.md`
- `TOOLS.md`
- `context/`
- `memory/`
- `scripts/`

## Exclude by default
- `MEMORY.md`
- `.env`
- secrets / tokens / credentials
- media / large binaries
- repo clones / build outputs / caches
- broad `agents/*/context`

## Agent context rule
Do not include `agents/*/context` by default.
If a specific agent context is truly needed for disaster recovery, add its relative path to:

`context/ops/STATE_SNAPSHOT_AGENT_CONTEXT_ALLOWLIST.txt`

Example:
- `agents/strategist/context`
- `agents/devops/context`

## Rationale
- `MEMORY.md` has durable personal/strategic context and should not be replicated widely even into private backup stores unless explicitly chosen.
- agent contexts vary in sensitivity and size; explicit allowlisting is safer than broad inclusion.
- `context/`, `memory/`, and `scripts/` preserve most recovery-critical operational knowledge.
