# Ralph Loop SSOT

Status: ACTIVE
Last updated: 2026-03-12
Owner: Topic 68 (`ralph-loop`)

## What Ralph Loop is
Ralph Loop is the **central intake / decomposition / deduplication / routing hub** for Aoineco & Co. internal business operations and agent infrastructure work.

It is not primarily a generic support queue. It is the place where cross-topic work gets:
1. forwarded in,
2. normalized,
3. broken into small executable tasks,
4. deduplicated / reclassified,
5. either executed directly or split back out into dedicated topics.

## Core operating model
- Other topics can generate **Ralph-loop-shaped work**.
- Those items should be forwarded into Ralph Loop first when they involve:
  - cross-topic coordination,
  - repeated operational loops,
  - backlog triage,
  - decomposition into verifiable sub-tasks,
  - dedup / conflict resolution,
  - routing to automation or dispatch.
- Ralph Loop then decides whether the work should:
  - stay in Topic 68 as queue/ops work,
  - become ledger tasks,
  - become a HF/SSOT item,
  - or be split back to a domain topic.

## Why it was fast before
Ralph Loop is fast when it behaves like a **small-task throughput engine**, not a vague planning room.

### Required behavior
- break large requests into **15–60 minute task units** when possible,
- keep WIP low,
- create frequent `done` events,
- require proof per task,
- avoid carrying huge context in one session,
- store state in files + git instead of context window memory.

### Anti-patterns
- leaving work as big vague epics only,
- having scan/monitoring without execution queue movement,
- too many `open` items with no explicit `doing`,
- transfer decisions discussed in chat but not written into SSOT files.

## Canonical sub-systems
- Playbook: `context/topics/ralph-loop_PLAYBOOK_V0_1.md`
- Topic state: `context/topic-state/ralph-loop.md`
- Handoff: `context/handoff/HF_ralph_loop_drift_integrity_restore_20260308.md`
- Sprint backlog: `context/ralph_loop/SPRINT_LOOP_BACKLOG_V0_1.md`
- Ledger: `context/ralph_loop/ledger.json`, `context/ralph_loop/ledger.md`
- Drift scope: `context/ralph_loop/DRIFT_CANONICAL_SCOPE_V0_1.md`
- Daily reports: `context/ops/reports/ralph_loop_daily/`

## Transfer-in rule
When another topic produces work that needs repeated scouting, batching, decomposition, or routing:
1. create a transfer note under `context/ralph-loop-*-transfer-YYYY-MM-DD.md`
2. summarize the source topic's operating intent
3. extract recurring task shapes
4. decide what stays in source topic vs what moves into Ralph Loop
5. create/update ledger tasks or HF entries

## Current transfer notes
- `context/ralph-loop-hackathons-transfer-2026-03-11.md`
- `context/ralph-loop-x-post-ops-transfer-2026-03-12.md`
- `context/ralph-loop-longform-transfer-2026-03-12.md`
- `context/ralph-loop-bazaar-transfer-2026-03-12.md`
- `context/ralph-loop-random-triage-note-2026-03-12.md`

## Current priority
Restore Ralph Loop from scan-centric recovery mode back into execution mode:
1. recover missing transfer docs,
2. extract small executable tasks from transferred topics,
3. register them in ledger/queue with WIP discipline,
4. keep scan/drift/state-save as guardrails rather than the main job.

### First live cards (2026-03-12)
- `RL-20260312-030` — hackathons transfer small-task decomposition
- `RL-20260312-031` — x-post ops decomposition
- `RL-20260312-032` — Ralph Loop throughput mode recovery

## Proof / memory anchor
- Operating model clarification recorded in `memory/2026-03-11.md`.
- Ralph Loop drift recovery and automation reconstruction recorded in `memory/2026-03-08.md`.
