# Topic State — inbox-dev

- Topic: `inbox-dev`
- Telegram topic id: `585`
- Status: ACTIVE
- Last saved: 2026-03-08 23:08 KST

## Current objective
- 긴급개발/핫픽스/데드라인 대응 (실행 우선)

## Latest checkpoint
- 긴급개발 토픽은 식별자 먼저, proof-first, 중단 직전 Next 3 남기기 규칙이 고정됨.
- 현재 대표 HF는 HF_inbox_dev_urgent_202603이며, 긴급개발/핫픽스/데드라인 대응의 기준 파일이다.
- GitHub auth 환경변수가 gh 인증을 덮어쓰는 함정도 공통 pitfall로 정리되어 있다.

## Decisions locked
- 모든 토픽은 기본적으로 `context/topic-state/<slug>.md`를 가진다.
- 반복 규칙은 Playbook, 열린 이슈는 HF, 즉시 복구 요약은 topic-state에 둔다.

## Next actions
1. 새 P0 발생 시 HF/토픽+키워드 식별자부터 확보.
2. 중단 전 Next 3를 이 파일 또는 HF에 남기기.
3. 배포 URL/PR/로그 등 최소 1개 proof 확보.

## Key files
- Playbook: `context/topics/inbox-dev_PLAYBOOK_V0_1.md`
- Handoff: `context/handoff/HF_inbox_dev_urgent_202603.md`
- Topic map: `context/telegram_topics/thread_topic_map.json`

## Restore instructions
- 먼저 이 파일을 읽고, 실제 내용이 얇으면 Playbook과 관련 HF를 최소만 추가로 읽는다.
- 복구 응답은 `현재 목표 / 마지막 체크포인트 / 다음 액션` 순서로 짧게 재구성한다.

## Notes
- inbox-dev는 속도보다 식별자/증빙 누락 방지가 더 중요하다.
