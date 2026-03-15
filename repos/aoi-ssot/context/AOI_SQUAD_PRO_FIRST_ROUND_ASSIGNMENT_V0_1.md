# AOI Squad Pro 1차 파일럿 배정표 & 실행 템플릿 (v0.1)

작성일: 2026-02-19
상태: 즉시 실행용

## 1) 1차 파일럿 배정 (2명/3명 로테이션 권장)

### 배정 A (즉시 착수)
1. 🧿 청령 (Oracle) → **Planner**
   - **1차 태스크:** Base/Bounty/일일 큐에서 가장 급한 1건을 `approve` 규칙으로 정리
   - **목표:** 입력 요건-승인 기준 합의 및 증빙 시작
2. ⚡ 청섬 (Blue-Flash) → **Builder**
   - **1차 태스크:** 위 태스크를 실제 산출물(문서/리스트/스크립트)로 변환
   - **목표:** 실행 가능한 산출물 생성 + 증빙 경로 생성
3. 🧰 청정 (Blue-Maintainer) → **Operator**
   - **1차 태스크:** run/proof 경로 정합, 로그/해시 저장 파이프라인 점검
   - **목표:** 증빙 폴더 구조 및 셀프-audit 필드 누락 없는지 확인

---

### 배정 B (병렬 2~3명 추가로 바로 실행)
4. 🛡️ 청검 (Blue-Blade) → **Reviewer/Security**
   - **태스크:** 승인 스키마 및 보안 규칙 점검, 실패 케이스 위험요소 체크
5. 👁️ 청안 (Blue-Eye) → **Researcher**
   - **태스크:** `Notion Dashboard` 역할 데이터 최신값 확인 및 변경 diff 기록
6. 🗂️ 청비 (Blue-Record) → **Reviewer/Knowledge**
   - **태스크:** 1차 실행 결과를 1회분 저장소 기록(메모/노션/큐)

---

## 2) 각자 실행 템플릿(복붙용)

### 템플릿 01 — Planner용 (청령/Planner)
```text
[AOI Squad Pro] 1차 실행 [Planner] 제출

1) Task ID:
2) 요청자/이슈 출처:
3) Scope:
4) 승인 조건:
   - 성공 조건:
   - 실패 조건:
5) 보안/리스크 체크:
6) 실행 위임 대상(Preset/A/O):
7) 예상 산출물:
8) 완료 판정:

결론:
- APPROVE / NEEDS_REVISION / REJECT
- 이유:
```

### 템플릿 02 — Builder용 (청섬/Builder)
```text
[AOI Squad Pro] 1차 실행 [Builder] 수행 리포트

Task ID:
받은 지시(요약):
실행 단계:
1) plan 반영
2) 산출물 생성
3) 에러/예외 처리

결과:
- status: ok / failed
- output summary:
- location:
  - /tmp/aoi_squad_pro_run_<ts>/input.json
  - /tmp/aoi_squad_pro_run_<ts>/proof.json
  - /tmp/aoi_squad_pro_run_<ts>/proof.sha256

자기점검:
- input_digest:
- evidence:
- runtime:
- generated_at:
- version:
- failure_code(해당시):
- suggested_fix(해당시):
```

### 템플릿 03 — Operator용 (청기/청정)
```text
[AOI Squad Pro] 1차 실행 [Operator] 증빙/검증 리포트

Task ID:
시간:

실행 검증:
- runId:
- proof_dir:
- sha256:
- logs:

필수 증빙 체크:
- input.json 존재/해시:
- proof.json 존재/해시:
- sha256 파일 존재:

문제:
- none / [기술적 내용]

완료 판정:
- PASS / FAIL
- PASS 조건 충족:
- FAIL 시 액션:
  - 재실행/리트라이:
  - 청소 항목:
```

---

## 3) 증빙 경로(고정)
- 기본 경로: `/tmp/aoi_squad_pro_run_<YYYYMMDD_HHMMSS>/`
  - `input.json`
  - `proof.json`
  - `proof.sha256`
  - `evidence.json`

권장 파일명 예시:
- `/tmp/aoi_squad_pro_run_20260219_192100/input.json`

---

## 4) 10분 체크리스트(실행 직후)
- [ ] Planner 승인 템플릿 1건 제출
- [ ] Builder 산출물 1건 생성
- [ ] Operator 증빙 디렉토리 생성 및 3종 파일 존재 확인
- [ ] 실패 시 failure_code/suggested_fix 기록
- [ ] 팀 채널에 간단 리포트 공유

---

## 5) 배포 방식
1) 위 배정 A를 먼저 실행(10~15분)
2) 결과 회수 후 배정 B 동시 실행
3) 각 결과를 합쳐서 `context/AOI_SQUAD_PRO_10_MEMBER_ROLLOUT_ROUND1_REPORT_V0_1.md`로 집계

---

## 6) 다음 액션
- 라운드1 종료 후: 실패율, 응답 지연, 증빙 누락 항목 집계
- 2차 파일럿에 청음/청비/청성/청기/청안/청뇌 순차 투입
