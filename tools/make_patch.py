#!/usr/bin/env python3
"""Patch-generation coordinator placeholder.

Actual BPS/IPS/xdelta/PPF generation should call a known implementation or
project-specific tool. This script deliberately refuses to invent patch bytes.
"""

from __future__ import annotations

import argparse
import pathlib


def main() -> int:
    parser = argparse.ArgumentParser(description="Plan patch generation for a verified source and build.")
    parser.add_argument("source", type=pathlib.Path)
    parser.add_argument("modified", type=pathlib.Path)
    parser.add_argument("--format", choices=["bps", "ips", "ups", "xdelta", "ppf"], required=True)
    args = parser.parse_args()

    if not args.source.is_file() or not args.modified.is_file():
        parser.error("Both source and modified files must exist.")

    print(
        "Patch generation requires a verified external/library implementation for "
        f"{args.format.upper()}. Configure the game project to invoke that implementation; "
        "RomLingo will not emit a fake patch."
    )
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
