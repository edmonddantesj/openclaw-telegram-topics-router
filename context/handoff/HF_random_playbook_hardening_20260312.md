# HF: random playbook hardening / compact-recovery apply

- **Status:** ACTIVE
- **Owner:** 청묘
- **Last updated:** 2026-03-12 21:29 KST
- **Where:** Telegram random(topic 81), `context/topics/random_PLAYBOOK_V0_1.md`

## Goal
- Random(topic 81)에 직접 반영 가능한 운영 규칙만 SSOT에 고정하고, 나머지 검증 필요 항목은 추적 가능한 HF로 전환한다.

## Current state (what works / what’s broken)
- proposal 문서(`PROPOSAL_RANDOM_TASK_20260310.md`, `PROPOSAL_RANDOM_STATUS_20260310.md`)는 존재했지만 `proposal_only` 상태였음.
- Random Playbook에는 이미 triage/HF 분리 방향이 있었으나, compact/context-loss 복구 규칙과 tracked artifact 전환 규칙은 명시도가 부족했음.
- A/B export 간 divergence가 있어, upstream-context 전체를 random SSOT로 곧바로 승격하기에는 추가 검토가 필요함.

## Decisions made
- Random에 직접 관련된 최소 규칙만 즉시 반영:
  - compact/context-loss 위험 시 복구 포인트를 명시적으로 남긴다
  - 장기화/다산출물/교차연결 작업은 HF로 분리한다
  - 즉시 실행이 어렵다면 암묵 보류 대신 tracked artifact로 전환한다
- B 소스의 전사 정책 일반론은 random 직접 규칙과 분리해서 후속 검토 대상으로 남긴다.

## Next actions (ordered)
1. A/B export divergence가 random 직접 규칙 판단에 영향을 주는지 최소 범위로 재검토
2. 필요 시 random 전용 status/checklist를 V0.2 또는 별도 SSOT로 승격
3. Random에서 새 장기 작업 발생 시 이 HF 또는 후속 HF로 연결

## Commands / paths / proofs
- Updated: `context/topics/random_PLAYBOOK_V0_1.md`
- Source proposals:
  - `_staging/backups/random/proposals/PROPOSAL_RANDOM_TASK_20260310.md`
  - `_staging/backups/random/proposals/PROPOSAL_RANDOM_STATUS_20260310.md`
  - `_staging/backups/random/conflicts/CONFLICTS_RANDOM_20260310.md`

## Risks / blockers
- A1/A2 export가 strict identical인지 미검증
- B에서 관찰된 일부 규칙은 random 직접 규칙이 아니라 전사 운영정책일 수 있음
