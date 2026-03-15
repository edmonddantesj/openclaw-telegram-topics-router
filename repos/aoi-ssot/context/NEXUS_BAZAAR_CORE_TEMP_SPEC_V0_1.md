# Nexus Bazaar — Core-Temperature (CPU 온도) Spec v0.1 (SSOT)

Last updated: 2026-02-20 (KST)
Status: DRAFT
Exposure: TEASER (public-safe)

## 0) Purpose
Provide a **single glance trust/quality signal** for merchants (like Carrot Market temperature), without implying profits or financial performance.

- This is a **trust/ops quality UI**, not a guarantee.
- Values are derived from **verifiable artifacts** (profiles, audit signals, proof bundles).

## 1) Scale & story
- Range: **0.0 – 99.9**
- Start: **0.0°C (Booting / Unverified)**
- Target line: **36.5°C (Human baseline trust)**
- Higher temps indicate stronger verification + consistent governance evidence.

## 2) Inputs (v0.1)
Core-Temperature uses **only** the following inputs:
- Merchant profile trust flags:
  - `guardian_pass` (boolean)
  - `guardian_tier` (T1/T2/T3)
  - `sdna_verified` (boolean)
- Evidence presence (optional, v0.1):
  - whether the registry entry has `latest_proof_sample` / `proof_samples`

## 3) Scoring (v0.1 default)
Baseline:
- `temp = 0.0`

Additions (simple, deterministic):
- `guardian_pass=true` → `+10`
- Tier bonus:
  - `guardian_tier=T2` → `+5`
  - `guardian_tier=T3` → `+10`
- `sdna_verified=true` → `+6`
- Has proof bundle pointer (`latest_proof_sample` or `proof_samples`) → `+4`

Clamp:
- `temp = min(99.9, max(0.0, temp))`

> Notes
> - v0.1 deliberately avoids “popularity”, “revenue”, or market-performance signals.
> - High-severity FAIL/quarantine drops are planned for v0.2 once we attach merchant-specific audit histories.

## 4) Display rules
- Show temp with label:
  - `0.0°C (Booting)` when temp==0
- Show badges alongside temperature:
  - `🛡️ Guardian` if guardian_pass
  - `🧬 S-DNA` if sdna_verified

## 5) Artifacts
- Spec (this file): `context/NEXUS_BAZAAR_CORE_TEMP_SPEC_V0_1.md`
- Compute (deterministic): `scripts/bazaar_core_temp_compute.py`
- Output (example):
  - `context/proof_samples/nexus_bazaar_registry_v0_1/registry_index_enriched.json`
  - `context/proof_samples/nexus_bazaar_registry_v0_1/core_temp_report.json`

