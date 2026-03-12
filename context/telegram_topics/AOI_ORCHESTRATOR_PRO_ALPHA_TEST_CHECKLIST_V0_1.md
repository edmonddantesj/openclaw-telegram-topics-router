# AOI Orchestrator PRO Alpha Test Checklist v0.1

Purpose: internal alpha-only test plan before any beta distribution.

## Current live target
- Chat: `telegram:-1003732040608`
- Topic: `6062`
- Topic slug: `cat-strategic`
- Primary owner: `청뇌`
- Collaborators: `청령`, `청비`

## Goal
Verify that this topic can act as a realistic internal proving ground for:
- topic-aware routing
- delegation decision
- topic isolation
- orchestrator runtime state/event handling
- failure/recovery behavior

## Phase A — Router SSOT sanity
- [x] `thread_topic_map.json` contains topic `6062 -> cat-strategic`
- [x] `thread_agent_map.json` contains `cat-strategic`
- [ ] `resolve_primary_agent.py --thread-id 6062` returns `청뇌`
- [ ] `delegation_decider.py` returns `should_delegate=true` for a meaningful request in this topic
- [ ] `delegation_state.py record/check` works under workspace context

## Phase B — Topic-local orchestration runtime
- [ ] test run creates dedicated runtime path keyed by topic/workstream
- [ ] `state.json` created
- [ ] `events.jsonl` created
- [ ] `turn_handoff` sequence visible
- [ ] final state closes cleanly (`mode=idle`, `currentTurn=null`)

## Phase C — Isolation / repeated use
- [ ] same topic repeated runs do not corrupt state
- [ ] different topics can be isolated by runtime path
- [ ] repeated run preserves auditability via runId/event trail

## Phase D — Failure injection
- [ ] stale lock recovery observed
- [ ] broken `state.json` fallback observed
- [ ] malformed last event line tolerated
- [ ] watchdog timeout preemption observed

## Go / No-Go
### GO minimum
- all Phase A items pass
- Phase B core items pass
- no cross-topic contamination observed
- state/event files remain readable after repeated runs

### NO-GO
- wrong primary owner resolution for topic 6062
- workspace-vs-home path mismatch remains
- runtime files overwrite each other across topics
- recovery cannot restore from broken state

## Notes
- This checklist is for internal alpha only.
- Do not package for beta until GO minimum is satisfied.
