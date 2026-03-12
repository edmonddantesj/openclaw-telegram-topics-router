# Ralph Loop ↔ bazaar transfer note

Status: ACTIVE
Recorded: 2026-03-12
Source topic: `bazaar` (55)
Target topic: `ralph-loop` (68)

## Transfer intent
`bazaar` remains the domain room for NEXUS Bazaar / The Archive / NEXUS Arena implementation and demo decisions.

Ralph Loop takes the repeated operational work around backlog slicing, proof-first packaging, checkpointing, and routing of implementation chores.

## Source-topic truth retained in bazaar
- product scope and demo boundaries
- receipt engine / Archive MVP decisions
- specific API / DB / UI implementation choices
- final deliverable acceptance for topic 55

## What moves into Ralph Loop
1. proof-first task slicing for implementation backlog
2. recurring checkpoint packaging (today / blocker / next)
3. append-only evidence discipline and SSOT routing
4. splitting large demo work into small executable technical tasks
5. deciding what becomes HF vs task card vs topic-local note

## Recurring task shapes for Ralph Loop
### RL-BZ-01 Backlog slice
- break implementation epics into proofable small tasks

### RL-BZ-02 Checkpoint packet
- convert topic status into `today / blocker / next` structure

### RL-BZ-03 Proof route
- ensure evidence lands in HF / logs / artifacts / SSOT paths

### RL-BZ-04 Scope guard
- prevent demo scope expansion before receipt pipeline closes

## Operating split
- `bazaar` topic = build room
- `ralph-loop` topic = decomposition / checkpoint / proof-routing room

## Gates
- internal slicing / SSOT / checkpointing: L1/L2
- external launch / irreversible exposure / sensitive infra changes: escalate per policy

## Proof / references
- `context/topics/bazaar_PLAYBOOK_V0_1.md`
- `context/topic-state/bazaar.md`
