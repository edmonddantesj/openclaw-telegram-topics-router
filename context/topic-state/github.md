# Topic State — github

- Topic: `github`
- Telegram topic id: `60`
- Status: ACTIVE
- Last saved: 2026-03-08 23:13 KST

## Current objective
- GitHub 링크 인입을 local apply + wide review 2층 처리로 운영하고, repo/PR/issue 단위로 재개 가능하게 유지한다.

## Latest checkpoint
- GitHub 인입은 즉시 적용(Local apply)과 AOI 전체 영향 검토(Wide review)로 분리하는 것이 기본값이다. Source: MEMORY.md#L36-L44
- Notion 기록 시 표 속성 + 본문 리포트까지 채워져야 완료이며, 동명 DB/유령 DB 오입력 방지가 중요하다.
- 복구 품질의 핵심 식별자는 repo / PR / issue / run id다.

## Decisions locked
- 리포트는 3줄 요약 + 기술 구조 + 적용 인사이트 포맷 유지.
- 실행 컨텍스트 auth 오염(GITHUB_TOKEN 등)을 우선 점검.
- 보고는 this-week apply / SSOT promotion / risks-conflicts 3버킷 유지.

## Next actions
1. 현재 다루는 repo/PR/issue 식별자를 state 또는 HF에 남긴다.
2. 큰 작업/막힘은 HF로 분리.
3. Notion 연계 작업이면 대상 DB ID와 본문 완결 여부를 검증.

## Key files
- Playbook: `context/topics/github_PLAYBOOK_V0_1.md`
- Handoff: (없음)
- Topic map: `context/telegram_topics/thread_topic_map.json`

## Restore instructions
- 먼저 이 파일을 읽고, 실제 내용이 얇으면 Playbook과 관련 HF를 최소만 추가로 읽는다.
- 복구 응답은 `현재 목표 / 마지막 체크포인트 / 다음 액션` 순서로 짧게 재구성한다.

## Notes
- GitHub 토픽은 식별자가 곧 복구 품질이다. 링크나 번호 없이 “그 작업”이라고만 남기지 않는다.
