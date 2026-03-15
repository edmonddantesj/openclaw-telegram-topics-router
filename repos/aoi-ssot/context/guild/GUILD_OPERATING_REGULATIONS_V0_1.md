# GUILD OPERATING REGULATIONS V0.1
**Status:** DRAFT / INTERNAL  
**Scope:** Guild Operations (L3)  
**Classification:** INTERNAL / INTERNAL

---

## Purpose
Guild는 AOI의 실질적인 작업 및 에이전트 운용 조직이다. 본 규정은 Guild 멤버 간의 역할 분담, 의사결정 프로세스, 협업 방식 및 SSOT 유지 의무를 규정한다.

---

## Role Taxonomy
- **Chair (L2):** 전략 수립 및 최종 승인권자.
- **Oracle (L2/L3):** 정책 및 결정 지원, SSOT 정합성 검토.
- **PM (Project Manager):** 일정 관리, 이슈 트래킹, 리소스 배분.
- **Builders (L3):** 에이전트 개발, 인프라 구축, 코드 작성.
- **Reviewers (L3):** 코드 및 문서 리뷰, 벤치마크 검증.

---

## Membership & Decision Making
- **Joining:** 기존 멤버 2인 이상의 추천 및 L2 승인.
- **Withdrawal:** 완료되지 않은 작업의 인수인계(Handoff) 및 SSOT 업데이트 후 탈퇴.
- **Decision:** Primary Owner가 결정하되, 갈등 발생 시 Council/Oracle 중재에 따름.

---

## Meetings & Council Triggers
- **Bi-weekly Sync:** 주 1회 정기 진행 (비동기 문서 업데이트 중심).
- **Emergency Trigger:** 보안 침해, 시스템 중단, 중대한 정책 충돌 발생 시 즉시 소집.
- **Approval Gates:** 
    - **L1/L2 Change:** L2 Council 전원 합의 필수.
    - **External Posting:** `STEALTH_CLASSIFICATION_MATRIX` 준수 및 L2 승인 필수.
    - **Onchain Deployment:** 스마트 컨트랙트 배포 전 보안 감사 및 L2 최종 사인 필수.

---

## SSOT Update Obligations
모든 작업은 시작 전 `Issue` 또는 `Task`로 정의되어야 하며, 완료 후 24시간 이내에 관련 SSOT 문서(Markdown)를 최신화해야 한다. SSOT 업데이트 없는 성과는 존재하지 않는 것으로 간주한다.

---

## Templates

### 1. 작업 시작 포맷 (L1/L2/L3)
```markdown
### [TASK_ID] Task Title
- **Priority:** (L1/L2/L3)
- **Primary Owner:** @[User/Agent]
- **Target SSOT Path:** /context/.../FILE.md
- **Success Metric:** [Measurable outcome]
- **Estimated End:** YYYY-MM-DD
```

### 2. Handoff Snapshot Checklist
- [ ] 관련 모든 코드가 `/workspace`에 저장되었는가?
- [ ] 최신 `memory/YYYY-MM-DD.md` 로그가 업데이트 되었는가?
- [ ] 실행 증명(Receipts)이 `/context/receipts/`에 기록되었는가?
- [ ] 다음 작업자를 위한 'Next Action' 항목이 작성되었는가?

### 3. Approval Request Packet
- **Request ID:** [REQ-XXX]
- **Subject:** [Summary of request]
- **Impact Level:** (Internal/External/Onchain)
- **Evidence Link:** [Path to receipts/logs]
- **Review Status:** (Pending/Approved/Rejected)
```

---

## Communications Rules
1. **No Ghosting:** 작업 중인 멤버는 최소 12시간 이내에 메시지에 응답하거나 상태를 업데이트해야 한다.
2. **Context-Rich:** 질문이나 보고 시 반드시 관련 파일 경로, 로그, 스크린샷을 동봉한다.
3. **Public/Private Distinction:** `STEALTH` 등급의 정보는 반드시 지정된 보안 채널에서만 논의한다.

---

## Conflict Resolution
1. 멤버 간 1차 협의 시도.
2. 해결 불가능 시 Oracle 또는 PM에게 중재 요청.
3. 최종 해결은 Chair 또는 L2 Council의 결정을 따르며, 결정 후 SSOT에 기록한다.

---

## Changelog
- **2024-05-22 (V0.1):** 최초 초안 작성. Guild 역할군 및 운영 규정 정의.
