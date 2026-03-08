# Topic State — adp

- Topic: `adp`
- Telegram topic id: `45`
- Status: ACTIVE
- Last saved: 2026-03-08 23:13 KST

## Current objective
- Aoineco Dataplane(ADP)의 운영/보드/라벨링/픽셀오피스 가시화 포털을 SSOT로 유지한다.

## Latest checkpoint
- ADP 정식 명칭, 서버 헬스 복구, tailnet URL/로컬 URL 구분, Ralph Loop 분류/집계 뷰 유지가 playbook에 고정돼 있다.
- ADP는 보드 분류 규칙과 라벨 정책을 Ralph Loop 실행 모드와 연결하는 허브 성격이 강하다.
- 실행 이슈가 생기면 헬스체크 결과와 뷰/라벨 누락 여부를 함께 기록해야 한다.

## Decisions locked
- ADP 명칭은 Aoineco Dataplane로 고정.
- 응답 먹통 시 restart는 가능하지만, 먼저 상태와 접근 URL 구분을 확인.
- Ralph Loop 뷰/라벨은 넓게 포함해 집계한다.

## Next actions
1. 현재 ADP 서버 상태와 접근 경로(tailnet/local)를 checkpoint에 남긴다.
2. 보드/라벨 누락이 있으면 Ralph Loop 태스크로 분리.
3. 헬스체크 자동화 후보는 ops/maintenance와 연결해 정리.

## Key files
- Playbook: `context/topics/adp_PLAYBOOK_V0_1.md`
- Handoff: (없음)
- Topic map: `context/telegram_topics/thread_topic_map.json`

## Restore instructions
- 먼저 이 파일을 읽고, 실제 내용이 얇으면 Playbook과 관련 HF를 최소만 추가로 읽는다.
- 복구 응답은 `현재 목표 / 마지막 체크포인트 / 다음 액션` 순서로 짧게 재구성한다.

## Notes
- ADP는 UI/보드/라벨이 섞이므로 “서버 상태”와 “뷰 정책”을 같이 적어야 덜 꼬인다.
