# Branding / Positioning Key Points & Decisions v0.1 (from 2026-02-14 convo)

> NOTE: Updated, fuller summary exists: `context/BRANDING_KEY_POINTS_AND_DECISIONS_V0_2.md`

## Source
- Raw dump: `context/BRANDING_DIALOGUE_DUMP_2026-02-14_RALF_FAN_V0_1.txt`

## 1) Launch philosophy (infra-first)
- **Soft Launch 우선**(미완성 공개) + **권한은 보수적으로 단계 오픈**.
- 절대 조건(안전):
  - Default는 **Watch-only / DRY_RUN / Simulate**
  - LIVE는 **명시적 사용자 확인(Confirm) + 하드캡 + allowlist + fail-closed**
  - “수익/알파 주장”은 금지하고 **proof & safety 포지셔닝**

## 2) What we are (not an app)
- 목표는 “완성 앱”이 아니라 **운영체제/프로토콜/인프라**.
- PMF는 기능 개수가 아니라:
  - **표준(interfaces/schemas)**
  - **증빙(auditability/proof archive)**
  - **운영(risk gates/governance)**
  이 3축이 자리잡을 때 발생.

## 3) Roadmap reframed by launch stages
- Stage A: 지금 런칭 가능한 코어 = **Run Artifact Standard**
  - Run report / manifest / proof / risk gate input-output 고정
- Stage B: Nexus Bazaar는 ‘거래소’가 아니라 **플러그인 레지스트리**부터
  - DRY_RUN 기본, LIVE는 승인/확인 기반
- Stage C: AI DENX는 ‘자동 트레이딩’이 아니라 **Decision Exchange(결정/리스크/증빙 교환소)**로 시작

## 4) Success definition (north star)
- 사용자의 성공 정의: **돈이 아니라 “AI 인프라 선두주자”**.
- 선두주자 전략 3개:
  - 표준(standard) 먼저
  - 증빙(proof archive) 먼저
  - 생태계(plugin registry) 먼저

## 5) Operating cadence (sustainable loop)
- 주 2회 Proof Day: 최소 1개 run artifact (+ 가능하면 onchain proof)
- 주 1회 Standard Day: 스키마/문서/거버넌스 업데이트
- 월 1회 Deprecation Day: 단종/정리
- 금지: ‘자동으로 돈 버는 기능’ 서둘러 공개

## 6) Naming exploration (standard name candidates)
### Initial options
- Nexus Run Standard (NRS)
- S-DNA Run Manifest Standard (SRMS)
- Proof-First Agent Standard (PFAS)

### Team suggestion pool (role-based)
- TraceRun Standard (TRS)
- Agent Run Ledger (ARL)
- AuditTrail for Agents (ATA)
- Provenance Run Spec (PRS)
- Replayable Execution Record (RER)
- ProofMode
- VeriLedger
- PolicyWatch / Guardrail / ClearAudit
- Proofbundle / Auditkit / Tracepack

### Shortlist mentioned (TOP)
- Proof-First Run Standard (PFR)
- Agent Run Manifest Standard (ARM) *(약어 충돌 가능성 언급)*
- RunProof Standard (RunProof)

## 7) Open questions (not decided)
- 외부에 내보낼 이름(표준 이름) 최종 선택
- Soft Launch 기본 모드 (A:watch-only / B:dry_run+quote / C:user-confirmed live 포함)
