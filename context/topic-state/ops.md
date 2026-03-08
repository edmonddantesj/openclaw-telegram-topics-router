# Topic State — ops

- Topic: `ops`
- Telegram topic id: `38`
- Status: ACTIVE
- Last saved: 2026-03-08 23:13 KST

## Current objective
- Mac mini/OpenClaw 운영(게이트웨이/launchd/cron/백업/드리프트)과 운영 규칙 SSOT를 안정적으로 유지한다.

## Latest checkpoint
- 운영 토픽의 핵심 반복축은 Gateway 상태 감지, launchd/cron 운용, Notion 연동 장애 분석, SAVE NOW 스냅샷 유지다.
- 큰 변경/불안정 조치 후엔 SAVE NOW로 상태를 박제하는 것이 고정 규칙이다. Source: context/ops/SAVE_NOW_PROTOCOL_V0_1.md
- 재시작/모델전환/설정변경은 선보고 후조치 원칙이 playbook에 고정되어 있다.

## Decisions locked
- 새 주기 작업은 먼저 1회 테스트 후 정기화.
- 운영 장애 대응은 “성공했다고 주장”보다 env/DB ID/실행 컨텍스트 증빙 우선.
- ops는 허브 토픽이므로 세부 사건은 HF/개별 SSOT에 분산하고 여기엔 핵심만 남긴다.

## Next actions
1. 현재 운영 장애나 변경 작업이 있으면 관련 HF와 proof 경로를 checkpoint에 즉시 추가.
2. 주기 작업은 성공/실패 패턴과 증빙 위치를 정리.
3. 큰 조치 전에는 승인 필요 여부를 먼저 분류.

## Key files
- Playbook: `context/topics/ops_PLAYBOOK_V0_1.md`
- Handoff: (없음)
- Topic map: `context/telegram_topics/thread_topic_map.json`

## Restore instructions
- 먼저 이 파일을 읽고, 실제 내용이 얇으면 Playbook과 관련 HF를 최소만 추가로 읽는다.
- 복구 응답은 `현재 목표 / 마지막 체크포인트 / 다음 액션` 순서로 짧게 재구성한다.

## Notes
- ops 토픽은 넓기 때문에 “현재 어떤 운영축을 만지고 있는지”를 첫 줄에 남겨야 복구 품질이 좋아진다.
