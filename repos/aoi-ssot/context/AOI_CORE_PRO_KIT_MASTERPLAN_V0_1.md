# AOI Core — Pro Kit Masterplan v0.1 (SSOT)

Last updated: 2026-02-20 (KST)
Owner: Edmond + Aoineco
Status: DRAFT

> Purpose: AOI Core를 “판매 가능한 통합 운영 키트(Pro)”로 패키징하기 위한 상위 SSOT.
> Principle: 모듈은 단독 실행 가능해야 하지만, Pro Kit는 **approve→run→proof**로 통합 운영된다.

---

## 0) One-liner
**AOI Core Pro Kit = Verifiable Agent Operations OS**
- AI agents, but with receipts.

## 1) Positioning
- Not: 캐릭터/소울 구축 프로토콜
- Is: 운영(거버넌스/증빙/리스크/재현성) 인프라 패키지

## 2) Customer ICP
- 에이전트 자동화를 이미 하는 팀/개인(하지만 사고/감사/재현 때문에 고통)
- 온체인/재무/리스크가 섞인 워크플로우 운영자

## 3) Product pillars (must)
1) **Governance**: L1/L2/L3, fail-closed
2) **Proof**: proof bundle(artifacts+sha256+logs)
3) **Automation**: cron bundles, retry/backoff, load shedding
4) **SSOT**: CURRENT_STATE + SSOT_INDEX + memory + Notion mirror

## 4) Pro Kit bundles (modules)
### Bundle A — Squad Pro (Ops Kit)
- SSOT (to create next): `context/AOI_SQUAD_PRO_OPS_KIT_MASTERPLAN_V0_1.md`
- Existing assets:
  - `skills/aoi-squad-pro/`
  - one-click demo: `scripts/aoi_squad_pro_oneclick_demo.sh`
  - proof samples: `context/proof_samples/public/AOI_SQUAD_PRO_PROOF_BUNDLE_DEMO_V0_1/`

### Bundle B — ACP Wallet Governance (Team purchase enablement)
- `context/ACP_WALLET_GOVERNANCE_V0_1.md`
- `context/ACP_AGENT_WALLET_EXPERIMENT_V0_1.md`
- `context/ACP_AGENT_WALLET_EXPERIMENT_DIRECTIVE_V0_1.md`
- `context/ACP_WALLET_ADAPTER_INTERFACE_V0_1.md`
- `scripts/acp_wallet_adapters_stub.ts`

### Bundle C — Longform Triage Summarizer (Lite→Pro)
- PRD: `context/SKILL_LONGFORM_TRIAGE_SUMMARIZER_PRD_V0_1.md`
- Lite skill WIP: `skills/longform-triage-summarizer-lite/`
- SOP:
  - `context/PDF_LONGFORM_INGEST_SOP_V0_1.md`
  - `context/CONTENT_INGEST_TO_POST_APPROVAL_SOP_V0_1.md`

### Bundle D — Ops Optimizer (rate limit/context/cost)
- `skills/aop-ops-optimizer/`

### Bundle E — SOL Phase 2 (roadmap)
- `context/SOL_PHASE2_ROADMAP_V0_1.md`

## 5) Packaging rules
- Public-safe vs Restricted 분리
- Release gate: Security Gate PASS + changelog + rollback plan
- External posting requires approval gate

## 6) Evidence / Demo requirements
- 10-minute Quickstart
- Pinned proof bundle demo
- 3–7 day operating history (case study)

## 7) Pricing & offer model (placeholder)
- Setup fee + monthly subscription (with caps)
- Premium: Guardian Tier3 rebuild, custom integrations

## 8) Next actions
1) Create Bundle A SSOT: Squad Pro Ops Kit masterplan
2) Create Pro Kit “module map” diagram (ASCII ok)
3) Define OPEN/TEASER/STEALTH exposure per bundle
