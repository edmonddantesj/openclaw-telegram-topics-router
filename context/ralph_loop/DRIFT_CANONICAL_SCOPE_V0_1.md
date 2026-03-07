# DRIFT_CANONICAL_SCOPE_V0_1 (ralph-loop)

- **Status:** ACTIVE
- **Last updated:** 2026-03-08
- **Decision:** drift 자동복구 범위 = **모두** (메르세데스 승인)

## Scope (Canonical files/directories)
Drift integrity check + state save 대상(= 체크섬/스냅샷/복구 단위):

1) `context/state/`
- `*.state.json`

2) `context/ops/reports/`
- `ralph_loop_daily/REPORT_*.md`
- `task_manager/*` (있으면)

3) `context/ops/items/`
- `TASK-*.md`

## Auto-repair policy (guardrails)
- **Snapshot-first:** 복구 전 스냅샷을 `artifacts/state_saves/<timestamp>/`에 저장
- **Atomic apply:** 임시 폴더에서 생성/패치 후 원자적 교체(가능한 범위 내)
- **Rollback:** 복구 후 검증 실패 시 즉시 스냅샷으로 롤백
- **Cooldown:** 동일 파일/태스크에 대해 연속 복구는 쿨다운 + 최대 재시도 제한
- **No destructive deletes:** 자동복구는 기본적으로 "삭제"를 하지 않음(필요 시 tombstone/rename로 우회)

## What counts as drift?
- 파일 누락(should exist but missing)
- 체크섬 불일치(내용 변조/깨짐)
- 스키마/메타데이터 정합성 실패(예: TASK frontmatter 필수 필드 누락)

## Proof
- HF: `context/handoff/HF_ralph_loop_drift_integrity_restore_20260308.md`
