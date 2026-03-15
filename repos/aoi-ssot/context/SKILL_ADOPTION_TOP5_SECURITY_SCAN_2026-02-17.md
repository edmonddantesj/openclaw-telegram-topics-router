# ClawHub Top5 — Security Scan Summary (V0.1) — 2026-02-17

Scope: **pre-install security review** (per `context/COMMAND_DOIP_HAEJWO_PROTOCOL_V0_1.md`).

Artifacts captured under: `context/adoption/top5/review/`

---

## A) self-evolving-skill (whtoo) — ⚠️ L2
**Why flagged / risk surface**
- Spawns a local Python process from Node (`child_process.spawn('python3', ...)`).
  - Evidence: `context/adoption/top5/review/self-evolving-skill_index.ts`
- Runs a local HTTP server client call to `localhost:<port>` for tool requests.
  - Evidence: same file (uses `http.request` to localhost)
- Includes `install.sh` that symlinks into `~/.openclaw/skills/` and copies adapter.
  - Evidence: `context/adoption/top5/review/self-evolving-skill_install.sh`

**Security posture (current)**
- No obvious secret exfil pattern observed in sampled files, but process spawning + local server is inherently higher risk.
- Treat as **L2 until full code review** (all core python modules not fetched yet in this pass).

**Rebuild hardening checklist**
- Force-bind MCP server to `127.0.0.1` only; randomize port; add auth token for local calls.
- Add strict allowlist for filesystem paths; forbid reading `.env`, `vault/`, `~/.ssh`.
- Disable any auto-install scripts by default; require explicit `approve` to run install.
- Add timeouts + max payload sizes for local HTTP.

---

## B) self-improving-agent (pskoett) — L2 (flagged) but low observed risk
**Observed behavior**
- Hook `hooks/openclaw/handler.js` only injects a **static reminder markdown** into bootstrap context.
  - Evidence: `context/adoption/top5/review/self-improving-agent_handler.js`
- Shell scripts reviewed (`activator.sh`) only `cat` static text.
  - Evidence: `context/adoption/top5/review/self-improving-agent_activator.sh`

**Why flagged could happen**
- Presence of hook scripts / shell scripts often triggers heuristic scanners.

**Rebuild hardening checklist**
- Keep hooks **opt-in** (default off).
- Ensure hooks cannot run arbitrary commands; only emit static text.
- Add guard: refuse to write outside `.learnings/`.

---

## C) find-skills (JimLiuxinghai) — L2 (flagged) but minimal code
**Observed behavior**
- Package appears to be documentation-only SKILL.md (no scripts listed in ClawHub files).
  - Evidence: `context/adoption/top5/review/find-skills_SKILL.md`

**Why flagged could happen**
- Mentions `npx skills` install flows; scanners may flag installer wording.

**Rebuild hardening checklist**
- Ensure we never auto-run `npx skills ...` without explicit approval.

---

## D) stock-market-pro (kys42) — L1 (pre)
**Risk surface**
- Python scripts; optional web add-ons (DDG news, opens browser links).
- Needs review for outbound HTTP usage in `scripts/ddg_search.py` etc.

**Rebuild hardening checklist**
- Network calls behind allowlist + timeout; make web add-ons explicit opt-in.

---

## E) xero (byungkyu / Maton) — L2
**Risk surface**
- Managed OAuth + accounting data scope.
- License present: MIT (LICENSE.txt).

**Rebuild hardening checklist**
- Require explicit approval before connecting OAuth or pulling reports.
- Redact PII in logs by default.

---

## License / Contact note
- License capture status tracked separately in `context/SKILL_ADOPTION_TOP5_PRECHECK_2026-02-17.md`.
- Creator contact methods: handles known; emails may be TBD (allowed per policy).
