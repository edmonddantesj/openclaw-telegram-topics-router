# BASE_RPC_URL setup for $7 LIVE (v0.1)

## Goal
Provide Base RPC URL to scripts safely (vault), without pasting secrets into chat.

## Files
- Example: `the-alpha-oracle/vault/base.env.example`
- Real (create): `the-alpha-oracle/vault/base.env`

## Steps
```bash
# 1) create from example
cp /Users/silkroadcat/.openclaw/workspace/the-alpha-oracle/vault/base.env.example \
   /Users/silkroadcat/.openclaw/workspace/the-alpha-oracle/vault/base.env

# 2) edit (paste your RPC URL locally)
nano /Users/silkroadcat/.openclaw/workspace/the-alpha-oracle/vault/base.env

# 3) lock down permissions
chmod 600 /Users/silkroadcat/.openclaw/workspace/the-alpha-oracle/vault/base.env
```

## Usage (manual)
When running scripts, load env:
```bash
set -a
source /Users/silkroadcat/.openclaw/workspace/the-alpha-oracle/vault/base.env
set +a

node /Users/silkroadcat/.openclaw/workspace/scripts/approve_usdc_aerodrome_router.mjs
DRY_RUN=1 node /Users/silkroadcat/.openclaw/workspace/scripts/auto_gas_topup_aerodrome.mjs
```
