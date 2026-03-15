# AOI Squad Pro 실질 시작 패키지 (Start-Pack v0.1)

**목표:** 템플릿만 있는 상태에서 실제 실행 착수로 전환.
**실행 책임:** 청묘(오퍼레이터) + 청령(오케스트레이션 리드)

---
## 0) 지금 바로 실행할 1차 액션
1. 아래 공지문을 청묘가 즉시 1회 발송
2. 10분 타이머 시작
3. 1차 제출 마감 시점 2차 집계
4. 미입력 항목만 청령이 재촉

---
## 1) 발송 기준 공지(복붙)
```text
[AOI Squad Pro — 1차 실무 시작]

이번부터 실제 실행 시작.
아래 템플릿으로 10분 안에 1차 리포트 제출.
필수: Task ID, proof_dir, input_digest, sha256, logs, 실패면 failure_code/suggested_fix.

규칙: 출처(로그/파일 경로) 없으면 DONE 금지.
제출 지연 2회면 BLOCK 처리하고 다음 슬롯으로 넘김.
```

---
## 2) 배정(1차 착수)
- Planner: 청령
- Builder: 청섬
- Operator: 청정
- Reviewer/Security: 청검
- Researcher: 청안
- Knowledge: 청비
- 예비 확장: 청성/청기/청음(상태 안정 시 즉시 확장)

---
## 3) 제출 템플릿(최소형)
```text
[AOI Squad Pro 결과]
- Task ID:
- Task Name:
- Status: DONE / BLOCK / NEEDS_SUPPORT
- 핵심 산출물:
- proof_dir: /tmp/aoi_squad_pro_run_<ts>/
- input_digest:
- sha256:
- logs:
- failure_code:
- suggested_fix:
- 다음 액션:
```

---
## 4) 집계 규칙(청령용)
- DONE/BLOCK/NEEDS_SUPPORT 집계
- DONE 5개 미만이면 라운드 미완주 처리
- BLOCK가 1건 이상이면 근거와 지원 항목만 선별 재요청
- 증빙 경로 미기재는 즉시 BLOCK

---
## 5) 금지/차단 항목(L3 트리거)
- 자금 이동/결제/지갑 서명
- 외부 키/토큰/시크릿 노출
- 파괴적 파일 조작(root-level, 브랜치 강제 push, rm -rf)

차단 시: 즉시 중단 → 증빙 남기고 청렴 라우트로 escalate

---
## 6) 실행 상태 기록 위치
- 라운드 집계: `context/AOI_SQUAD_PRO_1ST_ROUND_REPORT_V0_1.md`
- 운영 이력: `memory/2026-02-19.md`
- 현황: `CURRENT_STATE.md`
