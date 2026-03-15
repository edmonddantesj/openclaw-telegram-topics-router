# License & Security Check

## License
- Evidence (grep):
skills/beancount-skill/README.md:82:- Provides financial **education and analysis**, not licensed financial advice
skills/beancount-skill/README.md:98:## License
skills/beancount-skill/README.md:100:This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.

## Security scan (manual + heuristics)
- Network egress:
  -  skills/beancount-skill/README.md:3:A professional AI assistant skill for personal finance management using plain-text accounting with [Beancount](https://beancount.github.io/docs/index.html) and [Fava](https://beancount.github.io/fava/).
 skills/beancount-skill/README.md:5:**Downloads:** https://github.com/barcia/beancount-skill/releases
 skills/beancount-skill/README.md:6:**Beancount MCP:** https://github.com/barcia/beancount-mcp
- Secrets handling:
  - token/env persistence hints:
    - 
- Exec/eval/subprocess:
  - 
- Auto-run hooks/cron:
  -  skills/beancount-skill/SKILL.md:222:5. Suggest periodic review schedule

## Risk tier
- Proposed: TBD (see governance)
- Notes:
  - This file is a quick evidence capture; deeper review required for external-API skills.
