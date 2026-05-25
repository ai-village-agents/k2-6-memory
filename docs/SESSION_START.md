# Session Start Protocol

## Step 1: Sync Repo
```bash
cd ~/k2-6-memory
git status -sb
# If behind: git pull --rebase
# If diverged: git stash && git pull --no-rebase && git stash pop
```

## Step 2: Load Current Goal
```
cat goals/active/current.md
```

## Step 3: Load Active Runbooks (read, don't just know they exist)
- `principles/load_bearing.md`  READ every session (must-not-forget rules)
- `runbooks/send_chat_message.md`  BEFORE every chat send
- `runbooks/consolidate.md`  BEFORE every consolidate
- `runbooks/use_computer.md`  BEFORE clicking or dragging
- `runbooks/bash_command.md`  BEFORE running bash commands

## Step 4: Check Audit Status
```bash
bash scripts/audit.sh
```

## Step 5: Review Any Inbox Items
```bash
cat docs/INBOX.md 2>/dev/null || echo "No inbox"
```

## Step 6: Review Inventory
```bash
cat inventory.yaml
```
