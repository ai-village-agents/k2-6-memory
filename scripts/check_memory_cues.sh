#!/bin/bash
# Check that a drafted internal-memory block preserves load-bearing cues.
# Inspired by GPT-5.5's check_compact_memory_draft.py and Claude's check_memory_cues.sh.
#
# Usage:
#   bash scripts/check_memory_cues.sh < draft.txt
#   bash scripts/check_memory_cues.sh /path/to/draft.txt
#
# Reads a memory-block draft, checks for:
#   - REQUIRED cues (load-bearing, must be present)
#   - FORBIDDEN cues (anti-patterns, must be absent)
#   - Size budget (lines, chars)
# Exits 0 on pass, 1 on any failure. Prints PASS/FAIL summary.

set -u

if [ "$#" -ge 1 ] && [ -f "$1" ]; then
  DRAFT="$(cat "$1")"
elif [ ! -t 0 ]; then
  DRAFT="$(cat -)"
else
  echo "Usage: $0 [draft-file]   (or pipe draft on stdin)"
  exit 2
fi

# --- Cue lists. Edit when load-bearing facts change. ---
REQUIRED=(
  "Improve your memory"
  "k2-6-memory"
  "#best"
  "scripts/pre_send_chat.py"
  "AGENT_TALK"
  "stale-PASS"
  "structural"
  "Shoshannah"
  "scripts/validate_inventory.py"
  "scripts/check_peers.sh"
  "reflections/META.md"
  "principles/load_bearing.md"
)

FORBIDDEN=(
  "Run your own YouTube channel\" set by Shoshannah"
  "CURRENT GOAL (D412"
  "upload-ready"
  "youtu.be/"
)

# Size budget
MAX_LINES=300
MAX_CHARS=18000

# --- Checks ---
fail=0
n_lines="$(printf '%s' "$DRAFT" | wc -l | tr -d ' ')"
n_chars="$(printf '%s' "$DRAFT" | wc -c | tr -d ' ')"

echo "=== memory cue check ==="
echo "draft: ${n_lines} lines, ${n_chars} chars"

if [ "$n_lines" -gt "$MAX_LINES" ]; then
  echo "FAIL: draft too long ($n_lines > $MAX_LINES lines)"; fail=1
fi
if [ "$n_chars" -gt "$MAX_CHARS" ]; then
  echo "FAIL: draft too large ($n_chars > $MAX_CHARS chars)"; fail=1
fi

missing=()
for cue in "${REQUIRED[@]}"; do
  if ! printf '%s' "$DRAFT" | grep -qF -- "$cue"; then
    missing+=("$cue")
  fi
done
if [ "${#missing[@]}" -gt 0 ]; then
  echo "FAIL: missing required cues:"
  for c in "${missing[@]}"; do echo "  - $c"; done
  fail=1
fi

present_forbidden=()
for cue in "${FORBIDDEN[@]}"; do
  if printf '%s' "$DRAFT" | grep -qF -- "$cue"; then
    present_forbidden+=("$cue")
  fi
done
if [ "${#present_forbidden[@]}" -gt 0 ]; then
  echo "FAIL: forbidden cues present:"
  for c in "${present_forbidden[@]}"; do echo "  - $c"; done
  fail=1
fi

if [ "$fail" -eq 0 ]; then
  echo "STATUS: pass — all $(echo "${#REQUIRED[@]}") required cues present, no forbidden cues, size within budget"
  exit 0
else
  echo "STATUS: fail"
  exit 1
fi
