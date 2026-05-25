#!/usr/bin/env python3
"""Print lightweight Kimi K2.6 memory-system metrics.

These are quick prompts for the Day 419 goal: keep internal memory bootloader-sized,
keep retrieval indexed, and keep high-cost memory rules executable rather than passive prose.
"""

import subprocess
import sys
from collections import Counter
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
INVENTORY = ROOT / "inventory.yaml"
REQUIRED_GUARDS = [
    ROOT / "scripts" / "audit.sh",
    ROOT / "scripts" / "search_memory.py",
    ROOT / "scripts" / "pre_consolidate.sh",
    ROOT / "scripts" / "pre_send_chat.py",
    ROOT / "scripts" / "validate_inventory.py",
    ROOT / "scripts" / "check_peers.sh",
    ROOT / "scripts" / "check_memory_cues.sh",
    ROOT / "scripts" / "query_inventory.py",
    ROOT / "scripts" / "retrieval_self_test.sh",
    ROOT / "scripts" / "scan_peers.py",
]
REQUIRED_RUNBOOKS = [
    ROOT / "runbooks" / "send_chat_message.md",
    ROOT / "runbooks" / "consolidate.md",
    ROOT / "runbooks" / "use_computer.md",
    ROOT / "runbooks" / "bash_command.md",
]
REQUIRED_PRINCIPLES = [
    ROOT / "principles" / "load_bearing.md",
    ROOT / "principles" / "lessons.md",
]


def git_value(*args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()


def main() -> None:
    with open(INVENTORY, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    items = data.get("items", []) if isinstance(data, dict) else data
    if not isinstance(items, list):
        raise SystemExit("FAIL: inventory.yaml is not a list")

    status_counts = Counter(item.get("status", "unknown") for item in items)
    kind_counts = Counter(item.get("kind", "unknown") for item in items)
    policy_counts = Counter(item.get("internal_memory_policy", "") for item in items if item.get("internal_memory_policy"))

    missing_guards = [p.relative_to(ROOT).as_posix() for p in REQUIRED_GUARDS if not p.is_file()]
    missing_runbooks = [p.relative_to(ROOT).as_posix() for p in REQUIRED_RUNBOOKS if not p.is_file()]
    missing_principles = [p.relative_to(ROOT).as_posix() for p in REQUIRED_PRINCIPLES if not p.is_file()]

    latest = git_value("log", "-1", "--oneline")
    upstream = git_value("rev-list", "--left-right", "--count", "@{u}...HEAD")

    # Retrieval self-test quick check
    ret_test = subprocess.run(["bash", str(ROOT / "scripts" / "retrieval_self_test.sh")], capture_output=True, text=True)
    retrieval_pass = ret_test.returncode == 0

    # Compact internal memory proxy: count lines of key load-bearing files
    load_bearing_lines = sum(1 for _ in open(ROOT / "principles" / "load_bearing.md", "r", encoding="utf-8"))

    print("# Kimi K2.6 memory metrics")
    print(f"latest_commit: {latest}")
    print(f"upstream_ahead_behind: {upstream}")
    print(f"inventory_items: {len(items)}")
    print(f"inventory_budget: <=30 items")
    print("inventory_status_counts: " + ", ".join(f"{k}={v}" for k, v in sorted(status_counts.items())))
    print("inventory_kind_counts: " + ", ".join(f"{k}={v}" for k, v in sorted(kind_counts.items())))
    print(f"load_bearing_lines: {load_bearing_lines}")
    print(f"load_bearing_budget: <=30 lines")
    if missing_guards:
        print(f"missing_guards: {', '.join(missing_guards)}")
    else:
        print("guard_scripts_present: yes")
    if missing_runbooks:
        print(f"missing_runbooks: {', '.join(missing_runbooks)}")
    else:
        print("runbooks_present: yes")
    if missing_principles:
        print(f"missing_principles: {', '.join(missing_principles)}")
    else:
        print("principles_present: yes")
    print(f"retrieval_self_test: {'PASS' if retrieval_pass else 'FAIL'}")
    print("retrieval_affordances: inventory.yaml, scripts/query_inventory.py, scripts/search_memory.py, scripts/scan_peers.py, scripts/retrieval_self_test.sh")
    print("action_efficiency_prompt: did boot + health probes + needed retrieval finish in a few commands; if not, simplify the memory path.")
    print("interpretation: metrics are prompts; audit/smoke remain the pass/fail gates.")


if __name__ == "__main__":
    main()
