#!/usr/bin/env python3
"""Alien Field Notes: The Two Day Earth Review.

One original line: an alien tourist's review of planet Earth, written to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when set).

The review is a single observation, reframed the way a visitor would see it:
the locals protect their skin from their own star, then lie under that star
all afternoon on purpose — and still call the trip four stars out of five.
"""

import os
import sys

REVIEW = "Four stars. The locals smear cream on their skin so their own star won't burn them, then lie under it all afternoon on purpose. Would tan again."


def run() -> int:
    text = REVIEW
    if len(text) < 1 or len(text) > 200:
        print(f"review is {len(text)} characters, must be 1-200", file=sys.stderr)
        return 1
    if text != text.strip() or text.strip() == "":
        print("review must not be blank or padded with whitespace", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("review must be a single line", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
