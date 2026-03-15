# Restricted Classification Table v0.1 (ClawHub Publish Governance)

## Rule (default-deny)
If a skill can **move money**, **exfiltrate data**, or **change system state**, treat it as **Restricted** by default.

## Public-safe (OK to publish)
- Read-only data fetch / analysis / reporting
- Offline scanning (no outbound), outputs JSON/text only
- Local validation (e.g., config validate), snapshots (no apply)
- Utilities that do not touch credentials or external messaging

### Examples
- Prompt injection detection that reads text and prints a report
- Sandbox/config validator that does not restart/apply/patch

## Restricted (do NOT publish by default)
- Money movement: wallet signing, swaps/bridges, trading, deposits, withdrawals
- Payments/purchases: cards, Stripe, on-chain payments, x402 settlement execution
- Any outbound sending primitive:
  - webhook/http POST/PUT/PATCH sending external data
  - auto-posting/messaging/email
- System mutation:
  - gateway restart/config.patch
  - cron add/update/remove
  - destructive file operations
- Credential handling:
  - API keys/tokens/cookies, seed/private keys
- Autonomous execution without explicit user confirmation

## Policy binding
- Restricted skills are **internal-only**.
- If needed for external sharing, create a **public-safe fork/lite** version.
