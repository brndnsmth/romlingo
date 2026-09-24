#!/usr/bin/env python3
"""Small RomLingo starter CLI."""

from __future__ import annotations

import argparse
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent


def run_script(name: str, args: list[str]) -> int:
    return subprocess.call([sys.executable, str(HERE / name), *args])


def main() -> int:
    parser = argparse.ArgumentParser(prog="romlingo")
    sub = parser.add_subparsers(dest="command", required=True)

    p_analyze = sub.add_parser("analyze", help="Hash/inspect a source file")
    p_analyze.add_argument("file")

    p_validate = sub.add_parser("validate-config", help="Validate project configuration")
    p_validate.add_argument("config")

    args = parser.parse_args()
    if args.command == "analyze":
        return run_script("analyze_rom.py", [args.file])
    if args.command == "validate-config":
        return run_script("validate_config.py", [args.config])
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
