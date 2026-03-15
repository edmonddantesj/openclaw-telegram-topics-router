# Publish Warning Policy v0.1 (Skill-level)

## Scope
- Warnings are tracked per **skill slug/repo**, not per person.

## Warning reasons (only these 3)
A) Security Gate BLOCK bypass attempt
B) License/attribution unclear (esp. missing LICENSE or redistribution rights)
C) Missing release traceability (SemVer/changelog/rollback evidence)

## Escalation ladder
- Warning 1: keep public, but require a remediation PR before next publish.
- Warning 2: publish freeze (7–14 days) + reviewer approval required.
- Warning 3: delist/archive + internal-only (or major rewrite + new slug).

## Evidence
- Every warning entry must include: date, slug, reason(A/B/C), evidence link/path, decision.

## SSOT
- Local SSOT ledger (recommended): `aoi-core/state/publish_warnings.json` ✅ (created)
- Notion: monthly summary/statement only.
