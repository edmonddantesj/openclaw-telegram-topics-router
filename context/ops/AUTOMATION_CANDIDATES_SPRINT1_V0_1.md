# AUTOMATION_CANDIDATES_SPRINT1_V0_1

Scope (Sprint 1): ops / maintenance / inbox-dev / github

Policy: DM Export Shadow Ingest → Safe Promotion (`context/ops/DM_EXPORT_SHADOW_INGEST_AND_SAFE_PROMOTION_POLICY_V0_1.md`)

## A) launchd (fixed schedule) candidates

### A1. Maintenance digest (3h)
- Type: launchd
- Why: 고정 주기, 실패 시 즉시 알림이 중요
- Inputs: health checks + digest generator
- Output/Proof: `artifacts/digest/digest_YYYYMMDD_HHMMSS.txt` (PASS/FAIL)
- Status: 이미 maintenance playbook에 schedule 존재(SSOT). 실제 plist/runner 정합성 점검 필요.

### A2. Notion sync digest (AM/PM)
- Type: launchd
- Why: 고정 주기(08:50/20:50), 장애 감지(권한/env/유령 DB) 시 빠른 대응 필요
- Output/Proof: notion digest artifact/log
- Risk: env 불일치/키 누락은 false-success 유발 → proof link 강제

### A3. Knowledge index digest (daily)
- Type: launchd
- Why: 매일 09:01 고정, SSOT index 갱신

### A4. maintenance daily smoke
- Type: launchd
- Why: 매일 09:10 고정, 실패만 알림

### A5. SAVE NOW reminder (optional)
- Type: launchd
- Why: “큰 변경 후 스냅샷 박제”를 잊지 않게 리마인드(강제 실행은 아님)
- Note: 실행은 수동 트리거가 원칙. 리마인드만 자동.

## B) Ralph Loop (backlog/throughput) candidates

### B1. GitHub→Notion Reference backlog fill (table + open page content)
- Type: Ralph Loop
- Why: 항목이 쌓이는 백로그형. 매 시간/매일 N개 oldest-first로 처리 적합.
- Output/Proof: Notion DB row + detail page + HF 링크
- Failure modes: DB ID/워크스페이스 mismatch, content append 실패 → proof 갱신 필요

### B2. DM export “none/untagged” triage
- Type: Ralph Loop
- Why: 고정 주기보다 처리량 기반이 적합. 오래된 미분류부터 N개씩 태깅/승격.
- Output/Proof: playbook 섹션에 추가 + msgId 증빙

### B3. Ops incident postmortem capture
- Type: Ralph Loop
- Why: 사건 발생 시 큐로 쌓아두고, 여유 있을 때 HF/SSOT로 정리

## C) “Safe Promotion” candidates (to Forum topics)
- ops: Notion 장애 대응 체크리스트(유령 DB/ID 검증/env 불일치) → patch 1개로 발행 가능
- github: "표+본문" 완료 조건(Definition of Done) → patch 1개
- maintenance: 선보고 후조치 규칙 → patch 1개
- inbox-dev: 상태 만료/재스캔 1차 대응 룰 → patch 1개

## D) Next actions
1) (필수) 실제 launchd plist/runner 존재 여부 및 스케줄 정합성 감사 (maintenance 77 리포트 포맷으로 PASS/FAIL)
2) (권장) GitHub→Notion backlog를 Ralph Loop로 ‘N per hour’ 정책 정의
3) (권장) Safe Promotion 패치 4개를 각 토픽에 배포(충돌 체크 후)
