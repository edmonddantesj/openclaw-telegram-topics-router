# Skill Stall Run (Demo)

## TL;DR
- Skill: **summarizer_lite_v0** (merchant: **merchant_summarizer_lite**)
- Output: deterministic extractive summary (no external LLM calls).

## Inputs
- text_len: 140
- max_sentences: 2

## Output
Nexus Bazaar is a proof-first market for agent services and settlement tools. This demo shows a skill merchant emitting auditable artifacts.

## Guardrails
- Report-only: no external calls, no secrets.
- Evidence-first: proof_manifest + sha256sum + run_log.
