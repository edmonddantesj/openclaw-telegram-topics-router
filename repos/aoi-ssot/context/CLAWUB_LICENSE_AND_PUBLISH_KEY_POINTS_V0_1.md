# ClawHub publish + license discussion — Key points v0.1 (2026-02-15)

## Source
- Raw dump: `context/CLAWUB_LICENSE_AND_PUBLISH_DISCUSSION_DUMP_2026-02-15_V0_1.txt`

---

## 1) 운영 원칙(자사 오리지널 스킬)
- 이미 올린 스킬은 **지속 업데이트**한다.
- 단, 우리 프로그램은 **감사 기준(보안/추적가능성)**이므로 **보안에 흠집 나는 업데이트는 불허**.
- “알아서 올리고 업데이트”는 허용하되, **배포 게이트는 강제**로 설계해야 통제 부재로 읽히지 않음.

## 2) Release Gate 3단계(필수)
1) **Security Gate PASS** (권한/네트워크/키/외부 호출 등 스캔)
2) **Reproducible build + changelog** (변경 추적)
3) **Rollback plan** (이전 버전 복구 가능)

## 3) 누적경고제(추천)
- 사람/팀이 아니라 **스킬(레포) 단위**로 관리.
- 경고 사유는 3종만 인정:
  - (A) 보안 게이트 BLOCK 무시
  - (B) 라이선스/출처 불명확(재배포 금지/미명시 포함)
  - (C) 릴리즈 노트/버전/변경 추적 누락(감사 불가)
- 단계 예시:
  - 1회: 공개 유지 + 보안 개선 의무
  - 2회: publish 권한 일시정지 + 리뷰어 승인
  - 3회: delist/archive + 내부용 전환(또는 major rewrite 후 재등록)

## 4) Public-safe vs Restricted 분리
- Public-safe(기본): read-only 데이터/분석/로깅/유틸
- Restricted(원칙적으로 공개 금지): 결제/지갑/자동거래/메시징/포스팅/광권한/크리덴셜
- 로열티/지급 레일 같은 건 공개한다면 **실행이 아니라 프레임워크/런북/스키마**까지만.

## 5) 공개 템플릿(스킬 README/코멘트에 고정)
- Support policy
- Security posture(게이트 통과 원칙)
- Versioning(SemVer)
- Vulnerability disclosure channel + triage SLA

## 6) Security Gate v0.2 구현 및 활용
- 체크리스트 문서 + 실행 스크립트/패턴 파일로 구체화.
- BLOCK 2건을 기준으로 원인 리포트 생성 후 조치 결정.

## 7) BLOCK → public-safe 리빌드 전략
- BLOCK 걸린 스킬(aoineco-sandbox-shield, prompt-guard)을 그대로 publish하지 않고,
  **public-safe 범위로 기능을 잘라** AOI 오리지널로 재제작:
  - `aoi-sandbox-shield-lite` (snapshot + config validate only)
  - `aoi-prompt-injection-sentinel` (offline prompt injection detection only)

## 8) 배포 결정(MIT)
- 위 2개 리빌드 스킬을 **MIT 라이선스로 공개 배포** 결정.
- 공개 배포 전:
  - LICENSE(MIT) 포함
  - “lite 버전(실행/적용 없음)” 문구로 범위 고정
  - Security Gate 통과 확인

## 9) 증빙(링크)
- ClawHub:
  - https://clawhub.com/skills/aoi-sandbox-shield-lite
  - https://clawhub.com/skills/aoi-prompt-injection-sentinel
- Notion inventory pages:
  - https://www.notion.so/aoi-sandbox-shield-lite-3089c616de86810aa2effc3fbbca6103
  - https://www.notion.so/aoi-prompt-injection-sentinel-3089c616de8681f7ab97c0dfd0de9309

## 10) Open items
- ClawHub 퍼블리싱 정책 문서/체크리스트 파일의 현재 위치를 SSOT로 재확인(경로 정합성 점검)
- Restricted 범주(지갑/결제/메시징 등) 판정표를 더 명확히(예시 포함)
