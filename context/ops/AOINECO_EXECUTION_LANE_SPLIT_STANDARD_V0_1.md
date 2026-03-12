# AOINECO_EXECUTION_LANE_SPLIT_STANDARD_V0_1.md

Status: SSOT (local)
Last updated: 2026-03-13

## Purpose
Standardize how work is split across:
- **main-session**
- **Ralph Loop**
- **human gate**

This prevents repeated work from floating in memory and clarifies when a task should remain conversational versus move into a persistent execution lane.

## 1. main-session
### Role
Use main-session for:
- direction setting
- prioritization
- ambiguity resolution
- strategic judgment
- exception handling
- high-context user coordination

### What should stay here
- unclear requests
- tradeoff decisions
- prioritization across projects/topics
- human preference capture
- final approval before manual/external acts

### What should not stay here
- repeated sweeps
- repeated intake/decomposition
- routine checkpointing
- recurring operational follow-ups that can be packetized

## 2. Ralph Loop
### Role
Ralph Loop is the default execution lane for repeated, decomposable, proof-based business work.

Reference:
- `context/ops/RALPH_LOOP_BUSINESS_WIDE_APPLICATION_POLICY_V0_1.md`

### Move work into Ralph Loop when
- the task can be decomposed into task packets
- the task benefits from repeated scanning/triage/checkpointing
- the task should continue without constant user prompting
- the task has verifiable pass/fail or proof checkpoints
- the topic room should stay clean while repeated ops noise is separated out

### Common shapes
- intake triage
- backlog slicing
- scout / benchmark / signal / synthesis loops
- repeated proof-first packaging
- maintenance sweep / checkpoint / queue refresh

## 3. human gate
### Role
Human gate exists only where a person must perform or approve a manual / external / identity-bearing act.

### Typical human gates
- login
- account identity confirmation
- KYC
- captcha
- payment
- wallet signature / signing
- final submission approval
- external publishing / outward message send

### Rule
Do not pull a human into internal repeatable work too early.
Only escalate when the work reaches an actual manual / external gate.

## 4. Preparation-first rule
Before a deadline or submit moment, prepare in advance:
- build or runnable artifact
- repo/path ownership clarity
- README or usage note
- demo or screenshot path
- proof bundle / evidence
- submit/apply copy
- known blockers
- final human gate checklist

The preferred operating mode is:
**prepare first, submit later**
not
**panic first, improvise later**

## 5. Fast routing table
| Work shape | Default lane | Notes |
|---|---|---|
| strategy / ambiguity / tradeoff | main-session | keep close to user |
| repeated internal execution | Ralph Loop | packetize + proof |
| irreversible external action | human gate | explicit approval |
| repeated prep for submission | Ralph Loop | handoff to human gate at the end |
| recurring topic hygiene / state updates | Ralph Loop or topic playbook | depending on scope |

## 6. Short reusable wording
> main-session decides, Ralph Loop executes repeated internal work, and humans enter only at manual/external gates.
