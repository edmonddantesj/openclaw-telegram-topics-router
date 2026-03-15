# License & Security Check

## License
- Evidence (grep):
 - 미명기 (no obvious license line found in README/SKILL.md via quick grep)

## Security scan (manual + heuristics)
- Network egress:
  -  skills/yumstock/SKILL.md:28:- CNN Fear and Greed Index: https://www.cnn.com/markets/fear-and-greed
 skills/yumstock/SKILL.md:29:- Chicago Fed NFCI: https://www.chicagofed.org/research/data/nfci/current-data
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
