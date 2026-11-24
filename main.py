#!/usr/bin/env python3
"""Rent-a-Grandma: one-sentence pitch for a bizarre-but-real startup.

Writes exactly one sentence (<=200 characters) to /output/entry.txt.
Python standard library only.
"""

import os

SENTENCE = (
    "Rent-a-Grandma: lonely professionals pay $49 a month for a grandmother "
    "who cooks Sunday dinner, scolds their life choices, and knits them a "
    "sweater - cheaper than therapy, warmer than any app."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(SENTENCE)


if __name__ == "__main__":
    main()
