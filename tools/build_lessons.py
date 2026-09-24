#!/usr/bin/env python3
"""Lesson-generation integration point.

RomLingo intentionally keeps language generation separate from ROM insertion.
This starter utility checks dialogue records and creates empty lesson stubs for review.
"""

from __future__ import annotations

import argparse
import json
import pathlib


def make_stub(record: dict) -> dict:
    return {
        "dialogue_id": record.get("id"),
        "source_text": record.get("original", ""),
        "translation": None,
        "vocabulary": [],
        "grammar": None,
        "sentence_breakdown": [],
        "usage_notes": [],
        "memory_tip": None,
        "quiz": None,
        "review_status": "needs_linguistic_review",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Create reviewable lesson stubs from dialogue JSON.")
    parser.add_argument("dialogue_json", type=pathlib.Path)
    parser.add_argument("output_json", type=pathlib.Path)
    args = parser.parse_args()

    data = json.loads(args.dialogue_json.read_text(encoding="utf-8"))
    records = data if isinstance(data, list) else data.get("dialogue", [])
    lessons = [make_stub(record) for record in records]
    args.output_json.parent.mkdir(parents=True, exist_ok=True)
    args.output_json.write_text(json.dumps(lessons, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {len(lessons)} lesson stubs to {args.output_json}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
