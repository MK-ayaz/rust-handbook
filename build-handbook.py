#!/usr/bin/env python3
"""Build RUST-LEARNING-HANDBOOK-2026.md from the chapter files.

The chapter files are the single source of truth. This script concatenates
README.md, the seven numbered chapters in order, and RUST-STUDY-TRACKER.md
into one portable document so the repo never drifts between "split" and
"single-file" builds.

Usage:
    python build-handbook.py           # write the composite file
    python build-handbook.py --check   # exit 1 if the composite is stale

Requires only the Python standard library.
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUTPUT = ROOT / "RUST-LEARNING-HANDBOOK-2026.md"

PARTS = [
    "README.md",
    "01-fundamentals.md",
    "02-ownership-borrowing-lifetimes.md",
    "03-types-traits-generics.md",
    "04-projects-testing-errors.md",
    "05-concurrency-async.md",
    "06-advanced-unsafe-ffi-performance.md",
    "07-production-projects-reference.md",
    "RUST-STUDY-TRACKER.md",
]

SEPARATOR = "\n\n---\n\n"


def build() -> str:
    sections = []
    for name in PARTS:
        path = ROOT / name
        if not path.exists():
            sys.exit(f"error: missing part {name!r}")
        sections.append(path.read_text(encoding="utf-8").rstrip("\n"))
    return (SEPARATOR.join(sections) + "\n").encode("utf-8")


def main() -> int:
    content = build()

    if "--check" in sys.argv[1:]:
        current = OUTPUT.read_bytes() if OUTPUT.exists() else b""
        if current != content:
            print(
                "error: RUST-LEARNING-HANDBOOK-2026.md is out of date; "
                "run `python build-handbook.py`",
                file=sys.stderr,
            )
            return 1
        print("ok: composite handbook is up to date")
        return 0

    OUTPUT.write_bytes(content)
    print(f"wrote {OUTPUT.name} ({len(content.splitlines())} lines)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
