# Topic State — ralph-loop

- Topic: `ralph-loop`
- Telegram topic id: `68`
- Status: ACTIVE
- Last saved: 2026-03-08 23:08 KST

## Current objective
- ralph-loop(토픽 68)은 “반복 운영업무를 자동 순찰/정리하는 루프”의 SSOT. 핵심은 **WIP 제한(<=5), stale(SLA 24h), cron health, drift(상태 무결성) 감시/복구**를 매일 자동으로 굴리고, 결과/결정/증빙을 `context/`에 남기는 것.

## Latest checkpoint
- WIP 제한, stale SLA 24h, cron health, drift/integrity 감시/복구가 핵심 운영축으로 고정됨.
- 무결성 복구 관련 현재 열린 이슈는 HF_ralph_loop_drift_integrity_restore_20260308에 연결됨.
- 반복 루프 성격이 강하므로 규칙은 playbook, 사건은 HF, 즉시 재개는 topic-state로 나눈다.

## Decisions locked
- 모든 토픽은 기본적으로 `context/topic-state/<slug>.md`를 가진다.
- 반복 규칙은 Playbook, 열린 이슈는 HF, 즉시 복구 요약은 topic-state에 둔다.

## Next actions
1. 최근 drift/cron 상태를 checkpoint에 주기적으로 갱신.
2. 복구/교정 이슈는 HF에 누적.
3. 자동화 규칙 변경 시 playbook/ops SSOT 동시 갱신.

## Key files
- Playbook: `context/topics/ralph-loop_PLAYBOOK_V0_1.md`
- Handoff: `context/handoff/HF_ralph_loop_drift_integrity_restore_20260308.md`
- Topic map: `context/telegram_topics/thread_topic_map.json`

## Restore instructions
- 먼저 이 파일을 읽고, 실제 내용이 얇으면 Playbook과 관련 HF를 최소만 추가로 읽는다.
- 복구 응답은 `현재 목표 / 마지막 체크포인트 / 다음 액션` 순서로 짧게 재구성한다.

## Notes
- ralph-loop는 운영 무결성 축이라 상태가 낡으면 바로 갱신하는 편이 좋다.
