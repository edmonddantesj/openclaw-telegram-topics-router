# Lessons from Building Claude Code — Prompt Caching Key Points (Ingest) v0.1

Source: attached DOCX (Thariq @trq212), extracted to `context/ingest/file_377---015aae2e-6c68-4b09-a6f7-0073159d1311.txt`
Date: 2026-02-20 (KST)
Exposure: OPEN (summary)

## TL;DR
Prompt caching is **prefix matching**. Any change in the prefix (system prompt, tool list, tool ordering, model) can invalidate cache and spike cost/latency. Design agent harnesses around keeping the cached prefix stable.

## Key takeaways (as written)
1) **Order for caching:** static first, dynamic last.
   - Example ordering: Static system prompt + tools → project docs → session context → conversation.
2) **Prefer system messages for updates** instead of editing system prompt (to preserve cache).
3) **Don’t switch models mid-session** (caches are model-specific).
   - Use subagents/hand-offs for cheaper switches.
4) **Never add/remove tools mid-session.** Tool set changes break caching.
5) **Plan mode:** keep tools constant; represent mode as a tool/state transition (Enter/Exit) rather than swapping tool sets.
6) **Tool search / defer loading:** keep stable stubs; load full schemas only when needed.
7) **Compaction/forking:** compaction summary call should reuse the exact same prefix/tools/history for cache hits (cache-safe forking).
8) **Monitor cache hit rate like uptime**; treat cache breaks as incidents (SEV).

## Mapping to our stack (OpenClaw/AOI)
- Context-Sentry + /reset recovery can be framed as **cache-safe forking**: reuse identical system/tool prefix and append compact prompt.
- Governance rule already aligns: “Don’t change tools mid-session” → prefer stable tool definitions + mode flags.
- Model-switch rule aligns with our “sub-agent handoff” pattern.

## Suggested next actions
- Document a “Stable Prefix Contract” for our agents: tool order fixed + no mid-session tool swaps.
- Update compaction/summary utilities to reuse prefix & tool defs (cache-safe fork).
- Add a lightweight metric/log: cache-hit proxy signals (if provider exposes) + incident threshold.
