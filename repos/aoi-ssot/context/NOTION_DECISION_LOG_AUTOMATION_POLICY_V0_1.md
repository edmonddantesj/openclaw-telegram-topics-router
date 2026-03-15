# Notion Decision Log — Automation Policy (v0.1)

Date: 2026-02-20 (KST)
Owner: Edmond + Aoineco
Status: READY

## 0) Purpose
Standardize when and how we auto-create Notion Decision Log entries for SSOT changes.

## 1) Allowed automation scope (L1/L2)
Auto-create Decision Log entries for:
- SSOT status changes (e.g., DRAFT → READY)
- New policy documents (READY)
- New deterministic proof tests / CI gates
- Naming / exposure / publishing guardrail changes

**Never auto-create** entries for L3 actions (money, wallets, on-chain signing, external public posts).

## 2) Triggers (recommended)
Trigger a Decision Log entry when any of the following happens:
1) A document under `context/` or `aoi-core/docs/` changes `Status:` line
2) A new `context/*_POLICY_*.md` is created
3) A new GitHub Action workflow is added/modified under `.github/workflows/`
4) A new deterministic runner/test script is added under `scripts/` (proof-related)

## 3) Required fields
- Title
- Summary (TL;DR)
- Evidence paths (comma-separated local paths)
- Constraints (L1/L2/L3 & exposure tiers)
- Next actions (semicolon-separated)
- Tags

## 4) Implementation
- Primary writer:
  - `scripts/notion_decision_log_mirror.py create ...`
- Helper (this repo):
  - `scripts/notion_decision_log_auto.py` (dry-run by default)

## 5) Evidence
- Decision Log target SSOT: `context/NOTION_DECISION_LOG_TARGET_SSOT_V0_1.md`
