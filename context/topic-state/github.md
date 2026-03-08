# Topic State — github

- Topic: `github`
- Telegram topic id: `60`
- Status: ACTIVE
- Last saved: 2026-03-08 23:08 KST

## Current objective
- GitHub 링크 인입 → 분석/도입/적용(LOCAL APPLY) + 광역 영향(WIDE REVIEW) 분리 운영

## Latest checkpoint
- GitHub 관련 intake는 local apply + wide review 2층 처리 원칙을 따른다.
- PR/이슈/CI/코드 리뷰 등은 GitHub 운영 토픽에서 추적하고, 큰 작업은 별도 HF로 분리하는 구조가 맞다.
- 복구 시에는 현재 목표와 대상 repo/repo link를 가장 먼저 확인해야 한다.

## Decisions locked
- 모든 토픽은 기본적으로 `context/topic-state/<slug>.md`를 가진다.
- 반복 규칙은 Playbook, 열린 이슈는 HF, 즉시 복구 요약은 topic-state에 둔다.

## Next actions
1. 현재 repo/PR/issue 식별자를 checkpoint에 남기기.
2. 큰 변경/막힘은 HF에 누적.
3. 이번주 apply / SSOT promotion / risk buckets로 정리 유지.

## Key files
- Playbook: `context/topics/github_PLAYBOOK_V0_1.md`
- Handoff: (없음)
- Topic map: `context/telegram_topics/thread_topic_map.json`

## Restore instructions
- 먼저 이 파일을 읽고, 실제 내용이 얇으면 Playbook과 관련 HF를 최소만 추가로 읽는다.
- 복구 응답은 `현재 목표 / 마지막 체크포인트 / 다음 액션` 순서로 짧게 재구성한다.

## Notes
- GitHub 토픽은 식별자(repo, PR, issue) 없으면 복구 품질이 급락하니 항상 남긴다.
