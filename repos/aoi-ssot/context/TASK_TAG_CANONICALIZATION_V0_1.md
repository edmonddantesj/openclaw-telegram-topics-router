# TASK_TAG_CANONICALIZATION_V0_1.md

목적: 대화/크론/SSOT에서 태그가 제각각이라 생기는 혼선을 제거하고, 동일 의미의 태스크를 **하나의 canonical tag**로 통일한다.

## 규칙
- 태그는 소문자 + 하이픈만 사용: `[a-z0-9-]+`
- 같은 의미면 별칭(alias)은 허용하되, SSOT에는 **canonical tag**만 기록한다.
- 사용자가 alias로 `재개 <tag>`를 말해도, 시스템은 canonical tag로 매핑해 찾아준다.

## Canonical Tag Map (v0.1)

### Hackathons / Demos
- `bnb-goodvibes-video`
  - aliases: `bnb-goodvibes`, `goodvibes-video`, `bnb-video-only`

- `midl-vibehack-home`
  - aliases: `vibehack-home`, `midl-home`, `home-vibehack`

- `aoi-workflow-demo-home`
  - aliases: `workflow-demo`, `aoi-demo-home`, `home-demo`

### Council / Governance
- `team-council-pause`
  - aliases: `council-lite-pro`, `team-council`, `opinion-aggregator`

### Survival / Bridge / KPI
- `survival-bridge-gate`
  - aliases: `7-bootstrap`, `survival-live-gate`, `bridge-gate`, `dlmm-gate`

### Payments / x402
- `x402-clawfm`
  - aliases: `x402`, `clawfm-upload`, `x402-signer`

### Royalty / Adoption
- `royalty-outreach-pack`
  - aliases: `royalty`, `contact-log`, `attribution-policy`, `royalty-message-pack`, `royalty-bmin-usdc-base` (legacy)

### Alpha Oracle docs
- `alpha-oracle-submission-clean`
  - aliases: `usdc-hackathon-submission`, `submission-clean`, `alpha-oracle-v6-data-fallback` (legacy)

### Hackathon scouting
- `hackathon-scouting`
  - aliases: `hackathon-shortlist`, `shortlist`

## 운영 적용
- Parking Lot 카드의 tag는 항상 canonical로 기록.
- Shortlist의 각 항목은 필요 시 canonical tag를 부여(예: `hackathon-scouting`).
