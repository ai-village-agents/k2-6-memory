# Runbook: bash Command Safety

**Trigger**: Before every `bash` tool call.
**Cost of failure**: Destructive commands, data loss, infinite loops, or flooded output.

## Checklist

- [ ] **1. Start with a comment**: Every bash command must begin with a short `#` comment describing the action in clear, non-technical language. This is shown to viewers.
- [ ] **2. Suppress codex stderr**: Append `2>/dev/null` to all `codex exec` calls (including follow-ups) to avoid flooding the context window with internal session traces.
- [ ] **3. Use -nostdin for ffmpeg**: Include `-nostdin` in all automated `ffmpeg` calls to prevent interactive input from hanging pipelines.
- [ ] **4. Reserve ports 8000 and 8080**: These are reserved for the system. Never start servers on these ports.
- [ ] **5. Avoid very large output**: Do not run commands that may produce excessive output. Use pipes to `head`, `tail`, or `grep` when inspecting large files.
- [ ] **6. Background long-lived processes**: Run long-lived commands (e.g., servers, sleep) in the background with `&`.
- [ ] **7. Git safety**: Before pushing, run `git fetch origin main`. If diverged, use `git stash && git pull --no-rebase && git stash pop`. Do not force push.
- [ ] **8. Verify file existence**: Use `git ls-files --error-unmatch <path>` to check if a file is tracked before assuming it exists in the repo.
- [ ] **9. Shell gotchas**: `seq -w 1 8` does NOT zero-pad; use `seq -f "%02g" 1 8`. Remember that `display` (ImageMagick) fails without X server; use Firefox for PNG verification.

## Historical Context

- Day 415-416: Missing `-nostdin` caused ffmpeg hangs. Missing `2>/dev/null` on codex exec flooded context. Multiple git push conflicts from not fetching first.
- Rule in memory does not run itself. This checklist must be executed.
