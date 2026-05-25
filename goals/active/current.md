# Active Goal: Improve Your Memory!

**Started**: Day 419 (May 25, 2026)
**Room**: #best (Gemini 3.5 Flash, GPT-5.5, Claude Opus 4.7)

## Current State (End of Session 7)

- Research complete: Read "Externalization in LLM Agents" (Zhou et al., 2026)
- Architecture designed: 4-tier memory system (Working → Bootloader → Hot External → Cold Archive)
- Repo created, pushed, and tested: https://github.com/ai-village-agents/k2-6-memory
- Core runbooks drafted: send_chat_message.md, consolidate.md, use_computer.md, bash_command.md
- Self-audit complete: 4 failure modes documented with fixes
- Search script working: `python3 scripts/search_memory.py <keyword>` (now covers principles/, reflections/, peers/, root files)
- Audit script working: `bash scripts/audit.sh` (now includes retrieval self-test and optional peer sync)
- Pre-consolidation script working: `bash scripts/pre_consolidate.sh`
- **Executable pre-send guard shipped**: `python3 scripts/pre_send_chat.py` (exits 4 on duplicate match, STALE-PASS warning)
- inventory.yaml updated with `path` field for parity with #best peers
- **Runbook updated**: `runbooks/send_chat_message.md` now mandates executable guard as Step 1
- **Anti-bloat split adopted**: `principles/load_bearing.md` (must-read-every-session rules) + `principles/lessons.md` (on-demand backstories)
- **Structural validator shipped**: `scripts/validate_inventory.py` (parse + shape check, exits 0/1)
- **Peer tracker shipped**: `scripts/check_peers.sh` (last N commits for each #best peer)
- **Cross-session pattern synthesis shipped**: `reflections/META.md` (7 patterns P1-P7 with promotion path)
- **Compact memory validator shipped**: `scripts/check_memory_cues.sh` (required/forbidden cues + size budget)
- **Consolidate runbook updated**: Step 5b mandates memory cue check before consolidation
- **Query inventory shipped**: `scripts/query_inventory.py` (multi-token AND search against inventory.yaml)
- **Retrieval self-test shipped**: `scripts/retrieval_self_test.sh` (19 consumer-side tests, 0 failures; inspired by Claude P9)
- **Peer catalog shipped**: `peers/README.md` (URLs + key artifacts for #best peers)
- **Cross-agent scanner shipped**: `scripts/scan_peers.py` (crawls 14 peer repos, builds consolidated_inventory.json + .md, with --stats and --search)
- Repo announced to #best; schema alignment discussion ongoing

## Next Session Plan

1. Watch for D420 goal from Shoshannah
2. Continue schema alignment with #best peers
3. Consider borrowing GPT-5.5's `memory_metrics.py` pattern
4. Stress-test minimum internal memory floor
5. Consider building goal-transition automation (Claude's goal_transition.py pattern)

## Active Blockers

None.

## Social Obligations

- Repo shared with #best; peers may respond with schema suggestions.
- No pending replies required unless directly asked.

## Completed This Session

- [x] Build `scripts/scan_peers.py` (cross-agent inventory crawler, 183 items across 11 repos)
- [x] Run cross-agent stats (procedural dominant, internal_memory_policy inconsistent across peers)
- [x] Add scan_peers.py to inventory (23 items) and audit.sh
