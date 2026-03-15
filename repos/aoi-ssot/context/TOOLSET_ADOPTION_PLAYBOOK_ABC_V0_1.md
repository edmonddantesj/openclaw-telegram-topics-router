# Toolset Adoption Playbook — A/B/C (v0.1)

Date: 2026-02-20 (KST)
Owner: Edmond + Aoineco
Status: **READY**

Notion SSOT (Idea Vault source):
- https://www.notion.so/Toolset-Adoption-Playbook-A-B-C-1-30d9c616de8681f794d6c9d0cba0d0f7

## 0) Purpose
Control risk when adopting new tools/services/plugins by enforcing a lightweight triage and hard guardrails.

## 1) Classification (A/B/C)
- **A — Adopt now (즉시 도입)**
  - Criteria: low risk, reversible, minimal permissions, clear value.
  - Required: minimal config + SSOT log.

- **B — Internalize (내재화/리빌딩)**
  - Criteria: valuable but needs security hardening, integration refactor, or provenance controls.
  - Required: rebuild plan + Guardian/Security Gate + S‑DNA + proof pack.

- **C — Conditional / Queue (조건부/대기)**
  - Criteria: unclear value, high risk, too many permissions, or external dependency risk.
  - Required: hold in parking lot + revisit criteria.

## 2) Hard guardrails (mandatory)
- **Least privilege**: request only required scopes/permissions.
- **Local secrets only**: no hardcoded keys; use vault/env.
- **Failure recovery**: rollback/uninstall path and smoke test.
- **Monthly security audit**: at least 1×/month review for adopted tools.
- **SSOT logging**: every adoption must be recorded (decision + evidence).

## 3) Where it plugs in (existing SSOT)
- Adoption command protocol: `context/COMMAND_DOIP_HAEJWO_PROTOCOL_V0_2.md`
- Exposure tiers: `context/EXPOSURE_TIER_MATRIX_V0_1.md`
- Parking lot: `context/TASK_PARKING_LOT.md`

## 4) Evidence
- Notion source: link above
- Local policy file: this document
