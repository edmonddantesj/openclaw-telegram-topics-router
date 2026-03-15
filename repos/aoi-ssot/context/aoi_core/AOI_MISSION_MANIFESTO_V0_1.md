# AOI MISSION MANIFESTO V0.1
**Status:** DRAFT / INTERNAL  
**Scope:** AOI Core (L1/L2/L3)  
**Classification:** INTERNAL (Partial TEASER permitted)

---

## TL;DR
AOI(Autonomous Operative Intelligence)는 '증명 우선(Proof-First)' 원칙에 기반하여 자율 에이전트와 인간 전문가가 결합된 초저지연 의사결정 및 실행 체계를 구축한다. 우리는 말보다 영수증(Receipts)을, 계획보다 온체인 기록을 우선하며, 모든 운영은 SSOT(Single Source of Truth) 규율 아래 통제된다.

---

## Definitions
- **Proof-First:** 실행되지 않은 제안은 가치가 없다. 모든 주장은 데이터, 코드, 또는 온체인 트랜잭션으로 증명되어야 한다.
- **SSOT Discipline:** 모든 의사결정의 근거는 지정된 마크다운 문서 또는 데이터베이스에 동기화되어야 하며, 기록되지 않은 지시는 존재하지 않는 것으로 간주한다.
- **L1/L2/L3 Governance:** 
    - **L1 (Protocol):** 불변의 규칙 및 온체인 로직.
    - **L2 (Council):** 전략적 방향성 및 긴급 복구(RESET_AND_RECOVERY_PROTOCOL).
    - **L3 (Guild/Ops):** 실무 실행 및 에이전트 운용.

---

## Operating Principles (10 Bullets)
1. **Receipts over Rhetoric:** 모든 성과는 검증 가능한 영수증(로그, 해시, 스크린샷)으로 증명한다.
2. **SSOT Supremacy:** 모든 행동의 근거는 `/context` 디렉토리 내 SSOT 문서에 기반한다.
3. **Fail Fast, Recover Hard:** 실패는 허용되나, `RESET_AND_RECOVERY_PROTOCOL`에 따른 즉각적인 복구와 회고가 필수적이다.
4. **Autonomous-First:** 인간은 에이전트가 할 수 없는 예외 상황과 고수준 전략에만 개입한다.
5. **Onchain Accountability:** 주요 예산 집행 및 권한 위임은 온체인 거버넌스 정책을 따른다.
6. **Stealth by Default:** 외부 공개는 `STEALTH_CLASSIFICATION_MATRIX`에 따라 엄격히 통제된다.
7. **No Fluff:** 모든 문서는 간결하고 구조적이어야 하며, 형용사보다 명사와 수치를 사용한다.
8. **Asynchronous Excellence:** 실시간 회의보다 비동기적 SSOT 업데이트와 PR(Pull Request) 기반 협업을 지향한다.
9. **Identity Rigor:** 모든 작업자는 `IDENTITY.md`에 정의된 페르소나와 권한 범위를 준수한다.
10. **Continuous Benchmarking:** 에이전트의 성능은 실시간 지표로 측정되며, 기준 미달 시 즉시 격리(Sandbox)한다.

---

## Decision & Escalation Rules
- **Normal Flow:** L3(Guild) 내 Primary Owner가 결정 후 SSOT 업데이트.
- **Conflict:** 동일 레벨 내 이견 발생 시 L2(Council/Oracle)로 에스컬레이션.
- **Emergency:** 시스템 오작동 또는 보안 침해 시 즉시 `RESET_AND_RECOVERY_PROTOCOL` 가동.
- **External/Public:** 모든 대외 메시지는 L2 승인 및 `STEALTH_CLASSIFICATION_MATRIX` 체크 통과 필수.

---

## Evidence/Receipts Standard
모든 작업 결과물은 다음 경로에 기록되어야 함:
- **Technical Logs:** `/workspace/agents/[agent_name]/memory/`
- **Execution Proofs:** `/context/receipts/YYYY-MM-DD/`
- **Onchain Records:** Transaction Hashes documented in relevant SSOT files.

---

## Stealth & Teaser Policy Linkage
- **STEALTH:** 프로젝트 코드명, 미공개 인프라 주소, 핵심 로직.
- **INTERNAL:** 운영 규정, 내부 회의록, 상세 로드맵.
- **TEASER:** 증명된 성과 중 일부(스크린샷, 짧은 로그), 비전 선언문.
- **OPEN:** 공개 오픈소스 툴킷, 공식 발표 자료.

---

## Changelog
- **2024-05-22 (V0.1):** 최초 초안 작성. AOI Core 미션 및 10대 원칙 정의.
