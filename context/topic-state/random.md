# Topic State — random

- Topic: `random`
- Status: ACTIVE
- Last saved: 2026-03-08 23:00 KST

## Current objective
- Topic 81에서 섞여 나오던 규칙/반복업무/오픈 이슈를 Playbook + HF 구조로 분리해 재개성을 높이고, AOI PRO 관련 열린 이슈를 추적한다.

## Latest checkpoint
- Proof-first 프로토콜과 반복규칙 Playbook이 생성됨.
- Topic81 유래의 열린 이슈들이 HF로 분리되고 `context/handoff/INDEX.md`에 ACTIVE 등록됨.
- AOI PRO 베타 라이선스 이슈는 allowlist만으로 해결되지 않으며, 서명된 라이선스 JSON + issuer key 경로 탐색이 핵심 병목으로 정리됨.

## Decisions locked
- 반복 규칙은 Playbook으로 승격.
- 큰 이슈/열린 작업은 HF로 분리.
- AOI PRO 활성 조건은 signed license JSON 검증이 핵심이며 단순 allowlist 추가로는 해결 불가.

## Next actions
1. Topic81 계열 오픈 이슈는 각 HF 기준으로 추적.
2. AOI PRO issuer key 위치를 우선 탐색.
3. key 미발견 시 재발급 플랜 수립.

## Key files
- Playbook: `context/playbook/REPEATABLE_RULES_V0_1.md`
- Protocol: `context/protocols/PROOF_FIRST_STATUS_PROTOCOL_V0_1.md`
- Handoff index: `context/handoff/INDEX.md`
- Related HF: `context/handoff/HF_topic81_basebatches_submission_package_202603.md`, `context/handoff/HF_aoi_pro_install_quickstart_preflight_202603.md`, `context/handoff/HF_aoi_pro_lite_lifetime_spec_202603.md`, `context/handoff/HF_render_502_warmup_retry_policy_202603.md`

## Restore instructions
- 먼저 이 파일 읽기
- 이어서 반복 규칙은 Playbook, 열린 일은 관련 HF만 최소 읽기
- AOI PRO 쪽이면 라이선스/키 탐색 이슈부터 다시 잡기

## Notes
- `random`은 잡탕 토픽이라 topic-state를 특히 짧고 선명하게 유지해야 함.
