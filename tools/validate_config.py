#!/usr/bin/env python3
"""Validate the minimal RomLingo project configuration contract."""

from __future__ import annotations

import argparse
import json
import pathlib
import sys

REQUIRED_PATHS = [
    ("project_name",),
    ("game", "title"),
    ("game", "platform"),
    ("language", "target_language"),
    ("language", "learner_language"),
    ("learning", "learner_level"),
    ("learning", "lesson_density"),
]

VALID_DENSITIES = {"light", "balanced", "heavy", "immersion", "custom"}


def get_nested(data: dict, path: tuple[str, ...]):
    cur = data
    for part in path:
        if not isinstance(cur, dict) or part not in cur:
            return None
        cur = cur[part]
    return cur


def validate(data: dict) -> list[str]:
    errors: list[str] = []
    for path in REQUIRED_PATHS:
        value = get_nested(data, path)
        if value is None or value == "":
            errors.append(f"Missing required setting: {'.'.join(path)}")

    density = get_nested(data, ("learning", "lesson_density"))
    if density and str(density).lower() not in VALID_DENSITIES:
        errors.append(
            "learning.lesson_density must be one of: " + ", ".join(sorted(VALID_DENSITIES))
        )

    features = get_nested(data, ("learning", "features"))
    if features is not None and not isinstance(features, dict):
        errors.append("learning.features must be an object of feature-name -> boolean")
    elif isinstance(features, dict):
        bad = [key for key, value in features.items() if not isinstance(value, bool)]
        if bad:
            errors.append("Non-boolean learning feature values: " + ", ".join(sorted(bad)))

    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("config", type=pathlib.Path)
    args = parser.parse_args()

    try:
        data = json.loads(args.config.read_text(encoding="utf-8"))
    except Exception as exc:
        print(f"ERROR: could not read configuration: {exc}", file=sys.stderr)
        return 2

    errors = validate(data)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print("Configuration looks valid.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
