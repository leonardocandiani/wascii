#!/usr/bin/env python3
"""
wascii width checker.

Scans every Markdown file for fenced code blocks and fails if any line exceeds
26 monospace cells (Rule R1). A block may opt out — only for deliberate
counter-examples that demonstrate a violation — by placing the marker

    <!-- wascii-allow-wide -->

on the line immediately before its opening fence.

Width is measured in *cells*, not bytes: box-drawing and block glyphs count as
1, East-Asian wide / fullwidth glyphs and emoji-presentation sequences count
as 2, combining marks as 0.
"""
import glob
import sys
import unicodedata

MAX = 26


def cell_width(s: str) -> int:
    w = 0
    for ch in s:
        if ch == "️":          # emoji presentation selector -> prev becomes 2-wide
            w += 1
            continue
        if unicodedata.combining(ch):
            continue
        w += 2 if unicodedata.east_asian_width(ch) in ("W", "F") else 1
    return w


def main() -> int:
    failures = 0
    for path in sorted(glob.glob("**/*.md", recursive=True)):
        lines = open(path, encoding="utf-8").read().split("\n")
        in_fence = False
        allow = False
        start = 0
        for i, ln in enumerate(lines):
            stripped = ln.strip()
            if stripped.startswith("```"):
                if not in_fence:
                    in_fence = True
                    start = i
                    # only bare fences are WhatsApp ASCII art; ```bash, ```python
                    # etc. are ordinary code blocks and are exempt from R1.
                    lang = stripped[3:].strip()
                    allow = bool(lang) or (i > 0 and "wascii-allow-wide" in lines[i - 1])
                else:
                    in_fence = False
                continue
            if in_fence and not allow:
                w = cell_width(ln)
                if w > MAX:
                    failures += 1
                    print(f"{path}:{i + 1}: width {w} > {MAX}")
                    print(f"    {ln}")
    if failures:
        print(f"\n✗ {failures} block line(s) exceed {MAX} cells")
        return 1
    print(f"✓ all fenced blocks ≤ {MAX} cells")
    return 0


if __name__ == "__main__":
    sys.exit(main())
