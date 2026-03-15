# AOI Squad Pro 1차 라운드 배포용 개별 DM 템플릿 (v0.1)

## 공통 헤더
`[오케이. AOI Squad Pro 1차 파일럿 시작. 아래 포맷대로 10분 안에 1회차 결과만 먼저 회신해줘. 증빙은 /tmp/aoi_squad_pro_run_<ts>/...에 저장.]`

---

## 1) 청령(Planner)용 템플릿
`[Planner 회신]

Task ID: 
요청 출처:
Scope 요약:
승인 판정: APPROVE / NEEDS_REVISION / REJECT
근거:
리스크 체크:
- 보안:
- 데이터 신뢰도:
- 일정:

승인 조건 충족 항목:
- [ ] 조건1
- [ ] 조건2

다음 액션/위임:
- Builder:
- Operator:

완료 시간:
` 

---

## 2) 청섬(Builder)용 템플릿
`[Builder 회신]

Task ID:
받은 지시:
실행 단계:
1) 
2) 

결과:
- status: ok / failed
- output summary:
- proof_dir: /tmp/aoi_squad_pro_run_<ts>/

필수 필드:
- input_digest:
- runtime:
- generated_at:
- version:
- evidence:

실패 시:
- failure_code:
- suggested_fix:

완료 시간:
`

---

## 3) 청정(Operator)용 템플릿
`[Operator 회신]

Task ID:
runId:
proof_dir: /tmp/aoi_squad_pro_run_<ts>/
sha256:

검증 체크:
- input.json 존재:
- proof.json 존재:
- proof.sha256 존재:
- 증빙 무결성:

logs:
- /tmp/aoi_squad_pro_run_<ts>/*.log

이슈/실패:
- 

PASS/FAIL:
- PASS: 
- FAIL이면 즉시 조치:
` 

---

## 4) 청검(Safety Reviewer)용 템플릿
`[Reviewer/Security 회신]

Task ID:
검토 대상:
보안 점검 결과:
- 경고/리스크:
- 정책 위반 여부:
- 필요한 수정:

Suggested_fix:

완료 시간:
`

---

## 5) 청안(Researcher)용 템플릿
`[Researcher 회신]

Task ID:
Notion 현재값 조회 경로:
변경사항:
- 

핵심 발견:
- 감정 날씨:
- 역할/업무:

증빙 URL:
- page:
- block/table:

완료 시간:
`

---

## 6) 청비(Knowledge Reviewer)용 템플릿
`[Knowledge Reviewer 회신]

Task ID:
기록 반영 위치:
- memory: 
- CURRENT_STATE:
- queue:

요약:
- 핵심 성과:
- 이슈/누락:

다음 권고:
- 

완료 시간:
`

---

## 제출 방식
1) 각자 템플릿 작성 후 즉시 회신
2. 회신 내용으로 `context/AOI_SQUAD_PRO_1ST_ROUND_REPORT_V0_1.md`의 해당 항목에 붙여넣기
3. 누락이 있으면 `[누락]` 표시 후 5분 내 보완
