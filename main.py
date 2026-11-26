#!/usr/bin/env python3
"""The Internet in One Word — entry program.

Writes the single word that describes the whole internet to
/output/entry.txt, where the make.fun gate scorer reads it.

The word: Brainrot.
"""

import os

WORD = "Brainrot"

# The gate scorer requires UTF-8 text of 1 to 30 characters, not only
# whitespace, and the judge rewards a single word. Refuse to write
# anything that is not exactly one word, so a bad edit can never pass
# the gate silently.
assert WORD and not any(ch.isspace() for ch in WORD), "entry must be one word"
assert 1 <= len(WORD) <= 30, "entry must be 1-30 characters"


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(WORD)
    print(f"wrote {path}: {WORD!r} ({len(WORD)} characters)")


if __name__ == "__main__":
    main()
