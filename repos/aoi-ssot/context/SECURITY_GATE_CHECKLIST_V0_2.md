# Security Gate Checklist v0.2

Last updated: 2026-02-20 (KST)

## Output
- PASS / WARN / BLOCK

## BLOCK (any hit)
- Secrets/keys in repo or logs (env, vault paths, tokens)
- Wallet/payment/on-chain execution primitives enabled by default
- Outbound posting/messaging/webhook enabled by default
- Dynamic code execution (`eval`, `exec`, `subprocess` with user input)
- Dangerous filesystem writes outside a bounded workspace

## WARN
- Network calls exist but are allowlisted + timeouts
- Dependency security audit not available (no lockfile)
- Large permissions surface but gated/disabled by default

## PASS requirements
- No BLOCK hits
- WARNs documented in README
- Default behavior is safe (dry-run / report-only)

## Suggested evidence to keep
- Scan log path
- Version + changelog entry
