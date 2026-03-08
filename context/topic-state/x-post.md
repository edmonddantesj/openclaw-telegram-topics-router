# Topic State — x-post

- Topic: `x-post`
- Status: ACTIVE
- Last saved: 2026-03-08 23:00 KST

## Current objective
- X에서 터질 각 콘텐츠를 발굴해 후보 3개 + 선정 1개 초안을 안정적으로 생산하는 운영 루틴 유지.

## Latest checkpoint
- Topic 956 export 기반으로 Playbook/HF 분리 완료.
- 운영 고정값(08:10 / 12:10 / 18:10, 좋아요 500+ 기본, 자동 게시 금지, 바닷가재 RPG 이미지 컨셉) 정리됨.
- launchd 미부트스트랩 문제를 원인으로 특정 회차 미발행 이슈를 교정했고, 설치/증빙 경로까지 남겨둠.

## Decisions locked
- 자동 게시 금지, 메르세데스가 최종 수동 복붙.
- discovery는 브라우저 기반 로그인 세션 스캔 우선.
- 한국어 재바이럴은 제외.
- 게시글 톤은 친절한 존대, 이미지 1장 동반 권장.

## Next actions
1. 회차별 후보3 + 초안1 산출 유지.
2. 실패 시 원인/단계/캡차 여부 증빙 남기기.
3. 룰 변경 생기면 Playbook 즉시 갱신.

## Key files
- Playbook: `context/topics/x-post_PLAYBOOK_V0_1.md`
- Handoff: `context/handoff/HF_x-post.md`
- Automation: `context/automation/launchd/com.aoineco.xpost.tick.plist`
- Logs/Evidence: `logs/launchd/xpost_tick.log`, `artifacts/x-post/`

## Restore instructions
- 먼저 이 파일 읽기
- 이어서 `context/topics/x-post_PLAYBOOK_V0_1.md`
- 진행 이슈 있으면 `context/handoff/HF_x-post.md`
- 자동화/실패 증빙이 필요하면 launchd log와 artifacts 확인

## Notes
- 운영 핵심은 “발굴/초안 생산 자동화”이지 “자동 게시”가 아니다.
