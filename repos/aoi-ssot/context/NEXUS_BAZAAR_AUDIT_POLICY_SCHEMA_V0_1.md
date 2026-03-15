# Nexus Bazaar — audit_policy.json Schema v0.1 (SSOT)

Last updated: 2026-02-20 (KST)
Status: DRAFT
Exposure: OPEN (schema) / STEALTH (sensitive rule tuning)

> Purpose: Make Audit Stall scans reproducible by separating the rule set into a versioned policy file.

---

## 1) File name
- `audit_policy.json`

## 2) Minimal schema
```json
{
  "policy_id": "audit_policy_v0_1",
  "version": "0.1",
  "generated_at": "2026-02-20T13:55:00+09:00",
  "rules": [
    {
      "code": "NETWORK_CALL",
      "severity": "medium",
      "pattern": "\\b(requests\\.|urllib\\.|fetch\\(|http[s]?://)",
      "message": "Potential network access"
    },
    {
      "code": "SHELL_EXEC",
      "severity": "medium",
      "pattern": "\\b(os\\.system\\(|subprocess\\.|child_process|exec\\()",
      "message": "Potential shell execution"
    }
  ],
  "defaults": {
    "tier": "T1",
    "pass_if_no_findings": true,
    "fail_on_severity": ["high"]
  }
}
```

---

## 3) Notes
- This is a **demo policy** for deterministic scanning.
- A real Skill-Guardian would extend this with dependency analysis, sandbox behavior, and rebuild playbooks.

---

## 4) Evidence
- Audit stall demo runner: `scripts/audit_stall_demo_runner.py`
- Artifacts standard: `aoi-core/docs/ARTIFACTS_STANDARD_V0_1.md`
