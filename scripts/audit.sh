#!/bin/bash
# Memory Repo Audit Script
# Run before consolidation and at session start

echo "=== Memory Repo Audit ==="
echo "Date: $(date)"
echo ""

# 1. Check git status
echo "--- Git Status ---"
cd ~/k2-6-memory
git status -sb
UPSTREAM=$(git rev-list --left-right --count HEAD...@{u} 2>/dev/null | tr '\t' ' ')
if [ -n "$UPSTREAM" ]; then
    echo "Upstream: $UPSTREAM (ahead behind)"
else
    echo "Upstream: no tracking branch"
fi
echo ""

# 2. Check for uncommitted changes
if [ -n "$(git status --porcelain)" ]; then
    echo "WARNING: Uncommitted changes detected"
    git status --short
else
    echo "OK: Working tree clean"
fi
echo ""

# 3. Check critical files exist
echo "--- Critical Files ---"
for f in README.md docs/SESSION_START.md docs/self_audit.md principles/load_bearing.md principles/lessons.md runbooks/send_chat_message.md runbooks/consolidate.md goals/active/current.md; do
    if [ -f "$f" ]; then
        echo "OK: $f"
    else
        echo "MISSING: $f"
    fi
done
echo ""

# 4. Check executable guards exist
echo "--- Executable Guards ---"
for f in scripts/audit.sh scripts/search_memory.py scripts/pre_consolidate.sh scripts/pre_send_chat.py scripts/validate_inventory.py; do
    if [ -f "$f" ]; then
        echo "OK: $f"
    else
        echo "MISSING: $f"
    fi
done
echo ""

# 5. Check file sizes (internal memory proxy)
echo "--- File Sizes ---"
wc -l README.md docs/*.md principles/*.md runbooks/*.md goals/active/*.md 2>/dev/null
echo ""

# 6. Check git log
echo "--- Recent Commits ---"
git log --oneline -5 2>/dev/null || echo "No commits yet"
echo ""

# 7. Validate inventory.yaml structure
echo "--- Inventory Structure ---"
python3 scripts/validate_inventory.py || echo "WARNING: inventory.yaml structural validation failed"
echo ""

echo "=== Audit Complete ==="
