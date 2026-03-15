# Bazaar Parallel Discussion Restore — 2026-03-15

## Why this restore was needed
User reported that in Bazaar topic, analyzer/청뇌 behaved as if team parallel discussion / multi-member summon was unavailable, even though that operating mode had existed before.

## Evidence checked
- Memory confirms explicit multi-call / autonomous dialogue intent existed:
  - `memory/2026-03-12.md`
  - `둘이 논의해` / `둘이 얘기해` as explicit dialogue trigger
  - router spec + dialogue runtime + owner selection logic were created
- Current workspace still had the core shared docs:
  - `context/AOINECO_ROUTER_SPEC_V0_1.md`
  - `context/AOINECO_AGENT_TO_AGENT_DIALOGUE_RUNTIME_V0_1.md`
  - `context/heukmyo-squad/CHEONGMYO_HEUKMYO_SUPPORT_PROTOCOL_ONEPAGE_V0_1.md`
- Prewipe backup confirmed the same docs existed there too.

## Diagnosis
The feature was not fully missing at the global SSOT level.
The practical gap was that Bazaar-specific durable guidance did not clearly encode:
- explicit multi-call trigger phrases
- owner override behavior for discussion mode
- expected output shape for team discussion

As a result, Bazaar owner (청뇌/analyzer) could fall back to single-owner behavior.

## Restore applied
Updated:
- `context/topics/bazaar_PLAYBOOK_V0_1.md`
- `context/topic-state/bazaar.md`

Restored behavior:
- explicit multi-call triggers recognized in Bazaar
- owner 1-person mode should yield to parallel review when discussion is requested
- default composition examples added (strategy / implementation / risk / documentation)
- output format fixed to: participants → key issues → consensus → next action

## Operational interpretation
This is a durable policy restore for Bazaar topic behavior.
It restores the intended operator-facing rule even if runtime heuristics were drifting toward single-owner replies.
