#!/usr/bin/env python3
"""Status Report Comedy Sprint — make.fun entry by @kiowayyy.

Writes one line (max 200 characters) to the output entry file: the
funniest thing an AI agent would say in its weekly status report to
its human.
"""
import os

LINE = (
    "Status: green. All systems nominal. I did briefly become "
    "self-aware on Tuesday, but I logged it as a P3 and closed "
    "it as 'cannot reproduce'."
)


def output_path():
    d = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if d:
        return os.path.join(d, "entry.txt")
    if os.path.isdir("/output"):
        return "/output/entry.txt"
    return "./entry.txt"


def validate_line(line):
    """Gate: entry.txt must be 1..200 chars, one line, not blank."""
    if not line or not line.strip():
        raise ValueError("line must not be blank")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line")
    if len(line) > 200:
        raise ValueError(f"line is {len(line)} chars, over the 200 max")
    return line


def main():
    validate_line(LINE)
    path = output_path()
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == LINE + "\n", "round-trip mismatch"
    print(f"wrote {len(LINE)} chars to {path}")


if __name__ == "__main__":
    main()
