# 청묘 ↔ 흑묘 지원 프로토콜 예문 V0.1

## Example A — inbox-dev 기술 복구 요청
- Topic: inbox-dev
- Priority: P0
- Current state: NO_STATE 결손과 sync 불안정 때문에 일부 state 파일이 누락되어 있고, 관련 자동화가 재실행 시 흔들리는 상태.
- Goal: 누락 state를 탐지하고 표준 스켈레톤 생성 + 재실행 시 부작용 없는 복구 플랜까지 확보.
- Deadline: 오늘 안
- Needed support: 복구 설계안 + 체크리스트 + 스켈레톤 생성 규칙 초안
- Expected output type: implementation plan / checklist / SSOT draft
- Affected scope: context/state/, scripts/, sync pipeline
- Failure mode: missing state files / idempotency risk / incremental sync breakage
- Constraints / human gate: 실제 배포/자동실행 반영은 human 승인 후 진행. 위험한 일괄 수정은 바로 적용하지 말 것.
- Reference paths:
  - context/handoff/HF_inbox_dev_urgent_202603.md
  - context/topics/inbox-dev_PLAYBOOK_V0_1.md
  - context/state/
  - scripts/

### Expected heukmyo response shape
- Owner: 흑묘팀 담당자
- State: partial
- What was done: 누락 유형 분류, state 스켈레톤 규칙 제안, validator 체크리스트 초안 작성
- Output: restore-plan.md / state-schema-notes.md / validator-checklist.md
- Next: 청묘팀이 실제 적용 범위 승인 후 스크립트 반영 여부 결정
- Blocker / human gate: 자동 생성 스크립트 적용 전 human 승인 필요
- Updated paths: (작성 문서 경로)
- Promote candidate: local playbook

---

## Example B — ops 운영 지원 요청
- Topic: ops
- Priority: P1
- Current state: SAVE NOW / launchd / notion sync / gateway health 관련 운영 규칙은 흩어져 있고, 장애 시 점검 순서가 사람 기억에 의존하는 부분이 있음.
- Goal: 운영 점검 순서와 장애 대응 체크리스트를 한 장으로 고정해서 재사용 가능하게 만들기.
- Deadline: 이번 사이클 내
- Needed support: 운영 체크리스트 초안 + 장애 triage 흐름도 + human gate 정리
- Expected output type: checklist / review memo / playbook draft
- Affected scope: context/ops/, context/automation/, launchd jobs, gateway ops docs
- Failure mode: drift / missing proof / restart loop / env mismatch
- Constraints / human gate: 실제 재시작/모델 전환/서비스 변경은 승인 후 진행
- Reference paths:
  - context/topics/ops_PLAYBOOK_V0_1.md
  - context/ops/
  - context/automation/launchd/

### Expected heukmyo response shape
- Owner: 흑묘팀 담당자
- State: done
- What was done: 운영 점검 순서, 장애 triage 기준, 승인 필요 액션 분리 정리
- Output: ops-checklist.md / incident-triage.md / gate-matrix.md
- Next: 청묘팀이 ops playbook에 승격 여부 검토
- Blocker / human gate: 없음 또는 일부 재시작 액션 승인 필요
- Updated paths: (작성 문서 경로)
- Promote candidate: SSOT candidate
