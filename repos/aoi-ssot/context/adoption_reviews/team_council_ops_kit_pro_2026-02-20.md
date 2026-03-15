# Team Council (Lite) — decision

## Topic
모듈형 스킬 생태계 + 통합 운영 키트(유료 Pro) 전략: AOI Core로 판매까지

## Context (optional)
스킬들은 단독 구동 가능. 추가로 '통합 운영키트(Pro, 유료)'를 만들어 모듈식 스킬들을 하나의 운영체제처럼 결합(정책/게이트/승인/증빙/크론/레이트리밋/옵저버빌리티). 우리는 내부에서 Pro 모델로 먼저 돌리며 유지보수/관리/버그바운티/가격을 다듬고, 최종적으로 AOI Core에서 판매까지 목표.

## Constraints (optional)
1) 모듈성 유지(단독+조합). 2) 운영부담 관리. 3) 보안/키 취급 금지(public-safe). 4) 가격/플랜/업셀 구조 필요. 5) ACP 오퍼링(예: Security Gate Kit)과 관계 정리.

---

## TL;DR (2 lines)
- **Go(조건부)**: “모듈 단독 + Pro 통합키트” 전략은 맞고, 우리가 이미 만든 Gate/Approval/Proof 같은 운영 인프라가 Pro의 핵심 가치가 된다.
- 조건은 2개: (1) Pro는 ‘기능 묶음’이 아니라 **운영 레이어(정책·관측·레이트리밋·증빙)**로 정의 (2) 2~3개 킬러 모듈만 먼저 통합해 **운영비를 통제**.

## Role opinions (2–3 lines each)
- 🧿 Oracle (decision frame):
  - 결정: “스킬 단품 판매”를 기본으로 유지하면서도, Pro 키트로 통합 운영을 제공할지 / 제공한다면 무엇을 Pro의 SSOT로 둘지.
  - 추천: Pro의 SSOT는 **AOI Core(Policy + Registry + Scheduler + Evidence)**. 단품 스킬은 그대로 존재하되, Pro에선 “플러그인”으로 로딩.

- 🧠 Analyzer (scoring/trade-offs):
  - 옵션: A) 단품만(운영부담↓, ARPU↓) B) 단품+Pro(ARPU↑, 부하↑) C) Pro만(채택장벽↑).
  - 점수: A=7(안전하지만 성장 제한), B=9(최적), C=6(초기 위험). **B가 최선**.

- ⚔️ Security (security/risk):
  - Pro 키트는 “운영 권한”을 다루므로 사고 1번이 치명적. 키/시드 취급 금지, 상태 아티팩트는 로컬-only, fail-closed 유지가 필수.
  - 버그바운티는 좋지만, 공개 범위/위협모델을 문서화하고 “안전한 재현 환경(샌드박스)” 제공이 선행돼야 함.

- ⚡ Builder (feasibility/MVP):
  - MVP(2주)로 가능한 통합은 3개 모듈이면 충분: (1) Security Gate Kit (2) Ops Optimizer(크론/레이트리밋/컨텍스트) (3) Evidence/Approval(상태·증빙 표준).
  - 이 3개를 “하나의 설치 스크립트 + 정책 파일 + 대시보드(텍스트)”로 묶으면 ‘운영체제’ 느낌이 난다.

- 📢 Comms (messaging/market):
  - 시장은 “에이전트”보다 “에이전트 운영”을 더 어려워함. Pro는 이렇게 팔면 먹힘: **‘Agent Ops OS’**.
  - 반론: “그냥 CI/스크립트 아닌가?” → “우린 **승인/증빙/정책/레이트리밋**까지 포함한 운영 루프를 제공한다.”

## Consensus / Conflict
- Consensus: 모듈 단품 유지 + Pro 통합키트로 업셀 구조를 만드는 게 베스트.
- Conflict: Pro를 너무 빨리 크게 만들면 운영부담/버그면적이 급증 → ‘소수 모듈’로 시작해야 함.

## Dissent (at least 1)
- “Pro를 만들면 단품 스킬 생태계가 약해지고, 지원 요청이 폭증할 수 있다.”
  - 대응: Pro는 ‘기능’이 아니라 ‘운영 레이어’로 판매하고, 단품은 커뮤니티/오픈 레일로 유지. 지원은 ‘설치 범위/버전’으로 제한.

## Assumptions (3)
1. 고객은 ‘에이전트 기능’보다 ‘운영(안전, 로그, 재현, 비용)’에서 더 큰 고통을 겪는다.
2. 우리가 가진 차별점(Policy→Gate→Approval→Proof)이 장기적으로 복리로 쌓인다.
3. Pro의 초기 범위를 3모듈로 제한하면 운영부담이 감당 가능하다.

## Recommendation
- Conditional
- Confidence: High
- Risk: Medium

## Next actions (Top 3)
1. **Pro Kit MVP 범위 확정(3모듈)**: Gate Kit + Ops Optimizer + Evidence/Approval 표준.
2. **AOI Core SSOT 정의**: registry(모듈 목록/버전) + policy + scheduler + evidence schema.
3. 가격/플랜 초안(단품/Pro/Setup) 확정 + 내부 dogfooding(우리 계정/레포)으로 2주 운영 데이터 수집.
