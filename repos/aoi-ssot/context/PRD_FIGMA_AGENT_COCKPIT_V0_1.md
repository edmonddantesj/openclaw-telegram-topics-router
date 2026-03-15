# PRD v0.1 — Figma Agent Cockpit (Code↔Canvas Loop)

## 0) One-liner
AI 코딩 에이전트가 만드는 프런트엔드의 **현재 UI 상태를 주기적으로 Figma로 push**하고, 디자이너가 Figma에서 수정한 결과를 **구조화 diff로 다시 코드/에이전트 루프에 반영**한다.

## 1) Target user
- 5~30명 규모 제품팀(디자이너 1~3, 프런트 1~5)
- 에이전시/웹스튜디오

## 2) Problem
- 에이전트/터미널 기반 개발은 **진행 중 UI 피드백 루프가 느림**
- 디자이너 수정 의도가 코드로 전달될 때 번역 손실이 큼

## 3) MVP scope (2주 MVP)
- 단방향부터 시작: **에이전트 → Figma**
  - (MVP-1) URL 또는 로컬 dev 서버 화면 스냅샷/렌더를 Figma 프레임으로 업로드
  - (MVP-2) 주기(예: 2~5분)로 업데이트 + 변경 타임라인
  - (MVP-3) 체크포인트마다 “요청/의도/커밋 해시” 메타데이터 기록

## 4) v1 scope (4~6주)
- 제한된 양방향: **Figma 수정 → JSON diff**
  - 텍스트 변경, spacing, color, font size 등 제한된 속성만
  - diff를 PR 코멘트/issue spec으로 내보내기

## 5) Success metrics
- 디자이너 피드백 루프 시간(분) 50% 감소
- UI 관련 rework PR 수 감소

## 6) Risks
- Figma↔코드 매핑 난이도(semantic alignment)
- 디자인 시스템 없는 팀에선 효과 제한

## 7) Pricing (가설)
- Team: $39~$99/seat/mo 또는 프로젝트당 요금

## 8) Aoineco 적용 포인트
- Proof-first 아티팩트(스냅샷/manifest/sha256)를 기본 제공하여 “재현 가능”을 SSOT로 박제
