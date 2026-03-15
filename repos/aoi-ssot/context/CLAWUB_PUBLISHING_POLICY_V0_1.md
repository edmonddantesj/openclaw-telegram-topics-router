# ClawHub Publishing Policy v0.1 (Aoineco)

Last updated: 2026-02-20 (KST)
Status: ACTIVE (public-safe publishing only)

## Purpose
Publish public-safe skills to ClawHub while maintaining **auditability + security**.

## Scope
- Applies to any skill intended for ClawHub publishing under Aoineco.

## Release Gate (mandatory)
1) **Security Gate PASS**
   - Run checklist + scanner before release.
2) **Reproducible change + changelog**
   - Every release must have a version bump + release notes.
3) **Rollback plan**
   - Prior version tag + instructions to revert/delist if issues found.

## Block conditions (hard stop)
- Secrets / keys / vault data exposure risk
- Payment / wallet / on-chain execution / auto-trading
- External posting / outbound messaging / webhooks (unless explicitly OFF by default + allowlist + docs)
- `eval/exec` or dynamic code execution paths reachable from user input
- License/attribution unclear for redistributed code

## Warning / Strike System (skill/repo based)
- Strike reasons (only these count):
  - (A) Security Gate BLOCK ignored
  - (B) License/source unclear
  - (C) Missing release notes/version/change tracking (not auditable)
- 1st strike: keep public, but must patch
- 2nd strike: publishing pause (7–14 days) + reviewer approval required
- 3rd strike: delist/archive + (optional) major rewrite then re-register

## Public-safe vs Restricted
- **Public-safe (default allowed):** read-only data / analysis / logging / utilities
- **Restricted (do NOT publish):** payment/wallet/auto-trade/messaging/posting/credential handling

## Template snippet (for README / skill description)
> We publish this skill as public-safe and keep it under a security release gate.
> No keys, no wallets, no outbound posting by default. Changes are tracked and auditable.

## References
- Security Gate checklist: `context/SECURITY_GATE_CHECKLIST_V0_2.md`
- Security Gate runner: `scripts/security_gate_run.sh`
- Pattern list: `scripts/security_gate_patterns.txt`
- Skill scouting governance: `context/SKILL_SCOUTING_GOVERNANCE.md`
