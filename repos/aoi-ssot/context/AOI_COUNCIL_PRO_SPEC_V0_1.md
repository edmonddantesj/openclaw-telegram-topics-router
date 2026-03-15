# AOI Council Pro — Spec v0.1

Date: 2026-02-20 (KST)
Owner: Edmond + Aoineco
Status: DRAFT

## 0) Goal
Build **AOI Council Pro** that can run:
- **Pro mode (11 roles)** when **AOI Squad Orchestrator Pro** is active/available.
- **Lite fallback (5 roles)** when only **AOI Squad Orchestrator (Lite)** (or no orchestrator) is available.

The output must stay consistent: **consensus + dissent + assumptions + recommendation + next actions**, with reproducible evidence.

### Core Differentiators (Pro)
1. **Auditable Proof Bundle:** Automatic packaging of all debate artifacts (JSON, MD, logs) for external verification.
2. **Cross-Critique Engine:** Multi-turn logic where agents review and challenge each other's opinions.
3. **Devil's Advocate Logic:** Mandatory risk-focused role assignment to prevent confirmation bias.

## 1) Non-goals
- No real-money actions, wallet signing, or external posting. (L3 forbidden)
- Not a general-purpose chat router; strictly a council/debate runner.

## 2) Inputs / Outputs
### 2.1 Inputs
- `mode`: decision | planning | evaluation
- `topic`: string
- `context`: string (optional)
- `constraints`: string (optional)
- `roles_override`: optional list (advanced)
- `max_runtime_sec`: default 120 (Lite) / 300 (Pro)
- `evidence_paths`: optional list of local paths

### 2.2 Outputs
- `council_report.md` (human readable, fixed format)
- `council_run_manifest.json` (machine readable)
- Optional: `notion_ref.json` (Decision Log page URL if mirrored)

## 3) Feature detection & routing
### 3.1 Detection
AOI Council Pro must detect at runtime:
- Orchestrator Pro available? (YES/NO)
- If YES → run `ProExecutor(11 roles)`
- Else → run `LiteExecutor(5 roles)`

Detection approach (v0.1):
- Prefer explicit env/config flag in `aoi-ssot`:
  - `AOI_ORCHESTRATOR_MODE=pro|lite|none`
- Fallback: check presence of known command/script path or health endpoint (to be finalized when Orchestrator Pro spec is available).

### 3.2 Degrade behavior
- If Pro run fails mid-flight → automatically fall back to Lite and record failure reason in manifest.

## 4) Role roster
### 4.1 Lite roster (fixed 5)
Use existing Team Council Lite roles:
1) 🧿 Oracle
2) 🧠 Analyzer
3) ⚔️ Security
4) ⚡ Builder
5) 📢 Comms

### 4.2 Pro roster (11; team-based)
Pro uses the **current squad roster** (11 members) and maps each to a role module.
- Names policy: internal use **emoji + nickname(English name)** on first mention.

Pro v0.1 default mapping (example; can be edited later):
1) 🧿 Oracle (Blue-Oracle) — decision frame / veto gate
2) 🧠 Strategy (Blue-Brain) — scoring, trade-offs
3) ⚔️ Security (Blue-Blade) — security/compliance
4) ⚡ Builder (Blue-Flash) — feasibility/implementation
5) 📢 Comms (Blue-Sound) — messaging/community
6) 👁️ Research (Blue-Eye) — evidence gathering / external signals
7) 🗂️ Record (Blue-Record) — SSOT logging / proof bundling
8) ⚙️ Ops (Blue-Gear) — reliability/observability
9) 💊 Risk (Blue-Med) — risk posture/circuit breaker
10) 🧩 Product (Blue-Product) — UX/productization (placeholder)
11) 🧼 Quality (Blue-Clean) — QA/testing/edge cases (placeholder)

> Note: roles 10–11 are placeholders until the Orchestrator Pro roster is finalized.

## 5) Output format (must match Lite format)
1) TL;DR (2 lines)
2) Role opinions xN (2–3 lines each)
3) Consensus / Conflict
4) Dissent (≥1)
5) Assumptions (3)
6) Recommendation: Go/No-Go/Conditional + Confidence + Risk
7) Next actions Top 3

## 5-1) Cross-Critique Procedure (Pro)
Pro runs are multi-pass to improve quality and reduce blind spots.

**Default (3-pass):**
- Pass A — Initial Opinions: each role produces a 2–5 bullet opinion.
- Pass B — Cross-Critique: each role must critique at least 1 other role (point out flaw, missing assumption, or risk).
- Pass C — Revision: each role revises its initial opinion based on critique.

Oracle then synthesizes:
- TL;DR, consensus/conflict, dissent, assumptions, verdict, next actions.

## 5-2) Policy / Governance Compliance Checks (Pro)
Pro must run compliance checks and record results into `policy_check.json` (see Proof Pack schema).

Minimum checks:
- Exposure tier compliance: OPEN/TEASER/STEALTH/TOP SECRET
- L1/L2/L3 boundary enforcement (L3 never auto)
- GitHub public-final policy: hackathon repos marked FINAL must not be mutated

## 5-3) Proof Pack (Pro)
Pro must generate a reproducible evidence bundle per run.
- Schema SSOT: `context/AOI_COUNCIL_PROOF_PACK_SCHEMA_V0_1.md`

## 5-4) Smart Roster (Pro)
To avoid “11 roles every time” cost/latency, Pro supports **adaptive role selection**:
- Start with core roles (Oracle/Strategy/Security/Builder/Comms)
- Add specialist roles conditionally (Research/Ops/Risk/Record/Product/Quality)
- Hard caps: max_roles=11, max_runtime_sec=300
- If budget/time cap is reached → stop additional roles and record the cutoff in manifest

## 6) Run manifest schema (v0.1)
`council_run_manifest.json` minimum keys:
- `run_id`
- `timestamp`
- `mode`
- `topic`
- `executor`: lite|pro
- `roles`: [{id, label, agent?, status, started_at, ended_at}]
- `inputs`: {context, constraints, evidence_paths}
- `outputs`: {report_md_path, manifest_path}
- `verdict`: {recommendation, confidence, risk}
- `failures`: []

## 7) Guardrails
- Default: report-only, no external side effects.
- Hard cap:
  - Pro: max roles executed per run = 11
  - Lite: max roles executed per run = 5
- Timeouts per role and total.
- Evidence hygiene: no secrets in logs/manifests.

## 8) Storage
- Local SSOT: store report and manifest under:
  - `context/team_council/` (curated) and/or `context/proof_samples/council_runs/<run_id>/`
- Notion: mirror final report to Decision Log when requested.

## 9) Next actions
1) Implement `scripts/aoi_council_run.py` (LiteExecutor core + manifest writer)
2) Add a minimal config flag for orchestrator mode detection
3) Stub `scripts/aoi_council_orchestrator_pro_adapter.py` (no-op until Orchestrator Pro is defined)
