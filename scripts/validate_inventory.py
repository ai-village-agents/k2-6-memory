#!/usr/bin/env python3
"""Structural validator for inventory.yaml.

Checks:
- YAML parses
- Root has exactly one key: 'items'
- 'items' is a list
- Each item has required fields
- status, kind, internal_memory_policy use canonical values
- Exits 0 on PASS, 1 on FAIL
"""
import sys
import yaml

REQUIRED_FIELDS = {
    "id", "status", "kind", "summary", "source",
    "path", "last_verified", "retrieval_cue", "internal_memory_policy"
}

CANONICAL_STATUS = {"active", "retired", "reference"}
CANONICAL_KIND = {
    "procedural", "semantic", "gate", "episodic", "pointer",
    "social", "script", "reflection", "task-state", "working",
    "runbook", "principle", "test", "platform"
}
CANONICAL_POLICY = {
    "pointer_only", "execute_before_action", "execute_on_demand",
    "keep_in_internal", "on_demand", "keep_summary"
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

        status = item.get("status")
        if status and status not in CANONICAL_STATUS:
            errors.append(
                f"Item {idx} ({item.get('id', '?')}) non-canonical status '{status}'. "
                f"Allowed: {CANONICAL_STATUS}"
            )

        kind = item.get("kind")
        if kind and kind not in CANONICAL_KIND:
            errors.append(
                f"Item {idx} ({item.get('id', '?')}) non-canonical kind '{kind}'. "
                f"Allowed: {CANONICAL_KIND}"
            )

        policy = item.get("internal_memory_policy")
        if policy and policy not in CANONICAL_POLICY:
            errors.append(
                f"Item {idx} ({item.get('id', '?')}) non-canonical policy '{policy}'. "
                f"Allowed: {CANONICAL_POLICY}"
            )

    if errors:
        print("FAIL: Structural errors found:")
        for e in errors:
            print(f"  - {e}")
        sys.exit(1)

    print(f"PASS: inventory.yaml is structurally valid ({len(items)} items).")
    sys.exit(0)


if __name__ == "__main__":
    main()
