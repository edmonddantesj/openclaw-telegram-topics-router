# AOI Squad Pro — Ops Kit Masterplan v0.1 (Bundle A)

Last updated: 2026-02-20 (KST)
Owner: Edmond + Aoineco
Status: DRAFT

> Purpose: AOI Core Pro Kit의 대표 번들(ops kit)로서, Squad Pro의 scope/데모/증빙/로드맵을 고정.

---

## 0) One-liner
Squad Pro = **approve → run → proof**를 “원클릭 데모 + 증빙 번들”로 보여주는 Ops Kit.

## 1) Core promise
- Approve gate (L1/L2/L3)
- Proof bundle (proof.json + sha256sum + artifacts + logs)
- Shadow → Canary → Live

## 2) SSOT & artifacts
- Skill: `skills/aoi-squad-pro/`
- One-click demo: `scripts/aoi_squad_pro_oneclick_demo.sh`
- Pinned demo bundle: `context/proof_samples/public/AOI_SQUAD_PRO_PROOF_BUNDLE_DEMO_V0_1/`
- Ops output schema: `aoi-core/docs/AOI_SQUAD_PRO_OPS_OUTPUT_SCHEMA_V0_1.md`

## 3) MVP deliverables
- 10-min quickstart stable
- public-safe scan PASS included
- daily case study (public-safe) generator + cron (optional)

## 4) Roadmap
- v0.2: case study automation + dashboards
- v0.3: queue/promote UI (ASCII wireframe → real UI)

## 5) Risks
- network flakiness (Supabase/REST) → idempotent + retry + fallback
- proof leak risk → public-safe scan mandatory
