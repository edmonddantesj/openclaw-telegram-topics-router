# Topic State — random

- Topic: `random`
- Status: ACTIVE
- Last saved: 2026-03-08 23:13 KST

## Current objective
- 혼재된 이슈/규칙/오픈 태스크를 Playbook + HF 구조로 정리해 잡탕 토픽도 복구 가능하게 유지한다.

## Latest checkpoint
- Topic81 유래 작업들은 proof-first 프로토콜, repeatable rules playbook, 관련 HF 분리까지 완료됐다.
- AOI PRO 베타 라이선스 이슈는 allowlist만으로 해결되지 않고 signed license JSON + issuer key 탐색이 병목으로 정리돼 있다.
- 잡탕 토픽일수록 topic-state가 “현재 뭐가 메인인지”를 강하게 압축해야 한다.

## Decisions locked
- 반복 규칙은 playbook으로 승격.
- 큰 이슈는 HF로 분리.
- AOI PRO 활성은 signed license 검증이 핵심.

## Next actions
1. 현재 메인 이슈 1~2개만 checkpoint에 남기고 나머지는 HF 링크로 보낸다.
2. issuer key 탐색/재발급 플랜은 관련 HF에 누적.
3. 토픽이 더 섞이기 전에 새 main topic으로 분리할지 검토.

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
- random은 편하지만 기억엔 독이다. state를 자주 깎아줘야 한다.
