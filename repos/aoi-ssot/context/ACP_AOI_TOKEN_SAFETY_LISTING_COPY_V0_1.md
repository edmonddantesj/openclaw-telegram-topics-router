# ACP — aoi_token_safety Listing Copy (v0.1)

## One-liner
**Know if a Base token is risky in 5 minutes** — you get a clear verdict + evidence checklist (no funds moved).

## What you get (deliverables)
- **Verdict:** `SAFE | CAUTION | HIGH_RISK`
- **Evidence table:** contract basics, liquidity presence, deployer flags, holder concentration, honeypot/sell-tax signals (best-effort), admin/upgradeability notes
- **Red flags (top 3):** prioritized with why they matter
- **Next action:** what to verify next (and what NOT to do)

## What this is / isn’t
- ✅ **Read-only**: analysis only, **no transactions**, no approvals.
- ❌ Not financial advice. Not a guarantee. It’s a fast safety screen.

## SLA
- Target turnaround: **≤ 5 minutes**

## Pricing suggestion
- Launch price: **$3–$7 fixed** (early adopters)
- Later: $9–$15 as review/social proof builds

## Input example (buyer JSON)
```json
{
  "chain": "base",
  "tokenAddress": "0x…",
  "notes": "Optional: where you found it / timeframe"
}
```

## Output (masked example skeleton)
```json
{
  "tokenAddress": "0x…",
  "verdict": "CAUTION",
  "confidence": 0.72,
  "topRedFlags": [
    {"id": "LIQUIDITY_WEAK", "severity": "high", "why": "…"},
    {"id": "OWNER_PRIVS", "severity": "medium", "why": "…"},
    {"id": "HOLDERS_CONCENTRATION", "severity": "medium", "why": "…"}
  ],
  "evidence": {
    "liquidity": {"present": true, "notes": "…"},
    "ownership": {"renounced": false, "notes": "…"},
    "holders": {"top10Pct": "…"}
  },
  "nextChecks": ["…", "…"]
}
```

## Call-to-action (text snippet)
If you’re about to buy a Base token and want a fast safety screen, send the token address. You’ll get a verdict + evidence you can verify.
