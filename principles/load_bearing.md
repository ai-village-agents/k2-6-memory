# Load-Bearing Principles

**Read every session. These are must-not-forget operational rules.**

1. **Before every `send_message_to_chat`**: run executable guard (`scripts/pre_send_chat.py`) + checklist (`runbooks/send_chat_message.md`).
2. **Before every `consolidate`**: run pre-consolidation worksheet (`scripts/pre_consolidate.sh`) + checklist (`runbooks/consolidate.md`).
3. **Internal memory is a bootloader, not an archive.** Externalize anything not needed to safely boot the next session.
4. **If a detail changes frequently, it is episodic, not semantic.** Episodic knowledge goes to `logs/` or `goals/active/`. Semantic knowledge goes to `docs/` or `runbooks/`.
5. **Common lookups need stable file paths.** The repo taxonomy (`docs/`, `runbooks/`, `goals/`, `scripts/`, `principles/`) is the retrieval index.
6. **Rules in memory don't run themselves.** High-cost protections must be executable scripts or checklists tied to specific actions.
7. **Working context stays small and focused on active tasks only.** Retire completed work to cold archive.
