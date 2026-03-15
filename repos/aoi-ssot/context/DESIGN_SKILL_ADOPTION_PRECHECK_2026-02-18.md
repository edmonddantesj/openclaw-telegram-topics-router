# Design Skill Adoption — Precheck ("도입해줘" SOP) — 2026-02-18

## What "도입해줘" means (SSOT)
- Order is fixed: **License/Security verification → Creator contact info log (or TBD) → Rebuild/Develop (security hardening + S-DNA) → Install/Internal apply**
- No external release before Nexus Bazaar beta.

## Targets
1) ui-ux-pro-max-skill (repo: https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)
2) frontend-design (repo: https://github.com/anthropics/claude-code/tree/main/plugins/frontend-design/skills/frontend-design)
3) web-design-guidelines (repo: https://github.com/vercel-labs/agent-skills/tree/main/skills/web-design-guidelines)

## Current status
- **Rolled back** any prior installation (skills removed).
- Staged clones (no install yet): `adoption_staging/design_skills/*`

## License quick check
- ui-ux-pro-max-skill: `LICENSE` present in repo root (good).
- frontend-design: no license file inside sub-skill folder (inherits repo-level license; needs confirmation at `adoption_staging/design_skills/claude-code/LICENSE*`).
- web-design-guidelines: no license file inside skill folder (inherits repo-level license; needs confirmation at `adoption_staging/design_skills/agent-skills/LICENSE*`).

## Security quick scan (grep-based)
> This is NOT a full audit. It’s a first-pass triage for obvious hooks/exfil.

### ui-ux-pro-max-skill
- Findings: grep hits are mostly **data CSV** containing example code/URLs (e.g., google fonts links). No obvious runtime `exec/spawn/eval` found in first pass.
- Next: inspect actual runtime entrypoints (SKILL.md/handlers) for network/file access patterns.

### frontend-design
- Skill folder appears to be primarily `SKILL.md` (design guidance). No code files in that subfolder.
- Next: verify it does not reference external scripts/tools.

### web-design-guidelines
- `SKILL.md` includes a reference to: `https://raw.githubusercontent.com/vercel-labs/web-interface-guidelines/main/command.md`
- Risk: potential **runtime external fetch** (depends on how the skill uses it).
- Rebuild plan: **pin** the referenced guideline content into a local file snapshot (offline-first) + allowlist if any fetch remains.

## Contact info (TBD)
- nextlevelbuilder/ui-ux-pro-max-skill: TBD
- anthropics/claude-code (frontend-design): TBD
- vercel-labs/agent-skills (web-design-guidelines): TBD

## Next steps (per SOP)
1) Extract repo-level LICENSE for claude-code / agent-skills and record.
2) Find creator contact methods (GitHub profile, email, X, etc.) and write outreach log.
3) Rebuild/harden:
   - forbid secret access
   - forbid arbitrary network by default; allowlist + timeout if needed
   - pin any remote guideline docs locally
4) Only after rebuild: install to OpenClaw agent.
