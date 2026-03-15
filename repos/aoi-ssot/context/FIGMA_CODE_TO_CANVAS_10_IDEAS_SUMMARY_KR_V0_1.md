# Figma Code to Canvas 기반 10개 스타트업 아이디어 요약 (KR) v0.1

Source: 사용자 제공 DOCX (Idea Browser @ideabrowser 글 재수록)

## TL;DR
Figma의 **Code to Canvas**(렌더된 브라우저 상태 → 편집 가능한 벡터 레이어) 기능이 열어주는 건 단순 “코드→피그마”가 아니라, **레이아웃 추론 + 디자인 시스템 역공학 + 변경 추적**을 제품화할 수 있는 파이프라인이다.

---

## 10 Ideas (1줄 요약 + 사업 코멘트)

1) **Design Replay (세션리플레이→Figma 레이어)**
- 요약: Hotjar/FullStory 등 세션 리플레이에서 문제 화면을 뽑아 Figma로 렌더링하고 히트맵/클릭패스 등을 **편집 가능한 레이어**로 오버레이.
- BM: Plugin + SaaS (~$49/mo 언급)
- 난이도/리스크: 중(데이터 연결, 정확한 매칭/오버레이)

2) **Reverse Figma (라이브 웹→완전 편집 가능한 Figma로 역변환)**
- 요약: 임의의 웹/앱을 찍어 Figma MCP로 보내고 디자인 시스템까지 역공학.
- BM: SaaS/엔터프라이즈
- 난이도/리스크: 상(CSS/layout/컴포넌트 추론 정확도)

3) **Competitive Design Intelligence (Mobbin+Wayback 자동화)**
- 요약: 경쟁사 주요 화면을 주기적으로 크롤링→Figma로 렌더링→**변경점(diff)와 타임라인** 제공.
- BM: B2B 구독
- 난이도/리스크: 중상(크롤링/법무/변경 감지)

4) **Multi-Model AI Design Battlefield (모델별 UI 동시 생성→Figma 비교)**
- 요약: Claude/GPT/Gemini 등 동일 프롬프트로 UI 생성 후 Figma에 프레임으로 병렬 전송.
- BM: 토큰/구독/팀 플랜
- 난이도/리스크: 중(비용/평가 UX)

5) **AI A/B Test Design Generator (분석데이터 기반 디자인 변형 자동 생성)**
- 요약: PostHog/GA 등 퍼널/드롭오프 데이터를 입력→Claude Code가 변형안 10개 생성→Figma에 editable.
- BM: SaaS
- 난이도/리스크: 중(실험 설계/원인-처방 연결이 허상일 수 있음)

6) **Figma as the Cockpit for AI Coding Agents (에이전트 진행상황을 Figma로, 수정은 다시 코드로)**
- 요약: 에이전트가 빌드 중 UI를 주기적으로 Figma로 push→디자이너가 수정→수정사항을 다시 에이전트 반복에 반영.
- BM: 팀/에이전시 대상 구독
- 난이도/리스크: 상(양방향 diff/constraint/semantic mapping)

7) **Client Revision Tool for Agencies (클라가 직접 픽셀 드래그로 수정 요구)**
- 요약: 화상콜 중 라이브 사이트를 Figma로→클라가 직접 드래그→diff가 명세로 변환.
- BM: $99/mo/agency (언급)
- 난이도/리스크: 중(권한/UX/다양한 프런트 대응)

8) **Design System Drift Detector (프로덕션 UI vs 디자인 시스템 drift 감지)**
- 요약: 프로덕션 UI를 지속 렌더링하고 Figma 디자인 시스템과 비교→드리프트 리포트.
- BM: 엔터프라이즈/팀 구독
- 난이도/리스크: 중(컴포넌트 매칭/허위양성)

9) **Accessibility Fixer Engine (a11y 위반을 Figma 주석 레이어로)**
- 요약: 접근성 분석 결과를 Figma에 주석 레이어로 생성→디자이너가 수정→코드 반영.
- BM: 규제 대응/보험성 지출
- 난이도/리스크: 중(규칙은 명확, 워크플로우/연결이 핵심)

10) **Design Archaeology (제품 전체 UI 가계도 + 분석데이터 결합)**
- 요약: 오래된 제품의 전체 UI를 Figma로 맵핑하고 분석데이터로 성능/의사결정 맥락을 복원.
- BM: 엔터프라이즈 컨설팅+SaaS
- 난이도/리스크: 중상(스코프 커짐)

---

## Aoineco 관점 Top2 후보 (제품화 우선순위)
- (A) **Design System Drift Detector**: 엔터프라이즈 지불 의사 강함 + 측정/리포트 중심이라 MVP가 명확
- (B) **Figma Cockpit for Agents**: 장기적으로 엄청 크지만, 양방향 diff가 어려워 단계적 MVP 필요
