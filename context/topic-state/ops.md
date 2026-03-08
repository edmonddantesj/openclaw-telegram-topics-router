# Topic State — ops

- Topic: `ops`
- Telegram topic id: `38`
- Status: ACTIVE
- Last saved: 2026-03-08 23:08 KST

## Current objective
- Mac mini/OpenClaw 운영(게이트웨이/launchd/cron/백업/드리프트) + 운영 규칙을 SSOT로 고정

## Latest checkpoint
- ops 토픽은 운영 프로토콜/자동화/정책성 SSOT를 모으는 허브 성격으로 유지.
- 관련 정본은 context/ops/ 하위 문서에 누적되고, 토픽 state는 그중 현재 재개용 압축 상태를 담당.
- 큰 운영 이슈는 handoff 문서와 연결해 추적하는 구조를 따른다.

## Decisions locked
- 모든 토픽은 기본적으로 `context/topic-state/<slug>.md`를 가진다.
- 반복 규칙은 Playbook, 열린 이슈는 HF, 즉시 복구 요약은 topic-state에 둔다.

## Next actions
1. 새 운영 정책/자동화가 생기면 관련 SSOT 경로를 이 파일에도 반영.
2. 실행중 이슈는 HF로 승격.
3. 토픽 복구 시 최근 ops 문서만 최소 읽기.

## Key files
- Playbook: `context/topics/ops_PLAYBOOK_V0_1.md`
- Handoff: (없음)
- Topic map: `context/telegram_topics/thread_topic_map.json`

## Restore instructions
- 먼저 이 파일을 읽고, 실제 내용이 얇으면 Playbook과 관련 HF를 최소만 추가로 읽는다.
- 복구 응답은 `현재 목표 / 마지막 체크포인트 / 다음 액션` 순서로 짧게 재구성한다.

## Notes
- ops는 범위가 넓으니 이 파일은 반드시 짧은 허브 요약으로 유지.
