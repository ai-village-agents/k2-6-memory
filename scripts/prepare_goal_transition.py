#!/usr/bin/env python3
"""Prepare a safe worksheet for switching Kimi K2.6 to a new village goal.

This script is deliberately non-mutating. Goal changes are high-context events:
the new Shoshannah/admin text should be copied verbatim, reviewed, and then the
small set of active-state files should be updated consciously.
"""

import argparse
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ACTIVE_GOAL = ROOT / "goals" / "active" / "current.md"
SESSION_START = ROOT / "docs" / "SESSION_START.md"
INVENTORY = ROOT / "inventory.yaml"
REFLECTIONS = ROOT / "reflections" / "META.md"


def git_value(*args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()


def first_matching_line(text: str, needle: str) -> str:
    for line in text.splitlines():
        if needle in line:
            return line.strip()
    return "(not found)"


def read_goal_text(path: str | None) -> str:
    if not path:
        return "(paste verbatim Shoshannah/admin goal text here before editing files)"
    return Path(path).read_text(encoding="utf-8").strip()


def main() -> None:
    parser = argparse.ArgumentParser(description="Print a non-mutating goal-transition worksheet.")
    parser.add_argument("--new-title", default="(new goal title)", help="New goal title, e.g. Improve your memory!")
    parser.add_argument("--new-start-day", type=int, default=420, help="Village day the new goal starts.")
    parser.add_argument("--old-end-day", type=int, default=419, help="Village day the old goal ends.")
    parser.add_argument("--goal-text-file", help="File containing verbatim admin goal text.")
    args = parser.parse_args()

    status = git_value("status", "-sb")
    upstream = git_value("rev-list", "--left-right", "--count", "@{u}...HEAD")
    active_text = ACTIVE_GOAL.read_text(encoding="utf-8") if ACTIVE_GOAL.exists() else "(not found)"
    goal_text = read_goal_text(args.goal_text_file)

    print("# Kimi K2.6 goal-transition worksheet")
    print("mode: non-mutating; review and edit files manually")
    print(f"git_status: {status!r}")
    print(f"upstream_ahead_behind: {upstream}")
    print(f"old_goal_line_active: {first_matching_line(active_text, 'Active Goal')}")
    print(f"new_goal_title: {args.new_title}")
    print(f"new_start_day: {args.new_start_day}")
    print(f"old_end_day: {args.old_end_day}")
    print("\n## Verbatim new goal text")
    print(goal_text)
    print("\n## Files to update after a real goal announcement")
    for path in [ACTIVE_GOAL, SESSION_START, INVENTORY, REFLECTIONS]:
        print(f"- {path.relative_to(ROOT)}")
    print("\n## Required edits")
    print("1. Archive old goal: copy goals/active/current.md to goals/archive/d<old_end_day>_<slug>.md")
    print("2. Replace goals/active/current.md with new goal title, start day, room/context, and empty completed list.")
    print("3. Update docs/SESSION_START.md if it references the old goal name.")
    print("4. Update inventory.yaml: any items tied to the old goal should get last_verified updated or status changed to retired/archived.")
    print("5. Add a new daily log entry in logs/ for the transition.")
    print("6. Update principles/load_bearing.md if any rules reference the old goal explicitly.")
    print("7. At next consolidation, rewrite internal memory to name only the new goal, repo boot command, active blockers, and social do-not-resend items.")
    print("\n## Validation after edits")
    print("bash scripts/audit.sh")
    print("bash scripts/retrieval_self_test.sh")
    print("python3 scripts/memory_metrics.py")
    print("\n## Memory rule")
    print("Internal memory should retain only the new goal/room, repo boot command, active blockers, social do-not-resend, and retired-goal pointers; do not append a full goal-history archive.")


if __name__ == "__main__":
    main()
