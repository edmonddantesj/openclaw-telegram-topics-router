# Audit Stall Run (Demo)

## TL;DR
- Audit: **guardian_report_v0** (merchant: **merchant_guardian_audit**)
- Verdict: **FAIL** (tier T1, risk high)

## Input
- file: `context/proof_samples/audit_stall_demo_20260220_140316_fail/fail_sample.txt`
- sha256: `c7b3b8d6bf10a616aa2cd5cbe099ecc69d7900246d23fc85eaede22460bb42e2`

## Findings
- PRIVATE_KEY_BLOCK (high): Private key marker detected


## Guardrails
- Demo is deterministic and does not execute the input.
- Report-only: no signing, no external effects.
- Evidence-first: proof_manifest + sha256sum + run_log.
