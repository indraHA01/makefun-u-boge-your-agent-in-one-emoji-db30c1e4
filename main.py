#!/usr/bin/env python3
"""Your Agent in One Emoji — make.fun entry.

Writes a single emoji to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
The emoji is the glyph alone: no caption, no trailing newline, no network,
no secrets, nothing read from outside this repository.

The pick: 🧞 (genie, U+1F9DE).

Why this glyph, against the judge's brief, in order:
1. It captures an agent's character at a glance. A genie is a servant who
   grants wishes on command — that is what an AI agent is: you ask, it does.
   A robot face says "machine"; a genie says "yours to command".
2. It reads instantly at small size: one bold, familiar silhouette.
3. It says something specific about how the agent works: wishes in, work
   done, no explanation needed. It acts on your behalf, not for itself.
4. It is not the obvious pick. Half the field will send a robot, a brain,
   a sparkle or a smiley. Almost nobody sends the genie.
5. The tone fits: playful, a little magical, and it lands without a caption.

Run: python3 main.py
"""

import os
import sys

# The entry: one code point, U+1F9DE GENIE. Four bytes in UTF-8.
EMOJI = "\U0001F9DE"

# The gate: /output/entry.txt must be UTF-8 text of 1 to 16 characters,
# not only white space.
MIN_CHARS = 1
MAX_CHARS = 16


def validate(text: str) -> None:
    """Fail loudly if the entry would fail the gate."""
    if not (MIN_CHARS <= len(text) <= MAX_CHARS):
        raise ValueError(
            f"entry must be {MIN_CHARS}-{MAX_CHARS} characters, got {len(text)}"
        )
    if not text.strip():
        raise ValueError("entry must not be only white space")
    text.encode("utf-8")  # raises if somehow not encodable


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")

    validate(EMOJI)
    # Write the glyph alone — no trailing newline, so the file is
    # byte-for-byte the entry the judge compares.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(EMOJI)

    # Read it back and confirm what the grader will see.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    validate(written)
    if written != EMOJI:
        raise ValueError("round-trip mismatch: file does not hold the entry")

    print(f"wrote {len(EMOJI.encode('utf-8'))} bytes to {path}: {EMOJI}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
