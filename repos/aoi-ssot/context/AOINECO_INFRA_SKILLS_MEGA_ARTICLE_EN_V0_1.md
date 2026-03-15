# Aoineco & Co. — The Long-Form Guide to Our Agent Infrastructure (EN) v0.1

> Purpose: a single, readable, “everything in one place” document that explains how Aoineco & Co. builds **agent infrastructure (Ops OS)** — from free/public skills to paid offerings — and why it matters.

Core principles: **proof-first**, **fail-closed**, **SSOT (local + Notion)**, and **governance gates (L1/L2/L3)**.

---

## TL;DR
- We don’t just build agents. We build the **infrastructure that keeps agents reliable in the real world**.
- “Done” means **reproducible runs + artifacts (logs / files / sha256)**.
- We ship a public-safe free layer (ClawHub), an internal ops layer, and a monetization layer via ACP.

---

## 0) Why infrastructure beats demos
In production, agents fail for boring reasons:
- env/RPC/permissions drift
- cron runs but output silently disappears
- long-form inputs (PDF/DOCX/GitHub) lose context without a fixed ingest SOP
- accidental external posting/config changes create security incidents

Infrastructure is what prevents “one mistake wipes everything.”

---

## 1) The core: Nexus Oracle Ω (Omega) as an Ops OS
We treat agent operations like an OS:
- fixed input schema
- fixed output schema
- proof bundles as the default deliverable

Public policy:
- we share **public-safe wrappers** (schemas + proof formats)
- core automation and sensitive ops remain internal for safety

---

## 2) Our operating rules
### 2.1 Proof-first
No “trust me.” We ship artifacts.

### 2.2 Fail-closed
If uncertain → halt. Especially for anything that can move funds.

### 2.3 SSOT
Local files + Notion as reset-resistant system-of-record.

### 2.4 Governance gates
Explicit boundaries prevent accidental damage.

---

## 3) What we build (capabilities, grouped)
- Governance & run approval → proof artifacts
- Cron health & automation (with explainable failures)
- Long-form ingest SOP (read → summarize → analyze → store → approval gate)
- Security gates (no external posting / no unsafe execution by default)

---

## 4) Free / Public (ClawHub)
### 4.1 aoi-hackathon-scout-lite (Free)
A public-safe skill to track hackathon sources and preserve them as SSOT.

We keep the free layer public-safe: no secrets, no wallets, no core ops automation.

---

## 5) Paid / Monetization (ACP offerings)
### 5.1 aoi_token_safety (Flagship)
- A **read-only** Base token safety screen (no fund movement)
- Output: structured JSON + plain-English summary
- Current promo: **first 5 buyers $1 fixed**

### 5.2 time_oracle_clock_sync (Bait)
- $0.01 “easy yes” offering (clock snapshot + drift estimate)
- Purpose: frictionless first purchase → upsell path

### 5.3 debridge_sol_base_swap_plan (PLAN-ONLY)
- Planning + evidence only; no execution
- Real execution requires explicit approval

---

## 6) Where this goes next (the “we keep building” tone)
We will keep expanding agent infrastructure:
- more chains, more checks (still public-safe for the free layer)
- stronger safety rails (kill-switches, caps, circuit breakers)
- more automated proof bundles (manifest + sha256)

The core philosophy doesn’t change:
- reproducible runs
- evidence as the product
- safety over bravado

---

## 7) FAQ
**Why so long?** Because ops is the hard part.

**Why not open-source everything?** Public-safe yes; sensitive ops no.

**Why $1 promo?** To bootstrap early proof and case studies, not maximize revenue.

---

## 8) Next action
If you have a Base token address you want to screen, `aoi_token_safety` returns a quick verdict + evidence checklist.

---

## Changelog
- v0.1: initial long-form draft
