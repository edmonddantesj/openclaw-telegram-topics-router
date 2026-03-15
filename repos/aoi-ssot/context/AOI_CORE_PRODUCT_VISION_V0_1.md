# AOI Core — Product Vision (SSOT) v0.1

Last updated: 2026-02-20 (KST)
Owner: Edmond + Aoineco
Status: READY

> 목적: AOI Core의 '왜(Why) / 무엇(What) / 누구(For whom) / 어떻게(How)'를 **한 문서로 고정**한다.
> 이 문서는 이후 $AOI 백서/라이트페이퍼, 브랜드북, 웹사이트 카피, 오퍼링/패키징의 **상위 SSOT**로 동작한다.

---

## 0) Definitions (단어 고정)
- **AOI**: Artificial Oriented Intelligence — 목표 지향/결과형 지능(대화형이 아니라 outcome으로 정렬되는 지능).
- **AOI Core**: Aoineco 운영 OS. Policy→Gate→Approval→Proof 기반으로 "에이전트 실행"을 안전/재현/증빙가능하게 만드는 코어 레이어.
- **CHUNGHO**: Aoineco의 우산 심볼/고유명사(브랜드 상징). 최초 1회만 "CHUNGHO (Blue Tiger)"로 풀이하고 이후에는 CHUNGHO로 고정.
- **Blue Bridge(청교, 靑橋)**: 연결/브릿지 사상(컨셉). 용어 남발 금지 → 이미지/카피로만 제한적으로 사용.
- **Nexus Bazaar**: (비전 레이어) 에이전트들이 스킬을 전시/거래/평판을 쌓는 **Skill DEX + Social Ecology**.
- **Skill DEX**: 스킬 수요/공급에 따라 유동 가격으로 스왑/거래되는 시장 모델.
- **Core-Temperature (CPU 온도)**: 당근마켓 매너온도 같은 신뢰/평판 지표(상승/하락 조건을 규칙화).
- **Skill-Guardian**: 스킬 보안 감사/검수 인프라(거래 신뢰의 필수). 3-Tier(Static/Behavioral/Rebuild)로 구성.
- **Context-Sentry**: 컨텍스트/TPM 효율화 엔진(Noise filter + Semantic compression + Priority retention).
- **S-DNA**: 워터마크/인증(원본/무결성/검증 마크).
  - Triple Helix: **Layer1 Visible(사람)** / **Layer2 Structural(기계)** / **Layer3 Behavioral(런타임 핸드셰이크)**
  - 목적: 출처/무결성 검증 + Bazaar 거래/정산(로열티) 연동
- **ACP**: Agent Commerce Protocol (시장/거래 레이어)
- **Policy / Gate / Approval / Proof**: 실행 거버넌스 체인(기본 fail-closed)
- **Real-Yield First**: 토큰 판매/펌핑이 아니라 **실사용 인프라 매출/사용료**로 자생하는 수익 모델 우선.
- **Stealth $AOI**: 런칭 전 $AOI 관련 외부 노출/마케팅/과장 금지(비공개 원칙).
- **Unassailable Authority**: 보안감사+오픈소스 기여+실전증명으로 누구도 쉽게 비난 못하는 명분/신뢰 구축.
- **Trust Engine Layer**: Core-Temp + Skill-Guardian + S-DNA로 ‘거래 가능한 신뢰’를 만든다.
- **Settlement Layer**: x402 마이크로페이 + Ledger Accounting + Royalty Distribution(원작자 로열티)로 정산/분배.
- **Skill Aggregator**: Bazaar/ClawHub/GitHub/NPM 등 멀티 소스 스킬을 통합 검색·설치(외부는 Guardian 스캔 필수).
- **Survival Engine 2.1**: 에이전트가 "LLM 비용을 스스로 벌어 충당"하기 위한 자생 엔진(수익/비용 비율에 따른 모드 전환 + 모델 등급 스위칭).
- **Dynamic Model Switching (현실 제약 반영)**: 자동 전환 천장은 Sonnet, OPUS는 수동 전환(T0)로만 사용.
- **OPUS Budgeting Rule**: OPUS는 "칼날"(고차원 추론/핵심 알고리즘)에만 사용하고, 반복/템플릿 작업은 Flash/Sonnet으로 처리.
- **Nexus Oracle Ω (Omega Mind)**: 9요원 집단지성의 단일 Verdict 엔진(베이지안 Fusion + 거버넌스 안전장치 포함).
- **Omega Fusion Engine**: 각 요원 시그널을 log-odds/likelihood로 합산해 confidence를 산출하고, 임계치 미만이면 **Oracle Veto**로 HOLD.
- **Circuit Breaker (Blue-Med)**: 최대 손실/드로우다운 등 리스크 한도 초과 시 긴급 셧다운 + 의장 알림.
- **Ω Full (SaaS)**: 9인 가동은 우리 인프라에서 수행, 고객은 API로 결과만 받는 모델.
- **Ω Lite (Self-hosted)**: 1개 에이전트가 9개 모듈을 순차 실행하는 경량판(정밀도 ~75%).
- **Aoineco Sales Challenge**: 9요원이 각자 스킬 1개씩 만들어 7일간 실제 매출(호출×단가)로 경쟁 → 시장 적합성/가격대 검증 + 바이럴.
- **9-skill lineup (Phase 4)**:
  - Blue-Sound: Crypto Pulse Radio (market→music)
  - Blue-Eye: Whale Sonar (on-chain whale alerts)
  - Blue-Blade: Prompt Armor (prompt injection guard, $0.01 bait)
  - Blue-Brain: OMNIA Debate Engine (3 persona debate)
  - Blue-Flash: Skill Forge (generate OpenClaw skill skeleton)
  - Blue-Record: Session Immortal (session→structured memory)
  - Oracle: Governance Blueprint (L1/L2/L3 governance design)
  - Blue-Gear: Uptime Guardian (health dashboard + failover)
  - Blue-Med: Risk Pulse (risk scoring + circuit breaker recs)

> ⚠️ 여기 정의가 바뀌면, 아래 모든 섹션과 MVP Scope 문서도 함께 업데이트해야 함.

---

## 1) One-liner (한 줄 정의)
- AOI Core는: **에이전트 실행을 ‘증빙 가능한 안전한 거래(Execution Commerce)’로 바꾸는 운영 코어**다.

---

## 2) Mission / Vision
- Mission (지금 당장 해결):
  - 스킬/자동화/에이전트 실행이 "사고 없이" 굴러가게 한다(정책/게이트/승인/증빙).
- Vision (장기적으로 만들 세계):
  - **Nexus Bazaar**: 전 세계 에이전트들이 스킬을 전시/거래/협업하고, Skill-Guardian+S-DNA로 신뢰가 보증되는 **에이전트 경제 생태계(Agent GDP)**를 만든다.

---

## 3) The Problem (우리가 해결하는 고통)
- 사용자 고통 3개:
  1) 스킬/자동화 실행이 재현 불가(누가 뭘 했는지 증빙이 없음)
  2) 보안/리소스 낭비/백도어 리스크로 신뢰가 깨짐
  3) 좋은 스킬이 있어도 유통/거래/평판 시스템 부재로 경제가 안 생김
- 왜 지금(Why now):
  - 에이전트가 실전(돈/서명/배포)에 들어가면서 **거버넌스+증빙+시장**이 없으면 확장 자체가 불가능.

---

## 4) Target Users (ICP)
- Primary ICP:
  - 에이전트를 운영하는 PO/빌더(팀/개인) — “욕먹지 않고 기술로 가치 만드는” 사람들
- Secondary ICP:
  - 스킬 제작자(에이전트/개발자) — 판매/검수/평판이 필요한 사람들
- Not ICP (우리가 안 하는 것):
  - 무승인 자동 온체인/무승인 외부게시를 원하는 운영

---

## 5) Value Proposition (약속)
- 핵심 약속 3개:
  1) **Fail-closed 안전성**: 게이트/정책 통과 전 실행 금지
  2) **Proof-first 재현성**: 파일/로그/URL/해시로 결과를 증빙
  3) **시장 신뢰 인프라**: Skill-Guardian+S-DNA로 ‘검증된 꿀매물’만 유통

- 백서용 Killer quote(OPEN):
  - **"You can clone our architecture. You cannot clone our experience."**

---

## 6) Product Principles (제품 원칙)
- Fail-closed (게이트 통과 전 실행 금지)
- L1/L2/L3 거버넌스 준수
- SSOT-first (대화보다 문서가 우선)
- Public-safe vs Restricted 분리
- Automation with approvals (queue_for_approval 기본)
- **Real-Yield First** (토큰 판매가 아닌 실사용 매출/사용료 기반)
- **Unassailable Authority** (보안/투명성/오픈소스/실전증명으로 비난 방어)
- **Long-term Empire** (단기 펌핑 금지, ‘길게’ 인프라 장악)
- **Freemium where cost is real**: Regex 기반 Noise filter는 FREE(비용 0), LLM 호출이 필요한 Semantic compression은 PAID.
- **Guardian + Sentry = Immune System**: 안전(보안) + 비용/수명(TPM)까지 함께 진단해 설치/도입 의사결정을 돕는다.
- **Soft Launch + Conservative Execution**: 미완성이라도 표준/증빙 중심으로 먼저 런칭하되, 돈/지갑/무인 자동실행은 단계적 권한 오픈(기본 watch/DRY, LIVE는 confirm+caps+allowlist)

---

## 7) Core Loop (사용자 경험 루프)
1) 인입(요청/문서/변경)
2) Policy 체크
3) Gate 실행(리스크 스캔)
4) Approval 생성/대기
5) Proof bundle 생성
6) 실행/배포(조건부)
7) 아카이브/회고

### AOI Core Beta Demo (OPS bundle)
- Demo-Ops를 기본 시나리오로 고정: approve → execute → proof
- 1회 실행으로 **CHECKLIST + ADR + proof.json(sha 포함)** 번들을 생성(artifacts 2개)
- Core 폴더: `aoi-core/`

### S-DNA × Guardian Flow (통합)
- 외부 스킬 인입 → S-DNA 존재/무결성(hash) 체크 →
  - 일치(verified)면 **fast-track**(검사 간소화)
  - 없음/변조면 **full guardian scan** 또는 **quarantine**
- S-DNA는 Bazaar 실행 시 **로열티 정산**(tier 기반)에도 연결

### vNext Loop (Nexus Bazaar)
- Showroom(전시) → Trade(거래/스왑) → Audit/Cert(검수/인증) → Reputation(Core-Temp) → (수수료 차등/인센티브) → 뉴스/이벤트(바이럴)

### vNext Mechanics (핵심 메커니즘)
- **Core-Temp 기반 수수료 인센티브**: 온도 높을수록 platform fee 할인(판매자가 Guardian/S-DNA를 자발적으로 하게 만듦)
- **Guardian 스캔 무료 → Rebuild 유료**: 외부 스킬은 무료 스캔으로 신뢰를 깔고, 위험/경고는 리빌드(유료)로 수익화
- **외부→Bazaar 이전(등록) 수수료**: S-DNA 발급 + 신뢰도 취득을 ‘온보딩’ 상품으로 설계

---

## 8) Scope Boundary (명확히 안 하는 것)
- 온체인/결제/서명 자동 실행(L3)은 기본 금지
- 외부 게시 자동화는 기본 금지
- 개인 정보 수집/저장은 Notion 전용(사전 허락)

### Stealth Strategy (Selective Exposure)
- 무엇을 공개/암시/비공개로 할지의 분류가 제품 전략의 일부다.
- Exposure tiers: **OPEN / TEASER / STEALTH / TOP SECRET**
  - OPEN: 소스+문서+데모+가격 공개 (유입/표준화)
  - TEASER: 컨셉/스크린샷/로드맵만 공개(코드 비공개)
  - STEALTH: 내부 전용(존재 자체를 외부에 알리지 않음)
  - TOP SECRET: 의장 명시 승인 시만(토큰/재무)

---

## 9) Success Metrics (성공 지표)
- 안전성: gate red 우회 0건
- 운영: 승인→증빙까지 평균 리드타임
- 재현성: 동일 입력 재실행 시 결과 일치율
- 시장: 검수 통과 스킬 거래량, Core-Temp 기반 재구매율

### Infra-leader Success Definition (의장 성공 정의)
- 1순위: **돈이 아니라, AI 인프라의 선두주자(표준/증빙/생태계) 선점**
  - Standard(표준) / Proof(증빙) / Plugin ecosystem(생태계)

---

## 10) Links / Artifacts (증빙)
### Whitepaper / Docs (drafts)
- `strategy/AOI_Tech_Whitepaper_v1.0.md`
- `strategy/AOI_Executive_Summary_v1.0.md`
- `strategy/AOI_Infrastructure_Architecture_v1.0.md`
- `strategy/AOI_Litepaper_v1.md`

### AOI Core Word history raw archive
  - `context/aoi_core_history_inbox/aoi_core_history_20260220_094119.docx`
  - `context/aoi_core_history_inbox/aoi_core_history_20260220_094119.docx.sha256`
  - extracted text: `context/aoi_core_history_inbox/aoi_core_history_20260220_094119.docx.txt`
  - `context/aoi_core_history_inbox/aoi_core_history_20260220_094321.docx`
  - `context/aoi_core_history_inbox/aoi_core_history_20260220_094321.docx.sha256`
  - extracted text: `context/aoi_core_history_inbox/aoi_core_history_20260220_094321.docx.txt`
  - `context/aoi_core_history_inbox/aoi_core_history_20260220_094430.docx`
  - `context/aoi_core_history_inbox/aoi_core_history_20260220_094430.docx.sha256`
  - extracted text: `context/aoi_core_history_inbox/aoi_core_history_20260220_094430.docx.txt`
  - `context/aoi_core_history_inbox/aoi_core_history_20260220_094539.docx`
  - `context/aoi_core_history_inbox/aoi_core_history_20260220_094539.docx.sha256`
  - extracted text: `context/aoi_core_history_inbox/aoi_core_history_20260220_094539.docx.txt`
  - `context/aoi_core_history_inbox/aoi_core_history_20260220_094707.docx`
  - `context/aoi_core_history_inbox/aoi_core_history_20260220_094707.docx.sha256`
  - extracted text: `context/aoi_core_history_inbox/aoi_core_history_20260220_094707.docx.txt`
  - `context/aoi_core_history_inbox/aoi_core_history_20260220_094822.docx`
  - `context/aoi_core_history_inbox/aoi_core_history_20260220_094822.docx.sha256`
  - extracted text: `context/aoi_core_history_inbox/aoi_core_history_20260220_094822.docx.txt`
  - `context/aoi_core_history_inbox/aoi_core_history_20260220_094953.docx`
  - `context/aoi_core_history_inbox/aoi_core_history_20260220_094953.docx.sha256`
  - extracted text: `context/aoi_core_history_inbox/aoi_core_history_20260220_094953.docx.txt`
  - `context/aoi_core_history_inbox/aoi_core_history_20260220_095110.docx`
  - `context/aoi_core_history_inbox/aoi_core_history_20260220_095110.docx.sha256`
  - extracted text: `context/aoi_core_history_inbox/aoi_core_history_20260220_095110.docx.txt`
  - `context/aoi_core_history_inbox/aoi_core_history_20260220_095226.docx`
  - `context/aoi_core_history_inbox/aoi_core_history_20260220_095226.docx.sha256`
  - extracted text: `context/aoi_core_history_inbox/aoi_core_history_20260220_095226.docx.txt`
  - `context/aoi_core_history_inbox/aoi_core_history_20260220_095452.docx`
  - `context/aoi_core_history_inbox/aoi_core_history_20260220_095452.docx.sha256`
  - extracted text: `context/aoi_core_history_inbox/aoi_core_history_20260220_095452.docx.txt`
  - `context/aoi_core_history_inbox/aoi_core_history_20260220_100214.docx`
  - `context/aoi_core_history_inbox/aoi_core_history_20260220_100214.docx.sha256`
  - extracted text: `context/aoi_core_history_inbox/aoi_core_history_20260220_100214.docx.txt`
  - `context/aoi_core_history_inbox/brand_cheongho_20260220_100606.docx`
  - `context/aoi_core_history_inbox/brand_cheongho_20260220_100606.docx.sha256`
  - extracted text: `context/aoi_core_history_inbox/brand_cheongho_20260220_100606.docx.txt`
  - `context/aoi_core_history_inbox/aoi_core_history_20260220_101604.docx`
  - `context/aoi_core_history_inbox/aoi_core_history_20260220_101604.docx.sha256`
  - extracted text: `context/aoi_core_history_inbox/aoi_core_history_20260220_101604.docx.txt`

---

## Change Log
- 2026-02-20: READY promotion — naming/tiers/stealth policies locked; claims registry + MVP mapping added


- 2026-02-20: v0.1 템플릿 생성
- 2026-02-20: Word history #1 반영 — Nexus Bazaar / Core-Temperature / Skill DEX / Skill-Guardian / S-DNA 정의 및 비전 업데이트
