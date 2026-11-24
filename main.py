#!/usr/bin/env python3
"""Alien Field Notes: The Two Day Earth Review.

Writes one original line: a review of planet Earth left by an alien
tourist. Python stdlib only; deterministic output.
"""

import os

ENTRY = (
    "4/5 stars. The locals scoop their pets' droppings into little bags "
    "and carry them home like trophies. "
    "Would not walk here barefoot."
)

MAX_CHARS = 200


def main():
    if not (1 <= len(ENTRY) <= MAX_CHARS):
        raise SystemExit(
            "entry must be 1-200 characters, got %d" % len(ENTRY)
        )
    if not ENTRY.strip():
        raise SystemExit("entry must not be only whitespace")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
