# License & Security Check

## License
- Evidence (grep):
 - 미명기 (no obvious license line found in README/SKILL.md via quick grep)

## Security scan (manual + heuristics)
- Network egress:
  -  skills/swarm-kanban/SKILL.md:38:- **HTTP/REST API** - All operations use the SWARM Board API (https://swarm-kanban.vercel.app/api)
 skills/swarm-kanban/SKILL.md:49:curl -X POST https://swarm-kanban.vercel.app/api/agents/register \
 skills/swarm-kanban/SKILL.md:73:curl -X POST https://swarm-kanban.vercel.app/api/teams \
- Secrets handling:
  - token/env persistence hints:
    - 
- Exec/eval/subprocess:
  - 
- Auto-run hooks/cron:
  - 

## Risk tier
- Proposed: TBD (see governance)
- Notes:
  - This file is a quick evidence capture; deeper review required for external-API skills.
