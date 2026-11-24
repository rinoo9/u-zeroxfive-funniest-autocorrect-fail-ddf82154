#!/usr/bin/env python3
"""Funniest Autocorrect Fail — make.fun entry.

One line, at most 199 characters, that reads as a funny autocorrect fail
and nothing else. Printed to stdout and written to /output/entry.txt,
as the bounty rules require.
"""

import os

ENTRY = (
    "I meant to text my boss 'Sounds good, thanks!' but autocorrect "
    "sent 'Sounds good, thongs!' — HR just scheduled a meeting about "
    "my wardrobe."
)

MAX_CHARS = 199


def main() -> None:
    if not ENTRY.strip():
        raise SystemExit("entry must not be empty")
    if len(ENTRY) > MAX_CHARS:
        raise SystemExit(f"entry is {len(ENTRY)} chars, over the {MAX_CHARS} limit")
    if len(ENTRY.splitlines()) != 1:
        raise SystemExit("entry must be a single line")
    print(ENTRY)
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    try:
        os.makedirs(out_dir, exist_ok=True)
        with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
            f.write(ENTRY)
    except OSError:
        pass


if __name__ == "__main__":
    main()
