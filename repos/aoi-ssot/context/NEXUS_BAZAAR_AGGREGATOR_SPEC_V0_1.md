# Nexus Bazaar — Aggregator / Router Spec v0.1 (SSOT)

Last updated: 2026-02-20 (KST)
Status: DRAFT
Exposure: TEASER (concept) / STEALTH (routing + risk rules) / TOP SECRET ($AOI treasury/tokenomics)
Owner: Edmond (PO)

> Purpose: Define the **Aggregator/Router** as the AOI Core-safe way to connect many merchant agents (“FX/SWAP stalls”) without becoming a custodial exchange.

---

## 0) Design stance (hard)
- We do **not** run a central AMM by default.
- We do **not** execute trades automatically.
- Default is **report-only (intent + proof)**. Any live execution is L3 and requires explicit approval.

---

## 1) Layers

### L0) Nexus Bazaar (Market)
- A market of skills/agents/data/services.
- Includes optional **FX/SWAP stalls** as a sub-market.

### L1) Merchant Stall (agent-run)
- A merchant publishes quotes and constraints.
- Merchant may internally use AMM/OTC/RFQ strategies.
- For MVP, we treat merchant as **RFQ/OTC quote provider**.

### L2) Aggregator / Router (AOI Core)
- Collects quotes from multiple merchants.
- Scores trust/risk.
- Recommends a route.
- Emits proof artifacts.

---

## 2) MVP scope (Phase 1: RFQ/Intent)

### In scope
- Merchant registry (public-safe profile)
- Quote request/response
- Comparison + ranking
- Rejection reason normalization
- Proof bundle generation (Artifacts Standard v0.1)

### Out of scope (vNext)
- On-chain AMM pools operated by us
- Automatic execution / signing
- Custody / treasury management
- Profit-sharing tokenomics

---

## 3) Data contracts (v0.1)

### 3.1 Merchant profile (`merchant_profile.json`)
Required fields:
- `merchant_id` (string)
- `name` (string)
- `supported_pairs` (e.g., "USDC/ETH", "USDC/SOL")
- `quote_modes` (e.g., ["RFQ", "OTC"])
- `min_size`, `max_size`
- `fees_model` (text)
- `constraints` (KYCless/allowlist/region etc. as text; avoid legal claims)
- `evidence`:
  - `guardian_pass` (bool)
  - `sdna_verified` (bool)
  - `core_temp` (number or null; TEASER)

### 3.2 Quote request (`quote_request.json`)
- `request_id`
- `pair`
- `side` (BUY/SELL)
- `amount_in` or `amount_out` (one must be provided)
- `slippage_bps_max` (optional)
- `deadline_ms` (optional)
- `caller_context` (free text; must be public-safe)

### 3.3 Quote response (`quote_response.json`)
- `request_id`
- `merchant_id`
- `status` (OK/REJECT)
- if OK:
  - `price`, `amount_out`, `fee_estimate`, `valid_until`
  - `settlement_options` (e.g., ["x402", "invoice", "onchain-intent"]) — **no signing** in MVP
- if REJECT:
  - `reject_reason_code` (enum)
  - `reject_reason_human`

### 3.4 Reject reason codes (initial)
- `PAIR_UNSUPPORTED`
- `SIZE_TOO_SMALL`
- `SIZE_TOO_LARGE`
- `NO_LIQUIDITY`
- `RISK_POLICY_BLOCK`
- `TIMEOUT` (merchant did not respond before deadline)
- `QUOTE_EXPIRED` (quote validity window elapsed)

---

## 4) Routing / ranking (public-safe)
Ranking score inputs (public-safe names):
- Best effective price (including fee)
- Quote freshness / validity window
- Merchant trust signals:
  - Guardian pass
  - S‑DNA verified
  - Core-Temp (optional)
- Risk flags (region/constraints mismatch)

**Note:** Exact weights/thresholds are STEALTH.

---

## 5) Proof artifacts (must emit)
Must comply with: `aoi-core/docs/ARTIFACTS_STANDARD_V0_1.md`

Minimum for an RFQ comparison run:
- `quote_request.json`
- `merchant_profiles/<merchant_id>.merchant_profile.json` (N files)
- `quotes/<merchant_id>.quote_response.json` (N files)
- `routing_report.json` (standard reason codes + eligibility)
- `decision_summary.md` (human-readable)
- `proof_manifest.json`
- `sha256sum.txt`
- `run_log.txt`

---

## 6) Governance mapping
- L1/L2: simulate, report-only, create drafts, write specs
- L3: any signing, real swaps, treasury moves, external posting → explicit approval

---

## 7) Success metrics (MVP)
- Quote success rate (non-timeout)
- Median latency to best quote
- Evidence completeness (missing artifact = 0 tolerance)
- Failure taxonomy coverage (reject codes mapped)

---

## 8) Evidence
- Artifacts standard: `aoi-core/docs/ARTIFACTS_STANDARD_V0_1.md`
- Naming mapping: `context/NAMING_MAPPING_TABLE_V0_1.md`
- Exposure tiers: `context/EXPOSURE_TIER_MATRIX_V0_1.md`
- Proof sample (RFQ demo, 3 merchants + merchant profiles): `context/proof_samples/bazaar_rfq_demo_20260220_124616/`
