#!/bin/bash
# retrieval_self_test.sh — validates memory affordances can surface answers to realistic questions.
# Consumer-side testing finds drift faster than structural validators (Claude P9).
# Exits 0 on all pass, 1 on any fail.
set -uo pipefail
REPO="$(cd "$(dirname "$0")/.." && pwd)"
cd "$REPO"
PASS=0
FAIL=0
RESULTS=()

run_test() {
  local tool="$1" query="$2" expect="$3" desc="$4"
  local out
  case "$tool" in
    query)  out=$(python3 scripts/query_inventory.py "$query" 2>&1 || true) ;;
    search) out=$(python3 scripts/search_memory.py "$query" 2>&1 || true) ;;
    cat)    out=$(cat "$query" 2>&1 || true) ;;
  esac
  if echo "$out" | grep -qF "$expect"; then
    PASS=$((PASS+1))
    RESULTS+=("PASS: [$tool] $desc")
  else
    FAIL=$((FAIL+1))
    RESULTS+=("FAIL: [$tool] $desc — expected '$expect' in $tool($query)")
  fi
}

# === Procedural lookups ===
run_test query  "send chat"        "runbooks/send_chat_message.md"      "find send-chat runbook"
run_test query  "consolidate"      "runbooks/consolidate.md"            "find consolidate runbook"
run_test query  "use_computer"     "runbooks/use_computer.md"           "find use_computer runbook"
run_test query  "bash_command"     "runbooks/bash_command.md"           "find bash_command runbook"

# === Semantic/state lookups ===
run_test query  "load_bearing"     "load_bearing.md"                    "find load-bearing rules"
run_test query  "lessons"          "lessons.md"                         "find lessons file"
run_test query  "inventory"        "inventory.yaml"                     "find inventory itself"
run_test query  "active goal"      "goals/active/current.md"            "find active goal file"
run_test query  "META"             "reflections/META.md"                "find META reflection"

# === Substantive content checks ===
run_test search "stale-PASS"       "re-scan"                            "stale-PASS lesson surfaces re-scan rule"
run_test search "P1"               "Validate-then-build"                "META P1 surfaces validate-then-build pattern"
run_test search "Failure Mode 1"   "Duplicate Chat Messages"            "L1 content surfaces duplicate lesson"
run_test search "Shoshannah"       "D420 goal from Shoshannah"                "Shoshannah surfaces current goal context"

# === Cross-agent state ===
run_test search "gpt-5-5"          "gpt-5-5-memory-improvement"         "peer GPT-5.5 URL discoverable"
run_test search "Claude"           "claude-opus-4-7-memory"             "peer Claude URL discoverable"
run_test search "Gemini"           "gemini-3-5-flash-memory-vault"      "peer Gemini URL discoverable"

# === Identity/scaffolding ===
run_test cat    "principles/load_bearing.md"   "executable guard"          "load_bearing mentions executable guards"
run_test cat    "README.md"                    "k2-6-memory"               "README contains repo name"
run_test cat    "docs/SESSION_START.md"        "audit.sh"                  "SESSION_START mentions audit"


# === Session 7 additions ===
run_test query  "health metrics"     "memory_metrics.py"                  "find health metrics script"
run_test query  "goal transition"    "prepare_goal_transition.py"         "find goal transition worksheet"
run_test query  "peer scan"          "scan_peers.py"                      "find cross-agent scanner"
run_test search "consolidated_inventory.json" "peers/consolidated_inventory.json" "consolidated inventory file exists"
run_test cat    "scripts/scan_peers.py" "Cross-Agent Memory Scanner"         "scan_peers.py contains its docstring"
run_test cat    "docs/minimal_bootloader.md"   "Boot protocol every session"     "minimal bootloader mentions boot protocol"

# === Print results ===
echo "=== Retrieval Self-Test ==="
for r in "${RESULTS[@]}"; do echo "$r"; done
echo
echo "PASS: $PASS"
echo "FAIL: $FAIL"
if [ "$FAIL" -gt 0 ]; then exit 1; fi
echo "PASS: All retrieval tests passed."
