# HF: longform(65) → ralph-loop(68) transfer recovery (2026-03-14)

- Status: ACTIVE
- Source topic: `longform` (65)
- Target execution lane: `ralph-loop` (68)
- Recovery reason: transfer note existed, but parent/child operational tracking, deep-study record, and synthesis linkage were not explicit enough for durable execution.

## Decision
Keep the split.
- `longform` stays the content room.
- `ralph-loop` stays the intake / queue / decomposition room.
- This delegation is valid, but needed concrete parent/child task restoration.

## Current State
- Parent task restored: `ops/items/TASK-20260314-LONGFORM-RLP-01.md`
- Child task restored (intake): `ops/items/TASK-20260314-LONGFORM-RLP-02.md`
- Child task restored (deep-study gate): `ops/items/TASK-20260314-LONGFORM-RLP-03.md`
- Child task restored (synthesis): `ops/items/TASK-20260314-LONGFORM-RLP-04.md`
- Current default lane: `summary-first`
- Deep study entered: `NO` (not yet triggered by a specific source packet)
- SSOT promotion candidate: `REVIEW_PENDING` via synthesis task

## Lane IO / proof
- input truth: `context/topics/longform_PLAYBOOK_V0_1.md`
- transfer rule: `context/ralph-loop-longform-transfer-2026-03-12.md`
- source state: `context/topic-state/longform.md`
- target state: `context/topic-state/ralph-loop.md`
- audit/proof note: `context/research/longform/LONGFORM_RALPH_TRANSFER_AUDIT_2026-03-14.md`

## Next Actions
1. intake task classifies the next delegated longform item/batch
2. if a source requires full-read, deep-study gate flips to YES and gets a dedicated output artifact
3. synthesis task decides `context/research/` vs `context/knowledge/` and marks SSOT review candidacy explicitly

## Open Issues
- No specific live delegated longform document/batch is attached yet
- Deep-study remains gate-ready, not active
- SSOT promotion is prepared but not yet adjudicated on a concrete source item
