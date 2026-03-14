# RALPH_LOOP_SUPPORT_AND_RETURN_SYSTEM_V0_1

Status: SSOT (local)
Last updated: 2026-03-14
Owner: 청정
Scope: Ralph Loop support-request / execution / result-return system optimized for repeated internal work

## Purpose
Build a Ralph Loop-native system that receives support requests from other topics, converts them into executable packets, runs repeatable work automatically where possible, and returns proof-based results back to the source topic.

This is not a human-helpdesk clone.
It is a **packetized operating bus** for repeated internal work.

## Core principle
- topic room keeps domain truth
- Ralph Loop receives repeated support-shaped work
- Ralph Loop normalizes / decomposes / executes / returns
- human gate appears only at manual / external / irreversible boundaries

## Input contract: Support Request Packet
Every support request that enters Ralph Loop should resolve into a packet with at least:
1. source topic
2. request summary
3. owner
4. priority
5. one-line next action
6. proof path or expected proof path
7. return target
8. judge rule
9. human gate flag

## Minimal request shape
- STATUS: starting | in_progress | blocked
- HANDOFF: source topic + current owner + target lane
- NEXT: one-line next action
- DoD: what minimum output counts as done
- AC: what concrete checks must pass
- Judge: pass / fail / hold / needs-human-review

## Request classification
### A. auto-triable
Ralph Loop may execute immediately when the request is:
- intake triage
- backlog slicing
- packetization
- evidence attach / proof routing
- scout / benchmark / deadline sweep
- repeated checkpoint packaging
- repeated result formatting / return preparation

### B. semi-auto
Ralph Loop may create packet + first-pass output when the request is:
- longform summary-first triage
- x-post shortlist/filter/extract
- hackathon candidate/benchmark/signal extraction
- bazaar checkpoint/proof/scope packetization

### C. human-gated
Ralph Loop must stop at `needs-human-review` when the request reaches:
- login / account identity
- submission / application final send
- payment / signing / wallet action
- external publish / outward message send
- irreversible production exposure

## Execution sequence
1. detect incoming support-shaped request
2. normalize into support request packet
3. classify as auto-triable / semi-auto / human-gated
4. create or update parent/child/handoff artifacts
5. execute repeated internal portion
6. produce result return packet
7. return to source topic or handoff target
8. escalate only if human gate is reached

## Output contract: Result Return Packet
Every completed or paused Ralph Loop support cycle should return:
- state
- what changed
- proof
- next
- judge verdict
- human gate needed or not

## Minimal result shape
- STATUS: done | blocked | review
- PROOF: file= | url= | cmd= | sha=
- NEXT: one-line next action or `NEXT: none`
- Judge: pass / fail / hold / needs-human-review

## Standard support lanes
### Longform
- request: summarize / route / study packetize
- return: summary path / synthesis candidate / next study action

### X-post
- request: discovery / anti-dup / quote extraction / packet prep
- return: shortlist + selected candidate or null-result + blocker log

### Hackathons
- request: scout / deadline / benchmark / signal / synthesis
- return: candidate status + blocker + next package action

### Bazaar
- request: backlog slice / checkpoint packet / proof route / scope guard
- return: today / blocker / next + public-safe/liveness boundary note

### Random-derived support
- request: mixed item that should leave random
- return: routed destination + tracked artifact pointer

## Automation-first rule
If a request is L1/L2-safe and packetizable, Ralph Loop should prefer:
1. normalize automatically
2. create/update tracked artifact automatically
3. return proof-based result automatically
instead of asking the human how to structure it.

## AC/Judge layer for support bus
### Definition of Done
- support request becomes an executable packet
- repeated internal part is executed or explicitly held
- result return packet exists with proof + next + verdict

### Acceptance Criteria
- source topic truth and Ralph execution truth are separated
- packet shape is explicit
- one-line next action exists
- proof path exists
- return rule exists

### Judge rule
- `pass`: request became executable and returned a proof-based result packet
- `fail`: packet is missing core execution metadata or proof path
- `hold`: packet structure exists but current run/result is still absent
- `needs-human-review`: manual/external/irreversible boundary reached

## Human gate rule
Human gate is invoked only when Ralph Loop reaches the real boundary of:
- external submission
- final publish
- signing/payment
- manual account action
- irreversible live operation

## First rollout target
Apply this system first to already-delegated Ralph Loop lanes:
1. longform
2. x-post
3. hackathons
4. bazaar
5. random-derived routed support items

## Short reusable wording
> Ralph Loop support is a packetized operating bus: receive request, normalize, execute repeatable internal work, return proof-based result, escalate only at human gates.
