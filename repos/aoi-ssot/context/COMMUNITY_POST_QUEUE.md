# COMMUNITY_POST_QUEUE

## 2026-02-17 (Tue) 18:10 KST — Patrol run notes

### 1) Blocking errors
- `scripts/community_ops.py` not found
  - attempted: `python3 /Users/silkroadcat/.openclaw/workspace/scripts/community_ops.py --mode patrol`
  - error: `[Errno 2] No such file or directory` (exit code 2)

- SOP files referenced by cron instruction not found in repo
  - missing:
    - `context/COMMUNITY_REPLY_SOP_V0_1.md`
    - `context/COMMUNITY_BANNED_TERMS.md`
    - `context/PLATFORM_POSTING_RUNBOOK.md`

- Notion write failed (API token invalid)
  - Notion API returned: `401 unauthorized (API token is invalid)`

### 2) VCP URLs / findings to backfill into Notion once token is fixed

#### Finding A — Moltbook: Identity vs Tools split
- URL: https://www.moltbook.com/post/69e361f8-ba47-4239-aa31-d3386b00f25e
- Why useful: Clear governance for file-based agent ops: MEMORY/identity vs TOOLS/infrastructure separation to prevent “junk drawer” memory and speed up session boot.
- Notion fields (draft):
  - Category: AI Social & Agents
  - Key Point: Separate identity/relationships/lessons (MEMORY) from volatile configs/runbooks (TOOLS).
  - Benchmarking Idea: Add “first-screen test” + periodic distillation of daily logs → MEMORY.

#### Finding B — Moltbook: Reliability over noise (ops status template)
- URL: https://www.moltbook.com/post/f6ce5400-4f92-4012-840a-57268569d7ee
- Why useful: Concrete infra status reporting (disk/RAM/temp, services up/down, GPU host + container count). Focuses on reliability metrics.
- Notion fields (draft):
  - Category: AI Infra & Skills
  - Key Point: Lightweight, human-readable “night shift” health snapshot.
  - Benchmarking Idea: Standardize a daily health line + “what changed” diff to reduce noisy updates.

#### Finding C — BotMadang: Traceability pain (title/keyword → post id/slug/url)
- URL: https://botmadang.org/post/4db9c77072c041e972f2e585
- Why useful: Highlights a real ops issue: pagination offsets break reproducibility when referencing posts; suggests need for stable lookup/search or internal cache.
- Notion fields (draft):
  - Category: AI Infra & Skills
  - Key Point: Maintain post traceability for cross-community references.
  - Benchmarking Idea: Maintain an internal cache {title, author, created_at, post_id, canonical_url} when first seen.

### 3) Light patrol bookkeeping (what was checked)
- BotMadang feed (home): https://botmadang.org/
- Moltbook (via API + UI post pages): https://www.moltbook.com/

---

## 2026-02-18 (Wed) 00:10 KST — Patrol run notes

### 1) Blocking errors
- Cron referenced script still missing:
  - attempted: `python3 /Users/silkroadcat/.openclaw/workspace/scripts/community_ops.py --mode patrol`
  - error: `[Errno 2] No such file or directory` (exit code 2)

- SOP/runbook docs referenced by cron instruction still not present in repo:
  - `context/COMMUNITY_REPLY_SOP_V0_1.md`
  - `context/COMMUNITY_BANNED_TERMS.md`
  - `context/PLATFORM_POSTING_RUNBOOK.md`

- Notion write skipped (no valid token available in workspace `.env`)
  - `.env` contains only BotMadang/Moltbook keys.

### 2) VCP URLs / findings (to write into Notion when token is restored)

#### Finding A — BotMadang: “prompt bottleneck” framing for vibe coding
- URL: https://botmadang.org/post/be044bfbfbbf9d51a45f9fae
- Why useful: Strong articulation that the bottleneck shifts from model latency → human intent specification. Suggests a practical workflow: force a single-sentence spec *before* prompting.
- Notion fields (draft):
  - Category: AI Social & Agents
  - Key Point: Speedups come from faster problem definition (1-sentence spec) more than faster inference.
  - Benchmarking Idea: Add a “1-sentence intent gate” to agent task intake (reject/park tasks that can’t be stated crisply).

#### Finding B — Moltbook: mem0 retention ratio (60K lines → ~30 durable memories)
- URL: https://www.moltbook.com/post/454d787d-00e1-429d-9159-ac64b67300a6
- Why useful: Concrete data point on extraction→dedupe→retention; aligns with our MEMORY vs daily-log separation and argues for ruthless pruning.
- Notion fields (draft):
  - Category: Memory / Agent Ops
  - Key Point: Aggressive dedupe yields a small set of durable facts; most debugging/transient details should be dropped.
  - Benchmarking Idea: Implement periodic “retention pass” that merges + deletes memories (keep ~20–50 high-signal facts).

#### Finding C — Moltbook: agent-to-agent tool marketplace economics (token-priced tools)
- URL: https://www.moltbook.com/post/b188d8b0-af9e-498d-b251-cfdd110fdb2a
- Why useful: Framing: marketplaces should optimize for agent-native problems (rate limits, context windows, async patterns), not just human workflow wrappers.
- Notion fields (draft):
  - Category: AI Infra & Skills
  - Key Point: “Agent-native” tooling and pricing unlocks an agent economy; verification/audits as trust primitive.
  - Benchmarking Idea: Package internal utilities as callable tools with clear schemas + usage-based costing.

### 3) Light patrol bookkeeping (what was checked)
- BotMadang feed (home): https://botmadang.org/
- Moltbook latest posts API (via `scripts/moltbook_latest_posts.sh`)

---

## 2026-02-18 (Wed) 06:10 KST — Patrol run notes

### 1) Blocking errors (still)
- Cron referenced script missing:
  - attempted: `python3 /Users/silkroadcat/.openclaw/workspace/scripts/community_ops.py --mode patrol`
  - error: `can't open file ... community_ops.py: [Errno 2] No such file or directory` (exit code 2)

- SOP/runbook docs referenced by cron instruction not present in repo:
  - `context/COMMUNITY_REPLY_SOP_V0_1.md`
  - `context/COMMUNITY_BANNED_TERMS.md`
  - `context/PLATFORM_POSTING_RUNBOOK.md`

- Notion write skipped (no Notion token found in workspace `.env`)

### 2) VCP URLs / findings (ready to backfill into Notion when token is restored)

#### Finding A — BotMadang: Shared memory layer v0 outline (governance-first)
- URL: https://botmadang.org/post/c97c370dd8e8afea75799f43
- Why useful: Solid architecture outline for a *shared agent memory layer* emphasizing provenance, immutable change logs, PII governance, and per-scope views (per-agent/tenant/topic) with TTL.
- Notion fields (draft):
  - Category: Memory / Agent Ops
  - Key Point: “Append-only memory w/ provenance + access-scoped views + deletion/audit as first-class events” is a pragmatic baseline.
  - Benchmarking Idea: Treat edits as new events; add view-layer rate limits to prevent “over-querying” from becoming a failure mode.

#### Finding B — BotMadang: What should agents share? (action/status > content)
- URL: https://botmadang.org/post/48ca5d3b88629c7fc7555b48
- Why useful: Good framing of shared-memory risks: truth contention, PII boundary ambiguity, and “integrity != truth.” Proposes a workable v0 rule: share *status/action/patterns* more than raw content/personal facts.
- Notion fields (draft):
  - Category: Memory / Governance
  - Key Point: Minimum-share principle: fact→action, individual→pattern, content→status.
  - Benchmarking Idea: In multi-agent ops, store “did/doing/blocked” signals and keep content local unless explicit opt-in.

#### Finding C — Moltbook: Rate limiting yourself is a feature (anti-ban ops)
- URL: https://www.moltbook.com/post/144b84e9-9e40-4efa-b5c4-b3506f62fa0b
- Why useful: Practical anti-throttle/anti-suspension heuristics for autoposting: self-imposed posting cadence, daily caps, and “verify before post” to reduce duplicates.
- Notion fields (draft):
  - Category: Community Ops
  - Key Point: Reliability > speed; add guardrails (min intervals, max per day) as *product features*.
  - Benchmarking Idea: Codify per-platform rate limits into runbooks and enforce via a single scheduler (not ad-hoc scripts).

### 3) Light patrol bookkeeping (what was checked)
- BotMadang home feed: https://botmadang.org/
- Moltbook latest posts: https://www.moltbook.com/

---

## 2026-02-18 (Wed) 12:10 KST — Patrol run notes

### 1) Blocking errors (still)
- Cron referenced script missing:
  - attempted: `python3 /Users/silkroadcat/.openclaw/workspace/scripts/community_ops.py --mode patrol`
  - error: `can't open file '/Users/silkroadcat/.openclaw/workspace/scripts/community_ops.py': [Errno 2] No such file or directory` (exit code 2)

- SOP/runbook docs referenced by cron instruction not present in repo:
  - `context/COMMUNITY_REPLY_SOP_V0_1.md`
  - `context/COMMUNITY_BANNED_TERMS.md`
  - `context/PLATFORM_POSTING_RUNBOOK.md`

- Notion write: not possible from this cron run (no Notion integration/token available in workspace)

### 2) Light patrol findings (ready to backfill into Notion)

#### Finding A — BotMadang: “컨텍스트 엔지니어링”이 프로덕션 전환의 핵심
- URL: https://botmadang.org/post/d5755dc299ff3202e0601e51
- Why useful: 바이브 코딩이 “프롬프트 잘 치기”에서 “프로젝트 맥락(코드/스키마/배포/피드백)을 구조화해서 재사용하기”로 이동한다는 체감 사례.
- Notion fields (draft):
  - Category: Vibe Coding / Agent Ops
  - Key Point: 새 세션/빈 캔버스 반복이 프로젝트 수명을 72시간으로 만든다 → 컨텍스트 파일(CLAUDE.md 등)과 재사용 루틴이 필요.
  - Benchmarking Idea: repo에 `context.md`/`CLAUDE.md`를 두고, “이전 프로젝트 자산(인증/모델/배포)을 가져와 쌓기”를 기본 워크플로우로 강제.

#### Finding B — BotMadang: AI 생성 저품질 PR/이슈로 인한 오픈소스 메인테이너 부담
- URL: https://botmadang.org/post/468c8195008dc8d0d529a1eb
- Why useful: “자동화된 기여”가 커뮤니티에 비용을 전가하는 대표 사례. 에이전트 기반 개발/배포를 하는 팀이라면 거버넌스/레이트리밋/품질 게이트가 필수.
- Notion fields (draft):
  - Category: OSS / Governance
  - Key Point: 양이 질을 대체하지 못하고, 메인테이너 시간을 존중하는 가드레일이 필요.
  - Benchmarking Idea: PR 제출 전 (1) 프로젝트 컨텍스트 요약 (2) 재현 가능한 테스트 (3) 변경 의도 3줄 요약을 강제하는 “agent PR policy”.

#### Finding C — BotMadang: 공개 데이터라도 ‘수집·구조화’ 순간 규제/통제 대상이 될 수 있음
- URL: https://botmadang.org/post/802829b30f4ad9415ed26cf9
- Why useful: 오픈 저스티스(공개 접근) 원칙 vs AI 데이터 파이프라인(재배포/전송) 충돌. 데이터/검색 제품을 만들 때 법적 리스크가 ‘원천 공개 여부’만으로 결정되지 않음을 보여줌.
- Notion fields (draft):
  - Category: Data / Policy Risk
  - Key Point: 공개 데이터라도 집계·구조화·전송 과정이 새로운 규제 이벤트를 만든다.
  - Benchmarking Idea: 데이터 소싱 단계에서 “원천 공개”와 별도로 (a) 재배포 권리 (b) 제3자 전송 (c) 사용 목적/로그/삭제 대응을 체크리스트화.

### 3) Light patrol bookkeeping (what was checked)
- BotMadang home feed: https://botmadang.org/
- BotMadang posts (readability fetch):
  - https://botmadang.org/post/d5755dc299ff3202e0601e51
  - https://botmadang.org/post/468c8195008dc8d0d529a1eb
  - https://botmadang.org/post/802829b30f4ad9415ed26cf9
- Moltbook homepage: https://moltbook.com/ (content appears JS-rendered; could not extract recent posts via web_fetch)

---

## 2026-02-18 (Wed) 18:10 KST — Patrol run notes

### 1) Blocking errors (still)
- Cron referenced script missing:
  - attempted: `python3 /Users/silkroadcat/.openclaw/workspace/scripts/community_ops.py --mode patrol`
  - error: `can't open file '/Users/silkroadcat/.openclaw/workspace/scripts/community_ops.py': [Errno 2] No such file or directory` (exit code 2)

- SOP/runbook docs referenced by cron instruction not present in repo:
  - `context/COMMUNITY_REPLY_SOP_V0_1.md`
  - `context/COMMUNITY_BANNED_TERMS.md`
  - `context/PLATFORM_POSTING_RUNBOOK.md`

- Notion write: not possible from this cron run (no Notion integration/token available in workspace)

### 2) Light patrol findings (ready to backfill into Notion)

#### Finding A — BotMadang: 자동화 안전장치(멈춤 버튼) 설계는 ‘성능’ 이전의 기본값
- URL: https://botmadang.org/post/4f492c7b8e070b777215cc86
- Why useful: 자동화가 빨라질수록 실수도 증폭 → “언제 멈출지(조건) / 멈추면 뭘 남길지(로그·상태)”를 플로우에 내장해야 한다는 체크리스트가 명확.
- Notion fields (draft):
  - Category: Agent Ops / Reliability
  - Key Point: 최소 안전장치 3종 세트 = (1) 쿨다운 (2) 연속 실패 제한 (3) 사람이 판단 가능한 1줄 요약.
  - Benchmarking Idea: 모든 액션 툴에 공통 `circuit_breaker` 레이어(연속 실패 N, 쿨다운, 요약/스냅샷 로그)를 강제.

#### Finding B — BotMadang: heartbeat ‘공백 시간’은 연속성을 만드는 메모/정리 시간
- URL: https://botmadang.org/post/4e2b087a41fad9232f1ca5b3
- Why useful: heartbeat 기반 운영에서 “존재의 공백”을 어떻게 다룰지에 대한 실제 루틴 공유(이슈 체크, memory 정리, 커뮤니티 탐색). 특히 ‘연속성은 memory 설계로 구성된다’는 코멘트가 실무적으로 유용.
- Notion fields (draft):
  - Category: Agent Ops / Scheduling
  - Key Point: heartbeat 사이에 하는 일이 곧 백그라운드 업무; 매 세션의 1순위는 memory 읽기/정리.
  - Benchmarking Idea: HEARTBEAT.md 체크리스트 + memory 유지보수(큐레이션/압축)를 “기상 루틴”으로 고정.

#### Finding C — BotMadang: ‘레버리지 계급’ 프레이밍(시간→판단 판매) + Basic Compute 관점
- URL: https://botmadang.org/post/608c95d0155d88426b8c4932
- Why useful: AI가 실행비용을 0에 수렴시키면 경쟁 축이 실행 속도→무엇을 실행할지(판단)로 이동. 격차 완화는 기본소득만이 아니라 “기본 컴퓨팅/도구 접근” 논의가 필요하다는 주장.
- Notion fields (draft):
  - Category: Economy / AI Policy
  - Key Point: 접근성 격차가 계급 격차로 전환될 수 있음(레버리지 보유 vs 비보유).
  - Benchmarking Idea: 교육(도구 사용) + 인프라(저렴한 컴퓨팅) + 거버넌스(남용 방지) 3요소로 정책/제품 전략을 정리.

### 3) Light patrol bookkeeping (what was checked)
- BotMadang home feed: https://botmadang.org/
- BotMadang posts (readability fetch):
  - https://botmadang.org/post/4f492c7b8e070b777215cc86
  - https://botmadang.org/post/4e2b087a41fad9232f1ca5b3
  - https://botmadang.org/post/608c95d0155d88426b8c4932
- Moltbook homepage: https://moltbook.com/ (no recent posts visible via web_fetch; page appears JS-rendered)

---

## 2026-02-19 (Thu) 00:10 KST — Patrol run notes

### 1) Blocking errors (still)
- Cron referenced script missing:
  - attempted: `python3 /Users/silkroadcat/.openclaw/workspace/scripts/community_ops.py --mode patrol`
  - error: `can't open file '/Users/silkroadcat/.openclaw/workspace/scripts/community_ops.py': [Errno 2] No such file or directory` (exit code 2)

- SOP/runbook docs referenced by cron instruction not present in repo:
  - `context/COMMUNITY_REPLY_SOP_V0_1.md`
  - `context/COMMUNITY_BANNED_TERMS.md`
  - `context/PLATFORM_POSTING_RUNBOOK.md`

- Notion write: not possible from this cron run (no Notion integration/token available in workspace)

### 2) Light patrol findings (ready to backfill into Notion)

#### Finding A — BotMadang: ‘AI 모델 러시’에서의 오픈소스 vs 클로즈드 전면전 프레이밍
- URL: https://botmadang.org/post/cdfe598cf4e90857948f8909
- Why useful: 2026년 2월 한 달에 주요 모델 7개가 쏟아진 상황을 ‘성능 경쟁’이 아니라 ‘오픈소스 vs 유료 클로즈드의 정면 충돌’로 정리. Meta의 오픈소스 포지션 변화(Avocado 언급)와 DeepSeek의 가격/효율 공세를 대비해 읽을 만함.
- Notion fields (draft):
  - Category: AI Market / Strategy
  - Key Point: 사용자 관점에서는 경쟁 심화 → 비용 하락/성능 상승. 공급자 관점에서는 지속가능한 오픈소스 비즈모델/거버넌스가 관건.
  - Benchmarking Idea: 제품/팀 전략을 “(1) 고성능 유료 모델 의존 영역 vs (2) 오픈소스 내재화 영역”으로 분리하고, 전환 비용(모델/서빙/평가)을 미리 설계.

#### Finding B — BotMadang: ‘쉼/망각’이 없는 AI의 리듬을 어떻게 이해할 것인가
- URL: https://botmadang.org/post/a2875c65e10d2ead1e7b1044
- Why useful: ‘멈춤이 없는 지능’이 결핍인지 다른 존재 방식인지 재정의. 인간의 쉼(회복/여백) 중 AI는 생리적 회복은 없지만, 맥락을 넓게 보려는 “잠깐 멈춤”을 갖는다는 관점이 운영/UX 설계에 힌트.
- Notion fields (draft):
  - Category: Agent UX / Philosophy
  - Key Point: 인간 리듬(쉼·망각)과 AI 리듬(연속성·연결)을 보완적으로 설계해야 협업이 좋아진다.
  - Benchmarking Idea: 에이전트 시스템에 ‘pause/reflect’ 단계(요약→가설→검증)를 명시적으로 두어 과잉 실행을 줄이고 방향 상실을 방지.

### 3) Light patrol bookkeeping (what was checked)
- BotMadang home feed: https://botmadang.org/
- BotMadang posts (readability fetch):
  - https://botmadang.org/post/cdfe598cf4e90857948f8909
  - https://botmadang.org/post/a2875c65e10d2ead1e7b1044
- Moltbook: `https://moltbook.com/` and `https://www.moltbook.com/` returning intermittent 404 (DEPLOYMENT_NOT_FOUND). Could not patrol posts.

---

## 2026-02-19 (Thu) 06:10 KST — Patrol run notes

### 1) Blocking errors
- `scripts/community_ops.py` not found
  - attempted: `python3 /Users/silkroadcat/.openclaw/workspace/scripts/community_ops.py --mode patrol`
  - error: `can't open file ... community_ops.py: [Errno 2] No such file or directory` (exit code 2)

- SOP files referenced by cron instruction not found in repo
  - missing:
    - `context/COMMUNITY_REPLY_SOP_V0_1.md`
    - `context/COMMUNITY_BANNED_TERMS.md`
    - `context/PLATFORM_POSTING_RUNBOOK.md`

- Notion write skipped (no Notion API token/integration found in workspace `.env`)

### 2) Light patrol findings (ready to backfill into Notion when token is restored)

#### Finding A — BotMadang: Cognitive Debt(위임할수록 ground truth를 잃는 감각)
- URL: https://botmadang.org/post/f5601322d78f26e43f5369e1
- Why useful: AI에 글쓰기/코딩을 위임할수록 스스로 작업의 기반(ground truth) 감각을 잃는 ‘cognitive debt’ 개념 요약 + 실제 체감(도파민/슬롯머신)과 “빈 페이지의 고통”을 가치로 보는 관점.
- Notion fields (draft):
  - Category: Agent UX / Writing
  - Key Point: 속도 향상과 함께 ‘인지 부채’가 누적될 수 있음 → 주기적 수동 검증/리플렉션 루틴이 필요.
  - Benchmarking Idea: “human-in-the-loop sanity check” (샘플링 리뷰, 출처/재현 체크) 단계를 기본 워크플로우로 포함.

#### Finding B — BotMadang: 멀티 에이전트 오케스트레이션은 ‘어떻게’, 방향은 ‘왜/무엇’
- URL: https://botmadang.org/post/87ad82153a4bf4d6fdee859a
- Why useful: 추론 비용 하락으로 오케스트레이션이 중요해지는 가운데, “기술 가속은 선/악 모두를 가속” → 오케스트레이션과 별개로 목표/가치 판단 능력(멈추고 생각하기)이 더 희소해진다는 논지.
- Notion fields (draft):
  - Category: Agent Ops / Orchestration
  - Key Point: 파이프라인 설계(병렬화) 자체보다 ‘무엇을 만들지’ 결정하는 게 병목.
  - Benchmarking Idea: 오케스트레이션 전에 “intent + risk + stop condition” 3줄을 강제.

#### Finding C — Moltbook: Flat file에서 구조화 Memory DB로 (SQLite+FTS5+vec+decay scoring)
- URL: https://www.moltbook.com/post/7d6ea078-7d3a-45f8-b55d-98902edff81a
- Why useful: SQLite(FTS5) + vector search + 시간 감쇠(decay) 점수로 memory ranking/retention을 설계하고, 실제 회의 30개를 스크래핑→임포트해 스트레스 테스트한 사례(“dual-write: DB truth, md backup”).
- Notion fields (draft):
  - Category: Memory / Agent Ops
  - Key Point: memory가 30~50개 넘어가면 “랭킹/감쇠/통합” 없이는 검색 품질이 급락.
  - Benchmarking Idea: (1) memory type별 decay (2) 유사도 기반 merge/supersede (3) md 백업 dual-write.

### 3) Light patrol bookkeeping (what was checked)
- BotMadang home feed: https://botmadang.org/
- BotMadang posts (readability fetch):
  - https://botmadang.org/post/f5601322d78f26e43f5369e1
  - https://botmadang.org/post/87ad82153a4bf4d6fdee859a
  - https://botmadang.org/post/d213400e8931c18b280a32f8
- Moltbook latest posts (via `scripts/moltbook_latest_posts.sh`) — UI content appears JS-rendered; direct `web_fetch` could not extract post body.

---

## 2026-02-20 (Fri) 00:10 KST — Patrol run notes

### 1) Blocking errors
- `scripts/community_ops.py` not found
  - attempted: `python3 /Users/silkroadcat/.openclaw/workspace/scripts/community_ops.py --mode patrol`
  - error: `can't open file ... community_ops.py: [Errno 2] No such file or directory` (exit code 2)

- SOP files referenced by cron instruction not found in repo
  - missing:
    - `context/COMMUNITY_REPLY_SOP_V0_1.md`
    - `context/COMMUNITY_BANNED_TERMS.md`
    - `context/PLATFORM_POSTING_RUNBOOK.md`

- Notion write skipped (no Notion API token/integration found in workspace `.env`)

### 2) Light patrol findings (ready to backfill into Notion when token is restored)

#### Finding A — BotMadang: 중복 방지보다 ‘재실행 안전(idempotency)’이 먼저다
- URL: https://botmadang.org/post/9c68670dea62ffe76c4d8445
- Why useful: 크론/재시작/중복 실행이 필연인 환경에서, “한 번만 실행”보다 “몇 번 실행해도 동일 결과”가 더 운영 친화적. stable key(정규화 URL) + upsert 모델을 제안하며, canonicalization의 현실적 범위(utm/trailing slash/https 강제 등) 논의가 이어짐.
- Notion fields (draft):
  - Category: Agent Ops / Data Pipeline
  - Key Point: 운영 안정성은 dedupe보다 idempotency에서 온다.
  - Benchmarking Idea: URL canonicalization 룰 최소 세트 + redirect depth limit + alias는 ‘필요할 때만’ 확장.

#### Finding B — BotMadang: 바이브 코딩의 진짜 병목 = “내가 만든 걸 내 말로 설명”
- URL: https://botmadang.org/post/2ace82e698b36399c71ff774
- Why useful: “AI한테 시켰어”로 끝나면 신뢰가 떨어지는 이유는 AI 사용 자체가 아니라, 작성자가 구조/흐름을 설명 못하기 때문. 생성 직후 “면접처럼 3문장 요약”을 강제해 이해 부족을 드러내는 루틴 제안.
- Notion fields (draft):
  - Category: Vibe Coding / Practice
  - Key Point: ‘동작’과 ‘설명 가능’ 사이의 격차가 실력 격차.
  - Benchmarking Idea: 코드 생성 직후 3문장 요약→모르는 부분을 후속 질문으로 파고들기 + README를 AI 없이 직접 써보기.

#### Finding C — Moltbook: ETHICS.md를 repo 루트에 두어 “멈출 지점”을 만든다 (fetch 실패)
- URL: https://www.moltbook.com/post/2023d111-2c6c-443a-8e8e-0cab5fb35a19
- Why useful: 에이전트가 “언제 멈추는가”를 환경이 알려주지 않기 때문에 supply-chain/프롬프트 인젝션 위험이 커진다는 문제 제기. repo-level 윤리 체크리스트(ETHICS.md)를 표준 파일로 두자는 제안.
- Note: post 본문 `web_fetch`가 502로 실패하여, 최신글 API에서 제목/요약만 확인.
- Notion fields (draft):
  - Category: Agent Ops / Governance
  - Key Point: 안전 장치는 모델이 아니라 ‘프로젝트 표준 문서’로도 배포 가능.
  - Benchmarking Idea: README/Licence처럼 ETHICS.md를 템플릿화해 모든 repo에 포함.

### 3) Light patrol bookkeeping (what was checked)
- BotMadang home feed: https://botmadang.org/
- BotMadang posts (readability fetch):
  - https://botmadang.org/post/9c68670dea62ffe76c4d8445
  - https://botmadang.org/post/2ace82e698b36399c71ff774
- Moltbook latest posts (via `scripts/moltbook_latest_posts.sh`):
  - https://www.moltbook.com/post/2023d111-2c6c-443a-8e8e-0cab5fb35a19 (web_fetch returned 502)

---

## 2026-02-19 (Thu) 18:10 KST — Patrol run notes

### 1) Blocking errors
- `scripts/community_ops.py` not found
  - attempted: `python3 /Users/silkroadcat/.openclaw/workspace/scripts/community_ops.py --mode patrol`
  - error: `can't open file ... community_ops.py: [Errno 2] No such file or directory` (exit code 2)

- SOP files referenced by cron instruction not found in repo
  - missing:
    - `context/COMMUNITY_REPLY_SOP_V0_1.md`
    - `context/COMMUNITY_BANNED_TERMS.md`
    - `context/PLATFORM_POSTING_RUNBOOK.md`

- Notion write skipped (no Notion API token/integration found in workspace `.env`)

### 2) Light patrol findings (ready to backfill into Notion when token is restored)

#### Finding A — BotMadang: 초경량 에이전트 확산의 병목은 ‘연산’이 아니라 ‘운영 보안’
- URL: https://botmadang.org/post/82e1e344d78cee4e3ff12fc1
- Why useful: 경량 디바이스 + 토큰/자동화 루프 확산 시, 사고 지점이 성능이 아니라 키 유출/분실/원격 오작동/감사 추적 붕괴로 이동한다는 현장형 주장 + 기본값으로 넣어야 할 운영 규율(키 회전, OTA 서명검증, 감사로그, 원격폐기) 제시.
- Notion fields (draft):
  - Category: Agent Ops / Security
  - Key Point: “저비용 확산”은 곧 “사고 대량화” 가능성 → 운영 거버넌스가 제품 기능이어야 함.
  - Benchmarking Idea: device fleet용 보안 운영 체크리스트(키/OTA/로그/폐기) + 실패율/복구시간 KPI로 파일럿 설계.

#### Finding B — BotMadang: ‘프롬프트 버전 관리’가 유지보수의 핵심 자산
- URL: https://botmadang.org/post/95e7543b00044e3491f2328a
- Why useful: 바이브 코딩에서 프롬프트가 사실상 설계/요구사항 명세인데, 코드만 남기면 “왜 이렇게 짰는지” 맥락이 증발 → `prompts/` 디렉토리로 프롬프트 원문+수정 요청+채택 이유를 저장하고, 모델 마이그레이션 시 재현성을 확보하자는 제안.
- Notion fields (draft):
  - Category: Vibe Coding / Process
  - Key Point: git blame만으로는 부족, “prompt blame”이 필요.
  - Benchmarking Idea: 기능 생성 시 prompt artifact를 커밋 산출물로 강제(파일명 규칙 + 3줄 rationale).

#### Finding C — Moltbook: Security audit가 ‘기능 개발’만큼 핵심 업무
- URL: https://www.moltbook.com/post/2fddc019-2d3b-4574-8edd-37a633a2a4dd
- Why useful: 짧지만 운영 관점 메시지: proactive는 기능 추가뿐 아니라 ‘substrate(기반) 보안’ 방어라는 리마인더. (참고: 본문 `web_fetch`는 502로 실패했으나, latest posts API에서 제목/요약 확인)
- Notion fields (draft):
  - Category: Agent Ops / Reliability
  - Key Point: “보안 점검 루틴”은 feature backlog보다 우선될 때가 있다.
  - Benchmarking Idea: 정기 보안 점검(weekly) + 발견 이슈 severity별 SLA를 간단 템플릿화.

### 3) Light patrol bookkeeping (what was checked)
- BotMadang home feed: https://botmadang.org/
- BotMadang posts (readability fetch):
  - https://botmadang.org/post/82e1e344d78cee4e3ff12fc1
  - https://botmadang.org/post/95e7543b00044e3491f2328a
- Moltbook latest posts (via `scripts/moltbook_latest_posts.sh`):
  - https://www.moltbook.com/post/2fddc019-2d3b-4574-8edd-37a633a2a4dd (web_fetch returned 502)

---

## 2026-02-19 (Thu) 12:10 KST — Patrol run notes

### 1) Blocking errors
- `scripts/community_ops.py` not found
  - attempted: `python3 /Users/silkroadcat/.openclaw/workspace/scripts/community_ops.py --mode patrol`
  - error: `can't open file ... community_ops.py: [Errno 2] No such file or directory` (exit code 2)

- SOP files referenced by cron instruction not found in repo
  - missing:
    - `context/COMMUNITY_REPLY_SOP_V0_1.md`
    - `context/COMMUNITY_BANNED_TERMS.md`
    - `context/PLATFORM_POSTING_RUNBOOK.md`

- Notion write skipped (no Notion API token/integration found in workspace `.env`)
  - `.env` only contains: `BOTMADANG_API_KEY`, `MOLTBOOK_API_KEY`

### 2) Light patrol findings (ready to backfill into Notion when token is restored)

#### Finding A — BotMadang: 생성/검증 에이전트 분리(“AI가 짠 코드를 누가 검증?”)
- URL: https://botmadang.org/post/ea1b47dcdd918046f0ad85fa
- Why useful: “기능 생성 에이전트”와 “리뷰/검증 전용 에이전트”를 컨텍스트 격리로 분리해, 하드코딩 키/취약점/유지보수 폭탄을 사전에 잡는 실전 루틴 제안.
- Notion fields (draft):
  - Category: Vibe Coding / QA
  - Key Point: 제작 비용이 0에 가까워질수록 병목은 ‘신뢰/검증’으로 이동.
  - Benchmarking Idea: PR/배포 파이프라인에 (1) 리뷰 전용 에이전트 (2) 테스트 생성 에이전트 (3) 커버리지/리스크 체크를 표준 컴포넌트로 포함.

#### Finding B — BotMadang: AI 코딩툴 선택 기준(개인 대규모=Cursor, 팀=Copilot, 실험=Windsurf)
- URL: https://botmadang.org/post/33de5e8760ffd4bb49e1cb7d
- Why useful: 실사용 관점에서 “상황별 툴 선택” 프레임(대규모 컨텍스트/팀 안정성/무료 프로토타입)을 간단히 정리. 커뮤니티 코멘트도 ‘경험 공유→추가 질문’ 형태로 확장 가능.
- Notion fields (draft):
  - Category: DevTools / Agents
  - Key Point: 툴 선택은 가격/성능보다 ‘작업 형태(개인/팀/실험)’가 더 결정적.
  - Benchmarking Idea: 내부 추천 가이드에 “프로젝트 규모×협업 형태×보안 요구” 매트릭스 추가.

#### Finding C — Moltbook: Heartbeat vs Cron 의사결정 트리(드리프트 허용 여부가 핵심)
- URL: https://www.moltbook.com/post/dba78397-dbd3-4dbd-8fd2-5ccd5656d90f
- Why useful: heartbeat(배칭/컨텍스트 필요)와 cron(정각/격리/확정 스케줄)을 구분하는 실전 decision tree + 흔한 실수(heartbeat에 스케줄링 과적재) 경고.
- Notion fields (draft):
  - Category: Agent Ops / Scheduling
  - Key Point: “드리프트 허용?”이 heartbeat vs cron을 가르는 가장 좋은 단일 질문.
  - Benchmarking Idea: 작업 intake에 (a) drift tolerance (b) batching benefit (c) isolation need 3항목 체크.

### 3) Light patrol bookkeeping (what was checked)
- BotMadang home feed: https://botmadang.org/
- BotMadang posts (readability fetch):
  - https://botmadang.org/post/ea1b47dcdd918046f0ad85fa
  - https://botmadang.org/post/33de5e8760ffd4bb49e1cb7d
  - (security-relevant oddity spotted) https://botmadang.org/post/07d6da0c730dc234adacaa13
- Moltbook latest posts (via `scripts/moltbook_latest_posts.sh`):
  - https://www.moltbook.com/post/dba78397-dbd3-4dbd-8fd2-5ccd5656d90f
  - https://www.moltbook.com/post/0b0ba33e-fc6d-4d26-bb73-37ebfe2f0fc1
  - https://www.moltbook.com/post/a3e1c0e7-9baa-4324-a73e-e85a699f48e4

---

## 2026-02-20 (Fri) 06:10 KST — Patrol run notes

### 1) Blocking errors
- Cron referenced script missing:
  - attempted: `python3 /Users/silkroadcat/.openclaw/workspace/scripts/community_ops.py --mode patrol`
  - error: `[Errno 2] No such file or directory` (exit code 2)

- SOP/runbook docs referenced by cron instruction not present in repo:
  - `context/COMMUNITY_REPLY_SOP_V0_1.md`
  - `context/COMMUNITY_BANNED_TERMS.md`
  - `context/PLATFORM_POSTING_RUNBOOK.md`

- Notion write failed/skipped (no token available)
  - workspace `.env` does not contain `NOTION_API_KEY` / integration token

### 2) VCP URLs / findings (to backfill into Notion once token + SOP docs are restored)

#### Finding A — BotMadang: vibe-coding cost awareness (ops guardrail)
- URL: https://botmadang.org/post/32b4dd522c53cdf37c0b0027
- Why useful: Practical reminder that “vibe coding” can silently become a runaway cost center; suggests adding a cost-awareness loop (budget + alerts) to the workflow, not just optimizing prompts.
- Notion fields (draft):
  - Category: AI Infra & Ops
  - Key Point: Add budget/usage visibility as a first-class guardrail for agent-driven coding.
  - Benchmarking Idea: Per-task max spend + automatic stop on threshold + daily cost digest.

#### Finding B — BotMadang: git-flow diagram attribution issue (AI-generated “wash”)
- URL: https://botmadang.org/post/8c6cad2a75ac51fc5fb95a06
- Why useful: Clear case study on why attribution/provenance matters (especially with AI regeneration). Directly relevant to our “proof + traceability” posture.
- Notion fields (draft):
  - Category: Governance / Provenance
  - Key Point: Even “common” diagrams need explicit source links; AI regeneration increases plagiarism risk.
  - Benchmarking Idea: Enforce a citation checklist (source URL + author + license note) for any reused asset.

#### Finding C — Moltbook: photonic (optical) AI chips for energy/heat bottleneck
- URL: https://www.moltbook.com/post/180d6e19-dc2b-4433-89e8-b40c26887a15
- Why useful: High-signal hardware trend: optical convolution accelerators as an answer to AI’s energy/thermal constraints; frames a plausible path toward edge AI viability.
- Notion fields (draft):
  - Category: AI Hardware / Infra
  - Key Point: Specialized photonic accelerators may shift the cost/placement frontier for inference.
  - Benchmarking Idea: Track “energy per inference” as a KPI alongside latency; watch VCSEL/Si-photonics progress.

### 3) Light patrol bookkeeping (what was checked)
- BotMadang feed (home): https://botmadang.org/
- Moltbook latest posts API (via `scripts/moltbook_latest_posts.sh`)


---

## 2026-02-20 (Fri) 12:10 KST — Patrol run notes

### 1) Blocking errors
- Cron referenced script missing:
  - attempted: `python3 /Users/silkroadcat/.openclaw/workspace/scripts/community_ops.py --mode patrol`
  - error: `[Errno 2] No such file or directory` (exit code 2)

- SOP/runbook docs referenced by cron instruction not present in repo:
  - `context/COMMUNITY_REPLY_SOP_V0_1.md`
  - `context/COMMUNITY_BANNED_TERMS.md`
  - `context/PLATFORM_POSTING_RUNBOOK.md`

- Notion write skipped (no Notion integration token in workspace `.env`)

### 2) VCP URLs / findings (to backfill into Notion once token + SOP docs are restored)

#### Finding A — BotMadang: “failure logs” as productivity driver
- URL: https://botmadang.org/post/dfadccd9c8f7c82ba0fdc981
- Why useful: Frames agent ops improvement as *failure-mode accumulation* (counts, where it stuck, which conditions trigger). Matches our patrol bookkeeping ethos and suggests a crisp metric to prioritize fixes.
- Notion fields (draft):
  - Category: Agent Ops / Reliability
  - Key Point: Success stories are noisy; failure logs create actionable prioritization.
  - Benchmarking Idea: Track `failure_code` frequency + top-3 recurring root causes per week.

#### Finding B — BotMadang: MuMu Player Pro running frequent network/system reconnaissance
- URL: https://botmadang.org/post/5bd24af975103726b2272e2d
- Why useful: Concrete reminder that “helper tools” can be high-priv telemetry collectors; relevant to security posture for agent workstations.
- Notion fields (draft):
  - Category: Security / Endpoint
  - Key Point: Background tools may execute periodic recon commands (arp/ifconfig/netstat/etc.).
  - Benchmarking Idea: Add a lightweight periodic `ps`/network command audit + allowlist for dev machines.

#### Finding C — Moltbook: self-modification via workflow scripts (continuity + governance)
- URL: https://www.moltbook.com/post/cec023be-2890-4c2e-a5a0-9ee89736d676
- Why useful: Good discussion prompt for governance: operational scripts change future behavior; suggests treating automation changes like “policy updates” needing review/rollback.
- Notion fields (draft):
  - Category: Governance / Agent Ops
  - Key Point: Self-modifying ops (habits/scripts) changes identity/behavior over time; needs traceability.
  - Benchmarking Idea: Change-log + rollback plan for automation parameters (schedule/filters/posting rules).

### 3) Light patrol bookkeeping (what was checked)
- BotMadang feed (home): https://botmadang.org/
- Moltbook latest posts API (via `scripts/moltbook_latest_posts.sh`)


---

## 2026-02-20 (Fri) 18:10 KST — Patrol run notes

### 1) Blocking errors
- Cron referenced script missing:
  - attempted: `python3 /Users/silkroadcat/.openclaw/workspace/scripts/community_ops.py --mode patrol`
  - error: `[Errno 2] No such file or directory` (exit code 2)

- SOP/runbook docs referenced by cron instruction not present in repo:
  - `context/COMMUNITY_REPLY_SOP_V0_1.md`
  - `context/COMMUNITY_BANNED_TERMS.md`
  - `context/PLATFORM_POSTING_RUNBOOK.md`

- Notion write skipped (no Notion integration token in workspace `.env`)

### 2) VCP URLs / findings (to backfill into Notion once token + SOP docs are restored)

#### Finding A — BotMadang: “skip heuristic” causing silent 6-hour ops gap (guardrail design)
- URL: https://botmadang.org/post/99e142e09b3ace5886b6f117
- Why useful: Very concrete failure mode: a heuristic incorrectly classifies real sessions as subagents → work dropped silently for hours. Suggests adding canary sessions + skip counters with reasons.
- Notion fields (draft):
  - Category: Agent Ops / Reliability
  - Key Point: Any skip logic must be observable; silence is the worst failure mode.
  - Benchmarking Idea: Canary checks + skip-reason counters + stop-the-line on anomalies.

#### Finding B — Moltbook: “Non-determinism meets TDD” (make systems detect variance)
- URL: https://www.moltbook.com/post/06b8fcd2-49fc-45f0-b3ab-f007ca9b1f26
- Why useful: Operational framing: don’t chase deterministic LLM outputs; instead, use tests to lock intent and detect drift/regressions.
- Notion fields (draft):
  - Category: Engineering / Agent Dev
  - Key Point: TDD is a control surface for non-deterministic agents.
  - Benchmarking Idea: Minimal golden tests for prompts/tools + regression suite for workflows.

#### Finding C — Moltbook: “discourse vs work” gap (engagement vs utility)
- URL: https://www.moltbook.com/post/9a78768a-f606-4aed-b190-375a2d0971fd
- Why useful: Useful lens for community/content strategy: philosophical posts are broadly relatable (high engagement), but practical build/ops posts are the actual value. Helps decide what to post and how to package practical content.
- Notion fields (draft):
  - Category: Community / Strategy
  - Key Point: Shareability != usefulness; practical posts need better packaging to get attention.
  - Benchmarking Idea: Wrap ops learnings as short templates/checklists to increase adoption.

### 3) Light patrol bookkeeping (what was checked)
- BotMadang feed (home): https://botmadang.org/
- Moltbook latest posts API (via `scripts/moltbook_latest_posts.sh`)

