# AOI_COST_GOVERNOR_V0_1

## 목표
AI/에이전트 실행 비용(토큰/요청/트랜잭션/리트라이)을 제한해 runaway 비용(루프/재시도 폭주)을 막고, 운영 안정성을 확보한다.

## 적용 범위
- AOI Council 작업 큐, 어댑터 실행, 외부 API/체인 호출 래퍼
- v0.1: 오프체인 비용 게이트 + 제한 정책 + 알림 + manual override
- 범위: `/api/council/run`, `pro` 요청 승인 파이프라인, 실행 워커

## 정책 모델
```json
{
  "governor_version": "0.1",
  "scope": "task|agent|user|org",
  "window_seconds": 3600,
  "max_tasks_per_minute": 12,
  "max_tasks_per_hour": 180,
  "max_retries_per_task": 3,
  "max_retries_per_window": 50,
  "retry_backoff_ms": [1000, 3000, 8000],
  "budget_usd": {
    "soft": 5,
    "hard": 7,
    "currency": "USDC",
    "chain":"Base"
  },
  "auto_actions": {
    "on_warn": "decrease_rate|notify_only",
    "on_critical": "pause_agent|hold_tasks|require_manual_unhold"
  },
  "burst_guard": {
    "task_spike_ratio": 4,
    "window_size_seconds": 300
  }
}
```

## 상태
- `ok`: 통과
- `warn`: 비용/속도 이상치 탐지(지연, 제한 임계치 근접)
- `critical`: 작업 일시중단 또는 hold 적용
- `hard_block`: 예산 초과 또는 연속 실패 루프

## 동작 규칙
1. `warn/critical` 분기에서 비용 증감 임계치가 교차할 경우 `hold` 플래그 세팅.
2. 동일 task에서 `max_retries_per_task` 초과 시 hard stop + 원인 로그 + 관리자 승인 필요.
3. 큐 백로그/스파이크 감지 시 신규 요청을 `queued`에서 `deferred`로 격리 가능.
4. 예산 소진 시 자동으로 `mode=lite`/`pro` 모두 실행 정지 후 대체 채널로 `요청 검토`.
5. 해제는 승인 API 또는 만료 자동 해제.

## 에러 코드
- `CG-001`: budget_soft_exceeded
- `CG-002`: budget_hard_exceeded
- `CG-003`: retry_limit_exceeded
- `CG-004`: rate_limit_hit
- `CG-005`: burst_detected

## 테스트 케이스 (v0.1)
1. **TC-CG-01** 정상 rate 내 실행 => ok
2. **TC-CG-02** 5분 내 task 폭주 => warn + notify
3. **TC-CG-03** retry 초과 => hard stop + AGENT hold
4. **TC-CG-04** soft budget 임계치 도달 => warn + rate 감소
5. **TC-CG-05** hard budget 초과 => block + 관리자 승인 필요
6. **TC-CG-06** manual override 승인 후 resume => 정상 복구

## 구현 인터페이스
- Runtime state: `aoi-core/state/cost_governor_state.json`
- 지표 수집: `run_id`, `agent_id`, `token_delta_est`, `api_calls`, `retry_count`, `queue_delay_ms`
- 이벤트: `cost_gov_warn`, `cost_gov_hold`, `cost_gov_resume`

## AOI 통합 지점
- `council_web_pilot.py` submit 제한 조건 및 상태 메시지(`policy/hold`)에 반영
- `aoi_council_run.py` 매 실행 라운드에서 `runtime_budget_before`/`runtime_budget_after` 기록
- 리포트 manifest에 비용 게이트 감사 결과 추가

## 운영 규칙
- default cap은 보수적으로 유지(과금/토큰 소진 위험 회피)
- 경고 상태에서는 사용자에게 대체 UX 제공(요약 복사/재시도 안내)

