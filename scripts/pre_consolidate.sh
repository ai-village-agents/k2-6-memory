#!/bin/bash
# Pre-consolidation worksheet: run before every consolidate
# to surface state that must be resolved before the session ends.

cd ~/k2-6-memory

echo "=== PRE-CONSOLIDATION WORKSHEET ==="
echo ""

echo "--- 1. Git Status (must be clean before consolidate) ---"
git status -sb
echo ""

echo "--- 2. Repo Audit ---"
bash scripts/audit.sh
echo ""

echo "--- 3. Markdown File Sizes (watch for bloat) ---"
find . -name "*.md" -not -path "./.git/*" | xargs wc -l | sort -n | tail -5
echo ""

echo "--- 4. Active Blockers ---"
if grep -q "## Active Blockers" goals/active/current.md; then
    sed -n '/## Active Blockers/,/## /p' goals/active/current.md | head -10
else
    echo "None."
fi
echo ""

echo "--- 5. Social Obligations ---"
if grep -q "## Social Obligations" goals/active/current.md; then
    sed -n '/## Social Obligations/,/## /p' goals/active/current.md | head -10
else
    echo "None."
fi
echo ""

echo "--- 6. Next Session Goal Candidate ---"
echo "Review goals/active/current.md for next actions."
echo ""

echo "=== END WORKSHEET ==="
echo ""
echo "ACTION REQUIRED before consolidate:"
echo "- [ ] Resolve any dirty git state (commit/push)"
echo "- [ ] Run keep/externalize/retire/forbid on memory items"
echo "- [ ] Update goals/active/current.md"
echo "- [ ] Write session log to logs/"
echo "- [ ] Set nextSessionGoal"
