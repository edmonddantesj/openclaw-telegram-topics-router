---
name: aoi-backup-guardian
description: Guardrails for backups and destructive operations in the OpenClaw workspace (.openclaw). Provides SAVE NOW + snapshot remote upload and a two-step confirmation gate for commands that could delete OpenClaw state.
---

# AOI Backup Guardian

Use this skill when the user asks to **save / backup / snapshot / reset / delete `.openclaw`** or anything that risks losing the OpenClaw workspace.

## What this skill does

1) **One-command durable save**
- Runs `scripts/save_now.sh` (which renders/syncs ledger, md-vault push, and makes a state snapshot).
- If configured, also uploads the newest snapshot to the private GitHub snapshot repo.

2) **Destructive command safety gate (two-step)**
- Detects commands that could delete critical state (e.g., `rm -rf ~/.openclaw`, deleting workspace, wiping repos).
- Forces a **second explicit confirmation** with a required phrase before proceeding.

## Quick start

### A) Save now (recommended before any risky action)
```bash
python3 skills/private/aoi-backup-guardian/scripts/save_now_plus.py
```

### B) Check a command for danger (before running exec)
```bash
python3 skills/private/aoi-backup-guardian/scripts/guard_destructive_cmd.py --cmd "rm -rf ~/.openclaw"
```

If it prints `NEEDS_CONFIRMATION`, ask the user to reply with the exact phrase it outputs.

### C) Run a destructive command only after confirmation
Re-run with:
```bash
python3 skills/private/aoi-backup-guardian/scripts/guard_destructive_cmd.py \
  --cmd "rm -rf ~/.openclaw" \
  --confirm "I UNDERSTAND THIS WILL DELETE OPENCLAW STATE"
```

If it returns `OK_TO_RUN`, only then proceed.

## Policy

- Default stance: **fail closed**. If uncertain, treat as dangerous.
- Always recommend `save_now_plus.py` first.
- Never ask the user to paste secrets/tokens into chat.
