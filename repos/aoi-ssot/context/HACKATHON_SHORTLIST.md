# HACKATHON_SHORTLIST.md (SSOT)

> Setup guide (early users): `context/HACKATHON_SEARCH_SETUP_GUIDE_V0_1.md`

이 파일은 "지원/관찰(Watching)" 상태의 해커톤 후보 목록을 관리한다.
- 실제로 빌드/제출 진행하다 멈춘 항목은 `context/TASK_PARKING_LOT.md`로 관리한다.
- 태그 규칙은 `context/TASK_TAG_CANONICALIZATION_V0_1.md`의 canonical map을 따른다.
- 각 항목은 상태(applying|watching|paused|rejected)와 다음 액션을 가진다.

---

## Active (watching/applying)

### Airia AI Agents Hackathon
- Status: watching
- URL: https://airia-hackathon.devpost.com/
- Tracks: Airia Everywhere / Active Agents
- Prize: $7,000 total (per track 1st $2k / 2nd $1k / 3rd $500 + $250 Airia credits)
- Required: demo video max 4 minutes (YouTube/Vimeo) + **publish agent to Airia Community (public)** + include community URL
- Judging: Technological Implementation / Design / Potential Impact / Quality of Idea
- SSOT: `context/AIRIA_HACKATHON_SUMMARY_2026-02-18_V0_1.md`
- Deadline (shown): 2026-03-20 12:45pm (KST)
- Eligibility (shown): age of majority; excludes Brazil, Crimea, Cuba, Iran, North Korea, Quebec, Russia
- Next action: [보류] L3 게이트(공개 게시) 선행 후 Track 2 활성화 결정

### EigenCloud / EigenCompute — Open Innovation Challenge
- Status: applying (P0)
- Deadline: **Feb 20, 11:59pm PT** (from submission form)
- Prize: $10,000 best + EigenCompute credits for top 5
- Constraint: **No tokenized agents**
- Requires: demo link, repo link, and **announcement tweet** (tag @eigencloud)
- Links:
  - Ideas: https://ideas.eigencloud.xyz/
  - Dev portal: https://developers.eigencloud.xyz/
  - Submission form: https://docs.google.com/forms/d/e/1FAIpQLSdjCpocv1HibJOEMLtxBxbxleMOZoUIXSmUOT-B1QSv-7HLPg/viewform?pli=1
- Strategy: **A 먼저 구축(제출 가능 수준)** → 잘 되면 **B까지 확장**
  - A: Verifiable Proof Bundle Runner (proof-first manifest+sha256)
  - B: Verifiable Agent Identity Wrapper (roadmap/optional)
- Next action (today): A 컨셉 one-liner 확정 + EigenCompute hello-world/컨테이너 실행 뚫기 + 데모/레포/트윗 초안


### Amazon Nova AI Hackathon (Devpost)
- Status: watching (P2)
- URL: https://amazon-nova.devpost.com/
- Tracks: UI Automation / Multimodal Agents (Nova ecosystem 중심)
- Prize: 미공개/업데이트 필요
- Reuse fit: Medium-High
  - Our EigenProof Runner는 Proof-first Ops OS + 자동 증빙은 강점
  - 단, Nova FM/Nova Act 같은 플랫폼 종속 기능을 실제로 쓰려면 구현 오버헤드가 있음
- Required (요약):
  - Nova 기반 핵심 기능 적용(Agentic/Multimodal/UI/Voice)
  - 데모 영상 약 3분, Repo/데모 공개
  - 옵션: 블로그 포스트
- Risk / Constraint: 플랫폼 종속성으로 초기 진입 비용이 큼
- Next action: Elastic 먼저 제출해 성과 고정 후 Nova 전용 proof wrapper 시범 구현 여부 결정

### Elasticsearch Agent Builder Hackathon
- Status: watching (P1)
- URL: https://elasticsearch.devpost.com/
- Tracks: Multi-step agent / RAG / tool use
- Prize: 미공개/업데이트 필요
- Reuse fit: Very High (권장 Top1)
  - Squad Pro/오케스트레이션(플래너/실행기/리뷰어) 구조와 자연스럽게 일치
  - Proof Bundle(sha256 + manifest + policy)로 멀티스텝 완료 증빙이 강함
  - 공개 레포/라이선스 요구 대응 가능성 높음
- Required (요약):
  - Elastic Agent Builder + Elasticsearch 기반 multi-step 시스템
  - 데모 영상 ~3분
  - 공개 레포 + 공개 라이선스
- Risk / Constraint: 제출 형식/라이선스 확인 후 템플릿 즉시 맞춤
- Next action: EigenProof Runner를 Elastic Agent Builder 흐름으로 확장한 1-pager 작성 후 1차 제출안 생성

### DevStudio 2026 by Logitech Hackathon
- Status: watching (P3)
- URL: https://devstudiologitech2026.devpost.com/
- Tracks: Logitech ecosystem / app + plugin + 인터랙션
- Prize: 미공개/업데이트 필요
- Reuse fit: Medium
  - 피치/컨셉 제출 부담이 낮아 가성비가 좋음
  - Logitech 하드웨어/SDK 축이라 우리 솔루션 정합성은 중간
- Required (요약):
  - 1분 내외 피치/영상
  - 제품 적합성(웹/UX/SDK/액션) 체크
- Risk / Constraint: 하드웨어/생태 축( MX/Action SDK/Quest ) 중심이라 실제 승산은 중간
- Next action: 운영 관점 컨셉(예: Proof-first 운영 UI/대시보드)으로 파일럿 피치 문구 정리

### BUIDL CTC Hackathon (CTC / Creditcoin / Credit Labs)  
- Aliases: CTC / BUIDL CTC
- Status: watching (P1)
- URL: https://dorahacks.io/hackathon/buidl-ctc/detail
- Deadline: 2026-03-07 23:59 EST (extended)
- Winner announcement: 2026-03-21
- Prize pool: $15,000 (Grand $10k / 2nd $3k / 3rd $2k)
- Tracks: DeFi / RWA / DePIN / Gaming
- Submission requirements (notable): GitHub repo (README required) + deck/whitepaper (PDF URL) + demo video URL + **must be deployed on a testnet** + team member info (bio/role/country)
- Fit hypothesis: DeFi track — proof-first pay-to-deliver commerce primitive (x402 pattern) + evidence bundles
- Next action: decide track + MVP scope; verify Creditcoin testnet deployment steps; create deck template + 60s pitch

### Tempo Hackathon (Tempo x Canteen)
- Status: watching (P1)
- Why: Technical edge candidate (from durable memory priority list)
- Next action: confirm official page + dates + submission requirements

### UiPath AgentHack
- Status: watching
- Next action: confirm current season + track fit

### DeveloperWeek 2026 Hackathon
- Status: watching
- Next action: check themes + submission format

### DoraHacks (x402 & ERC-8004 focus)
- Status: submitted ✅
- Next action: **SKALE 크레딧 지원 신청서 작성/제출** (SKALE 측 요청)
  - Timing: EigenCloud 작업 끝나면 바로

### Sui: Calling All Agents
- Status: applying/active (P1)
- Track assignment (historical): Track 1 Safety=⚔️청검, Track 2 Jarvis=🧿청령(+growth)
- Next action: confirm current deadlines + deliverables

### Virtuals ACP Hackathon
- Status: active (P0)
- Notes: 1 Masterpiece + 9 skills + bait strategy (see memory durable files)
- Next action: confirm required LITE_AGENT_API_KEY + final submission artifacts

### MIDL VibeHack
- Status: paused (PARKED; home-only blocker)
- Where tracked: `context/TASK_PARKING_LOT.md` (tag: `midl-vibehack-home`)
- Blocker: Xverse extension 연결 + 1 on-chain action이 **집/안전환경에서만 가능**
- Next action: 집 도착 시 재개 신호 → tx hash + explorer proof + 데모 영상 확보

---

## Rejected / Archived
- (Add items here when rejected)
