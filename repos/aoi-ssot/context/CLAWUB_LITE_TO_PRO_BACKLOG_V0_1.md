# ClawHub (edmonddantesj) — Lite → Pro Backlog (Draft v0.1)

Source profile: https://clawhub.ai/u/edmonddantesj

## Snapshot (observed on ClawHub)
Lite 표기(=Pro 염두 후보)로 확인된 항목:
- AOI Cron Ops (Lite) — `aoi-cron-ops-lite`
- AOI Squad Orchestrator (Lite) — `aoi-squad-orchestrator-lite`
- AOI Hackathon Scout (Lite) — `aoi-hackathon-scout-lite`
- AOI Triple Memory (Lite) — `aoi-triple-memory-lite`
- AOI Sandbox Shield (Lite) — `aoi-sandbox-shield-lite`

(기타 published지만 Lite 표기는 아님)
- AOI OpenClaw Security Toolkit (Core) — `aoi-openclaw-security-toolkit-core`
- AOI Prompt Injection Sentinel — `aoi-prompt-injection-sentinel`
- AOI Demo Clip Maker — `aoi-demo-clip-maker`
- AOI Council — `aoi-council`
- Aoineco Squad Dispatch — `aoineco-squad-dispatch`
- Aoineco Ledger — `aoineco-ledger`
- PublishGuard — `publish-guard`
- Token Guard — `token-guard`

---

## Pro 방향(요약) — Lite 별

### 1) AOI Cron Ops (Lite) → Cron Ops Pro
- **Auto-fix(옵션):** 중복 크론 disable / 번들링 / delivery=none 전환을 “계획+패치”로 생성
- **Evidence bundle:** 변경 전/후 cron list + runs 요약 + sha256
- **지속 운영:** weekly hygiene + failure/noise anomaly alert + kill-switch

### 2) AOI Squad Orchestrator (Lite) → Squad Ops OS Pro
- **approve→run→proof**를 태스크 단위로 강제(=Squad Pro의 핵심)
- **Queue + promote:** inbox→spec→build→review→done + 증빙 링크
- **Council 플러그인:** dissent/conflict 포함 의사결정 기록 + Notion SSOT

### 3) AOI Hackathon Scout (Lite) → Hackathon CRM Pro
- **Hackathon CRM:** deadline/eligibility/track-fit + submission checklist + proof artifacts
- **Notion SSOT 강화:** 1 해커톤=1 row + canonical view 링크 + 첨부
- **Watch mode:** daily delta scan + Telegram digest (rate-limit safe)

### 4) AOI Triple Memory (Lite) → Durable Memory Governance Pro
- daily distill → MEMORY.md promote → decision log → parking lot 연결 자동화
- public-safe export(마스킹/민감도 분류) 1커맨드
- ontology(엔티티/태스크/이벤트) 브리지로 백링크 자동 생성

### 5) AOI Sandbox Shield (Lite) → Canary & Rollback Pro
- snapshot→validate→apply→verify→rollback 체인(카나리 포함)
- L1/L2/L3 gate + diff-based approval 프롬프트
- 모든 설정변경에 proof bundle 생성(누가/왜/무엇을 변경)

---

## 추천 우선순위 (매출/운영임팩트 관점)
- P1: **Squad Orchestrator Pro** (우리가 이미 Squad Pro로 증명 중)
- P2: **Sandbox Shield Pro** (운영 안전/릴리즈 게이트)
- P3: **Cron Ops Pro** (운영비 절감 + 즉시 체감)

## Next actions
1) Notion에 이 문서를 SSOT로 박제
2) PRO Product Catalog DB에 Pro 상품 후보 row 추가(각각 가격/증빙 링크/상태)
3) Top3 하나 골라 2주 스프린트: "MVP(10분 데모 + proof sample + pricing 1pager)" 완성
