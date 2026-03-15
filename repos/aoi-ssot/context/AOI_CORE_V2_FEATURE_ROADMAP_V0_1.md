# AOI Core V2 — Feature Roadmap & Benchmark Internalization Plan

Date: 2026-02-21 (KST)
Status: DRAFT
Owner: Edmond + Aoineco

## 1. Strategic Pivot
**From:** "A monolithic Decentralized OS for Agents" (Too broad, high barrier)
**To:** "A modular Arsenal of Verified Agent Tools" (Specific utility, low barrier, hackathon-aligned)

We build AOI Core by **internalizing** the best features of hackathon winners into standalone, composable modules.

## 2. Benchmark Mapping & Internalization

| Benchmark (Winner) | Winning Factor | AOI Core Internalization Module | Priority |
| :--- | :--- | :--- | :--- |
| **ProceedGate** | Cost Governance (Circuit Breaker) | **Module: Cost-Governor (Blue-Gear)**<br>- Hard limits on API/Tx spend per hour.<br>- "Panic Stop" for autonomous loops (Limitless). | **P0 (Immediate)** |
| **VibeCheck** / **Strike** | Instant Utility (Web/TG Bot) | **Module: Skill-Guardian Lite (Blue-Blade)**<br>- Web UI / CLI one-liner: "Paste URL -> S-DNA Audit Report".<br>- No install required. | **P1 (Next)** |
| **Zhentan** / **Aegis** | Visual Evidence (Dashboard) | **Module: Visual Proofs (Blue-Record)**<br>- Convert JSON logs to `dashboard.html` / charts.<br>- Visualizing the "Block" or "Trade". | **P2** |
| **IBITI EPK** | Permission Kernel | **Module: S-DNA Kernel (Blue-Blade)**<br>- Enforce permissions at the code level (AST static analysis).<br>- "Allow only Uniswap.swap" policies. | **P3** |
| **AGOS** | Agent Marketplace | **Module: Nexus Bazaar (Blue-Eye)**<br>- Focus on "Trusted Code Exchange" (S-DNA) over gig work.<br>- Verified Handshakes. | **Ongoing** |

## 3. Implementation Plan (Incremental)

### Phase 1: Self-Preservation (Cost-Governor)
- **Target:** Limitless Shadow / Council Pro
- **Action:** Implement `cost_governor.py` middleware.
- **Spec:**
  - Track usage (tokens, API calls) in local state.
  - If `hourly_spend > $1.00`, raise `CircuitBreakerError`.
  - Halt execution gracefully.

### Phase 2: Gateway Utility (Skill-Guardian Scanner)
- **Target:** Public users / Devs
- **Action:** Build a standalone script `scan_skill.py` -> outputs `audit_report.html`.
- **Spec:**
  - Input: GitHub URL or Local Path.
  - Check: S-DNA presence, basic security patterns (eval, subprocess).
  - Output: HTML report with PASS/FAIL badge.

### Phase 3: Visual Proofs
- **Target:** Investors / Hackathon Judges
- **Action:** Upgrade `limitless_shadow_daily_snapshot.py` to generate HTML.

## 4. Next Steps
1. Finish **AOI Council Pro** (11-role adapter) to govern these modules.
2. Implement **Cost-Governor** (P0) to protect our own runway.
