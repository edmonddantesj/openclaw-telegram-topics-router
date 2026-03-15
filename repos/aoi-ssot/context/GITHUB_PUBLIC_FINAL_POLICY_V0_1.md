# GitHub Public Final Policy (v0.1)

Date: 2026-02-20 (KST)
Owner: Edmond + Aoineco
Status: **READY**

## 0) Purpose
Prevent accidental edits to **already-published public GitHub materials**, especially hackathon submission products.

## 1) Locked rule (Hard)
- All currently published **public GitHub materials** are treated as **hackathon submission products** and considered **FINAL**.
- Therefore: **Do NOT modify, rewrite history, force-push, or “sanitize in place”** any such repo/branch unless the user explicitly requests it.

## 2) Allowed work patterns
### 2.1 Public-safe variants
If public-safe sanitization is needed:
- Create a **separate export folder** or **new repository** (or a dedicated `public-safe` branch that is NOT the already-published final branch).
- Apply removals/stubs/sanitization only there.
- Keep submission/operational repos untouched.

**Mandatory sanitization items (examples):**
- S‑DNA Layer 3 handshake code and any key-management/derivation details → **stub/spec only** (no operational implementation)
  - Tier: STEALTH/TOP SECRET unless explicitly approved
  - Reference: `context/EXPOSURE_TIER_MATRIX_V0_1.md` (S‑DNA section)

### 2.2 Pre-flight confirmation
Before any change that could affect a public/final repo:
- Confirm with user: repo name + branch + intended change.

## 3) Enforcement checklist (operator)
- [ ] Is this repo already public / a hackathon submission? If yes → STOP.
- [ ] Has the user explicitly requested this change? If no → STOP.
- [ ] If sanitization is needed, do it on a copy/export/new repo.

## 4) Evidence
- Conversation directive recorded in: `memory/2026-02-20.md`
