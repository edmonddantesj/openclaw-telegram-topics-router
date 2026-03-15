# AOI Squad Pro — Lite vs Pro Diff (v0.1)

Purpose: capture what changed from the early “Lite” concept to the current “Pro (Ops OS)” product direction.

---

## 1) One-line definitions
- **Lite (early concept)**: **Safe install + update + smoke** kit for OpenClaw skills (guardrails to avoid footguns).
- **Pro (current)**: **Proof-first Agent Ops OS** — runs are standardized as **approve → run → proof** and produce verifiable evidence bundles.

---

## 2) Category shift (why it’s not an Ensoul clone)
- Lite: tooling / packaging.
- Pro: **operating system for verifiable ops** (governance + evidence + risk controls).

Ensoul-like systems focus on *identity/soul construction*.
AOI Squad Pro focuses on **reproducibility, auditability, and safe automation**.

---

## 3) Feature checklist
### Lite (what we had)
- [x] Installer + updater (tag-based)
- [x] Allowlist gate (fail-closed)
- [x] Quickstart + demo scripts
- [x] Minimal QA safety regression runner

### Pro (what we added / became)
- [x] **Core promise**: approve → run → proof
- [x] **Proof Bundle**: artifacts + logs + sha256 + manifest (`proof.json`)
- [x] **Ops-native output schema (6 dimensions)**
  - Intent / Action / Artifacts / Risk-Gates / Result / Next
  - SSOT: `aoi-core/docs/AOI_SQUAD_PRO_OPS_OUTPUT_SCHEMA_V0_1.md`
- [x] **Governance tiers**: L1/L2/L3 embedded into product behavior
- [x] **Risk gates**: Shadow → Canary → Live (caps + kill-switch patterns)
- [x] **SSOT sync mindset**: local + Notion + Supabase to preserve ops history
- [x] **Public-safe assets**
  - Proof sample (masked): `context/PROOF_BUNDLE_SAMPLE_LIMITLESS_SHADOW_V0_1.md`
  - Copy pack (KR/EN): `context/AOI_SQUAD_PRO_PRODUCT_COPY_KR_EN_V0_1.md`
- [x] **One-click demo**: generates a proof bundle folder in one shot
  - Script: `scripts/aoi_squad_pro_oneclick_demo.sh`
- [x] **GTM scaffolding**
  - First customers & pricing: `context/AOI_SQUAD_PRO_FIRST_CUSTOMERS_AND_PRICING_V0_1.md`
  - GTM checklist: `context/AOI_SQUAD_PRO_GO_TO_MARKET_CHECKLIST_V0_1.md`

---

## 4) “Proof-first” impact
- Lite success criteria: installs cleanly + smoke passes.
- Pro success criteria: runs produce **verifiable receipts** (artifacts + sha256) and can be audited/reproduced.

---

## 5) What changed in our development philosophy
- Lite mindset: “make it easy to install and not break.”
- Pro mindset: “make it **hard to claim done without evidence**.”

---

## 6) Next steps
1) Add a README section: **One-click demo → proof bundle created**.
2) Add optional public-safe scanner output into the proof bundle (PASS/FAIL) for share-ready artifacts.
3) Convert the Quickstart draft into a polished 10-minute onboarding path with expected outputs.
