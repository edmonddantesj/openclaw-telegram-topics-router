# Principle — Idea → Schema → Proof → Registry (v0.1)

Last updated: 2026-02-20 (KST)
Status: ACTIVE
Exposure: OPEN

> This is an operating principle for Aoineco/AOI Core building.
> It explains why execution stays fast and consistent even as scope grows.

---

## TL;DR
**Idea → Schema → Proof → Registry. Everything else is optional.**

---

## Why it matters (the 5 levers)
1) **SSOT-first decisions**
   - Decisions live in files (`context/SSOT_INDEX.md` + SSOT docs), not in chat.
   - So work always resumes from “the next line in the SSOT.”

2) **Artifacts Standard (proof bundles)**
   - Every feature outputs the same backbone artifacts (`proof_manifest.json`, `sha256sum.txt`, `run_log.txt`, `decision_summary.md`).
   - Implementation becomes repeatable; verification becomes trivial.

3) **Hard MVP boundary, especially for money/on-chain**
   - Start with report-only / intent-first.
   - Any signing / execution / wallets / external posting is L3 → explicit approval.

4) **Schema-driven decomposition**
   - Define contracts (`merchant_profile`, `quote_request/response`, `routing_report`, `registry_index`) first.
   - Then code is “just generate these files.”

5) **Notion mirroring to prevent ‘documentation debt’**
   - Ship the decision and proof to Decision Log immediately.
   - No re-explaining later.

---

## Evidence (examples in this workspace)
- Artifacts standard: `aoi-core/docs/ARTIFACTS_STANDARD_V0_1.md`
- Bazaar registry bundle: `context/proof_samples/nexus_bazaar_registry_v0_1/`
- SSOT index: `context/SSOT_INDEX.md`
