# AOI Core (Main Project) — Timeline v0.1 (2026-02-17)

> This is a **separate** plan from “AOI Squad Pro — Launch Plan (D-7)”.
> Goal: build the **core product** that Pro/Lite/skills plug into.

## Working title (가제)
- **AOI Agent Ops OS**
  - tagline: Proof-first + Governance-by-default + SSOT (Notion+Local)

## North Star
- “에이전트가 일을 했다”가 아니라 **증빙(artifact/proof)이 남는 운영체제**
- 핵심 루프: **Request → Plan → Approve → Execute → Proof → Digest → ADR**

## Beta (2/21 Sat 12:00 KST) — minimum demo
A) 1 request를 넣으면
B) 승인 게이트(deny/approve) 1회 거치고
C) 실행(또는 DRY-RUN) 1회 하고
D) proof artifact 1개 생성 + digest에 링크로 노출

### Demo scenario (둘 중 택1)
- Demo-Doc: README 수정 + patch proof
- Demo-Ops: Launch checklist/ADR 생성 + proof

## Architecture (MVP)
- **SSOT Local:** `context/` + `/tmp` artifacts + `CURRENT_STATE.md`
- **SSOT Notion:** Idea Vault / Decision Log(ADR) / Reference Inbox
- **Execution:** “safe_run wrapper + strict output limits”
- **Governance:** allowlist + approval-required actions + fail-closed

## Workstreams
1) **Core Runner (P0)**: task spec → steps → artifact writer → summary writer
2) **Approval Gate (P0)**: approve/reject + diff/sha proof
3) **Proof Format (P0)**: 1-line proof + file path + sha256 + optional Notion URL
4) **Digest Layer (P0)**: AM/PM digest + failure 3-line summary + log path
5) **Notion SSOT Writer (P1)**: ADR 저장 + run log 링크

---

# Schedule (2 weeks, beta-first)

## D0 (today ~ 2/17 night): Scope lock + skeleton
- Define 1 demo scenario (Doc vs Ops)
- Freeze proof schema v0.1
- Create runner skeleton + safe_run integration

## D1 (2/18): Core runner + artifacts
- Implement `run_task.py` skeleton
- Artifact write: `/tmp/aoi_run_<id>/` + `proof.json`
- Summary format: 8–12 lines

## D2 (2/19): Approval gate wired
- Implement approve/reject flow (local JSON state)
- Patch apply (dry) + sha mismatch test

## D3 (2/20): Demo polish + rehearsal
- Demo script end-to-end rehearsal (fresh env)
- Troubleshooting notes
- 6-case QA runner

## D4 (2/21 Sat <12:00): Beta cut
- Tag `beta-0.1`
- 1-page beta report (what works / known gaps / next)

## Week2 (2/22~2/28): Hardening
- Notion ADR auto-save
- Better queueing + dedup
- Improve failure diagnostics

## Week2.5 (3/1~3/3): Packaging
- Connect to “AOI Squad Pro” distribution plan (installer/updater)

---

# Risks / Guardrails
- Output truncation → safe_run + log path only
- External leakage → no posting, no secrets, no internal nicknames
- Broken state → atomic write (tmp→rename)
