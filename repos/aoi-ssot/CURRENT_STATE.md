# CURRENT_STATE.md — SSOT (Auto-synced)

Last update: 2026-02-20 19:37 KST

## 1) Alpha Oracle V6 (latest)
- Run: 2026-02-20 16:43 KST
- Archive: `the-alpha-oracle/results/v6_20260220_164305_BTC-USD.json`
- Final: **LONG** | Agreement: **STRONG** | Risk: **CLEAR (VaR95 -0.18%)** | Kelly Position: **3.41%** | MC Win Rate: **99.0%**

## 2) AOI/ACP Infra — Policy → Gate → Approval → Proof
- ACP automation policy (v0.1)
  - SSOT: `aoi-core/state/acp_automation_policy_v0_1.json`
  - Default: `queue_for_approval`
  - Micro preapproval: `GUARDED_MICRO`
  - Limits: **$2/tx**, **$7/day**, **USDC only**, provider: **privy/coinbase**, action: **swap only**
- Adoption Gate checklist SSOT: `context/ADOPTION_GATE_CHECKLIST_V0_1.md`

## 3) ClawShield internalization (commit gate)
- pre-push hook + GitHub Actions fail-closed enforced
- txhash doc exception only when safe doc-hint context exists

## 3-1) Runtime note — MoltGuard (port 8900)

## ✅ 현재를 저장 (Snapshot)
- State integrity: `python3 skills/aoineco-state-guardian/scripts/state_integrity.py`
  - Result: **ALL GREEN**
  - Timestamp: 2026-02-20 19:37 KST
- Fresh TEASER-safe proofs regenerated (deterministic):
  - Root: `/tmp/aoi_public_teaser_proofs_20260220_193722/`

- Current stance: **leave as-is** if operations are stable.
- Observed: port `127.0.0.1:8900` is served by a LaunchAgent-managed MoltGuard process; OpenClaw plugin status may show MoltGuard as disabled.
- Decision: This mismatch is acceptable as long as:
  - OpenClaw gateway (18789) RPC probe is OK
  - `lsof -iTCP:8900 -sTCP:LISTEN` shows a listener
  - `openclaw security audit` has **0 critical**

## 4) SSOT READY promotions (today)
- ✅ `context/AOI_CORE_PRODUCT_VISION_V0_1.md` → **READY**
- ✅ `context/AOI_CORE_MVP_SCOPE_V0_1.md` → **READY** (includes §5 Claims ↔ Evidence mapping)
- ✅ `context/PUBLIC_CLAIMS_REGISTRY_V0_1.md` → **READY** (deterministic tests pass)
- ✅ `context/TOOLSET_ADOPTION_PLAYBOOK_ABC_V0_1.md` → **READY**

## 5) Top TODO (next)
### A) Longform Summarizer skill (Lite→Pro track)
- [ ] PRD(v0.1) 기준으로 Lite MVP 구현 계획 확정 (DOCX/PDF 추출 + 요약 + S/A/B/C + public-safe scan + drafts)
- [ ] ACP Pro는 allow_post=false 기본 + 승인토큰 기반 설계(스펙만, 실행은 L3)

### A-0) Nexus Bazaar Aggregator (RFQ/intent-first)
- [x] Aggregator SSOT: `context/NEXUS_BAZAAR_AGGREGATOR_SPEC_V0_1.md`
- [x] Merchant profile schema: `context/NEXUS_BAZAAR_MERCHANT_PROFILE_SCHEMA_V0_1.md`
- [x] Routing report schema: `context/NEXUS_BAZAAR_ROUTING_REPORT_SCHEMA_V0_1.md`
- [x] Proof bundle demo (3 merchants, trust-aware + freshness/timeout + routing_report, report-only): `context/proof_samples/bazaar_rfq_demo_20260220_124616/`
- [x] RFQ runner: `scripts/bazaar_rfq_demo_runner.py`

### A-0-2) Skill Stall demo (proof-first)
- [x] Skill stall runner (deterministic, no LLM): `scripts/skill_stall_demo_runner.py`
- [x] Skill catalog schema: `context/NEXUS_BAZAAR_SKILL_CATALOG_SCHEMA_V0_1.md`
- [x] Proof sample (+ merchant_profile + skill_catalog): `context/proof_samples/skill_stall_demo_20260220_125349/`

### A-0-3) Bazaar Storefront Registry (minimal)
- [x] Registry index schema: `context/NEXUS_BAZAAR_REGISTRY_INDEX_SCHEMA_V0_1.md`
- [x] Registry generator (auto-scan supported; includes AUDIT stalls): `scripts/bazaar_registry_generate.py`
- [x] Registry markdown renderer (shows 🌡️ core-temp + badges): `scripts/bazaar_registry_render_md.py`
- [x] Generated registry bundle: `context/proof_samples/nexus_bazaar_registry_v0_1/` (includes README.md)

### A-0-3a) Bazaar Trust UI — Core-Temperature
- [x] v0.1 spec (0°C booting → 36.5°C baseline): `context/NEXUS_BAZAAR_CORE_TEMP_SPEC_V0_1.md`
- [x] v0.2 spec (fail-closed freeze + sdna autodetect): `projects/nexus-bazaar-private/context/NEXUS_BAZAAR_CORE_TEMP_SPEC_V0_2.md`
- [x] Deterministic compute: `scripts/bazaar_core_temp_compute.py` (also mirrored in private repo)
- [x] Enriched registry output: `context/proof_samples/nexus_bazaar_registry_v0_1/registry_index_enriched.json`
- [x] README rendering updated: `context/proof_samples/nexus_bazaar_registry_v0_1/README.md`

### A-0-3b) Bazaar Trust Signal — S-DNA verify flow v0.1
- [x] Schema: `context/NEXUS_BAZAAR_SDNA_VERIFY_SCHEMA_V0_1.md`
- [x] Flow spec (upload section, verify-only): `context/NEXUS_BAZAAR_SDNA_VERIFY_FLOW_SPEC_V0_1.md`
- [x] Demo runner (proof bundle): `scripts/sdna_verify_demo_runner.py`
- [x] Proof sample: `context/proof_samples/sdna_verify_demo_20260220_145451/`

### A-0-3c) Bazaar Search/Sort
- [x] v0.1 schema: `context/NEXUS_BAZAAR_SEARCH_INDEX_SCHEMA_V0_1.md`
- [x] Generator: `scripts/bazaar_registry_search_index_generate.py`
- [x] Output: `context/proof_samples/nexus_bazaar_registry_v0_1/registry_search_index.json`
- [x] CLI query tool: `scripts/bazaar_query.py`
- [x] Static local UI (v0.1→v0.2 filters): `context/ui/bazaar/index.html`
- [x] Private repo package (internal build): https://github.com/edmonddantesj/nexus-bazaar-private
- [ ] (PARKED) Next build backlog stored in `context/TASK_PARKING_LOT.md` (tag: bazaar-terminology-backlog)

- [x] Demo one-pager (public-safe): `context/NEXUS_BAZAAR_DEMO_ONEPAGER_V0_1.md` (registry linked)
- [x] Base batch addendum copy (public-safe): `context/BASE_BATCHES_ADDENDUM_NEXUS_BAZAAR_V0_1.md`

### A-0-4) Audit Stall demo (Guardian-style report)
- [x] Audit stall runner (deterministic): `scripts/audit_stall_demo_runner.py`
- [x] Versioned audit policy (+ severity gating): `context/proof_samples/audit_stall_demo_20260220_135002/audit_policy.json`
- [x] Proof samples: PASS `context/proof_samples/audit_stall_demo_20260220_135002/` / FAIL `context/proof_samples/audit_stall_demo_20260220_140316_fail/`
- [x] Registry README surfaces PASS/FAIL + policy: `context/proof_samples/nexus_bazaar_registry_v0_1/README.md`
- [x] Mini regression test: `scripts/test_audit_stall_demo.py`
- [x] FX+Skill regression test: `scripts/test_bazaar_fx_skill_demo.py`
- [x] CI workflow (deterministic): `.github/workflows/bazaar-proof-tests.yml`

### B) Hackathon lane (Evidence-first)
- Policy SSOT: `context/HACKATHON_PARTICIPATION_RULES_V0_1.md` (post-48h triage + public-safe + scope lock)
- ✅ BNB hackathon: **SUBMITTED (DONE)**
- ❌ USDC hackathon: **ENDED — not submitted**
- ✅ EigenCloud Open Innovation Challenge: **SUBMITTED (DONE)**
- [ ] Elastic Agent Builder hackathon 제출 패키지(Proof Bundle + repo + 3분 데모) 초안 고정
- [ ] BUIDL CTC(Creditcoin) — ProofPay MVP: Creditcoin testnet이 EVM인지 확인(스펙/배포 툴 확정)
- [ ] Airia는 Public publish 필수 → **L3 외부노출 승인 없으면 보류**

### A-2) Royalty infra (B-min, Base/USDC)
- [x] Spec SSOT: `context/ROYALTY_RAIL_USDC_BMIN_SPEC_V0_1.md`
- [x] Statement generator (report-only): `scripts/royalty_statement_generate.py`
- [ ] Ledger entries 채우기(creator/skill_ref/amount/month/status)
- [ ] 실제 테스트 송금은 L3 승인 + tx_hash 기록으로만 진행

### A-3) Parking Lot (집/키/촬영 필요로 pause)
- SSOT: `context/TASK_PARKING_LOT.md` (tag: deferred-bundle-2026-02-16)
  - Midl VibeHack (Xverse extension + on-chain action + tx hash proof + 데모 촬영)
  - BNB GoodVibes DEX Agent (multi:dry→multi:live + BscScan tx 링크 + 영상)

### B) ACP Wallet Experiment — Team Purchase Enablement
- Governance SSOT: `context/ACP_WALLET_GOVERNANCE_V0_1.md`
- Experiment plan: `context/ACP_AGENT_WALLET_EXPERIMENT_V0_1.md`
- Directive (copy/paste): `context/ACP_AGENT_WALLET_EXPERIMENT_DIRECTIVE_V0_1.md`
- Adapter interface: `context/ACP_WALLET_ADAPTER_INTERFACE_V0_1.md`
- [ ] Round 2 실행(목표: 그룹별 실패율 <10% + 증빙 누락 0)
- [ ] 팀원별 micro budget funding (L3) — tx_hash 기록 후 진행

### B) AgentFaucet standardization
- [ ] B1 Plan schema v0.1: `context/ACP_AGENTFAUCET_PLAN_SCHEMA_V0_1.md`
- [ ] B1-2 Proof bundle schema v0.1: `context/ACP_PROOF_BUNDLE_SCHEMA_V0_1.md`
- [ ] B3 Policy hooks: `context/ACP_AGENTFAUCET_POLICY_HOOKS_V0_1.md`

## 5) Notes
- CURRENT_STATE.md was previously corrupted (contained AGENTS.md content). Backup created:
  - `.state_backups/20260220_0935__CURRENT_STATE.md`
- Upbit remaster skill folder exists but is **WIP/incomplete** (do not treat as adopt-complete):
  - `skills/aoi-upbit-market-data-remaster/README.md`
- Survival bridge/autonomy (Base→Solana, deBridge/CCTP, Canary, Guarded Autonomy) is currently **NOT implemented**; kept as roadmap notes:
  - `context/SURVIVAL_BRIDGE_AUTONOMY_SECURITY_NOTES_V0_1.md`
