# Adoption Gate Checklist (v0.1)

목적: 외부 프로젝트/코드/아이디어(해커톤, OSS, 블로그, 패키지)를 AOI Squad Pro/ACP에 **도입(내재화 포함)**할 때,
흥분해서 붙였다가 사고 나는 걸 막기 위한 **표준 게이트**.

원칙: **Fail-Closed** — 체크가 안 되면 도입하지 않고 `bench_only` 또는 `queue_for_approval`로 보낸다.

---

## 0) Intake (필수 메타)
- [ ] 소스 URL (DoraHacks/GitHub/npm/docs)
- [ ] 라이선스 / 저작권 표기 링크
- [ ] 데모/문서/README 존재 여부
- [ ] 유지보수 신호(최근 커밋/릴리즈/이슈응답)
- [ ] 우리 목적과의 정합성(ACP 자동화/승인/증빙/지갑/운영)

결론(택1): `adopt` / `internalize` / `bench_only` / `reject`

---

## 1) Security Gate (필수)
### 1-1 공급망/패키지
- [ ] 패키지 이름/레포가 일치하는가(typosquatting 방지)
- [ ] 의존성 잠금파일(lockfile) 존재
- [ ] install script / postinstall / curl|wget|bash 실행 여부
- [ ] 네트워크/파일시스템/프로세스 권한 요구 범위

### 1-2 시크릿/키/지갑
- [ ] 시드/프라이빗키/토큰을 저장하거나 전송하지 않는가
- [ ] 서명/approve가 포함되면: 한도/allowlist/시뮬레이션/승인 흐름이 있는가
- [ ] 외부 호출 endpoint 목록이 문서화되어 있는가

### 1-3 데이터/프라이버시
- [ ] PII/대화로그/지갑주소 처리 범위 명시
- [ ] 로그에 민감정보 누출 가능성 평가

Security 결론: `PASS` / `PASS_WITH_CONDITIONS` / `BLOCK`

---

## 2) Reproducibility Gate (필수)
- [ ] 로컬에서 1-command로 실행 가능한가
- [ ] 최소 실행 환경이 명시돼 있는가(버전/OS/런타임)
- [ ] deterministic output(동일 입력→동일 결과) 가능 영역이 있는가

Repro 결론: `PASS` / `BLOCK`

---

## 3) Governance & Evidence Gate (필수)
- [ ] 우리 정책 SSOT와 연결 가능한가
  - `aoi-core/state/acp_automation_policy_v0_1.json`
- [ ] proof bundle(해시/로그/결과 JSON) 남길 수 있는가
- [ ] 실패 시 상태표기(BLOCKED/PENDING)로 남길 수 있는가

Gov 결론: `PASS` / `PASS_WITH_CONDITIONS` / `BLOCK`

---

## 4) ROI Gate (권장)
- [ ] 1주 내 데모 가치(해커톤 시연/영상) 있는가
- [ ] 2주 내 내부 운영 효율 개선(시간/비용/리스크) 측정 가능?
- [ ] 유지비(Infra, API 비용, 운영 복잡도) 추정

ROI 결론: `WORTH_IT` / `NOT_NOW`

---

## 5) License Gate (필수)
- [ ] LICENSE 파일/라이선스 유형 확인
- [ ] 상업적 사용 가능 여부
- [ ] 파생/수정/배포 의무(카피레프트) 확인

License 결론: `PASS` / `NEEDS_REVIEW` / `BLOCK`

---

## 6) 최종 판정 템플릿
- 판정: `adopt | internalize | bench_only | reject`
- 근거(요약):
- 조건(있으면):
- 다음 액션 Top3:
  1)
  2)
  3)

---

## 운영 팁
- **도입(adopt)**은 드물게, 기본은 **내재화(internalize)**로 생각한다.
- L3(돈/서명/온체인/외부게시)는 자동 실행 금지. 반드시 승인 큐.
- 게이트를 통과하지 못한 건 “별로”가 아니라 **아직 위험/불명확**일 뿐이다.
