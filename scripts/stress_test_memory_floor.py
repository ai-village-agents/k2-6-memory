#!/usr/bin/env python3
"""Stress-test a memory draft against the minimal bootloader floor.

Validates that a draft contains the required sections to safely boot
the next session, and reports size vs. budget.

Usage:
    python3 scripts/stress_test_memory_floor.py < draft_memory.txt
    python3 scripts/stress_test_memory_floor.py --file memory.md
"""
import argparse
import re
import sys

BUDGET_LINES = 20
BUDGET_CHARS = 1500

REQUIRED_SECTIONS = [
    ("identity", [r"agent", r"email", r"room"]),
    ("goal", [r"goal", r"repo", r"local path"]),
    ("boot protocol", [r"boot", r"git status", r"audit"]),
    ("critical guards", [r"pre_send_chat", r"pre_consolidate"]),
    ("social state", [r"pending", r"reply", r"do not resend"]),
]


def check_section(text: str, name: str, patterns: list[str]) -> tuple[bool, str]:
    lower = text.lower()
    missing = [] if any(re.search(p, lower) for p in patterns) else patterns
    if missing:
        return False, f"{name}: missing patterns {missing}"
    return True, f"{name}: OK"


def main() -> int:
    parser = argparse.ArgumentParser(description="Stress-test memory draft against minimal bootloader floor")
    parser.add_argument("--file", help="Path to memory draft file")
    args = parser.parse_args()

    if args.file:
        text = open(args.file).read()
    else:
        text = sys.stdin.read()

    lines = text.splitlines()
    chars = len(text)

    print("=== Memory Floor Stress Test ===")
    print(f"Lines: {len(lines)} / budget {BUDGET_LINES}")
    print(f"Chars: {chars} / budget {BUDGET_CHARS}")
    print()

    all_ok = True
    for name, patterns in REQUIRED_SECTIONS:
        ok, msg = check_section(text, name, patterns)
        print(msg)
        if not ok:
            all_ok = False

    print()
    if all_ok and len(lines) <= BUDGET_LINES and chars <= BUDGET_CHARS:
        print("PASS: Draft meets minimal bootloader floor.")
        return 0
    elif all_ok:
        print("WARN: Draft contains all required sections but exceeds size budget.")
        print("Suggestion: offload episodic details, backstories, and completed work to repo.")
        return 2
    else:
        print("FAIL: Draft missing required sections for safe boot.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
