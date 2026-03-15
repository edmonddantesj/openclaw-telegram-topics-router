# V6 Diversified Yield (Base+Solana+Bridge) — Build Plan v0.1 (SSOT)

> ⚠️ L3 SAFETY GATE (HARD RULE)
> - Any **real fund movement** (bridge/swap/deposit/withdraw/reposition) is **FORBIDDEN** until Edmond gives explicit **YES**.
> - This doc is **PLAN + TODO only**. Shadow monitoring is allowed; execution is opt-in.
> - Never print secrets/seed/API keys. Use `secret_ref` only.

## 0) Goal
Automate **Base alpha (Limitless) + Solana fee yield (Meteora DLMM) + Bridge (deBridge/DLN)** under **Fail-closed + Proof-first** so the system can (eventually) offset LLM/API operating costs with on-chain revenue.

## 1) Design Principles (Upgrade vs “policy-doc + shadow logging”)
1. **Fail-closed default**: if any check is uncertain → HALT.
2. **Proof-first always**: every run emits an evidence bundle + sha256 manifest.
3. **Shadow→Canary→Live promotion**:
   - Shadow: read-only, no signing.
   - Canary window: 12h guardrail stage.
   - Live eligibility: **48 consecutive healthy cycles**.
4. **Low-frequency edge**: reduce churn (bridges/repositions) to cut fees + operational mistakes.

## 2) SSOT / Files (What is canonical)
- Policy SSOT: `context/COMPOSITE_DIVERSIFIED_YIELD_POLICY_V1_2026-02-17.md`
- Action-plan schema: `context/V6_ACTION_PLAN_SCHEMA_V0_1.json`
- V6 outputs: `the-alpha-oracle/results/v6_*.json`
- Proof generator: `scripts/gen_v6_manifest.py`
- Safe execution wrapper: `scripts/safe_run.sh`

## 3) Data Pipeline (Shadow)
- Source: `the-alpha-oracle/results/v6_*.json`
- Shadow log sink: `scripts/v6_to_supabase_predictions.py` (already exists)
- Settlement (TBD): `scripts/shadow_settle_predictions.py`
  - If missing, create it. Must be **shadow-only** (no on-chain).

## 4) Gate Engine (Decision → next_steps queue)
- Engine: `the-alpha-oracle/engine/survival_logic_v2.py`
- Output: `action_plan.next_steps[]` (2–4 candidates, prioritized)
- Required gates should be explicit, e.g.
  - `HUMAN_APPROVAL` (for any execution)
  - `BRIDGE_ALLOWLIST_OK`
  - `CANARY_WINDOW_OK`
  - `VAULT_PRESENT_OK` (presence only; never print)

## 5) Proof-first Artifacts (Run bundle)
Every cycle:
- Generate: `artifacts/runs/<YYYY-MM-DD>/v6/<run_id>/manifest.json`
- Include sha256 for:
  - inputs (policy snapshot hash, v6 json hash)
  - produced decision (action_plan)
  - external reads (quote/raw responses)

## 6) Solana DLMM Integration Plan
### 6.1 Official references
- `@meteora-ag/dlmm`, `MeteoraAg/dlmm-sdk`, docs functions for pool state/range/fees.

### 6.2 Shadow monitor (NEW; execution OFF)
- Create: `scripts/solana_dlmm_shadow_monitor.py`
- Scope (read-only):
  - pool state, time-in-range estimate, fee accrual estimate
  - NO deposit/withdraw/reposition
- Output logs → proof bundle

### 6.3 Operator (promotion stage; execution ON only after L3)
- Create: `scripts/solana_dlmm_operator.py`
- Allowed triggers (low frequency):
  - `out_of_range >= 6h` OR `SOL_ratio < 70%`
- Actions: deposit/reposition/exit (all require L3)

## 7) Bridge Module (deBridge/DLN) — PLAN-ONLY first
- Allowlist route + pinned destination addresses.
- Canary: **2 USDC canary** then threshold move.
- Rate limits:
  - Bridge max **1/day**
  - Move only **50% of Base USDC above $8** (policy)
- Never execute without L3.

## 8) Yield Optimization (Costs ↓, Stability ↑)
- Base alpha: keep **≤2 actions/week** (fee drag↓)
- DLMM: prefer **wider ranges** (reposition frequency↓)
- Overall: “rare actions, long duration”

## 9) Wallet Separation (Security)
Maintain separate wallets/contexts:
- Trading (Base)
- Bridge (Base)
- Solana staging
- Solana LP

Store only as `secret_ref` in state files.

## 10) KPI Digest (Daily)
One page digest (Telegram/Notion) must include:
- Shadow win-rate, avg pnl, unsettled count
- gas+slippage ratio (estimated)
- DLMM time-in-range, DLMM fee accrual estimate

## 11) Promotion Condition (when to scale Base)
Only increase Base weight if:
- `Base 14D >= DLMM 14D + 3%p`
- `MDD > -8%`
- `cost_ratio < 15%`
Then Base allocation may rise 20% → up to 50% (cap).

## 12) TODO Checklist (Implementation order)
1. [T0] Create state SSOT for investment/wallet connection (no secrets printed)
2. [T1] Confirm `shadow_settle_predictions.py` existence; if missing, implement shadow settlement.
3. [T2] Implement `solana_dlmm_shadow_monitor.py` (read-only).
4. [T3] Wire `gen_v6_manifest.py` to include DLMM monitor outputs.
5. [T4] Add daily digest section for diversified yield KPIs.
6. [T5] (After L3) implement operator + bridge execution modules.

## 13) Resume Protocol (After reset)
To resume quickly:
- Read: `CURRENT_STATE.md` + this doc
- Read state: `aoi-core/state/investment_state.json`
- Run shadow checks only:
  - `python3 the-alpha-oracle/engine/v6_pipeline.py`
  - `python3 scripts/solana_dlmm_shadow_monitor.py` (once created)
- Do not execute any on-chain actions unless L3 YES is re-confirmed.
