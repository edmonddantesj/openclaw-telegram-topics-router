# AUTOMATION_CANDIDATES_SPRINT3_V0_1

Status: DRAFT (Sprint 3 seed)
Last updated: 2026-03-08

Sprint 3 topics: v6-invest / x-post / longform / hackathons

## Candidate list (initial)

### v6-invest
- Routine artifacts + HF health check (existing) 강화
  - Trigger: hourly or daily
  - Output: `artifacts/v6_invest_routine/*` + HF update hint
  - Risk: L3 gates (money/keys) must stay fail-closed

### x-post
- Candidate discovery run 3/day (08:10 / 12:10 / 18:10 KST)
  - Output: 후보3 + 초안1 + 인용박스
  - Guard: 자동 게시 금지 (copy/paste only)
  - Engine: browser discovery + jina-ai extraction fallback

### longform
- PDF/link ingest → 요약 + 핵심 인용 + SSOT 승격 경로 패키징
  - Trigger: on-demand + (optional) daily batch
  - Guard: 모델 선택(TPM) 정책 준수

### hackathons
- Repo scan → 제출 패키지 skeleton 생성
  - Trigger: weekly
  - Guard: 외부 제출/게시(L3) 분리, 내부 패키징은 L1/L2

## Decision rule: launchd vs Ralph Loop
- launchd: 고정주기, 로컬 안정성/비인터랙티브 실행
- Ralph Loop: 백로그/드리프트/상태 저장/triage 결합이 필요할 때

## Next
- Sprint 3 shadow-ingest를 진행하면서 항목을 구체화(입력/산출/증빙/알림/롤백).
