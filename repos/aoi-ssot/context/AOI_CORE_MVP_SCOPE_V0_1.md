# AOI Core — MVP Scope (SSOT) v0.1

Last updated: 2026-02-20 (KST)
Owner: Edmond + Aoineco
Status: READY

> 목적: AOI Core MVP가 **정확히 무엇을 포함/제외**하는지 고정한다.
> Product Vision(상위 SSOT)과 충돌하면 **MVP 문서가 따라간다**.

---

## 0) MVP One-liner
- MVP는: **Policy → Gate → Approval → Proof** 파이프라인을 최소 기능으로 제공한다.

---

## 1) In-Scope (이번 MVP에 반드시 포함)
### 1.1 Ingestion (인입)
- [x] 원문 저장 규칙
  - 입력(대화/문서/링크) 원문은 그대로 아카이브
  - 기본 저장 경로: `context/aoi_core_history_inbox/`
- [ ] 인입 메타데이터 (v0.1 최소)
  - source, date, author(optional), tags, sensitivity(public-safe/restricted)

### 1.2 Summarize → Decide (요약/결정)
- [ ] 요약 템플릿 고정(핵심/결정/미결정/리스크/다음 액션)
- [x] SSOT 업데이트 대상:
  - `context/AOI_CORE_PRODUCT_VISION_V0_1.md`
  - `context/AOI_CORE_MVP_SCOPE_V0_1.md`

### 1.3 Governance Hooks (거버넌스)
- [x] L1/L2/L3 분류 원칙 (운영 규칙은 MEMORY/정책 문서 참조)
- [x] 기본은 `queue_for_approval`

### 1.4 Proof (증빙)
- [x] 문서 업데이트/결정에는 최소 1개 증빙(파일 경로/로그/URL/해시)

---

## 2) Out-of-Scope (이번 MVP에 포함 안 함)
- [x] 자동 온체인 트랜잭션 실행
- [x] 자동 외부 게시(브랜드/PR)
- [x] 결제/구독 시스템
- [x] 복잡한 사용자 관리/권한 시스템(필요시 vNext)
- [x] Nexus Bazaar(마켓플레이스) 전체 구현 — **Vision에는 포함, MVP에는 제외**
  - Storefront/Trust Engine/Settlement 레이어 구현은 vNext
  - Skill Aggregator(ClawHub/GitHub/NPM 통합 검색·설치)도 vNext
  - 단, 위 기능들의 **단어/정의/원칙/플라이휠(인센티브)** 고정 작업은 MVP 문서 작업으로 포함 가능
- [x] Nexus Oracle Ω (9-agent collective verdict) 상품 구현 — vNext
  - 단어/스펙/가격/구동모델(SaaS vs Lite) 고정은 MVP 문서 작업으로 포함 가능
- [x] 9인 개별 스킬(상용 오퍼링) 전부 구현/판매 자동화 — vNext
  - 단, 라인업/가격 전략/Go-to-market(7일 Sales Challenge) 정의 고정은 MVP 문서 작업으로 포함 가능
- [x] Stealth Strategy 분류 매트릭스에 의해 **STEALTH/TOP SECRET**으로 분류된 자산의 외부 공개/배포 — vNext(또는 금지)

---

## 3) MVP Deliverables (산출물)
- (D1) AOI Core Word History Inbox 폴더 + 운영 규칙
- (D2) Product Vision SSOT v0.1
- (D3) MVP Scope SSOT v0.1
- (D4) (선택) Whitepaper/Lightpaper와의 매핑 테이블 v0.1
- (D5) (선택) Brandbook과의 매핑 테이블 v0.1
- (D6) AOI Core 베타 OPS 데모(E2E) 스펙/재현 커맨드(approve→run_task→proof) 고정

---

## 4) Acceptance Criteria (완료 기준)
- 최소 5개 히스토리 원문이 inbox에 저장됨
- 각 히스토리마다:
  - 10줄 내 요약
  - 결정/미결정 분리
  - Vision/MVP 문서에 반영 여부 표시
- Whitepaper/Brandbook과 충돌 항목 0개(또는 충돌 목록이 명시됨)

---

## 5) Public Claims ↔ Evidence Mapping (OPEN/TEASER)

> 목적: “우리가 외부에 말해도 되는 주장(Claim)”이 **반드시 증빙(Proof/Evidence)** 로 연결되게 고정한다.
> 원칙: **Claim은 SSOT에 등록**되고, 증빙은 **경로 + 재현 커맨드**로 따라붙는다.

### 5.1 Allowed public claims (examples)
- **Claim:** AOI Core MVP는 *Policy → Gate → Approval → Proof* 파이프라인을 제공한다.
  - Evidence: `context/PRINCIPLE_IDEA_SCHEMA_PROOF_REGISTRY_V0_1.md`

- **Claim (TEASER):** Nexus Bazaar는 proof-first registry/search 데모(v0.1)를 제공한다.
  - Evidence bundle:
    - `context/proof_samples/nexus_bazaar_registry_v0_1/README.md`
    - `context/proof_samples/nexus_bazaar_registry_v0_1/registry_search_index.json`
  - Reproduce:
    - `python3 scripts/bazaar_registry_generate.py --auto`
    - `python3 scripts/bazaar_registry_render_md.py`
    - `python3 scripts/bazaar_registry_search_index_generate.py`

- **Claim (TEASER):** Audit Stall은 정책 기반 PASS/FAIL을 fail-closed로 낸다.
  - Evidence bundles:
    - PASS: `context/proof_samples/audit_stall_demo_20260220_135002/`
    - FAIL: `context/proof_samples/audit_stall_demo_20260220_140316_fail/`
  - Reproduce:
    - `python3 scripts/audit_stall_demo_runner.py --mode pass`
    - `python3 scripts/audit_stall_demo_runner.py --mode fail`

- **Claim (TEASER):** S‑DNA는 verify-only 기본 흐름을 제공한다.
  - Evidence bundle:
    - `context/proof_samples/sdna_verify_demo_20260220_145451/`
  - Spec:
    - `context/NEXUS_BAZAAR_SDNA_VERIFY_FLOW_SPEC_V0_1.md`

### 5.2 Deterministic proof tests (CI gate)
- Workflow: `.github/workflows/bazaar-proof-tests.yml`
- Local reproduce:
  - `python3 scripts/test_audit_stall_demo.py`
  - `python3 scripts/test_bazaar_fx_skill_demo.py`

### 5.3 Disallowed claims (until evidence exists)
- “✅ Complete / production-ready / live-tested” 같은 표현은 **증빙 번들+재현 커맨드가 없는 한 금지**.
- Stealth $AOI 관련(토큰/가격/분배/treasury/wallet/운용)은 **TOP SECRET**: 외부 커뮤니케이션 금지.

---

## Evidence (증빙)
- inbox created: `context/aoi_core_history_inbox/`
- whitepaper drafts:
  - `strategy/AOI_Tech_Whitepaper_v1.0.md`
  - `strategy/AOI_Executive_Summary_v1.0.md`
  - `strategy/AOI_Infrastructure_Architecture_v1.0.md`
- history #1 archived:
  - `context/aoi_core_history_inbox/aoi_core_history_20260220_094119.docx`

---

## Change Log
- 2026-02-20: v0.1 템플릿 생성
- 2026-02-20: Word history #1 반영 — Nexus Bazaar는 vNext(비전)로 분리 명시
- 2026-02-20: Added §5 Public Claims ↔ Evidence Mapping; aligned with Whitepaper evidence appendix
