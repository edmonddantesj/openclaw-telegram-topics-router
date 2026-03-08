# Topic State — announcements

- Topic: `announcements`
- Telegram topic id: `32`
- Status: PAUSED
- Last saved: 2026-03-08 23:13 KST

## Current objective
- 외부 공지/발행성 작업의 승인 게이트와 산출 흐름을 추후 재개 가능하게 보관한다.

## Latest checkpoint
- 현재는 paused 상태지만, 외부 발행 토픽은 승인 게이트와 증빙 번들이 항상 전제되어야 한다.
- 커뮤니티 Auto-Archive의 Live-Sync 원칙상, 게시 후 최종 URL을 활동 로그에 남기는 것이 장기 규칙이다. Source: MEMORY.md#L28-L31
- 재가동 시 채널/톤/승인 단계부터 먼저 적어야 한다.

## Decisions locked
- 외부 게시/공지성 작업은 기본적으로 승인 전제.
- 최종 게시 후 URL 증빙을 남긴다.
- paused 토픽은 재개 조건을 명확히 적는다.

## Next actions
1. 재가동 시 목적, 채널, 승인권자, 산출 포맷을 checkpoint에 채운다.
2. 반복 흐름이 생기면 playbook 승격.
3. 큰 캠페인은 HF로 분리.

## Key files
- Playbook: `context/topics/announcements_PLAYBOOK_V0_1.md`
- Handoff: (없음)
- Topic map: `context/telegram_topics/thread_topic_map.json`

## Restore instructions
- 먼저 이 파일을 읽고, 실제 내용이 얇으면 Playbook과 관련 HF를 최소만 추가로 읽는다.
- 복구 응답은 `현재 목표 / 마지막 체크포인트 / 다음 액션` 순서로 짧게 재구성한다.

## Notes
- announcements는 비활성이어도 승인/증빙 규칙만은 잊지 않게 남겨두는 토픽이다.
