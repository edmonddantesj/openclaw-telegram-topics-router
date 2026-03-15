# Audit Stall Run (Demo)

## TL;DR
- Audit: **guardian_report_v0** (merchant: **merchant_guardian_audit**)
- Verdict: **PASS** (tier T1, risk low)

## Input
- file: `scripts/bazaar_registry_generate.py`
- sha256: `0f8cc407825c09f1a129c0277b21d9c99e573bcd58dd4cae6049f4712cae5b64`

## Findings
- (none)


## Guardrails
- Demo is deterministic and does not execute the input.
- Report-only: no signing, no external effects.
- Evidence-first: proof_manifest + sha256sum + run_log.
