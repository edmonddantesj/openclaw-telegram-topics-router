# AOI Squad Pro 공지/집계 템플릿 모음 (v0.1)

## 1) 청묘 공지용 1회 메시지 (복붙)

```text
[AOI Squad Pro — 1차 수행 공지]

청음/청검/청안/청비/청성/청기/청섬/청정 (해당 1차 배정권자)

이번 라운드는 별도 DM 확인 루프 없이 **각자 바로 실행 + 템플릿 제출**로 진행한다.

아래 템플릿을 10분 내로 제출.
필수 항목이 비면 BLOCK 처리됨.

- Task ID:
- Task Name:
- 상태(Status): DONE / BLOCK / NEEDS_SUPPORT
- 핵심 산출물:
- 수핼 근거(한 줄):
- proof_dir: /tmp/aoi_squad_pro_run_<YYYYMMDD_HHMMSS>/
- input_digest:
- sha256:
- logs:
- 실패 시: failure_code / suggested_fix
- 다음 액션:

규칙:
- output은 실제 산출물 경로 위주로 남길 것.
- 승인 필요한 변경은 diff 제안 후 승인 단계에서 적용.
- 완료면 approval 적용 결과까지 기록.

제출 마감: +10분 (타임스탬프 기준)
```

---

## 2) 역할별 실행 응답폼(단축형)

### Planner/Researcher/Operator 공통
```text
[AOI Squad Pro 결과]
- Task ID:
- Status:
- Task Name:
- 핵심 산출물:
- proof_dir:
- input_digest:
- sha256:
- logs:
- failure_code:
- suggested_fix:
- 다음 액션:
```

### Reviewer(Security)용
```text
[AOI Squad Pro - Reviewer]
- Task ID:
- 상태:
- 보안/리스크 체크:
- 정책 위반 여부(Y/N):
- 필요한 수정:
- proof_dir:
- input_digest/sha256:
- logs:
- suggested_fix:
- 다음 액션:
```

### Ops(운영자)용
```text
[AOI Squad Pro - Operator]
- Task ID:
- runId:
- proof_dir:
- sha256:
- input_digest:
- 적용 여부:
- 증빙 파일 존재:
  - input.json:
  - proof.json:
  - proof.sha256:
- BLOCK 사유(있으면):
- 다음 액션:
```

---

## 3) 청령 집계용 즉시 붙여넣기 템플릿

### 라운드 집계 헤더
```text
[AOI Squad Pro 1차 라운드 집계]
총 대상: N명 / 완료: A건 / BLOCK: B건 / NEEDS_SUPPORT: C건
수집 시작: {start_time} / 종료: {end_time}

| 멤버 | Task ID | 상태 | 산출물 | proof_dir | sha256 | BLOCK 사유 | 다음 액션 |
|---|---|---|---|---|---|---|---|
```

### 멤버 라인 예시
```text
| 청음 | TASK-001 | DONE | docs/LAUNCH_CHECKLIST.md 생성 | /tmp/... | 9f1c... |  | next: 승인 후 검토 |
| 청검 | TASK-002 | BLOCK | 보안 스캔 미흡 | /tmp/... |  | 민감경로 미승인 | 경로 재정의 |
```

### 집계 후 후속 규칙
- DONE 5개 이하: 미달 보완 대상
- BLOCK가 1개 이상: 청령이 NEEDS_SUPPORT 항목만 선별 재요청
- 완료분만 `memory/2026-02-19.md` + `CURRENT_STATE.md` 요약 반영
- P0 미완료 1개 이상 + 20분 초과 시 긴급 점검 전환

---

## 4) 최종 기록 패턴(권장)
```text
- 제출 수단: context/AOI_SQUAD_PRO_1ST_ROUND_REPORT_V0_1.md
- 증빙 보관: /tmp/aoi_squad_pro_run_<ts>/input.json|proof.json|proof.sha256
- 실패 이력: memory + CURRENT_STATE 단일 라인
```
