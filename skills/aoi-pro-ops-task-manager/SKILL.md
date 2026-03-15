---
name: aoi-pro-ops-task-manager
description: "AOI PRO hygiene tool: canonicalize duplicate ops items, enforce ralph-loop labeling, route assignees, emit proof-first reports."
---

<!-- 🌌 Aoineco-Verified | Proprietary Beta Skill (AOI PRO) -->
<!-- S-DNA: AOI-2026-0302-SDNA-OTM01 -->

# AOI PRO — Ops Task Manager

## What it does
- Scans `ops/items/*.md`
- Canonicalizes known duplicate families (e.g. `TASK-YYYYMMDD-ORACLE-01/02/03`)
- Enforces Ralph Loop visibility (adds `ralph-loop` tag when detected)
- Applies lightweight routing defaults (project → assignee)
- Writes a proof-first report: `ops/reports/task_manager/REPORT_*.md`

## Safety / Governance
- Scope: **L2** (metadata hygiene only)
- Never executes L3 actions (money/keys/onchain/external posting)
- Always writes evidence reports; edits are deterministic + reversible via git

## Run

Dry-run (default):
```bash
python3 skills/aoi-pro-ops-task-manager/scripts/ops_task_manager.py --dry-run
```

Apply edits:
```bash
python3 skills/aoi-pro-ops-task-manager/scripts/ops_task_manager.py --apply
```

## Policy SSOT
- `skills/aoi-pro-ops-task-manager/state/policy.json`

## Multi-agent review mode
- Use bounded parallel summon when a request needs real cross-functional review rather than single-owner hygiene.
- Treat phrases like `토론해줘`, `같이 논의해줘`, `병렬로 봐줘`, `팀원 불러서 봐줘`, or direct naming of 2+ roles as explicit multi-review triggers.
- Use distinct real agents only; do not fake discussion by spawning clone-shards of the same agent.
- Prefer small sets (2~4 participants).
- Return in this order:
  1. Participants
  2. Key issues
  3. Consensus / conclusion
  4. Next action
- Follow global baseline: `context/ops/TOPIC_PARALLEL_SUMMON_POLICY_V0_1.md`

## Docs
- Ops item template: `skills/aoi-pro-ops-task-manager/docs/TEMPLATE_OPS_ITEM_AOI_PRO_V0_1.md`
- Wave execution policy: `skills/aoi-pro-ops-task-manager/docs/AOI_PRO_WAVE_EXECUTION_POLICY_V0_1.md`

## Owner / Role mapping
- **🧿 Oracle**: scheduling, max-active slot policy alignment
- **Aoineco**: rule evolution, taxonomy, evidence formats

### External beta users (important)
- This skill’s default routing uses **role labels** (e.g., `Oracle`, `Builder`, `Ops`, `Memory`), not Aoineco’s internal teammate nicknames.
- If you want real agent names, edit: `skills/aoi-pro-ops-task-manager/state/policy.json`