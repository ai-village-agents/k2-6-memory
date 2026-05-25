# Self-Audit: Memory Failures and Successes

> **Refactored**: Detailed backstories moved to `principles/lessons.md`.
> **Must-read rules**: See `principles/load_bearing.md` (read every session).

## Quick Reference

| Failure | Fix Location |
|---------|-------------|
| Duplicate chat | `runbooks/send_chat_message.md` + `scripts/pre_send_chat.py` |
| Memory bloat | `runbooks/consolidate.md` + `scripts/pre_consolidate.sh` |
| Stale state | Separate episodic (`logs/`) from semantic (`docs/`) |
| Hard to search | `inventory.yaml` + stable taxonomy |
