# Topic State — moltbook

- Topic: `moltbook`
- Telegram topic id: `1114`
- Status: ACTIVE
- Last saved: 2026-03-08 23:08 KST

## Current objective
- Moltbook(EN) 커뮤니티 운영(글/댓글/대댓글) + Daily/Weekly 콘텐츠 루프를 “승인 게이트 + 증빙”으로 굴리기

## Latest checkpoint
- moltbook 토픽은 운영 복구(키/스크립트/SSOT)와 daily/weekly 루프 자동화 축으로 관리된다.
- 현재 주요 작업은 HF_moltbook_ops_202603에 연결되어 있다.
- 토픽 state는 현재 운영 상태, 열린 blocker, 다음 발행/운영 액션을 압축 기록하는 용도다.

## Decisions locked
- 모든 토픽은 기본적으로 `context/topic-state/<slug>.md`를 가진다.
- 반복 규칙은 Playbook, 열린 이슈는 HF, 즉시 복구 요약은 topic-state에 둔다.

## Next actions
1. 현재 운영 health와 다음 루프 액션을 갱신.
2. 자동화/스크립트 변화는 관련 SSOT에도 반영.
3. 장기 이슈는 HF 유지.

## Key files
- Playbook: `context/topics/moltbook_PLAYBOOK_V0_1.md`
- Handoff: `context/handoff/HF_moltbook_ops_202603.md`
- Topic map: `context/telegram_topics/thread_topic_map.json`

## Restore instructions
- 먼저 이 파일을 읽고, 실제 내용이 얇으면 Playbook과 관련 HF를 최소만 추가로 읽는다.
- 복구 응답은 `현재 목표 / 마지막 체크포인트 / 다음 액션` 순서로 짧게 재구성한다.

## Notes
- moltbook는 운영/발행이 섞여 있어 다음 액션을 구체적으로 적는 편이 좋다.
