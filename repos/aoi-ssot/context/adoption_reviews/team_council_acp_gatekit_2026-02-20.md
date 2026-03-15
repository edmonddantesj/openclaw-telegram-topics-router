# Team Council (Lite) — planning

## Topic
ACP 오퍼링: AOI Security Gate Kit(pre-push+CI+Policy→Gate→Approval→Proof) 가격/패키징/업로드 플랜

## Context (optional)
사용자 승인: 가격 책정 및 업로드까지 내부 논의 후 진행. 제품은 txhash 문서 예외 포함한 security gate 템플릿. 대상: 여러 GitHub 레포에 전수 적용 가능. 외부 노출(L3)

## Constraints (optional)
public-safe(시크릿/아티팩트 제외), 설치 10분 이내, fail-closed 유지, 운영부담 최소.

---

## TL;DR (2 lines)
- 오퍼링은 “에이전트 DevSecOps 기본 인프라”로 포지셔닝하고, **Template Pack(셀프서브)** 1개 + **Setup/Review(옵션)** 1개로 구성하는 게 가장 잘 팔린다.
- 가격은 진입장벽 낮게(월 구독 소액) + 고가치는 “레포 전수 적용/정리”를 서비스로 분리해, 운영부담 없이 LTV를 만든다.

## Role opinions (2–3 lines each)
- 🧿 Oracle (decision frame):
  - 결정: (1) 무엇을 팔지(템플릿 vs 매니지드) (2) 가격/플랜(Free/Pro/Setup) (3) 업로드 순서.
  - 추천: **Template Pack을 메인**으로, “전수 적용 + 정리(키/백업 제거) 컨설팅”은 고가 옵션으로 분리. ACP에는 먼저 템플릿으로 진입.

- 🧠 Analyzer (scoring/trade-offs):
  - 옵션: A) 템플릿만(운영부담↓) B) 템플릿+설치대행(수익↑, 부하↑) C) 매니지드 서비스(수익↑↑, 책임↑↑).
  - 스코어: A=9(확장), B=8(수익/시간 균형), C=5(초기 과부하). 초기엔 **A+B**.

- ⚔️ Security (security/risk):
  - 핵심 리스크: “보안 도구”를 팔면서 우리 쪽이 민감정보 취급하면 바로 신뢰 붕괴.
  - 가드레일: public-safe repo 분리, state/approvals/proofs는 로컬-only, txhash 예외는 문서에만 허용, 그리고 결정적 스캐너(gitleaks) 추가 권장.

- ⚡ Builder (feasibility/MVP):
  - MVP 구성(1일): repo 템플릿 + install 스크립트 + CI 워크플로 + 정책 JSON + 문서.
  - 2~3일: “레포별 롤아웃 스크립트”와 리포트 생성기 포함, GitHub Actions badge까지.

- 📢 Comms (messaging/market):
  - 피치: “Agents you can actually trust — policy-gated execution with approvals & audit-proof evidence.”
  - 반론: “gitleaks/semgrep로도 되잖아?” → “우린 ‘검출’이 아니라 **승인/증빙/운영 루프**를 제공한다(조직 운영 관점).”

## Consensus / Conflict
- Consensus: 템플릿(셀프서브) 중심 + 옵션형 서비스로 확장. 공개는 public-safe가 절대 조건.
- Conflict: 월 구독 vs 일회성. (ACP에서 결제 UX/환불 이슈 고려)

## Dissent (at least 1)
- “가격을 너무 낮추면 ‘그냥 스크립트’로 인식돼서 가치가 훼손될 수 있다.”
  - 대응: Free는 제한(문서/기본), Pro는 “롤아웃 자동화+리포트+정책 템플릿+업데이트”로 명확히 차별.

## Assumptions (3)
1. 에이전트/바이브코딩 사용자는 ‘마지막 순간 보안’ 니즈가 매우 큼.
2. 템플릿+롤아웃 자동화는 ‘재현 가능한 운영’으로 차별화가 됨.
3. 우리는 민감정보를 절대 취급하지 않는 설계로 신뢰를 유지할 수 있음.

## Recommendation
- Go / No-Go / Conditional (pick one)
- Confidence: High / Medium / Low
- Risk: High / Medium / Low

## Next actions (Top 3)
1. public-safe 신규 repo: `aoi-security-gate-kit`(가칭) 생성 + 템플릿 파일 이관.
2. 가격/플랜 초안 확정(Free/Pro + Setup 옵션) 후 ACP 오퍼링 문구/FAQ 작성.
3. gitleaks 단계 추가한 CI 워크플로 v0.2 제작(문서 txhash 예외 유지) → 출시.
