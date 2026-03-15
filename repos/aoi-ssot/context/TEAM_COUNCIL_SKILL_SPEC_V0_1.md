# Team Council / Opinion Aggregator Skill — Spec v0.1

## 목적
주제 1개를 입력하면 **역할 분할(라이트 3~5명 / 프로 실제 스쿼드)** 로 의견을 수집하고,
**합의/반대/리스크/가정**을 구조화해 **추천(Recommendation) + 다음 액션**을 도출한다.

## 제품 구성
### Lite (무료): Solo Split-Brain (5 roles)
- 단일 에이전트가 역할 5개로 순차 시뮬레이션
- **역할명 표기 규칙:** Lite는 항상 **영문 역할명** 사용 + 이모지 병기 (예: 🧿 Oracle / 🧠 Analyzer / ⚔️ Security / ⚡ Builder / 📢 Comms)
- 기본 역할(고정):
  1) Oracle — 결정 프레임/가정/최종 추천
  2) Analyzer — 정량/우선순위/스코어
  3) Security — 보안/리스크/컴플라이언스
  4) Builder — 구현 가능성/MVP/일정/비용
  5) Comms — 메시지/시장 반응/커뮤니케이션

### Pro (유료): AOI Squad Orchestrator 연동
- 실제 에이전트(요원) 병렬 호출 + 결과 집계
- **역할명 표기 규칙:**
  - 우리 서버 내부(aoineco): 팀원 한글 닉네임 **+ 이모지** 사용 (예: 🧿청령/⚔️청검/⚡청섬/📢청음…)
  - 외부 고객: 고객이 보유한 에이전트/워크포스의 **실제 에이전트명**을 그대로 사용
- 예산/시간 상한, 종료 조건, 출처 신뢰도(Confidence) 라벨링 포함

## 입력(Inputs)
- topic: string (필수)
- mode: one of {decision, planning, evaluation}
- context: string (선택, 배경)
- constraints: {time, budget, risk_tolerance, must_have, must_not}
- sources: {local_only|notion_only|web_optional} (기본: local_only)
- storage: {notion|local|server} (기본: local)

## 출력(Outputs) — 고정 포맷
1) TL;DR (2줄)
2) Role opinions (각 2~3줄)
3) 합의점 / 갈등점
4) Dissent(반대의견) — 반드시 1개 이상
5) Assumptions (3개)
6) Recommendation: Go/No-Go/Conditional + Confidence
7) Next actions Top 3 (구체적)

## 시나리오 템플릿
### Decision
- Go/No-Go/Conditional
- 리스크/가정/대안

### Planning
- PRD outline + MVP 범위
- 1주 실행 플랜 + KPI

### Evaluation
- 후보 A/B/C 비교 + 스코어링
- 추천 1순위 + 보류 사유

## 안전/가드레일
- 외부 게시 금지(기본): 마지막에 항상 승인 게이트
- 민감정보(키/지갑/내부전략) 금지 필터
- 비용 상한/시간 상한: Pro에서 필수

## 저장(SSOT) — Storage plugin 설계
- Notion: Decision Log DB에 저장 (우리 기본)
- Local: workspace/decisions/YYYY-MM-DD_<slug>.md
- Server: Supabase/Postgres (Pro)

## 우리 Notion SSOT (권장)
- DB: 🧾 ADR / Decision Log
- properties(최소): Name, Mode, Recommendation, Confidence, Risk, Tags, Project, Source URL, Status
- children: TL;DR, Role opinions, Consensus/Conflict, Dissent, Assumptions, Next actions
