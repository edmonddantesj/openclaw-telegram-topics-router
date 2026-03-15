# Smart-Manager — Product SSOT v0.1

Last updated: 2026-02-20 (KST)
Status: DRAFT
Exposure: TEASER (external) / STEALTH (detailed routing policies)

> Purpose: Define Smart-Manager as the product wrapper around AOI Core primitives.

---

## 1) What it is (definition)
**Smart-Manager** is an execution router that turns requests into governed work:
- chooses the cheapest capable model/tooling
- enforces Policy→Gate→Approval→Proof
- emits proof artifacts for audit

---

## 2) Core loop
1) Intake → classify (risk, exposure tier, L-level)
2) Plan → split into steps with required evidence
3) Gate → approvals required? (L3 always)
4) Execute → tool/model routing
5) Proof → artifacts + hashes
6) Record → Decision Log + SSOT updates

---

## 3) Outputs (artifact list)
- `plan.json` (steps, risk, required approvals)
- `run_log.txt` (commands, timestamps)
- `proof_manifest.json` (sha256, evidence paths)
- `decision_summary.md` (TL;DR + next actions)

---

## 4) Safety defaults
- Default mode: **report-only** unless explicitly approved.
- Money/wallet/signing/external posting are L3 → never auto.

---

## 5) Evidence
- AOI Core: `context/AOI_CORE_ALIGNMENT_MAP_V0_1.md`
- Model routing policy: `context/OPENAI_V1_AUTO_ROUTING_POLICY_V0_1.md`
