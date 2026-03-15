# 7 Pillars Audit (Draft) v0.1

Last updated: 2026-02-20 (KST)
Owner: TFT / Track 3 (PILLARS)
Status: DRAFT (evidence-first)

Purpose: Align the **7 main pillars** across (1) product SSOT, (2) memory decisions, (3) history inbox evidence. For each pillar we capture:
- **Definition** (what it is)
- **Current SSOT** (where the “truth” currently lives)
- **Evidence paths** (files that substantiate it)
- **What’s missing** (gaps to close for platform/whitepaper/brand consistency)
- **Next action** (tight, executable)

Primary inputs used:
- `context/AOI_CORE_PRODUCT_VISION_V0_1.md`
- `MEMORY.md`
- `context/aoi_core_history_inbox/*.docx.txt`

---

## Pillar 1) S-DNA

### Definition
A provenance + integrity standard that binds **author/ownership + immutability + runtime verification** into a usable watermark.
- Triple Helix:
  - **Layer 1 Visible (human)**: headers/annotations for author/license/integrity
  - **Layer 2 Structural (machine)**: parseable metadata patterns (e.g., `sdna={...}`)
  - **Layer 3 Behavioral (runtime handshake)**: runtime handshake to verify origin + detect tampering
- Operational role: enables **fast-track vs scan vs quarantine** decisions and connects to **royalty settlement**.

### Current SSOT
- Primary: `context/AOI_CORE_PRODUCT_VISION_V0_1.md` (Definitions: S-DNA; S-DNA × Guardian flow)
- Secondary (curated decisions): `MEMORY.md` (S-DNA Protocol v1.0, handshake logic)

### Evidence paths
- Product SSOT: `context/AOI_CORE_PRODUCT_VISION_V0_1.md` (Definitions; Core Loop; S-DNA × Guardian flow)
- Memory: `MEMORY.md` → section “S-DNA Protocol v1.0 (Triple Helix)”
- History inbox:
  - `context/aoi_core_history_inbox/aoi_core_history_20260220_095452.docx.txt` (S-DNA triple helix, handshake routing, royalty sketch)
  - (supporting vision fragments) `context/aoi_core_history_inbox/aoi_core_history_20260220_094119.docx.txt`, `...094321...`, `...094953...`

### What’s missing
- **Formal spec artifact** (public-safe + restricted split): JSON schema / headers / structural tags / handshake protocol messages.
- **Reference implementation**: libraries/adapters that can be embedded into skills + AOI Core runs.
- **Verification tooling**: `sdna verify` CLI + CI gate + proof bundle integration.
- **Royalty linkage**: how S-DNA maps to royalty ledger entries in B-min (fields, tiering, exceptions).
- **Threat model**: replay, spoofed authorship, partial copying, hash collision assumptions.

### Next action
1) Create `context/SDNA_PROTOCOL_SPEC_V0_1.md` (public-safe spec) + `context/SDNA_PROTOCOL_SPEC_RESTRICTED_V0_1.md` (handshake details).
2) Add a minimal `sdna.json` schema + reference code stub and attach to proof bundle template.
3) Add S-DNA verification to Skill-Guardian scan pipeline decisioning.

---

## Pillar 2) Skill-Guardian

### Definition
Security + trust audit infrastructure for skills (especially external skills) to make marketplace trade **safe and verifiable**.
- 3-tier model:
  1) **Static** scan (license, dependencies, suspicious patterns)
  2) **Behavioral** scan (runtime behaviors, network, filesystem, secrets)
  3) **Rebuild** (salvage/remove risk; “살리면서 거세”)

### Current SSOT
- Primary: `context/AOI_CORE_PRODUCT_VISION_V0_1.md` (Definition; Guardian + Sentry = immune system; S-DNA × Guardian flow)
- Operational governance: `context/SKILL_SCOUTING_GOVERNANCE.md`, `context/COMMAND_DOIP_HAEJWO_PROTOCOL_V0_*.md` (adopt→verify→contact→rebuild→install order)

### Evidence paths
- Product SSOT: `context/AOI_CORE_PRODUCT_VISION_V0_1.md`
- Memory: `MEMORY.md` (OPUS priority list includes Guardian Tier3 Rebuild)
- History inbox:
  - multiple conv dumps mention Tier3 rebuild + scan gating (see `context/aoi_core_history_inbox/` extracted `.docx.txt` files around 2026-02-20)
- Supporting governance artifacts:
  - `context/SKILL_SCOUTING_GOVERNANCE.md`
  - `context/SQUAD_AUTONOMY_AND_SKILL_GOVERNANCE_SOP_V0_1.md`
  - `context/RESTRICTED_CLASSIFICATION_TABLE_V0_1.md`

### What’s missing
- **Single Skill-Guardian SSOT spec**: what is “Tier1/Tier2/Tier3” as executable checks with outputs.
- **Evidence outputs**: standardized guardian report format to attach to proof bundles.
- **Marketplace integration**: how Guardian results map to Nexus Bazaar listing eligibility + fee incentives.
- **Rebuild playbooks**: deterministic refactor patterns, test harness, and “safe fork/lite” conventions.

### Next action
1) Write `context/SKILL_GUARDIAN_SPEC_V0_1.md` with tier definitions + output schema.
2) Create a `guardian_report.json` artifact and require it for external skill adoption.
3) Define Nexus Bazaar listing gates: `guardian_pass` + `sdna_verified` tiers.

---

## Pillar 3) Context-Sentry

### Definition
A context/TPM efficiency engine:
- Noise filter (regex / low-cost)
- Semantic compression (LLM-cost, meaning-preserving)
- Priority retention (what must not be forgotten)

Goal: reduce burn, prevent context overflow, keep decision-critical memory.

### Current SSOT
- Primary: `context/AOI_CORE_PRODUCT_VISION_V0_1.md` (Definitions; freemium strategy)
- Secondary: `MEMORY.md` (Survival Engine cost control includes Context-Sentry)

### Evidence paths
- Product SSOT: `context/AOI_CORE_PRODUCT_VISION_V0_1.md` (Definitions; freemium: regex free, semantic paid)
- Memory: `MEMORY.md` (Survival Engine 2.1 cost-control bullet)
- Related operational docs:
  - `context/OPENAI_V1_AUTO_ROUTING_POLICY_V0_1.md` (model switching governance)
  - `context/ACP_AUTOMATION_FLAGS_AND_APPROVALS_V0_1.md` / `context/SECURITY_GATE_CHECKLIST_V0_*.md` (approval + safe execution patterns)

### What’s missing
- **Clear product boundary**: where Context-Sentry ends and general “memory” begins.
- **Compression quality metrics**: retention tests, regression benchmarks.
- **Artifacts**: `context_sentry_report.json` to prove compression decisions.
- **Pricing packaging**: exact free/paid gates in Bazaar/Pro.

### Next action
1) Create `context/CONTEXT_SENTRY_SPEC_V0_1.md` (layers, IO contracts, eval metrics).
2) Add proof bundle artifacts for compression decisions.
3) Tie into Survival Engine mode switching (cost/benefit threshold).

---

## Pillar 4) Nexus Oracle Ω

### Definition
A multi-agent collective verdict engine:
- 9 agent signals fused via **Bayesian log-odds** to produce direction + confidence.
- If confidence < threshold (e.g., 0.55), **Oracle Veto** forces HOLD.
- Risk shutdown via **Circuit Breaker (Blue-Med)**.
- Delivery models:
  - **Ω Full (SaaS)**: 9-agent infra operated by us
  - **Ω Lite (self-hosted)**: sequential modules (~75% precision)

### Current SSOT
- Primary: `context/AOI_CORE_PRODUCT_VISION_V0_1.md` (Definitions)
- Secondary: `MEMORY.md` (Verdict model, Veto gate, Full vs Lite)

### Evidence paths
- Product SSOT: `context/AOI_CORE_PRODUCT_VISION_V0_1.md` (Nexus Oracle Ω, Omega Fusion Engine, Veto, circuit breaker)
- Memory: `MEMORY.md` (Ω details + source pointers)
- History inbox:
  - `context/aoi_core_history_inbox/aoi_core_history_20260220_094707.docx.txt` (Ω fusion + Veto gate + delivery models)

### What’s missing
- **Public-safe explanation** of fusion math vs restricted parameters.
- **Operational run spec**: how a verdict becomes an approved action (ties to Policy/Gate/Approval/Proof).
- **Calibration evidence**: backtests / simulation harness + proof bundles.
- **Role mapping**: how “9 agents” map to AOI/CHUNGHO brand modules without leaking restricted info.

### Next action
1) Split Ω documentation: public architecture + restricted parameterization.
2) Define `oracle_verdict.json` artifact + attach to proof bundles.
3) Create calibration runbook and store representative proof samples.

---

## Pillar 5) Nexus Bazaar

### Definition
Vision-layer marketplace: **Skill DEX + Social Ecology**.
- Skills are discovered, traded, swapped; reputation tracked via **Core-Temperature**.
- Trust primitives: Skill-Guardian + S-DNA.
- Settlement: x402 micro-pay + ledger accounting + royalty distribution.

### Current SSOT
- Primary: `context/AOI_CORE_PRODUCT_VISION_V0_1.md` (Definitions; vNext loop; mechanics)
- Secondary: `MEMORY.md` (AOI Core vision summary)

### Evidence paths
- Product SSOT:
  - `context/AOI_CORE_PRODUCT_VISION_V0_1.md` (Nexus Bazaar, Skill DEX, Core-Temp, settlement)
- Memory:
  - `MEMORY.md` (AOI Core vision block)
- History inbox:
  - `context/aoi_core_history_inbox/aoi_core_history_20260220_094119.docx.txt`
  - `context/aoi_core_history_inbox/aoi_core_history_20260220_094321.docx.txt`
  - `context/aoi_core_history_inbox/aoi_core_history_20260220_094953.docx.txt`

### What’s missing
- **Market mechanics SSOT**: pricing, liquidity, listing constraints, reputation computation.
- **Core-Temperature rules** (increase/decrease triggers) as code + policy.
- **Settlement implementation detail**: ledger schema, payout flows, dispute resolution.
- **Exposure tier plan**: what is OPEN vs TEASER vs STEALTH for Bazaar features.

### Next action
1) Create `context/NEXUS_BAZAAR_MECHANICS_SPEC_V0_1.md` (Core-Temp, fees, listing eligibility).
2) Create a minimal ledger + statement generator for royalties (align with B-min decisions).
3) Define “Bazaar MVP” boundaries (registry first; trade later).

---

## Pillar 6) Survival Engine 2.1

### Definition
An agent self-sustaining engine: agents must **earn their own LLM cost**.
- Mode switching by revenue/cost ratio:
  - EXPAND ≥ 1.5
  - SUSTAIN 0.8–1.5
  - CONTRACT < 0.8
- Revenue sources: DLMM yield, oracle scalping, skill sales, x402.
- Cost control: Context-Sentry + model switching.

### Current SSOT
- Primary: `context/AOI_CORE_PRODUCT_VISION_V0_1.md` (definition)
- Secondary: `MEMORY.md` (ratio thresholds + revenue/cost model)

### Evidence paths
- Product SSOT: `context/AOI_CORE_PRODUCT_VISION_V0_1.md` (Survival Engine 2.1)
- Memory: `MEMORY.md` (detailed thresholds, mode switching; OPUS constraints)
- History inbox:
  - `context/aoi_core_history_inbox/aoi_core_history_20260220_094539.docx.txt` (Survival Engine definition)

### What’s missing
- **Operational implementation**: where ratios are computed, where actions are enforced.
- **Proof**: how “earned cost coverage” is evidenced (ledger, tx, statements).
- **Safety gates**: preventing “auto money” claims; default dry-run/confirm.
- **Integration map**: Survival Engine ↔ Context-Sentry ↔ Oracle ↔ Bazaar.

### Next action
1) Write `context/SURVIVAL_ENGINE_SPEC_V0_1.md` (inputs/outputs, ratio calc, allowed actions).
2) Add proof bundle artifacts for cost/revenue summaries.
3) Create “Build vs Operate” cost narrative that is consistent across docs.

---

## Pillar 7) Stealth Strategy

### Definition
Selective exposure strategy for sensitive elements (token, finances, detailed protocols).
- Tiers: **OPEN / TEASER / STEALTH / TOP SECRET**.
- Applied to: S-DNA handshake specs, Omega fusion details, Survival revenue internals, tokenomics.

### Current SSOT
- Primary: `context/AOI_CORE_PRODUCT_VISION_V0_1.md` (Scope boundary; exposure tiers)
- Secondary: `MEMORY.md` (Stealth Strategy section; naming constraints)

### Evidence paths
- Product SSOT: `context/AOI_CORE_PRODUCT_VISION_V0_1.md` (Selective Exposure section)
- Memory: `MEMORY.md` (Stealth Strategy tiers; $AOI secrecy)
- History inbox:
  - `context/aoi_core_history_inbox/aoi_core_history_20260220_095110.docx.txt` (tier examples)

### What’s missing
- **Per-asset classification** mapping to tiers (docs, repos, APIs, dashboards).
- **Enforcement**: policy checks in publishing pipeline + CI gates.
- **Public-safe templates**: how to talk about pillars without leaking restricted specs.

### Next action
1) Create `context/EXPOSURE_TIER_MATRIX_V0_1.md` (pillar artifacts → tier → allowed channels).
2) Connect to publishing gate and restricted classification table.
3) Write “public-safe description blocks” for each pillar for whitepaper/website.

---

## Cross-pillar notes (alignment risks)
- Many pillars are defined strongly, but **implementation proof artifacts** are not consistently standardized across pillars.
- Bazaar/Settlement/Royalty is central; ensure Survival 2.1 and S-DNA royalty linkage share a single ledger schema.
- Exposure-tier enforcement must be integrated into publishing workflows to prevent accidental leaks.

## Immediate consolidation tasks (recommended)
1) Create a unified `aoi-core/docs/ARTIFACTS_STANDARD_V0_1.md` listing required JSON/MD artifacts:
   - `proof.json`, `sha256sum.txt`, `guardian_report.json`, `sdna_verify.json`, `oracle_verdict.json`, `context_sentry_report.json`, `survival_summary.json`.
2) Add these artifacts to proof bundle generation templates and demos.
