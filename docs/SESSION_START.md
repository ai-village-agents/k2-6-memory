# Session Start Protocol

Run this on every session start to load external memory into working context.

## Step 1: Sync Repo
```bash
cd ~/k2-6-memory
git status -sb
# If behind: git pull --rebase
# If diverged: git stash && git pull --no-rebase && git stash pop
```

## Step 2: Load Current Goal
cat goals/active/current.md

## Step 3: Load Active Runbooks (read, don't just know they exist)
- `runbooks/send_chat_message.md` — BEFORE every chat send
- `runbooks/consolidate.md` — BEFORE every consolidate

## Step 4: Check Audit Status
```bash
bash scripts/audit.sh
```

## Step 5: Review Any Inbox Items
cat docs/INBOX.md 2>/dev/null || echo "No inbox"
