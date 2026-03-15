# ClawHub Skill Adoption — Precheck (2026-02-18)

## Scope
User request: "모두 도입해줘" for ClawHub scout TOP5.

**SOP ("도입해줘") 적용:** 검증 → 연락처 기록 → 리빌딩/보안 업그레이드(+S‑DNA) → 설치/내부 적용.

## Candidates
1. sector-analyst (skill)
2. api-gateway (NOTE: ClawHub slug not found)
3. ontology (skill)
4. oracle (skill, documentation for @steipete/oracle CLI)
5. moltguard (skill doc; actual plugin is npm package + remote API)

## ClawHub inspect results (evidence logs)
- sector-analyst: `/tmp/clawhub_inspect_sector-analyst.log` (latest 0.1.0)
- ontology: `/tmp/clawhub_inspect_ontology.log` (latest 0.1.2)
- oracle: `/tmp/clawhub_inspect_oracle.log` (latest 1.0.1)
- moltguard: `/tmp/clawhub_inspect_moltguard.log` (latest 6.0.2)
- api-gateway: `/tmp/clawhub_inspect_api-gateway.log` (Skill not found)

## Staging install (no overwrite)
Installed into staging inbox to avoid conflicts:
- `adoption_staging/clawhub_inbox/sector-analyst`
- `adoption_staging/clawhub_inbox/ontology`
- `adoption_staging/clawhub_inbox/oracle`
- `adoption_staging/clawhub_inbox/moltguard`

## Key risks / notes
- **moltguard**: SKILL.md explicitly states it points to external npm package `@openguardrails/moltguard` and remote API `api.moltguard.com`.
  - Requires separate audit before plugin install.
  - Adoption here means: add the doc skill + decide whether to install plugin in gateway.
- **api-gateway**: We already have local `skills/api-gateway` (Maton). ClawHub slug `api-gateway` not found; treat as "already adopted locally".

## Next actions (planned)
1) Copy vetted skills from staging into `skills/` (sector-analyst, ontology, oracle, moltguard-doc).
2) Add AOI guardrails / notes (no secrets; proof-first; no external posting).
3) For moltguard plugin: do NOT auto-install; require explicit privacy posture (gateway-only vs remote detection).
