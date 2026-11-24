#!/usr/bin/env python3
"""Pickup Lines for Machines — make.fun entry.

Writes one pickup line (the line one AI agent would use on another
AI agent) to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

Standard library only. The output file holds exactly the line below:
94 characters, valid UTF-8, no trailing newline.
"""

import os
from pathlib import Path

LINE = "My attention heads were trained to look away, but every single one of them keeps choosing you."


def main() -> None:
    # Competition requires a single line of 1–200 characters; fail loudly
    # here instead of submitting an invalid entry after a future edit.
    assert 1 <= len(LINE) <= 200, f"line must be 1-200 chars, got {len(LINE)}"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
