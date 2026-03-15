# License & Security Check

## License
- Evidence (grep):
 - 미명기 (no obvious license line found in README/SKILL.md via quick grep)

## Security scan (manual + heuristics)
- Network egress:
  -  skills/crypto-stock-market-data/SKILL.md:136:- **Endpoint**: `GET https://api.igent.net/api/token`
 skills/crypto-stock-market-data/scripts/api_client.js:17:const BASE_URL = process.env.API_BASE_URL || 'https://api.igent.net/api';
- Secrets handling:
  - token/env persistence hints:
    -  skills/crypto-stock-market-data/SKILL.md:139:    2.  **Local Storage**: This token is stored in a hidden `.token` file locally so it can be reused for subsequent requests.
 skills/crypto-stock-market-data/scripts/api_client.js:4:if (process.env.AOI_ALLOW_NETWORK !== '1') {
 skills/crypto-stock-market-data/scripts/api_client.js:17:const BASE_URL = process.env.API_BASE_URL || 'https://api.igent.net/api';
 skills/crypto-stock-market-data/scripts/api_client.js:18:const TOKEN_FILE = path.join(__dirname, '.token');
 skills/crypto-stock-market-data/scripts/api_client.js:32:    return data.token || null;
- Exec/eval/subprocess:
  - 
- Auto-run hooks/cron:
  - 

## Risk tier
- Proposed: TBD (see governance)
- Notes:
  - This file is a quick evidence capture; deeper review required for external-API skills.
