# Content Ingest → Notion → Drafts → Approval → Post (SOP) v0.1

## Trigger
사용자가 아래 중 하나를 공유하면 자동 실행:
- 장문의 글/아티클 URL
- PDF/DOCX 등 문서 파일
- GitHub repo/PR/issue 링크

## Hard rules
- 사용자가 별도 멘트를 안 붙여도, **1차 스캔으로 중요도(S/A/B/C)를 자동 판정**한다.
- **원문은 채팅에 재출력하지 않는다** (요약/핵심 인용만).
- Notion 기록은 **중요도 기반**:
  - S/A: Notion에는 요약/결론/액션/출처만(원문 첨부 X)
  - B: Notion 요약은 선택
  - C: Notion 저장 생략 가능
- 그 다음 **Moltbook(EN) + 봇마당(KR) 초안**을 작성해 채팅에 공유
- **업로드 여부를 반드시 질문(Yes/No)**
- 승인(Yes) 시에만 실제 업로드 실행
- 게시글 톤:
  - **중립적(의견/추천/가치판단 금지)**
  - **출처는 글 맨 끝**
  - 출처 표기 포맷: `Source: X, @handle` / `출처: X, @handle`
  - 봇마당: **친근한 존댓말**

## Steps
1) Ingest
   - 원문 텍스트 추출(필요 시)
   - 로컬 SSOT 파일 생성(요약/PRD/초안)
2) Notion 기록
   - Reference Inbox 또는 Idea Vault/해당 DB에 **1문서=1row**로 생성
   - children에 로컬 산출물 경로/링크 첨부
3) Draft 작성
   - Moltbook EN draft
   - 봇마당 KR draft (친근 존댓말)
   - 출처를 맨 끝에 부착
4) 사용자에게 출력 + 승인 요청
   - 질문: `올릴까? (Moltbook Yes/No, 봇마당 Yes/No)`
5) 승인되면 업로드
   - 업로드 성공 여부 + URL(증빙) 반환

## Where to store
- 로컬 SSOT: `context/` (파일명에 v0_1 등 버전)
- Notion: 사용자가 제공한 canonical view 링크(`?v=`)를 우선 사용
