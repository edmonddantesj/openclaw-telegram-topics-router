# Topic State — v6-invest

- Topic: `v6-invest`
- Telegram topic id: `1029`
- Status: ACTIVE
- Last saved: 2026-03-08 23:13 KST

## Current objective
- V6/Limitless 운영의 결정·검증·반복업무를 SSOT로 고정하고, 운영 중단 없이 이어받게 한다.

## Latest checkpoint
- 거래 룰은 고정 시간이 아니라 EV 최대 타임 슬롯 선택 정책으로 전환되었고, 초기 고정시간은 폐기됐다.
- Limitless agents-starter DRY_RUN에서 zero-price edge case가 발견돼 LIVE 전 guardrail 필요가 확인됐다. Source: memory/2026-03-05.md#L568-L584
- 현재 active HF는 `context/handoff/HF_v6_invest_live_restart_202603.md`이며, 재개발/실투 재개/자동화 루틴이 이 축으로 이어진다.

## Decisions locked
- 큰 작업은 HF 1장 분리.
- Live 전환은 proof 우선.
- Fail-closed/가드 우선, 카나리 한도 자동 상향 금지.
- 중복 알림은 원문 재공유 대신 기존 HF만 유지.

## Next actions
1. 현재 live/dryrun 상태와 blocker를 checkpoint에 갱신.
2. entrypoint/repo/commit/env path 식별자를 유지.
3. launchd routine 산출물과 HF의 일치 여부를 주기 확인.

## Key files
- Playbook: `context/topics/v6-invest_PLAYBOOK_V0_1.md`
- Handoff: `context/handoff/HF_v6_invest_live_restart_202603.md`
- Topic map: `context/telegram_topics/thread_topic_map.json`

## Restore instructions
- 먼저 이 파일을 읽고, 실제 내용이 얇으면 Playbook과 관련 HF를 최소만 추가로 읽는다.
- 복구 응답은 `현재 목표 / 마지막 체크포인트 / 다음 액션` 순서로 짧게 재구성한다.

## Notes
- v6-invest는 상태가 빨리 변한다. “마지막 저장 시각 + 현재 모드(dry/live)”를 꼭 남겨라.
