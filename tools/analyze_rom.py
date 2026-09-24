#!/usr/bin/env python3
"""Basic immutable source-file inspection for RomLingo projects."""

from __future__ import annotations

import argparse
import hashlib
import json
import pathlib
import zlib


def hash_file(path: pathlib.Path) -> dict[str, str | int]:
    md5 = hashlib.md5()
    sha1 = hashlib.sha1()
    sha256 = hashlib.sha256()
    crc = 0
    size = 0

    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            size += len(chunk)
            md5.update(chunk)
            sha1.update(chunk)
            sha256.update(chunk)
            crc = zlib.crc32(chunk, crc)

    return {
        "filename": path.name,
        "size_bytes": size,
        "crc32": f"{crc & 0xFFFFFFFF:08X}",
        "md5": md5.hexdigest(),
        "sha1": sha1.hexdigest(),
        "sha256": sha256.hexdigest(),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Inspect a source game file without modifying it.")
    parser.add_argument("file", type=pathlib.Path)
    parser.add_argument("--json", action="store_true", help="Output JSON")
    args = parser.parse_args()

    path = args.file
    if not path.is_file():
        parser.error(f"File not found: {path}")

    result = hash_file(path)
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print("RomLingo source inspection")
        print(f"File:    {result['filename']}")
        print(f"Size:    {result['size_bytes']} bytes")
        print(f"CRC32:   {result['crc32']}")
        print(f"MD5:     {result['md5']}")
        print(f"SHA-1:   {result['sha1']}")
        print(f"SHA-256: {result['sha256']}")
        print("\nNote: platform/script identification is game-specific and is not inferred by this generic tool.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
