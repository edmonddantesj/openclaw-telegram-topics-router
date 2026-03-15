# Team Council (Lite) — planning

## Topic
AOI Council Pro: 11-member role debate w/ Squad Orchestrator Pro integration + Lite fallback

## Context (optional)
User wants **AOI Council Pro** that can run with **AOI Squad Orchestrator Pro** when active (team size = 11). If only **AOI Squad Orchestrator (Lite)** exists, AOI Council Pro should degrade to **AOI Council Lite** behavior (max 5 roles). Need team opinions and a decision on architecture + rollout plan.

## Constraints (optional)
- No external posting. No L3 money/signing.
- Published public hackathon repos are FINAL unless explicitly requested.
- Prefer deterministic, reproducible orchestration (manifests/logs).
- Store decision in SSOT + Notion Decision Log.

---

## TL;DR (2 lines)
- Build **AOI Council Pro** as an *adapter* that can run on top of Orchestrator Pro (11 roles) but always supports a **Lite fallback (5 roles)** when Pro is not available.
- Decision: **Conditional Go** — implement the Lite-compatible core first + add Pro integration hooks behind feature detection.

## Role opinions (2–3 lines each)
- 🧿 Oracle (decision frame):
  - We’re deciding the interface contract: (inputs → role roster → outputs → storage). Key assumptions: Orchestrator Pro can provide presence/role routing; Pro may not always be installed.
  - Recommendation: define a single “Council Run Manifest” schema, then have Pro/Lite executors fill it.

- 🧠 Analyzer (scoring/trade-offs):
  - Options: A) hard-depend on Orchestrator Pro (fast but fragile), B) dual-mode adapter (slower but robust), C) keep Lite only.
  - Score: **B best**. It prevents lock-in and keeps 5-role Lite always usable.

- ⚔️ Security (security/risk):
  - Risks: uncontrolled agent tool access, accidental data leakage across roles, runaway fan-out (11 agents) cost/time.
  - Guardrails: strict allowlists per role, max turns/timeouts, and “report-only” default. No secrets in manifests.

- ⚡ Builder (feasibility/MVP):
  - MVP: reuse existing Team Council Lite format and add a Pro “roster” + “executor” layer.
  - Implement feature detection: if orchestrator-pro endpoints unavailable → run 5-role mode.

- 📢 Comms (messaging/market):
  - Clear value: “11 perspectives when available, but still works in minimal mode.”
  - Objection: “multi-agent = slow/expensive.” Response: “adaptive roster + capped runtime; Lite fallback by default.”

## Consensus / Conflict
- Consensus: dual-mode is best; Lite must remain first-class.
- Conflict: how much of Orchestrator Pro to require initially vs phased integration.

## Dissent (at least 1)
- Dissent: “Ship only Lite until Orchestrator Pro is proven stable; Pro integration later to avoid complexity creep.”

## Assumptions (3)
1) Orchestrator Pro can expose an API to enumerate available teammates/roles and route tasks.
2) We can keep outputs deterministic enough via manifests + timeouts.
3) Users prefer a stable report format over maximum agent count.

## Recommendation
- **Conditional Go**
- Confidence: **Medium**
- Risk: **Medium**

## Next actions (Top 3)
1) Write SSOT spec: `context/AOI_COUNCIL_PRO_SPEC_V0_1.md` (roster model, feature detection, run manifest).
2) Implement core runner with Lite fallback: `scripts/aoi_council_run.py` (5 roles) + stub hooks for Pro.
3) If Orchestrator Pro is present: implement adapter `scripts/aoi_council_orchestrator_pro_adapter.py` (11 roles) + rate limits.
