# Topic State — handoff

- Topic: `handoff`
- Telegram topic id: `586`
- Status: ACTIVE
- Last saved: 2026-03-08 23:08 KST

## Current objective
- SSOT 기반 handoff/dispatch/compact로 ‘컨텍스트 끊김’ 방지 + 토픽 간 병렬 운영을 제어

## Latest checkpoint
- handoff 토픽은 진행중 큰 작업을 끊김없이 재개하기 위한 HF 중심 허브다.
- ACTIVE 인덱스는 context/handoff/INDEX.md가 정본이며, 각 작업은 HF_*.md로 관리된다.
- topic-state는 현재 어떤 HF를 우선 복구해야 하는지 압축 요약하는 역할을 맡는다.

## Decisions locked
- 모든 토픽은 기본적으로 `context/topic-state/<slug>.md`를 가진다.
- 반복 규칙은 Playbook, 열린 이슈는 HF, 즉시 복구 요약은 topic-state에 둔다.

## Next actions
1. ACTIVE HF 우선순위를 checkpoint에 반영.
2. 새 에픽/큰 작업 시작 시 HF 생성.
3. 완료된 작업은 DONE 처리 및 산출물 링크 남기기.

## Key files
- Playbook: `context/topics/handoff_PLAYBOOK_V0_1.md`
- Handoff: `context/handoff/HF_handoff_compact_reminder_202603.md`
- Topic map: `context/telegram_topics/thread_topic_map.json`

## Restore instructions
- 먼저 이 파일을 읽고, 실제 내용이 얇으면 Playbook과 관련 HF를 최소만 추가로 읽는다.
- 복구 응답은 `현재 목표 / 마지막 체크포인트 / 다음 액션` 순서로 짧게 재구성한다.

## Notes
- handoff는 개별 작업 세부보다 우선순위와 연결 포인터가 중요하다.
