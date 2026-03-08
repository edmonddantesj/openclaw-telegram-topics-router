# Reset & Recovery Protocol v0.1

## Trigger phrases
- **"현재를 저장"**
  - Make the workspace resumable after a context reset.
  - Actions (L1/L2): update MD SSOTs + append daily memory + sync md-vault.

- **"이 토픽 저장" / "토픽 저장: <slug>"**
  - Save a topic-local checkpoint to `context/topic-state/<slug>.md`.
  - Focus on resumable summary: objective, latest checkpoint, locked decisions, next actions, key files.

- **"복구해줘"**
  - Must **first ask one disambiguation question**:
    1) "전체 상태 복구"를 의미해? (저장해둔 SSOT를 읽고 이전과 동일한 상태로 재개)
    2) "현재 토픽 복구"를 의미해? (`context/topic-state/<slug>.md` 기반으로 재개)
    3) 아니면 "특정 폴더/파일 복구"를 의미해? (git/backup/restore 등)

- **"이 토픽 복구" / "토픽 복구: <slug>"**
  - Restore from `context/topic-state/<slug>.md`, then read only the minimum linked Playbook/HF/docs.

## Reset recovery (meaning #1)
If user selects (1):
- Load the prepared SSOT set (RUNBOOK/context/indices/daily memory notes) and resume from the saved checkpoint.
- Do not re-ask for already stored configuration (unless missing).

## File/folder recovery (meaning #2)
If user selects (2):
- Ask which path + desired source (md-vault/git backup/other) and perform a targeted restore plan.

## Guardrails
- Never claim recovery completed unless verified.
- Secrets never pasted; only presence/locations.
