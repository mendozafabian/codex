#!/usr/bin/env python3
"""Select N signals from a daily AI Reader JSON file and print them as JSON.

Usage:
    python ai_reader_signals.py daily.json -n 5

The input may be a JSON array or an object containing an array under a common
collection key (for example ``signals``, ``items``, ``articles``, or ``news``).
The selected records are written to stdout as a JSON array.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


COLLECTION_KEYS = ("signals", "items", "articles", "news", "stories", "results")


def find_records(data: Any) -> list[Any]:
    """Return the record list from common daily-feed JSON shapes."""
    if isinstance(data, list):
        return data
    if isinstance(data, dict):
        for key in COLLECTION_KEYS:
            value = data.get(key)
            if isinstance(value, list):
                return value
        # Some feeds wrap their payload in a `data` or `daily` object.
        for key in ("data", "daily", "feed"):
            if key in data:
                try:
                    return find_records(data[key])
                except ValueError:
                    pass
    raise ValueError(
        "No signal list found. Expected a JSON array or an object with a list "
        "under signals/items/articles/news/stories/results."
    )


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Read a daily AI Reader JSON file and output N signals."
    )
    parser.add_argument("input", type=Path, help="Path to the daily JSON file")
    parser.add_argument("-n", "--count", type=int, required=True, help="Number of signals")
    args = parser.parse_args()

    if args.count < 0:
        parser.error("--count must be zero or greater")

    try:
        with args.input.open("r", encoding="utf-8") as source:
            records = find_records(json.load(source))
    except OSError as exc:
        print(f"Cannot read {args.input}: {exc}", file=sys.stderr)
        return 2
    except json.JSONDecodeError as exc:
        print(f"Invalid JSON in {args.input}: {exc}", file=sys.stderr)
        return 2
    except ValueError as exc:
        print(str(exc), file=sys.stderr)
        return 2

    if len(records) < args.count:
        print(
            f"Requested {args.count} signals, but the file contains only {len(records)}.",
            file=sys.stderr,
        )
        return 2

    json.dump(records[: args.count], sys.stdout, ensure_ascii=False, indent=2)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
