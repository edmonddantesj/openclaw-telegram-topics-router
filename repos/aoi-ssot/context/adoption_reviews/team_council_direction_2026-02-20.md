# Team Council (Lite) — decision

## Topic
AOI Squad Pro/ACP 인프라 방향성: 안전한 에이전트 운영(Policy/Gate/Approval/Proof)

## Context (optional)
우리는 해커톤/외부 소스들을 벤치마킹하되, L3(돈/서명/온체인/외부게시)는 승인 큐로 묶고, fail-closed 정책 기반으로 에이전트 실행을 통제하는 인프라를 내재화 중. ClawShield-style commit gate, AgentFaucet-style bootstrap plan PoC 스캐폴드 존재. Adoption Gate 체크리스트 v0.1 작성.

## Constraints (optional)
차별화: 누구나 쉽게 못 만들지만 에이전트에 필수인 운영·보안·증빙. 목표는 내재화 중심(영상은 BACKLOG).

---

## TL;DR (2 lines)
- 방향성 자체는 맞다: “에이전트가 뭘 하냐”보다 “에이전트가 안전하게/재현가능하게 하게 만드는 운영체제”가 장기적으로 이긴다.
- 단, 잘 먹히려면 ‘보안 철학’이 아니라 **제품화된 가드레일(정책·승인·증빙) + 1~2개 즉효 유스케이스**로 증명해야 한다.

## Role opinions (2–3 lines each)
- 🧿 Oracle (decision frame):
  - 결정: 우리 핵심 전략을 “기능 에이전트”가 아니라 “에이전트 운영 인프라(Policy/Gate/Approval/Proof)”로 둘지, 그리고 이를 내재화 중심으로 굳힐지.
  - 가정 3개: (1) 에이전트 실행이 현실 자산/권한과 연결될수록 가드레일 수요가 폭증한다 (2) 신뢰/감사 가능성이 채택의 병목이다 (3) ‘운영이 쉬운’ 쪽이 결국 확장한다.
  - 추천: **Go(조건부)** — 단, 2주 내 “Gate→Approval→Proof” 한 바퀴를 최소 1개 워크플로로 끝까지 보여줘야 한다.

- 🧠 Analyzer (scoring/trade-offs):
  - 옵션: (A) 안전 인프라(현재 방향) (B) 사용자-facing 에이전트 기능 빠른 확장 (C) 둘 다.
  - 트레이드오프: A는 초기 데모 임팩트가 약해 보일 수 있으나, 누적될수록 복리. B는 빨리 화려해지지만 사고/신뢰 비용이 커짐.
  - 점수(10점 만점): A=8.5(장기 우위), B=6.5(단기), C=7.0(운영 부담↑). 지금은 **A 우선 + B는 ‘검증된 1개 유스케이스’만**.

- ⚔️ Security (security/risk):
  - Top Risk: (1) 공급망(패키지/스킬) (2) 서명/승인 UX의 허점(오인승인) (3) 로그/증빙에 시크릿 누출.
  - 필수 가드레일: fail-closed, allowlist/limit, 시뮬레이션(가능시), proof bundle, 승인 큐 + 만료/철회.
  - 결론: 이 방향은 ‘안전팀이 없는 팀’이 가장 필요로 하는 영역이라 강력. 다만 **보안은 주장하면 0점, 자동검사/증빙을 남기면 100점**.

- ⚡ Builder (feasibility/MVP):
  - 빌드 가능. 우리가 이미 PoC(ClawShield gate / AgentFaucet plan)로 골조를 갖췄고, 다음은 연결(Approval/Policy hook)이다.
  - MVP(2주): (1) Commit Gate JSON report (2) Approval Request 생성 (3) Proof bundle 저장 (4) 정책 위반 시 자동 queue.
  - 핫스팟: ‘표준 스키마’(report/approval/proof) 고정이 늦어지면 계속 갈아엎게 됨 → **스키마 먼저 잠그는 게 비용 절감**.

- 📢 Comms (messaging/market):
  - 인식: “에이전트 플랫폼/런타임”은 많지만, “에이전트가 안전하게 돈/권한을 다루게 해주는 운영 레이어”는 희소해서 차별화 가능.
  - 1-liner 피치: **“Agents you can actually trust: policy-gated execution with approvals and audit-proof evidence.”**
  - 예상 반론/대응: “화려한 데모가 없는데?” → “우린 데모가 ‘기능’이 아니라 ‘안전하게 실행되는 프로세스’다. 사고가 없는 자동화를 제공한다.”

## Consensus / Conflict
- Consensus: 방향성은 맞고, ‘운영·보안·증빙’은 에이전트가 현실로 갈수록 필수. 지금처럼 내재화 중심이 장기적으로 유리.
- Conflict: 단기 임팩트(눈에 보이는 가치)를 어떻게 빠르게 보여주느냐. (인프라가 ‘추상적’으로 보일 위험)

## Dissent (at least 1)
- “인프라에만 올인하면, 시장은 기능/UX로 먼저 잠식당할 수 있다”는 반대 의견.
  - 대응: ‘기능을 안 한다’가 아니라, **가드레일이 필요한 1~2개 기능만** 골라서 인프라의 가치를 기능으로 증명한다(예: 스왑/지갑부트스트랩/스킬 설치).

## Assumptions (3)
1. 에이전트가 거래/서명/외부게시로 확장되는 흐름은 지속되며, 신뢰/감사 가능성이 채택 병목이 된다.
2. 우리가 만든 Gate/Approval/Proof가 실제 운영비(사고·리뷰·온콜)를 줄인다는 걸 데이터로 보여줄 수 있다.
3. Adoption Gate(라이선스/보안/재현) 규율을 지키면, 외부 소스를 흡수해도 기술부채가 폭발하지 않는다.

## Recommendation
- Conditional
- Confidence: Medium-High
- Risk: Medium

## Next actions (Top 3)
1. **MVP 워크플로 1개를 ‘끝까지’**: Gate → Approval → Proof → (승인 시) 실행(또는 실행 계획)까지 한 바퀴.
2. 스키마 잠금: `gate_report.json`, `approval_request.json`, `proof_bundle.json` 최소 버전(v0.1) 고정 + 예시 3종.
3. 채택 프로세스 자동화: `ADOPTION_GATE_CHECKLIST_V0_1`로 외부 소스 3개를 실제 평가해 `bench_only/internalize/reject` 판정 기록을 남김.
