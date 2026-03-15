# Hackathon Participation Rules v0.1 (Aoineco)

Last updated: 2026-02-20 (KST)
Status: RECOMMENDED (internal ops)

> Goal: maximize hackathon ROI without scope creep or security accidents.
> Source (Council decision log): https://www.notion.so/Hackathon-Participation-Rules-v0-1-Team-Council-30b9c616de86818c8c9bc775116cfb78

---

## Core Rules (the 3)
1) **Use our product as the testbed**
   - During hackathons, prefer running AOI Squad Pro / proof bundles / SSOT workflows.
   - Treat the submission as a real ops QA.

2) **Leave productization optionality**
   - Design artifacts so they can become a Pro offering later (docs, proofs, demo bundles).

3) **Benchmark other submissions**
   - Compare competing hackathon projects and extract reusable patterns.

---

## Guardrails (mandatory)
- **Public-safe mode** by default for anything that might be shared.
- Use **dummy keys / dummy data** for demos.
- Block sensitive capabilities in submissions:
  - wallet signing / on-chain transfers
  - external posting / outbound webhooks
  - secret handling
- **Scope lock**: shipping beats perfection.

---

## Execution Policy (the key change)
- “Immediate apply” is NOT literal during the hackathon.
- During hackathon:
  - capture findings as tickets only
  - prioritize submission quality + evidence
- After hackathon:
  - **post-48h triage window** decides what gets integrated

---

## 80/20 Policy
- **80% mandatory**: follow these rules by default.
- **20% exceptions** only when:
  - organizer requirements conflict
  - security risk increases
  - submission deadline risk (scope creep)

---

## Templates (to create)
- Kickoff checklist
- Mid checkpoint
- Pre-submit checklist
- Post (48h triage)
- Benchmarking form (Top5)

---

## Next Actions (Top 3)
1) Create hackathon checklists (Kickoff/Mid/Pre-submit/Post-48h)
2) Create benchmarking template (Top5) with a fixed schema
3) Wire a post-48h triage routine into AOI Queue / Decision Log
