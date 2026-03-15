# Nexus Bazaar — S‑DNA Verify Flow v0.1 (Upload section + verify-only) (SSOT)

Last updated: 2026-02-20 (KST)
Status: DRAFT
Exposure: TEASER (public-safe)

## Goal
Make S‑DNA a **first-class trust signal** in Bazaar without forcing modifications to any uploaded content.

## Core principles
1) Default = **verify-only** (report-only, no imprint).
2) Any “imprint/modify third-party artifact” requires **explicit consent + license check + Decision Log** (treat as L3).
3) S‑DNA verification affects **Trust UI** (badge + Core-Temperature uplift), but never claims absolute safety.

## Upload UI section (v0.1)
### Section name
- "S‑DNA Certification (optional)"

### Fields
- Checkbox: `Request S‑DNA verification` (default OFF)
- Input: `Target` (file path or proof bundle path)
- Optional: `Declared author_id` (string)
- Optional: `Declared sdna_id` (string)

### Output
- Generates `sdna_verify.json` (schema: `context/NEXUS_BAZAAR_SDNA_VERIFY_SCHEMA_V0_1.md`)
- Updates merchant trust snapshot (report-only; no mutation required):
  - `sdna_verified = true/false`

## Badge rules
- If latest verify result has `verified=true`:
  - show `🧬 S‑DNA` badge
  - Core-Temperature v0.1 uplift (as per spec): `+6`

## Artifacts
- `sdna_verify.json`
- `decision_summary.md` (optional in demo)
- `proof_manifest.json` + `sha256sum.txt` + `run_log.txt`

