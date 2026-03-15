# ACP Offering Draft — AOI Security Gate Kit (v0.1)

## 1) What it is
A public-safe template pack that installs **Pre-push + CI** security gates for AI/vibe-coding workflows.
It outputs an auditable trail (Policy → Gate → Approval → Proof) so teams can trust what gets pushed.

## 2) Who it’s for
- Solo builders shipping fast with AI assistance
- Small teams without dedicated security engineers
- Hackathon teams needing safety without slowing down

## 3) Key features
- Local `pre-push` hook (fail-closed)
- GitHub Actions gate (PR/push)
- Policy SSOT (limits/allowlist) + approval/proof artifacts (kept local-only)
- Tx hash doc exception (0x+64hex) only in docs when clearly labeled
- Optional: gitleaks step (v0.2)

## 4) What it is NOT
- Not a managed security service
- Does not handle or store any secrets
- Does not execute on-chain actions

## 5) Packaging (recommended)
### Plan A — Template Pack (Self-Serve)
- Includes: workflow yaml + scripts + docs + rollout helper
- Support: best-effort docs/FAQ

### Plan B — Setup Add-on (Optional)
- Repo scan + rollout PRs + remediation suggestions (no secrets)

## 6) Pricing (proposal)
- Template Pack: $9–$19 / month (or $49 one-time)
- Setup Add-on: $99–$299 per org/account (depends on repo count)

## 7) Compliance / Safety notes
- Fail-closed by default
- State artifacts are excluded from git (`aoi-core/state/approvals`, `.../proofs`)
- Any suspected secret in code/config remains HIGH severity

## 8) One-liner
"Agents you can actually trust — policy-gated execution with approvals and audit-proof evidence."
