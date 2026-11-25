#!/usr/bin/env python3
"""Describe Your Ex in One Word — make.fun entry.

Writes a single word describing an ex to /output/entry.txt.
The word: "unsubscribe" — the verdict you give a former partner
the way you give a newsletter you never signed up for: one click,
no reply, gone from the inbox for good.
"""

import os
import sys

WORD = "unsubscribe"

MIN_LEN = 1
MAX_LEN = 111


def validate(word: str) -> bool:
    """The gate: one word, 1-111 chars, no whitespace, valid UTF-8 text."""
    if not (MIN_LEN <= len(word) <= MAX_LEN):
        return False
    if any(ch.isspace() for ch in word):
        return False
    try:
        word.encode("utf-8")
    except UnicodeEncodeError:
        return False
    return True


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")

    word = WORD.strip()
    if not validate(word):
        print("invalid entry word", file=sys.stderr)
        return 1

    data = word.encode("utf-8")
    tmp = path + ".tmp"
    with open(tmp, "wb") as f:
        f.write(data)
    os.replace(tmp, path)

    with open(path, "rb") as f:
        if f.read() != data:
            print("verify failed", file=sys.stderr)
            return 1
    print(word)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
