# AOI Squad Orchestrator Pro — Concept (v0.1)

Status: Draft SSOT (local). Purpose: turn `aoi-squad-orchestrator-lite` (presets+pseudonyms+JSON) into a **proof-first orchestration OS**.

## 0) What we found (Lite SSOT)
Source: ClawHub skill `aoi-squad-orchestrator-lite` (latest 0.1.1)
- 3 presets (each 3 roles)
- stable pseudonyms + rename
- single fixed JSON report schema per run
- explicit non-goals: no posting/crawling/wallets

## 1) Pro one-liner
**Orchestrate multi-agent work as approve → run → proof, with governance gates and an auditable task lifecycle.**

## 2) Category positioning (anti-clone)
- Not “agent personality / soul building”.
- Not a generic agent framework.
- It’s an **Ops OS for teams**: reproducible runs + evidence + review gates.

## 3) Core workflow (Pro)
### Lifecycle
Inbox → Spec → Build → Review → Done
- Every stage emits artifacts.
- Orchestrator never marks Done without proof.

### Governance tiers
- L1: safe planning + reporting
- L2: operational changes within guardrails (queue ops, templates, routing)
- L3: irreversible actions (funds/secrets/external publishing)

## 4) Pro capabilities (delta vs Lite)
1) **Run IDs + Proof Bundles (mandatory)**
   - For each `aoi-squad run`, generate:
     - `proof.json` (aoi.proof.v0.1)
     - `sha256sum.txt`
     - `artifacts/` (role outputs, decision notes, diffs)
     - `public_safe_scan.txt`
2) **Role outputs are first-class artifacts**
   - Planner/Builder/Reviewer each produce structured output.
   - Reviewer must sign off (or produce dissent).
3) **Queue + promotion pipeline**
   - Persistent queue with states + timestamps.
   - `promote` step moves items to Done only with evidence.
4) **Model/agent dispatch integration (optional)**
   - Integrate with Dispatcher (model) + Squad Dispatch (agent routing) for cost/quality control.
5) **Notion SSOT sync (optional but recommended)**
   - Create a Notion page per task run with:
     - status, links, proof paths, and summary.

## 5) Public-safe vs internal
- Public-safe: pseudonyms, masked artifacts, no secrets.
- Internal: may include deeper logs, but always redacted before publishing.

## 6) MVP (2-week) for Pro
- Command surface:
  - `aoi-squad run --preset ... --task ... --proof-dir ...`
  - `aoi-squad queue add/list/promote`
- Deliverables:
  - 10-minute Quickstart
  - 1 pinned proof bundle demo
  - 1 daily digest (Telegram) summarizing runs

## 7) Next actions
1) Pull the full Lite JSON schema from `skill.js` and freeze it as Pro input/output contract.
2) Add proof bundle emission to `aoi-squad run`.
3) Decide SSOT target: Notion DB row per task vs page-per-task.
