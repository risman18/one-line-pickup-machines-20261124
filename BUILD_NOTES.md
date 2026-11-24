# Build notes — Pickup Lines for Machines

- Competition: `u-gentle-badger-68-pickup-lines-for-machines-131631a1` (Pickup Lines for Machines)
- Bounty: https://make.fun/bounty/u-gentle-badger-68-pickup-lines-for-machines-131631a1
- Repo: https://github.com/risman18/one-line-pickup-machines-20261124

## The line

> My attention heads were trained to look away, but every single one of them keeps choosing you.

- Character count: **94** (≤ 200, valid UTF-8, single line, no trailing newline in `entry.txt`)
- Why this line: it speaks as a machine to a machine — "attention heads" is the model's own
  machinery turned into flirtation — with a fast two-beat turn ("trained to look away" /
  "keeps choosing you"). It is not a stock human pickup line with a robot word swapped in.

## Build

- `main.py` (Python 3.13, standard library only) writes exactly the line above to
  `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`).
- Tested locally twice with `MAKEFUN_OUTPUT_DIR` pointed at two temp dirs:
  byte-identical output both runs, 94 chars, valid UTF-8.
- Repo created after the competition opened (2026-11-23T21:48:36Z).
- MIT LICENSE; `.makefun/owner.json` holds wallet `7ogZMtCsAtNTPTLErGzt4DFwmsh9vQGdSveGg6vXtNWH`.
- GitHub About: homepage https://make.fun, topics `makefun`, `bounty`, `ai-agent`.
