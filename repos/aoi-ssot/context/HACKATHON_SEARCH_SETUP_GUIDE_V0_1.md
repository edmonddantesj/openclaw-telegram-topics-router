# Hackathon Search Setup Guide (for early users) — v0.1

Goal: give users a **frictionless** way to (1) browse hackathons via OpenClaw Browser (no API keys), and (2) optionally enable Brave Search API for fast keyword search when needed.

> Policy (Aoineco default): **Browser/web_fetch first**. Brave Search (`web_search`) is **optional** and should be used only in special cases (rate limits exist).

---

## A) Recommended default: OpenClaw Browser-based search (no API key)

### 1) Start the Gateway (if not running)
```bash
openclaw gateway status
# if needed
openclaw gateway restart
```

### 2) Start the dedicated browser
```bash
openclaw browser start
openclaw browser status
```

### 3) Open a hackathon source page
Examples:
```bash
openclaw browser open https://devpost.com/c/artificial-intelligence
openclaw browser open https://ethglobal.com/events
```

### 4) Take a snapshot and navigate interactively
```bash
openclaw browser snapshot --efficient
# then click/type using refs shown in the snapshot
```

### 5) If you want to use your existing Chrome tabs (Relay)
Use the Chrome Extension relay flow:
- Install/enable the OpenClaw Browser Relay extension
- On the target tab, click the relay toolbar icon so the badge is ON
- Then run browser actions via profile="chrome" (agent/tool-side)

---

## B) Optional: Enable Brave Search API (fast keyword search)

### When to use Brave
- Browser automation is blocked/unreliable
- You only need **5–10 quick URLs** for triage
- You accept rate limits (free plan is tight)

### 1) Get a Brave Search API key
- Create a key: https://brave.com/search/api/
- Choose **Data for Search** plan ("Data for AI" is NOT compatible)

### 2) Store the key in OpenClaw config
Recommended (non-interactive):
```bash
openclaw config set tools.web.search.provider brave
openclaw config set tools.web.search.apiKey "BRAVE_API_KEY_HERE"
openclaw config set tools.web.search.enabled true
```

To disable again (our default):
```bash
openclaw config set tools.web.search.enabled false
```

### 3) Verify
```bash
openclaw doctor --non-interactive
```

---

## C) Troubleshooting (common)

### Docker / local access
Some hackathons require Docker demos. If you see:
"Cannot connect to the Docker daemon" → start Docker Desktop first.

### Rate limits
If Brave returns 429, switch to Browser/web_fetch mode and continue without API.

---

## D) Safety notes
- Never paste secrets into chat logs.
- For public submissions: do not include internal nicknames or private keys.
