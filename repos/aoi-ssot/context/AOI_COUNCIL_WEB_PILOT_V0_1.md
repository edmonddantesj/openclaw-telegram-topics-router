# AOI Council Web Pilot (v0.1)

## Purpose
웹에서 가볍게 AOI Council Lite/Pro 의사결정 지원을 테스트할 수 있는 최소 파일럿 서버.
실행은 report-only로, L3 변경(돈/지갑/온체인 서명/외부게시/비가역)은 정책 점수로 경고/조치 권고.

## Entry point
- `scripts/council_web_pilot.py`
- 서버 구동: `python3 scripts/council_web_pilot.py --port 8080`
- 기본: `/` 접속

## Runtime modes
- `--pro-access`:
  - `direct` (기본): Pro 입력 즉시 실행
  - `request` (요청형 큐): Pro는 큐(승인요청)로 들어감
  - `off`: Pro 비활성(요청 즉시 거부)

## 승인형 운영 예시
1. 파일럿 서버 실행
   - `python3 scripts/council_web_pilot.py --port 8080 --pro-access request --pro-admin-token <TOKEN>`
2. 사용자가 Pro 실행 요청 시 응답:
   - `{"status":"approval_required","request_id":"proreq_..."}`
3. 운영자 승인:
   - `curl -H 'X-Admin-Token: <TOKEN>' -H 'Content-Type: application/json' -X POST /api/council/pro-requests/resolve -d '{"request_id":"proreq_...","action":"approve"}'`

## Endpoints
- `GET /` : UI
- `POST /api/council/run`
  - payload: `{topic, context, mode: lite|pro, profile, constraints}`
  - returns `accepted/task_id` and completion can be polled
- `GET /api/council/task/<task_id>`
- `GET /api/profiles`
- `GET /api/council/run/<run_id>`
- `GET /api/council/pro-requests?status=pending`
- `POST /api/council/pro-requests/resolve`
  - payload: `{request_id, action: approve|reject}`
  - requires header `X-Admin-Token`

## Output
응답에는 다음이 포함됨:
- run id
- synthesis (recommendation/confidence/risk)
- policy summary (`status`, `score`, `warn_count`, `fail_count`, `weighted_breakdown`)
- artifact paths (`manifest.json`, `report.md`, `policy_check.json`, `policy_scorecard.json`, ...)
- report preview (요약 텍스트)

## Safety behavior
- 기본적으로 report-only 실행
- `--pro-access request` 조합 시 Pro는 승인 큐형 (수동 승인 필요)
- 설정은 실행 시 `AOI_COUNCIL_POLICY_CONFIG`에 의해 정책 엔진 오버라이드

## SSOT 링크
- Policy config: `AOI_COUNCIL_POLICY_ENGINE_CONFIG_V0_1.json`
- Profile: `AOI_COUNCIL_POLICY_ENGINE_PROFILE_*_V0_1.json`
- Runner: `scripts/aoi_council_run.py`


## 비동기 동작
- `/api/council/run`은 `accepted/task_id` 형식으로 즉시 응답 후 백그라운드 실행합니다.
- 클라이언트는 `GET /api/council/task/<task_id>`로 상태를 폴링합니다.
- 상태: `queued`, `running`, `completed`, `failed`.
- 완료 시 `manifest`와 `report_preview`를 포함해 반환됩니다.


## UI UX
- 질문 입력 시 `Conversation` 영역에 사용자 발화/상태/조언이 순차적으로 표시되는 채팅형 UX로 전환됨.
- 제출 즉시 `Task ID` 응답, 브라우저가 `/api/council/task/<task_id>`를 폴링해 queued/running/completed 상태를 자동 갱신.

## Task polling 응답 스키마(동기화 반영, v0.1.1)
- `/api/council/task/<task_id>` 완료 응답(`status=completed`)에서 다음 필드를 확인해 **Action/Permission/Cost 게이트 정합성**을 함께 노출/검증:
  - `manifest.verdict.action`
  - `manifest.verdict.evidence_id`
  - `manifest.verdict.permission.status`
  - `manifest.verdict.permission.decision`
  - `manifest.verdict.cost_governor.status`
  - `manifest.verdict.cost_governor.decision`
  - `manifest.verdict.cost_governor.auto_action`
  - `manifest.verdict.cost_governor.reason`
  - `manifest.policy_check` (기존)
  - `manifest.permission_scope_check`
  - `manifest.cost_governor_check`
- UI `Conversation` 카드/요약/`verdict` JSON 뷰에서도 위 필드가 반영되므로 사람이 읽는 증적과 기계 판독 증적이 일치.
- smoke 체크 권고:
  1. `/api/council/run` 제출 후 `task_id` 획득
  2. `/api/council/task/<task_id>` 완료 시 위 3축 게이트 항목 교차 확인
  3. `manifest.failures`와 `synthesis.action_decision`/`manifest.verdict.action` 일치성 확인
