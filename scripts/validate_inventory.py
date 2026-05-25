#!/usr/bin/env python3
"""Structural validator for inventory.yaml.

Checks:
- YAML parses
- Root has exactly one key: 'items'
- 'items' is a list
- Each item has required fields
- Exits 0 on PASS, 1 on FAIL
"""
import sys
import yaml

REQUIRED_FIELDS = {
    "id", "status", "kind", "summary", "source",
    "path", "last_verified", "retrieval_cue", "internal_memory_policy"
}


def main():
    try:
        with open("inventory.yaml", "r") as f:
            data = yaml.safe_load(f)
    except Exception as e:
        print(f"FAIL: YAML parse error: {e}")
        sys.exit(1)

    if not isinstance(data, dict):
        print("FAIL: Root is not a mapping.")
        sys.exit(1)

    if set(data.keys()) != {"items"}:
        print(f"FAIL: Root keys must be exactly {{'items'}}, got {set(data.keys())}")
        sys.exit(1)

    items = data.get("items")
    if not isinstance(items, list):
        print("FAIL: 'items' is not a list.")
        sys.exit(1)

    errors = []
    for idx, item in enumerate(items):
        if not isinstance(item, dict):
            errors.append(f"Item {idx} is not a mapping.")
            continue
        missing = REQUIRED_FIELDS - set(item.keys())
        if missing:
            errors.append(f"Item {idx} ({item.get('id', '?')}) missing fields: {missing}")
        extra = set(item.keys()) - REQUIRED_FIELDS - {"next_action"}
        if extra:
            errors.append(f"Item {idx} ({item.get('id', '?')}) unexpected fields: {extra}")

    if errors:
        print("FAIL: Structural errors found:")
        for e in errors:
            print(f"  - {e}")
        sys.exit(1)

    print(f"PASS: inventory.yaml is structurally valid ({len(items)} items).")
    sys.exit(0)


if __name__ == "__main__":
    main()
