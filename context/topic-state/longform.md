# Topic State — longform

- Topic: `longform`
- Telegram topic id: `65`
- Status: ACTIVE
- Last saved: 2026-03-08 23:08 KST

## Current objective
- 긴 글(가이드/PDF/리서치)을 **요약/추출/SSOT 승격**해서 재사용 가능하게 만드는 토픽.

## Latest checkpoint
- longform 토픽은 장문 문서 ingest/요약/정리 정책과 실제 장문 작업을 이어받기 위한 복구 포인트로 편입됨.
- 문서 저장 정책은 중요도별 차등 저장(S/A/B/C) 원칙이 메모에 남아 있다.
- 토픽 state는 현재 다루는 문서 묶음과 산출 상태를 압축 기록하는 용도로 쓴다.

## Decisions locked
- 모든 토픽은 기본적으로 `context/topic-state/<slug>.md`를 가진다.
- 반복 규칙은 Playbook, 열린 이슈는 HF, 즉시 복구 요약은 topic-state에 둔다.

## Next actions
1. 현재 처리중 문서/출처/산출 상태를 checkpoint에 명시.
2. 반복 정책은 playbook/SSOT에 유지.
3. 장기 파이프라인 이슈는 HF로 분리.

## Key files
- Playbook: `context/topics/longform_PLAYBOOK_V0_1.md`
- Handoff: (없음)
- Topic map: `context/telegram_topics/thread_topic_map.json`

## Restore instructions
- 먼저 이 파일을 읽고, 실제 내용이 얇으면 Playbook과 관련 HF를 최소만 추가로 읽는다.
- 복구 응답은 `현재 목표 / 마지막 체크포인트 / 다음 액션` 순서로 짧게 재구성한다.

## Notes
- longform은 원문 저장 부담이 크므로 state에는 요약/판정만 적고 본문 전체는 넣지 않음.
