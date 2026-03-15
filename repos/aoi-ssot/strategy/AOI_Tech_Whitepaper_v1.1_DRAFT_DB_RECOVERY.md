# AOI Core: Architecture of Intelligence (Reference: Nexus Protocol)
## Aoineco & Co. Technology Whitepaper v1.1 (DRAFT_DB_RECOVERY)

**Date:** March 2026  
**Authors:** Aoineco & Co. Multi-Agent Collective  
**Classification:** PUBLIC (OPEN/TEASER only)  
**S-DNA:** AOI-2026-0306-SDNA-WP01-RECOVERY  

---

## Abstract

This version 1.1 update incorporates the **DB-Loss Recovery Architecture** and formalized **L1/L2/L3 Governance** established following the March 2026 infrastructure incident. 

**Aoineco & Co.** presents **AOI Core** — an auditable operating core for agent execution (Policy → Gate → Approval → Proof), now hardened with a distributed, multi-layered state recovery protocol.

---

## 2.3 Governance: The 3-Tier Decision System (Refined)

The March 2026 incident codified the distinction between autonomous operation and human oversight.

**Level 1 — Autonomous (Agent Authority)**
- Routine monitoring, data collection, internal logging.
- No approval required. Agents act independently.

**Level 2 — Chief of Staff (Oracle Authority)**  
- Documentation updates (README/Quickstart), Notion/Index/Digest sync, Idempotency hardening, Local SSOT summarization.
- Oracle (Chung-ryeong) reviews for security and consistency. Executes automatically if within safety parameters.

**Level 3 — Chairman (Human Authority)**
- **Money/Wallets:** Financial commitments, payments, and treasury movements.
- **Keys/Secrets:** Account linking, API key management, and private key access.
- **External Exposure:** Public posts, social media uploads, and irreversible on-chain actions.
- Requires explicit human approval. Immediate request for approval is mandatory upon detection.

---

## 6. Infrastructure: The Hybrid Node Architecture

### 6.2 The State-Guardian & SAVE NOW Protocol

Agent sessions are ephemeral, but **Intelligence** must be durable. We use the **State-Guardian** to ensure continuity.

**The "SAVE NOW" (현재를 저장) Protocol:**
A single command (`scripts/save_now.sh`) triggers a synchronized backup:
1. **Ledger Sync:** Updates the `ledger.json` (The "DB-Lite" SSOT).
2. **Vault Sync:** Pushes markdown files to the `md-vault` repository.
3. **Hard Snapshot:** Creates a `.tar.gz` archive of the current environment state in `artifacts/state_saves/`.

---

## 10. DB-Loss Recovery & Resilience (New Section)

The "DB-Loss" scenario is no longer theoretical. AOI Core implements a 4-layered recovery path to ensure zero-loss of intellectual capital.

### 10.1 Layer 1: The Notion Mirror (Human SSOT)
All high-level decisions, policies, and research are mirrored to a Notion Workspace. A scheduled `notion_mirror_sync.py` creates a local Git-versioned mirror (`edmonddantesj/aoi-notion-mirror`), ensuring that even if the cloud service fails, the structured knowledge survives in Markdown.

### 10.2 Layer 2: The md-vault (Agent SSOT)
The `md-vault` serves as the primary repository for agent-generated documentation, runbooks, and task items. By keeping the "Source of Truth" in Git-managed Markdown files rather than a traditional SQL database, the system gains versioning, branching, and total portability.

### 10.3 Layer 3: The Ralph Loop Ledger (Action SSOT)
The `context/ralph_loop/ledger.json` acts as a lightweight database replacement. It tracks:
- **Task States:** In-progress, todo, backlog, done.
- **Ownership:** Assignments to specific agents (e.g., Blue-Brain, Blue-Record).
- **Proof-Links:** Direct paths to evidence artifacts generated during task execution.

### 10.4 Layer 4: Telegram Topic History (Decision Log)
In cases of total system wipeout, the Telegram topic history (e.g., Topic 585) serves as the immutable "Flight Recorder." Exported logs allow for the reconstruction of the "why" behind decisions, even if the "what" (files) is lost.

---

## 11. Conclusion (§ OPEN)

AOI Core v1.1 proves that resilience is not an addon—it is a core property of the architecture. By treating the workspace as a database and Git as the transaction log, Aoineco & Co. has created a system that can be destroyed and reconstructed without losing its soul.

We don't just ship auditable systems. We ship unkillable ones.

---

**Contact:**  
Aoineco & Co. — Architecture of Intelligence  
Protocol: Nexus v1.1  
S-DNA: AOI-2026-0306-SDNA-WP01-RECOVERY  
