#!/usr/bin/env python3
"""Generic lesson-text validation helpers.

This file intentionally does not pretend every game uses the same font metrics.
Game adapters should supply actual glyph widths and textbox constraints.
"""

from __future__ import annotations

import argparse
import json
import pathlib


def measure_line(line: str, glyph_widths: dict[str, int], default_width: int) -> int:
    return sum(glyph_widths.get(ch, default_width) for ch in line)


def validate_pages(
    text: str,
    max_width_px: int,
    max_lines_per_page: int,
    glyph_widths: dict[str, int],
    default_width: int,
) -> list[str]:
    errors: list[str] = []
    pages = text.split("\f")
    for p_index, page in enumerate(pages, start=1):
        lines = page.splitlines() or [""]
        if len(lines) > max_lines_per_page:
            errors.append(
                f"page {p_index} has {len(lines)} lines; maximum is {max_lines_per_page}"
            )
        for l_index, line in enumerate(lines, start=1):
            width = measure_line(line, glyph_widths, default_width)
            if width > max_width_px:
                errors.append(
                    f"page {p_index}, line {l_index} is {width}px; maximum is {max_width_px}px"
                )
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate already-wrapped lesson text.")
    parser.add_argument("text_file", type=pathlib.Path)
    parser.add_argument("--width", type=int, required=True, dest="max_width")
    parser.add_argument("--lines", type=int, required=True, dest="max_lines")
    parser.add_argument("--glyph-widths", type=pathlib.Path)
    parser.add_argument("--default-width", type=int, default=8)
    args = parser.parse_args()

    text = args.text_file.read_text(encoding="utf-8")
    glyph_widths: dict[str, int] = {}
    if args.glyph_widths:
        glyph_widths = json.loads(args.glyph_widths.read_text(encoding="utf-8"))

    errors = validate_pages(
        text,
        max_width_px=args.max_width,
        max_lines_per_page=args.max_lines,
        glyph_widths=glyph_widths,
        default_width=args.default_width,
    )

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    print("Text fits the supplied constraints.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
