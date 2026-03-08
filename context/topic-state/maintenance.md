# Topic State — maintenance

- Topic: `maintenance`
- Status: ACTIVE
- Last saved: 2026-03-08 23:13 KST

## Current objective
- 운영 유지보수 토픽에서 자동화 루프를 안정적으로 돌리고, 성공 시 침묵 / 실패 시 알림 규칙을 유지한다.

## Latest checkpoint
- daily skill scouting 루프 복구와 launchd 세트가 정리돼 있다.
- 성공 시 침묵, 실패 시 topic 77 알림, 원인분석은 즉시/재시작·모델전환·설정변경은 선보고 후승인 원칙이 고정돼 있다.
- 3h digest / notion sync / daily smoke / x-post tick 유지도 maintenance가 품는 운영 범위다.

## Decisions locked
- 성공 시 노이즈 최소화.
- 실패 시 proof와 영향 범위를 우선 정리.
- 과격한 조치 전 승인.

## Next actions
1. 각 루프의 마지막 성공/실패 상태를 필요 시 checkpoint에 갱신.
2. 실패 시 관련 로그/플리스트/스크립트를 바로 연결.
3. 규칙 변경은 playbook과 automation 문서를 같이 갱신.

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
- maintenance는 “조용히 굴러가야 좋은 토픽”이다. 이상 징후가 있을 때만 두껍게 쓴다.
