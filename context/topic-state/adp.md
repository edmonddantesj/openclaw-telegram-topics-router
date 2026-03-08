# Topic State — adp

- Topic: `adp`
- Telegram topic id: `45`
- Status: ACTIVE
- Last saved: 2026-03-08 23:08 KST

## Current objective
- Aoineco Dataplane(ADP) — 운영/업무/픽셀오피스/라벨링/보드(Jira/Ralph) 가시화 포털을 SSOT로 고정

## Latest checkpoint
- ADP 관련 플레이북/참고노트/체크리스트가 context/adp 및 topics playbook으로 정리되어 있다.
- 토픽 state는 ADP 관련 현재 추진축과 열린 이슈를 압축 보관하는 용도로 편입되었다.
- 세부 증빙은 관련 SSOT/HF 문서에서 읽는 구조다.

## Decisions locked
- 모든 토픽은 기본적으로 `context/topic-state/<slug>.md`를 가진다.
- 반복 규칙은 Playbook, 열린 이슈는 HF, 즉시 복구 요약은 topic-state에 둔다.

## Next actions
1. 현재 추진중인 ADP 이슈가 생기면 checkpoint를 구체화.
2. 반복 규칙은 playbook에 유지.
3. 장기 작업은 HF로 분리.

## Key files
- Playbook: `context/topics/adp_PLAYBOOK_V0_1.md`
- Handoff: (없음)
- Topic map: `context/telegram_topics/thread_topic_map.json`

## Restore instructions
- 먼저 이 파일을 읽고, 실제 내용이 얇으면 Playbook과 관련 HF를 최소만 추가로 읽는다.
- 복구 응답은 `현재 목표 / 마지막 체크포인트 / 다음 액션` 순서로 짧게 재구성한다.

## Notes
- ADP는 참조 문서가 많아 topic-state는 우선순위/현 상태 위주로만 쓴다.
