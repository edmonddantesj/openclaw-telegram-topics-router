# Topic State — v6-invest

- Topic: `v6-invest`
- Telegram topic id: `1029`
- Status: ACTIVE
- Last saved: 2026-03-08 23:08 KST

## Current objective
- V6/Limitless 운영의 결정·검증·반복업무를 SSOT로 고정하고, 운영 중단 없이 이어받을 수 있게 유지한다.

## Latest checkpoint
- V6/Limitless 운영은 결정·검증·반복업무를 SSOT로 고정하고 운영 중단 없이 이어받는 것이 핵심이다.
- 현재 열린 주요 작업은 HF_v6_invest_live_restart_202603에 연결되어 있다.
- 실행 타이밍/재개발/운영 복구는 topic-state에서 압축, 세부 증빙은 HF/관련 스크립트에서 읽는 구조다.

## Decisions locked
- 모든 토픽은 기본적으로 `context/topic-state/<slug>.md`를 가진다.
- 반복 규칙은 Playbook, 열린 이슈는 HF, 즉시 복구 요약은 topic-state에 둔다.

## Next actions
1. 현재 운영 상태와 blocker를 checkpoint에 주기적으로 갱신.
2. 실투/자동화/검증 변화는 HF와 함께 업데이트.
3. 반복 업무 규칙은 playbook 유지.

## Key files
- Playbook: `context/topics/v6-invest_PLAYBOOK_V0_1.md`
- Handoff: `context/handoff/HF_v6_invest_live_restart_202603.md`
- Topic map: `context/telegram_topics/thread_topic_map.json`

## Restore instructions
- 먼저 이 파일을 읽고, 실제 내용이 얇으면 Playbook과 관련 HF를 최소만 추가로 읽는다.
- 복구 응답은 `현재 목표 / 마지막 체크포인트 / 다음 액션` 순서로 짧게 재구성한다.

## Notes
- v6-invest는 시간/운영상태가 빨리 변하므로 마지막 저장 시각이 특히 중요.
