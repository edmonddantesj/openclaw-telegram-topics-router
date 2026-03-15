# Survival — Bridge Autonomy & Security Notes v0.1 (History → Current mapping)

Last updated: 2026-02-20 (KST)
Status: NOTES (not implemented)

> Source: `context/aoi_core_history_inbox/conv_dump_20260220_102535.docx` (2026-02-11 convo dump)
> Purpose: extract **reusable security/ux principles** while clearly separating them from current implementation.

---

## 1) What the history claims (high-level)
- Cross-chain move concept: Base( Limitless ) → Solana( Meteora DLMM ) using deBridge(DLN) or Circle CCTP.
- Survival engine versions mentioned: v1.2 Trauma-Shield / v1.3 Omni-Sovereign.
- Autonomy tiers:
  - Tier1 Guarded Autonomy (small amounts auto, larger require approval)
  - Tier2 Condition-based Autonomy (only when conviction is extremely high)
  - Tier3 Full Autonomy (within seed budget)

## 2) Current workspace reality (facts)
- `the-alpha-oracle/engine/survival_logic_v1.py` exists but is a **risk-gate module** (no bridging, no Solana SDK).
- `the-alpha-oracle/submission.json` is V3-oriented and does **not** reflect the Solana narrative from the dump.
- Therefore: the bridge/autonomy system is **not currently implemented**; treat as roadmap only.

## 3) Principles worth keeping (L1/L2, safe to adopt as rules)
### 3.1 Interpretation-first approvals (Security Context Card)
When requesting approval for any sensitive action (bridge/payout/posting):
- Action summary (what/where/how much)
- Destination verification status (whitelist match)
- Threat assessment (LOW/MED/HIGH) + 1-2 human-readable reasons
- Worst-case scenario (bounded)

### 3.2 Guarded autonomy (default)
- Allow micro-autonomy only under **strict budgets** (per-tx + per-day caps).
- Anything above caps requires explicit approval.

### 3.3 Canary protocol for bridge/payout
- Never move the whole amount first.
- Send a tiny canary amount → confirm arrival → then proceed.

### 3.4 No unlimited approvals
- Avoid unlimited token approvals.
- Prefer exact-amount or one-time approvals.

### 3.5 Fixed destination gate
- Destination must be allowlisted + stable (no dynamic destination from untrusted input).

### 3.6 Prompt-injection isolation
- Any transfer/bridge decision must be derived from internal state only.
- External text sources (social/news) must not directly trigger transfer actions.

## 4) Implementation constraints (governance)
- Any real wallet signing / on-chain transfer automation is **L3**.
- Until L3 approval, only:
  - report-only simulations
  - policy docs
  - proof bundles

---

## Evidence
- Source dump: `context/aoi_core_history_inbox/conv_dump_20260220_102535.docx`
- Current minimal survival gate: `the-alpha-oracle/engine/survival_logic_v1.py`
- Current submission doc: `the-alpha-oracle/submission.json`
