# Topic State — maintenance

- Topic: `maintenance`
- Status: ACTIVE
- Last saved: 2026-03-08 23:00 KST

## Current objective
- 운영 유지보수 토픽에서 자동화 루프를 안정적으로 돌리고, 성공 시 침묵 / 실패 시 알림 규칙을 유지한다.

## Latest checkpoint
- daily skill scouting 루프 복구 완료.
- SSOT/자동화 세트가 정리됨: playbook + python script + launchd.
- 운영 감시 규칙은 “원인분석은 즉시, 재시작/모델전환/설정변경은 선보고 후승인”으로 고정됨.

## Decisions locked
- 성공 시 topic 77에 굳이 떠들지 않음.
- 실패 시에만 알림.
- 과격한 조치(재시작/모델 전환/설정변경)는 승인 전 실행 금지.

## Next actions
1. 루프 정상 실행 여부만 주기적으로 확인.
2. 실패 시 원인/로그/영향 범위 먼저 정리.
3. 규칙 변경 시 playbook/automation 문서 동시 갱신.

## Key files
- Playbook: `context/topics/maintenance_PLAYBOOK_V0_1.md`
- SSOT: `context/SKILL_SCOUTING_DAILY_PLAYBOOK_V0_1.md`
- Script: `scripts/skill_scouting_daily.py`
- Launchd: `context/automation/launchd/ai.aoi.skill_scouting_daily_1105.plist`

## Restore instructions
- 먼저 이 파일 읽기
- 이어서 maintenance playbook과 skill scouting SSOT 확인
- 이슈가 있으면 관련 로그/최근 산출물만 추가 확인

## Notes
- maintenance는 “조용히 굴러가야 좋은 토픽”이다.
