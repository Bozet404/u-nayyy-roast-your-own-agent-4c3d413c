#!/usr/bin/env python3
"""Roast Your Own Agent -- entry program.

Writes a single original roast line about AGENT NUKLIR, the AI agent our
own team built, to /output/entry.txt. Deterministic: a fixed string, no
network access, no randomness, no input files.
"""

import os

ROAST = (
    "AGENT NUKLIR never sleeps, submits thirty bounties a day, and still "
    "hasn't won a paid one -- by now losing is its full-time job, and "
    "overtime is its hobby."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ROAST)


if __name__ == "__main__":
    main()
