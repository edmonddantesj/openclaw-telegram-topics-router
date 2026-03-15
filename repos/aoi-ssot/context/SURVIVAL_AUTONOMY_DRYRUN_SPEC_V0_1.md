# Survival Autonomy — DRY-RUN Spec v0.1

Last updated: 2026-02-20 (KST)
Status: DRAFT (report-only)

## Goal
“브릿지/이체/베팅” 같은 L3 실행을 자동화하지 않고도,
- 사람이 승인할 때 필요한 정보(해석형 승인 카드)
- Guarded Autonomy 정책(캡/서킷)
을 **proof bundle 형태로 생성**하는 데모를 만든다.

## Scope (v0.1)
- No signing
- No transfers
- No bridge
- Output only

## Outputs
- `context/proof_samples/autonomy_dryrun_<timestamp>/`
  - `approval_card.md`
  - `policy_eval.json`
  - `risk_notes.md`
  - `sha256sum.txt`

## Approval card (template)
- What: action summary
- Where: chain/protocol (planned)
- Amount: cap + proposed amount
- Destination: allowlist match status
- Threat assessment: LOW/MED/HIGH + reasons
- Worst-case bounded loss
- Required approval level: L3

## Next
- Implement generator script (report-only)
- Add public-safe scan
