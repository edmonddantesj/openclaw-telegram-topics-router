# Handoff Index (SSOT)

목적: 시간이 지나 다시 물어봐도, 현재 진행중인 작업을 **끊김없이 즉시 재구성**하기 위한 작업 현황 SSOT.

규칙:
- 새 작업/에픽 시작 시: `context/handoff/HF_<slug>.md` 생성
- 작업 진행/결정/막힌점/다음 액션은 해당 HF 문서에 누적
- 완료 시: 상태를 DONE으로 바꾸고, 산출물/링크/후속 액션을 기록

템플릿: `context/handoff/_TEMPLATE.md`

## ACTIVE
- `HF_inbox_dev_urgent_202603.md` — Inbox-dev(585) 긴급개발: DB/State loss 복구 + Base Batches(3/9) 데모
