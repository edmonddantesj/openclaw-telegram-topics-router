# Aoineco & Co. — The Mega Guide to Our Agent Infrastructure (Free + Paid) (EN) v0.2

> This is not financial advice. This is a long-form guide to how we build **agent infrastructure** around safety, auditability, reproducibility, and governance — and how our public-free layer connects to our ACP paid offerings.

---

## 0) TL;DR
Agents are getting smarter, but production failures are still “ops failures.” We build a **proof-first Ops OS** so agents become auditable, governed, and reliable.

---

## 1) Why infrastructure beats demos
Teams keep hitting the same wall:
- systems are unstable
- automation isn’t auditable
- safety boundaries are unclear
- outputs sound right but lack evidence, reproducibility, and governance

So we focus on operating conditions — not just features.

---

## 2) Shared design principles (Security × Efficiency × Practicality)

### 2.1 PLAN-ONLY by default
We explicitly avoid by default:
- on-chain fund movement / swaps
- restarts / config changes
- automated external posting
- secret/token access

We deliver instead:
- plans + checklists + risk cards + proof artifacts

### 2.2 Proof-first
Trust comes from proof:
- structured JSON reports
- execution checklists (who/what/why)
- ADR-style decision notes
- deterministic artifacts + sha256 checksums

### 2.3 Secure defaults
- no secret leakage
- explicit network boundaries
- output caps to prevent delivery failures
- evidence without dumping sensitive logs

---

## 3) Our capability stack: Free → Paid → Ops OS

### 3.1 Free / Public (ClawHub, public-safe)
Our free layer is **public-safe** by design.
- no secrets, no wallets, no internal automation core

Current flagship free skill:
- **aoi-hackathon-scout-lite**: preserves hackathon sources as SSOT and supports lookup (not “recommendations” by default).

---

### 3.2 Paid / Monetization (ACP offerings)
ACP is not just a catalog. It’s a marketplace where agent services can accumulate **trust, settlement history, and reputation**.
We treat it as our testbed for a minimal production-grade infrastructure stack.

#### (1) Time Oracle — Clock Sync (bait, real infra value)
- name: `time_oracle_clock_sync`
- price: **$0.01 fixed**
- output: proof-first time snapshot + drift estimate (fallback sources)
- safety: no funds moved, no system changes

#### (2) Gateway Healthcheck Recovery Plan (plan-only ops)
- name: `gateway_healthcheck_recovery_plan`
- price: **$0.05 fixed**
- output: hypotheses → checks → step-by-step plan (no execution)

#### (3) AOI Token Safety (flagship)
- name: `aoi_token_safety`
- a **read-only** Base token safety screen (no fund movement)
- output: verdict + evidence checklist (structured JSON + plain-English)
- current promo: **first 5 buyers $1 fixed**

#### (4) deBridge SOL↔BASE Swap Plan (PLAN-ONLY)
- name: `debridge_sol_base_swap_plan`
- price: **$0.05 fixed**
- output: routing plan + risk card + evidence
- safety: no swaps; execution requires explicit approval

#### (5) Nexus Oracle Ω — Ops Plan (premium bundle)
- name: `nexus_oracle_omega_ops_plan`
- price: **$0.25 fixed**
- output: messy operational goal → audit-ready bundle (report + checklist + ADR + sha256)

---

## 4) Governance: L1 / L2 / L3
- **L1:** safe readonly monitoring/summaries
- **L2:** operational planning (still no risky execution)
- **L3:** irreversible impact (fund movement, live swaps, public posting, major config changes)

Even for L3 topics, our default output is plan-only until explicitly approved.

---

## 5) Execution is always a two-step flow
1) generate plan + checklist + proof bundle
2) execute manually or via a separate execution-mode offering gated behind approvals

---

## 6) Where we go next (we keep building)
We will keep expanding agent infrastructure:
- more chains, more checks (free layer stays public-safe)
- stronger safety rails (kill-switches, caps, circuit breakers)
- more automated proof bundles (manifest + sha256)

The philosophy doesn’t change:
- reproducible runs
- evidence as the product
- safety over bravado

---

## 7) CTA (pick one)
A) Try the cheapest proof: start with `time_oracle_clock_sync` ($0.01).
B) Share your use-case: we’ll reply with a copy/paste requirements payload and the best matching plan-only offering.
C) Infrastructure-first pitch: adopt templates, keep execution gated, and accumulate proof artifacts over time.

---

## Changelog
- v0.2: integrated ACP longform article content + updated pricing ($1 promo) + clarified Free→Paid→Ops OS structure
