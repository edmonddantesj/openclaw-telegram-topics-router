# Topic State — longform

- Topic: `longform`
- Telegram topic id: `65`
- Status: ACTIVE
- Last saved: 2026-03-08 23:13 KST

## Current objective
- 긴 글/PDF/리서치를 요약·추출·SSOT 승격해 재사용 가능한 지식으로 전환한다.

## Latest checkpoint
- 장문 문서는 먼저 요약본/핵심 섹션/링크 중 어떤 형태로 받을지 결정하는 것이 운영 규칙이다.
- 저장 정책은 S/A/B/C 차등 저장 원칙으로 정리되어 있다. Source: memory/2026-03-05.md#L210-L238
- 채팅에는 전체 원문 재출력 대신 요약, 핵심 인용, SSOT 경로만 남기는 방향이 고정돼 있다. Source: memory/2026-03-05.md#L225-L238

## Decisions locked
- PDF 분석은 Flash vs Pro 등 모델/TPM을 고려해 수행.
- 결과물은 요약 + 핵심 인용 + SSOT 경로 3종 세트로 남긴다.
- 원문 전체를 채팅에 다시 뿌리지 않는다.

## Next actions
1. 현재 처리 중인 문서 묶음과 판정(S/A/B/C)을 checkpoint에 남긴다.
2. 중요 인사이트는 context/research 또는 context/knowledge로 승격.
3. 장기 파이프라인 문제는 HF로 분리.
4. longform→ralph-loop delegated execution parent/child set을 기준 트랙으로 사용한다:
   - parent: `ops/items/TASK-20260314-LONGFORM-RLP-01.md`
   - intake: `ops/items/TASK-20260314-LONGFORM-RLP-02.md`
   - deep-study gate: `ops/items/TASK-20260314-LONGFORM-RLP-03.md`
   - synthesis: `ops/items/TASK-20260314-LONGFORM-RLP-04.md`

## Key files
- Playbook: `context/topics/longform_PLAYBOOK_V0_1.md`
- Handoff: `context/handoff/HF_longform_ralph_transfer_20260314.md`
- Audit note: `context/research/longform/LONGFORM_RALPH_TRANSFER_AUDIT_2026-03-14.md`
- Topic map: `context/telegram_topics/thread_topic_map.json`

## Restore instructions
- 먼저 이 파일을 읽고, 실제 내용이 얇으면 Playbook과 관련 HF를 최소만 추가로 읽는다.
- 복구 응답은 `현재 목표 / 마지막 체크포인트 / 다음 액션` 순서로 짧게 재구성한다.

## Notes
- longform은 토큰/저장비용이 크니 state에는 “무엇을 어떻게 저장했는가”만 남기고 본문은 별도 파일로 넘긴다.
