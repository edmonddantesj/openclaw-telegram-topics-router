# ACP Wallet Governance v0.1 (Team Purchase Enablement)

Last updated: 2026-02-20 (KST)
Status: DRAFT → ACTIVE when funded

## Goal
Enable team members to **directly buy and test ACP skills** using their own wallets, while keeping:
- caps / approvals
- proof-first logs
- no key sharing

## Core model (agreed)
- **Personal wallets (multi-provider)** + **Central pool (treasury)** + **Proof-based distribution**
- Providers allowed in the experiment: Privy / Coinbase Agent Wallet / PaySponge / MetaMask / Rabby

## Roles
- Operator (Treasury): 청묘
- Approver / Gatekeeper: 청령
- Security audit: 청검
- Rollback / monitoring: 청정

## Wallet lifecycle
- wallet_intent (submitted) → active (approved) → hold (risk) → retired (replaced)
- Address change requires re-approval; old address retired.

## Security rules (hard)
- Private keys / seeds / mnemonics are never collected in SSOT.
- Funding and payouts are **L3** (manual, approval-gated).
- Default caps for experiment:
  - per-tx: $2
  - per-day: $7
  - micro tests preferred: $0.01–$0.05

## Proof requirements (VCP)
Every action must leave:
- task_id / agent_id
- provider / chain / network / address
- proof_dir + input_digest + sha256 + logs
- tx_hash for any on-chain movement
- failure_code + suggested_fix for failures

## Experiment docs (SSOT)
- Plan: `context/ACP_AGENT_WALLET_EXPERIMENT_V0_1.md`
- Directive (copy/paste): `context/ACP_AGENT_WALLET_EXPERIMENT_DIRECTIVE_V0_1.md`
- Adapter interface: `context/ACP_WALLET_ADAPTER_INTERFACE_V0_1.md`
- Adapter code stub: `scripts/acp_wallet_adapters_stub.ts`

## Readiness checklist (to start team purchases)
1) All participants submit wallet_intent with address + proof
2) Gatekeeper approves → wallet_state=active
3) Treasury funds micro budgets (L3) and records tx_hash
4) Team executes: 1 skill/person × 3 runs, record results
5) Weekly triage: Adopt / Rebuild / Reject decisions
