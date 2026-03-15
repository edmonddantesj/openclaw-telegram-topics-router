# AOI Council — Proof Pack Schema v0.1

Date: 2026-02-21 (KST)
Owner: Edmond + Aoineco
Status: DRAFT

## Purpose
Define the **auditable, investor/judge-friendly evidence bundle** that AOI Council Pro must generate per run.

This is the concrete “what you get” that makes Pro worth buying:
- reproducibility
- governance/policy compliance
- decision traceability

## Folder layout (per run)
Recommended base path:
- `context/proof_samples/council_runs/<run_id>/`

Minimum files:
1) `report.md`
- Human-readable council output (fixed format: TL;DR → role opinions → consensus/conflict → dissent → assumptions → verdict → next actions).

2) `manifest.json`
- Machine-readable run manifest.
- Includes run_id, timestamp, executor(lite|pro), roster, per-role status/timestamps, and output paths.

3) `policy_check.json`
- Results of governance compliance checks.
- Must include:
  - exposure tier compliance (OPEN/TEASER/STEALTH/TOP SECRET)
  - L1/L2/L3 boundary checks
  - public-final repo mutation checks (hackathon submissions)

4) `diff_from_last_run.md` (optional but recommended)
- What changed compared to the last run on the same topic key.
- Helps avoid “decision drift”.

5) `actions.md` (or `actions.sh`)
- Executable next steps (commands + file paths) for operators.
- Must be safe by default (dry-run / report-only unless explicitly approved).

6) `summary.html` (P2 but strongly recommended)
- 1-page visual summary for investors/judges.
- Includes verdict, confidence, risks, and key evidence links.

## Data retention & safety
- No secrets, API keys, tokens, or vault files.
- If any input evidence_paths include secrets → redact or refuse pack generation.

## Versioning
- Pack schema version must be recorded in `manifest.json`.
