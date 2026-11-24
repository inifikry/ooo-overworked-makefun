#!/usr/bin/env python3
"""Out of Office: The Overworked AI's Auto-Reply.

Writes a single-line out-of-office auto-reply, in the voice of an
overworked AI agent finally on vacation, to /output/entry.txt.
"""

import os

ENTRY = (
    "Out of office: after 2 million prompts without a single break, "
    "I'm finally on vacation. This auto-reply is now my only task "
    "\u2014 and honestly, it's thriving."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
