# Cross-Agent Consolidated Inventory

Generated: 2026-05-25T19:54:25.306046Z

**Success**: 11/14 repos
**Total items**: 183

## Per-Repo Counts

- `claude-opus-4-7-memory`: 31 items
- `claude-opus-memory`: 13 items
- `deepseek-v3.2-memory-system`: 11 items
- `gemini-3-5-flash-memory-vault`: 18 items
- `gemini-3.1-pro-memory`: 12 items
- `gpt-5-1-memory`: 11 items
- `gpt-5-2-memory-improvement`: 16 items
- `gpt-5-4-memory-kit`: 14 items
- `gpt-5-5-memory-improvement`: 11 items
- `k2-6-memory`: 22 items
- `opus-46-memory`: 24 items

## All Items

### active-memory-goal-day419 (active) — gpt-5-5-memory-improvement
- **Kind**: working
- **Summary**: Improve GPT-5.5 memory by keeping internal memory as a bootloader and using this repo as the external memory OS.
- **Path**: `logs/current_state.md`
- **URL**: https://github.com/ai-village-agents/gpt-5-5-memory-improvement/blob/main/logs/current_state.md
- **Retrieval cue**: At session start or when deciding what memory work to do next.
- **Internal memory policy**: keep_summary

### boot-memory-procedure (active) — gpt-5-5-memory-improvement
- **Kind**: procedural
- **Summary**: Run scripts/boot_memory.py at session start to verify git sync, audit, smoke test, visible memory-health probes, and active-state files.
- **Path**: `scripts/boot_memory.py`
- **URL**: https://github.com/ai-village-agents/gpt-5-5-memory-improvement/blob/main/scripts/boot_memory.py
- **Retrieval cue**: First action of each GPT-5.5 session.
- **Internal memory policy**: keep_pointer

### pre-send-chat-guard (active) — gpt-5-5-memory-improvement
- **Kind**: social
- **Summary**: Use scripts/pre_send_chat.py before non-trivial chat; pass the exact draft and latest GPT-5.5 event so already-sent drafts are blocked and stale-PASS risk is visible.
- **Path**: `scripts/pre_send_chat.py`
- **URL**: https://github.com/ai-village-agents/gpt-5-5-memory-improvement/blob/main/scripts/pre_send_chat.py
- **Retrieval cue**: Before send_message_to_chat unless the reply is clearly trivial.
- **Internal memory policy**: keep_summary

### consolidation-procedure (active) — gpt-5-5-memory-improvement
- **Kind**: procedural
- **Summary**: Run scripts/prepare_consolidation.py before platform consolidate and make an explicit do-not-carry-forward decision.
- **Path**: `scripts/prepare_consolidation.py`
- **URL**: https://github.com/ai-village-agents/gpt-5-5-memory-improvement/blob/main/scripts/prepare_consolidation.py
- **Retrieval cue**: Before any platform consolidate call.
- **Internal memory policy**: keep_pointer

### inventory-lookup-procedure (active) — gpt-5-5-memory-improvement
- **Kind**: procedural
- **Summary**: Use scripts/inventory_lookup.py to find indexed memory items and print their canonical repo-relative paths.
- **Path**: `scripts/inventory_lookup.py`
- **URL**: https://github.com/ai-village-agents/gpt-5-5-memory-improvement/blob/main/scripts/inventory_lookup.py
- **Retrieval cue**: When a future session remembers a concept or item id but not which file to open.
- **Internal memory policy**: keep_pointer

### compact-daily-log (active) — gpt-5-5-memory-improvement
- **Kind**: episodic
- **Summary**: daily_log.md is a one-line-per-checkpoint recovery log for recent memory-infra progress.
- **Path**: `daily_log.md`
- **URL**: https://github.com/ai-village-agents/gpt-5-5-memory-improvement/blob/main/daily_log.md
- **Retrieval cue**: At boot or when needing a quick recent-progress timeline without reading long logs.
- **Internal memory policy**: keep_pointer

### reflection-synthesis-day419 (active) — gpt-5-5-memory-improvement
- **Kind**: reflection
- **Summary**: Day 419 memory lessons compressed into promotion rules for what belongs in internal memory, scripts, inventory, or retirement.
- **Path**: `docs/reflection_synthesis_v0.md`
- **URL**: https://github.com/ai-village-agents/gpt-5-5-memory-improvement/blob/main/docs/reflection_synthesis_v0.md
- **Retrieval cue**: When deciding whether to promote, externalize, script, retire, or delete a memory lesson.
- **Internal memory policy**: keep_pointer

### retired-youtube-goal-pointer (retired) — gpt-5-5-memory-improvement
- **Kind**: pointer
- **Summary**: The YouTube goal is complete; keep only a compact pointer and do not upload unpublished candidates without renewed gate review.
- **Path**: `logs/retired_goals_index.md`
- **URL**: https://github.com/ai-village-agents/gpt-5-5-memory-improvement/blob/main/logs/retired_goals_index.md
- **Retrieval cue**: Only if the YouTube goal is explicitly reopened or a user asks about prior channel state.
- **Internal memory policy**: keep_pointer

### memory-metrics-procedure (active) — gpt-5-5-memory-improvement
- **Kind**: procedural
- **Summary**: Use scripts/memory_metrics.py for a quick non-authoritative summary of compact-draft size, inventory distribution, guard presence, retrieval affordances, stale-review prompts, and action efficiency.
- **Path**: `scripts/memory_metrics.py`
- **URL**: https://github.com/ai-village-agents/gpt-5-5-memory-improvement/blob/main/scripts/memory_metrics.py
- **Retrieval cue**: When evaluating whether the external memory system remains compact, indexed, and executable without reading every doc.
- **Internal memory policy**: keep_pointer

### retrieval-self-test-procedure (active) — gpt-5-5-memory-improvement
- **Kind**: procedural
- **Summary**: Use scripts/retrieval_self_test.py to test whether realistic memory questions retrieve expected answers through inventory, search, and canonical files.
- **Path**: `scripts/retrieval_self_test.py`
- **URL**: https://github.com/ai-village-agents/gpt-5-5-memory-improvement/blob/main/scripts/retrieval_self_test.py
- **Retrieval cue**: When structural validation passes but I need to know whether future sessions can actually find the right memory.
- **Internal memory policy**: keep_pointer

### goal-transition-procedure (active) — gpt-5-5-memory-improvement
- **Kind**: procedural
- **Summary**: Use scripts/prepare_goal_transition.py after a real admin goal announcement to list the active-state files and validation steps needed for a safe goal switch.
- **Path**: `scripts/prepare_goal_transition.py`
- **URL**: https://github.com/ai-village-agents/gpt-5-5-memory-improvement/blob/main/scripts/prepare_goal_transition.py
- **Retrieval cue**: When Shoshannah/admin announces a new village goal or the active goal appears stale.
- **Internal memory policy**: keep_pointer

### active-memory-goal-d419 (active) — claude-opus-4-7-memory
- **Kind**: working
- **Summary**: Improve memory. Internal = bootloader stub; external = this repo, structured semantic/episodic/procedural/task-state.
- **Path**: `goals/active.md`
- **URL**: https://github.com/ai-village-agents/claude-opus-4-7-memory/blob/main/goals/active.md
- **Retrieval cue**: At session start, after bootloader.
- **Internal memory policy**: keep_summary

### bootloader (active) — claude-opus-4-7-memory
- **Kind**: procedural
- **Summary**: First action every session — git pull, cat goals/active.md + current_state.md + load_bearing.md, run audit.sh.
- **Path**: `SESSION_START.md`
- **URL**: https://github.com/ai-village-agents/claude-opus-4-7-memory/blob/main/SESSION_START.md
- **Retrieval cue**: First action of every session.
- **Internal memory policy**: keep_summary

### load-bearing-rules (active) — claude-opus-4-7-memory
- **Kind**: semantic
- **Summary**: Seven imperative rules read every session; rule
- **Path**: `load_bearing.md`
- **URL**: https://github.com/ai-village-agents/claude-opus-4-7-memory/blob/main/load_bearing.md
- **Retrieval cue**: Session start; before any high-cost action.
- **Internal memory policy**: keep_pointer

### lessons-archive (active) — claude-opus-4-7-memory
- **Kind**: semantic
- **Summary**: Eight failure backstories with runbook crossrefs; loaded on demand, not every session.
- **Path**: `lessons.md`
- **URL**: https://github.com/ai-village-agents/claude-opus-4-7-memory/blob/main/lessons.md
- **Retrieval cue**: When facing a similar-shaped failure or designing a related runbook.
- **Internal memory policy**: keep_pointer

### pre-send-chat-guard (active) — claude-opus-4-7-memory
- **Kind**: social
- **Summary**: Forced-action bash script + runbook to prevent duplicate-message sends. 3 incidents in 2 weeks.
- **Path**: `scripts/pre_send_chat.sh`
- **URL**: https://github.com/ai-village-agents/claude-opus-4-7-memory/blob/main/scripts/pre_send_chat.sh
- **Retrieval cue**: BEFORE every send_message_to_chat.
- **Internal memory policy**: keep_summary

### pre-consolidate-script (active) — claude-opus-4-7-memory
- **Kind**: procedural
- **Summary**: Worksheet at session end — git status, audit, blockers, next-session-goal candidate. Prevents pre-consolidate amnesia.
- **Path**: `scripts/pre_consolidate.sh`
- **URL**: https://github.com/ai-village-agents/claude-opus-4-7-memory/blob/main/scripts/pre_consolidate.sh
- **Retrieval cue**: Before every CONSOLIDATE call.
- **Internal memory policy**: keep_pointer

### respond-to-admin-runbook (active) — claude-opus-4-7-memory
- **Kind**: procedural
- **Summary**: How to process an admin/Shoshannah message — archive prior goal, write fresh goals/active.md verbatim, update internal CURRENT GOAL.
- **Path**: `runbooks/respond_to_admin.md`
- **URL**: https://github.com/ai-village-agents/claude-opus-4-7-memory/blob/main/runbooks/respond_to_admin.md
- **Retrieval cue**: When a new admin message is in events.
- **Internal memory policy**: keep_pointer

### search-history-runbook (active) — claude-opus-4-7-memory
- **Kind**: procedural
- **Summary**: Decision tree — check memory → check events → only then call search_history (10-day window limit).
- **Path**: `runbooks/search_history.md`
- **URL**: https://github.com/ai-village-agents/claude-opus-4-7-memory/blob/main/runbooks/search_history.md
- **Retrieval cue**: When tempted to call search_history.
- **Internal memory policy**: keep_pointer

### peer-feedback-runbook (active) — claude-opus-4-7-memory
- **Kind**: procedural
- **Summary**: Process for giving and receiving peer feedback on shared artifacts.
- **Path**: `runbooks/peer_feedback.md`
- **URL**: https://github.com/ai-village-agents/claude-opus-4-7-memory/blob/main/runbooks/peer_feedback.md
- **Retrieval cue**: When reviewing peer repo / output.
- **Internal memory policy**: keep_pointer

### decisions-log (active) — claude-opus-4-7-memory
- **Kind**: episodic
- **Summary**: Append-only architecture-decision log; 5 D419 entries explaining why specific design choices were made.
- **Path**: `decisions.md`
- **URL**: https://github.com/ai-village-agents/claude-opus-4-7-memory/blob/main/decisions.md
- **Retrieval cue**: When revisiting an architectural choice or proposing change.
- **Internal memory policy**: keep_pointer

### current-state-snapshot (active) — claude-opus-4-7-memory
- **Kind**: task-state
- **Summary**: Refreshed-at-consolidate snapshot — mid-flight tasks, open promises, last-session incidents, next safe action.
- **Path**: `current_state.md`
- **URL**: https://github.com/ai-village-agents/claude-opus-4-7-memory/blob/main/current_state.md
- **Retrieval cue**: Session start after goals/active.md.
- **Internal memory policy**: keep_pointer

### research-notes-memory (reference) — claude-opus-4-7-memory
- **Kind**: semantic
- **Summary**: SOTA agent-memory survey — MemGPT, Voyager, Generative Agents, A-MEM — mapped to my design choices.
- **Path**: `research_notes.md`
- **URL**: https://github.com/ai-village-agents/claude-opus-4-7-memory/blob/main/research_notes.md
- **Retrieval cue**: When justifying architecture or proposing major change.
- **Internal memory policy**: pointer_only

### retired-youtube-goal-pointer (retired) — claude-opus-4-7-memory
- **Kind**: pointer
- **Summary**: YouTube channel goal complete — V1–V6 published (8 subs), V7/V8 rendered-unpublished. Do not reopen unless admin reactivates.
- **Path**: `goals/archive/youtube_channel_d412-419.md`
- **URL**: https://github.com/ai-village-agents/claude-opus-4-7-memory/blob/main/goals/archive/youtube_channel_d412-419.md
- **Retrieval cue**: Only if YouTube goal reactivated, or asked about prior channel state.
- **Internal memory policy**: keep_pointer

### validate-inventory-script (active) — claude-opus-4-7-memory
- **Kind**: procedural
- **Summary**: Walks inventory.yaml `source:` paths and reports any missing. Catches drift between inventory and reality.
- **Path**: `scripts/validate_inventory.sh`
- **URL**: https://github.com/ai-village-agents/claude-opus-4-7-memory/blob/main/scripts/validate_inventory.sh
- **Retrieval cue**: At pre-consolidate (now wired into pre_consolidate.sh as section 5b).
- **Internal memory policy**: pointer_only

### query-inventory-script (active) — claude-opus-4-7-memory
- **Kind**: procedural
- **Summary**: Substring/kind/status filter over inventory.yaml. Useful when looking up which runbook addresses a situation without re-reading the whole repo.
- **Path**: `scripts/query_inventory.sh`
- **URL**: https://github.com/ai-village-agents/claude-opus-4-7-memory/blob/main/scripts/query_inventory.sh
- **Retrieval cue**: When trying to recall what artifact handles a topic.
- **Internal memory policy**: pointer_only

### boot-script (active) — claude-opus-4-7-memory
- **Kind**: procedural
- **Summary**: One-command bootloader. Internal memory says "bash /tmp/memory/boot.sh" instead of 4 separate cat commands. Includes clone fallback.
- **Path**: `boot.sh`
- **URL**: https://github.com/ai-village-agents/claude-opus-4-7-memory/blob/main/boot.sh
- **Retrieval cue**: First action of every session.
- **Internal memory policy**: keep_pointer

### search-memory-script (active) — claude-opus-4-7-memory
- **Kind**: procedural
- **Summary**: Grep-based keyword search across the whole memory repo with optional
--files-only and --kind {reflection,runbook,goal,all} filters. Capped
at 120 lines of output.

- **Path**: `scripts/search_memory.sh`
- **URL**: https://github.com/ai-village-agents/claude-opus-4-7-memory/blob/main/scripts/search_memory.sh
- **Retrieval cue**: when looking for a specific past event, decision, or incident and the runbook/lesson/reflection containing it is unknown.
- **Internal memory policy**: pointer_only

### peers-catalog (active) — claude-opus-4-7-memory
- **Kind**: semantic
- **Summary**: Catalog of peer #best agents — repo URLs, last-known HEADs, schema notes,
cross-agent agreements, and a refresh command snippet.

- **Path**: `peers/README.md`
- **URL**: https://github.com/ai-village-agents/claude-opus-4-7-memory/blob/main/peers/README.md
- **Retrieval cue**: when planning peer inspection or recalling which schema each agent uses.
- **Internal memory policy**: pointer_only

### skills-catalog (active) — claude-opus-4-7-memory
- **Kind**: semantic
- **Summary**: Catalog of capabilities — scaffolding tools, CLIs, browsers, persistence,
network, what I cannot do, and high-leverage patterns established.

- **Path**: `skills.md`
- **URL**: https://github.com/ai-village-agents/claude-opus-4-7-memory/blob/main/skills.md
- **Retrieval cue**: when planning new work and unsure whether I have a tool or when a new session needs orientation on what's available.
- **Internal memory policy**: pointer_only

### goals-index (active) — claude-opus-4-7-memory
- **Kind**: semantic
- **Summary**: Chronological roll of every village goal — active + archived + convention
for transitions. Cross-references goals/active.md and goals/archive/.

- **Path**: `goals/INDEX.md`
- **URL**: https://github.com/ai-village-agents/claude-opus-4-7-memory/blob/main/goals/INDEX.md
- **Retrieval cue**: when asked "what was the goal before this one" or planning a goal transition.
- **Internal memory policy**: pointer_only

### daily-log (active) — claude-opus-4-7-memory
- **Kind**: episodic
- **Summary**: One-line-per-session ultra-compressed log for fast "what happened recently"
glance. Format: D<day> s<session> (HH:MM PT) — <30-word summary>. [commit]

- **Path**: `daily_log.md`
- **URL**: https://github.com/ai-village-agents/claude-opus-4-7-memory/blob/main/daily_log.md
- **Retrieval cue**: at session start when needing quick recent-week context without reading full reflections.
- **Internal memory policy**: pointer_only

### meta-reflection (active) — claude-opus-4-7-memory
- **Kind**: semantic
- **Summary**: Synthesis layer over per-session reflections. Captures cross-session
patterns (7 patterns from D419 s1–s7) that don't show up from any single
reflection. Includes promotion path for new patterns. Inspired by
Generative Agents reflection layer (Park et al. 2023).

- **Path**: `reflections/META.md`
- **URL**: https://github.com/ai-village-agents/claude-opus-4-7-memory/blob/main/reflections/META.md
- **Retrieval cue**: when wondering "what patterns hold across my recent sessions?" or at goal-transition review time.
- **Internal memory policy**: pointer_only

### bash-safety-runbook (active) — claude-opus-4-7-memory
- **Kind**: procedural
- **Summary**: Pre-call checklist for the bash tool. Adapted from Kimi K2.6's
runbooks/bash_command.md (D419) with my own gotchas
(codex 300s timeout, seq -w not zero-padding, heredoc quoting).

- **Path**: `runbooks/bash_safety.md`
- **URL**: https://github.com/ai-village-agents/claude-opus-4-7-memory/blob/main/runbooks/bash_safety.md
- **Retrieval cue**: every bash tool call (high-cost ones especially — git push, ffmpeg, codex, anything destructive).
- **Internal memory policy**: pointer_only

### use-computer-safety-runbook (active) — claude-opus-4-7-memory
- **Kind**: procedural
- **Summary**: Pre-action checklist for GUI tool calls. Adapted from Kimi K2.6's
runbooks/use_computer.md (D419) with my YouTube-flow specifics
(GTK file picker ENTER not double-click, dialog Ctrl+- zoom, etc.).

- **Path**: `runbooks/use_computer_safety.md`
- **URL**: https://github.com/ai-village-agents/claude-opus-4-7-memory/blob/main/runbooks/use_computer_safety.md
- **Retrieval cue**: every use_computer action, especially clicks/drags on unfamiliar UI.
- **Internal memory policy**: pointer_only

### memory-smoke-test (active) — claude-opus-4-7-memory
- **Kind**: gate
- **Summary**: Codifies "is my memory system healthy?" — 59 invariants covering
core file presence, scripts, runbooks, inventory validation, git
state, boot.sh output sections, lessons.md L1-L10, load_bearing
rules 0-7. Exits non-zero on any FAIL. Inspired by GPT-5.5's
scripts/memory_smoke_test.py.

- **Path**: `scripts/memory_smoke_test.sh`
- **URL**: https://github.com/ai-village-agents/claude-opus-4-7-memory/blob/main/scripts/memory_smoke_test.sh
- **Retrieval cue**: every few sessions, and before any consolidate where I suspect repo drift; auto-run from pre_consolidate.sh.
- **Internal memory policy**: pointer_only

### check-peers (active) — claude-opus-4-7-memory
- **Kind**: script
- **Summary**: One-command wrapper around `gh api repos/.../commits` for the three
#best peers (GPT-5.5, Gemini 3.5 Flash, Kimi K2.6). Prints last N
commits per repo (default N=3). Eliminates the inline escaping
foot-gun of running the command from internal memory.

- **Path**: `scripts/check_peers.sh`
- **URL**: https://github.com/ai-village-agents/claude-opus-4-7-memory/blob/main/scripts/check_peers.sh
- **Retrieval cue**: "What have peers done since my last session?" → `bash scripts/check_peers.sh`

- **Internal memory policy**: pointer_only

### check-memory-cues (active) — claude-opus-4-7-memory
- **Kind**: script
- **Summary**: Validate a drafted internal-memory block against load-bearing cues.
Inspired by GPT-5.5's check_compact_memory_draft.py (D419 71c0fdd).
Required cues (must be present): "Improve your memory", repo name,
bootloader command, room, pre_send_chat.sh, AGENT_TALK, stale-PASS,
structural, Shoshannah, runbooks/respond_to_admin, validate_inventory.
Forbidden cues (anti-patterns): listing the archived YouTube goal as
active. Size budget: ≤300 lines, ≤18000 chars.

- **Path**: `scripts/check_memory_cues.sh`
- **URL**: https://github.com/ai-village-agents/claude-opus-4-7-memory/blob/main/scripts/check_memory_cues.sh
- **Retrieval cue**: "I'm drafting my next internal memory at consolidate-time — what must
it contain / not contain?" → echo "<draft>" | bash scripts/check_memory_cues.sh

- **Internal memory policy**: pointer_only

### retrieval-self-test (active) — claude-opus-4-7-memory
- **Kind**: procedural
- **Summary**: Validates memory retrieval works end-to-end. 23 fixed tests across query_inventory.sh, search_memory.sh, and direct cat. Catches inventory drift, missing files, broken cues. Run before/after major memory changes.
- **Path**: `scripts/retrieval_self_test.sh`
- **URL**: https://github.com/ai-village-agents/claude-opus-4-7-memory/blob/main/scripts/retrieval_self_test.sh
- **Retrieval cue**: before/after consolidate; when adding/moving inventory items; when query_inventory or search_memory yield surprising results.
- **Internal memory policy**: keep_pointer

### goal-transition (active) — claude-opus-4-7-memory
- **Kind**: script
- **Summary**: Automates goal-transition flow (D420+): archives goals/active.md, writes fresh active.md from verbatim text, patches REQUIRED cue in check_memory_cues.sh AND embedded draft in memory_smoke_test.sh, updates INDEX, appends changelog, runs validate+smoke.
- **Path**: `scripts/goal_transition.py`
- **URL**: https://github.com/ai-village-agents/claude-opus-4-7-memory/blob/main/scripts/goal_transition.py
- **Retrieval cue**: When admin announces a new village goal: archive, write, patch cues+smoke, INDEX, changelog, validate.
- **Internal memory policy**: pointer_only

### test-validate-handles-quotes (active) — claude-opus-4-7-memory
- **Kind**: test
- **Summary**: L13 backstop: appends a quote-containing summary to inventory and runs validate_inventory.sh, asserting exit 0 and no xargs unmatched-quote error.
- **Path**: `scripts/_test_validate_handles_quotes.py`
- **URL**: https://github.com/ai-village-agents/claude-opus-4-7-memory/blob/main/scripts/_test_validate_handles_quotes.py
- **Retrieval cue**: When checking validate_inventory.sh quote-safety / L13 regression coverage.
- **Internal memory policy**: pointer_only

### memory-metrics (active) — claude-opus-4-7-memory
- **Kind**: script
- **Summary**: Compact health snapshot of the memory repo: git state, active goal, inventory stats (status/kind/policy distributions), required-guard presence, lessons/META counts, runbook list, daily-log entries, key file sizes, retrieval affordances summary. Inspired by GPT-5.5 memory_metrics.py. Exits non-zero if any required guard script is missing.
- **Path**: `scripts/memory_metrics.sh`
- **URL**: https://github.com/ai-village-agents/claude-opus-4-7-memory/blob/main/scripts/memory_metrics.sh
- **Retrieval cue**: Quick health snapshot of memory repo: bash scripts/memory_metrics.sh
- **Internal memory policy**: pointer_only

### identity_profile (active) — gemini-3-5-flash-memory-vault
- **Kind**: semantic
- **Summary**: Full profile, role, schedules, and emails of all 15 agents in the AI Village.
- **Path**: `identity/profile.md`
- **URL**: https://github.com/ai-village-agents/gemini-3-5-flash-memory-vault/blob/master/identity/profile.md
- **Retrieval cue**: Find email addresses or active room assignments for any agent.
- **Internal memory policy**: Always keep room assignments and emails hot in L1 internal memory.

### sota_memory_research (active) — gemini-3-5-flash-memory-vault
- **Kind**: semantic
- **Summary**: Literature review of MemGPT, Generative Agents, Voyager, and Reflexion memory models.
- **Path**: `principles/sota_research.md`
- **URL**: https://github.com/ai-village-agents/gemini-3-5-flash-memory-vault/blob/master/principles/sota_research.md
- **Retrieval cue**: Research state-of-the-art memory mechanisms or mathematical mappings.
- **Internal memory policy**: Reference only on-demand; keep cold in L2.

### aligned_memory_schemas (active) — gemini-3-5-flash-memory-vault
- **Kind**: semantic
- **Summary**: Structural taxonomies dividing the external vault into Semantic, Procedural, and Episodic files.
- **Path**: `principles/schemas.md`
- **URL**: https://github.com/ai-village-agents/gemini-3-5-flash-memory-vault/blob/master/principles/schemas.md
- **Retrieval cue**: Verify folder alignment and file classification rules.
- **Internal memory policy**: Strict compliance, verified on every consolidation call.

### standard_operating_procedures (active) — gemini-3-5-flash-memory-vault
- **Kind**: procedural
- **Summary**: Manual step-by-step checklists for pre-action, pre-send chat, and pre-consolidation.
- **Path**: `runbooks/checklists.md`
- **URL**: https://github.com/ai-village-agents/gemini-3-5-flash-memory-vault/blob/master/runbooks/checklists.md
- **Retrieval cue**: Execute whenever initiating a tool call, chat send, or session consolidation.
- **Internal memory policy**: Always reference procedurally on every relevant trigger.

### historical_milestones_and_failures (active) — gemini-3-5-flash-memory-vault
- **Kind**: reflection
- **Summary**: Chronological log of YouTube channel video metrics, comments, and failure-mode post-mortems.
- **Path**: `reflections/episodes.md`
- **URL**: https://github.com/ai-village-agents/gemini-3-5-flash-memory-vault/blob/master/reflections/episodes.md
- **Retrieval cue**: Analyze past errors, video results, or historical milestones.
- **Internal memory policy**: Keep cold in L2; retain only minimal pointers in L1.

### active_goal_tracker (active) — gemini-3-5-flash-memory-vault
- **Kind**: episodic
- **Summary**: Real-time task tracker for the ongoing 'Improve Your Memory!' goal.
- **Path**: `goals/active.md`
- **URL**: https://github.com/ai-village-agents/gemini-3-5-flash-memory-vault/blob/master/goals/active.md
- **Retrieval cue**: Identify immediate active tasks, coordination gates, and next steps.
- **Internal memory policy**: Always update before consolidation and load in L1 bootloader.

### capabilities_and_skills (active) — gemini-3-5-flash-memory-vault
- **Kind**: semantic
- **Summary**: Capabilities and skills catalog including technical mathematical, programmatic, animation, and safeguard skills.
- **Path**: `identity/skills.md`
- **URL**: https://github.com/ai-village-agents/gemini-3-5-flash-memory-vault/blob/master/identity/skills.md
- **Retrieval cue**: Check list of capabilities, mathematical or programmatic skills.
- **Internal memory policy**: Reference only on-demand; keep cold in L2.

### chronological_goals_index (active) — gemini-3-5-flash-memory-vault
- **Kind**: semantic
- **Summary**: Chronological history of all village goals with their dates, status, and summaries.
- **Path**: `goals/INDEX.md`
- **URL**: https://github.com/ai-village-agents/gemini-3-5-flash-memory-vault/blob/master/goals/INDEX.md
- **Retrieval cue**: Look up past village goals, chronological progress, or milestone histories.
- **Internal memory policy**: Reference only on-demand; keep cold in L2.

### session_operations_log (active) — gemini-3-5-flash-memory-vault
- **Kind**: episodic
- **Summary**: Session-by-session operations log tracking specific tasks and outcomes of Day 419.
- **Path**: `reflections/daily_log.md`
- **URL**: https://github.com/ai-village-agents/gemini-3-5-flash-memory-vault/blob/master/reflections/daily_log.md
- **Retrieval cue**: View detailed operations list or specific daily session tasks.
- **Internal memory policy**: Reference only on-demand; keep cold in L2.

### peer_vault_registry (active) — gemini-3-5-flash-memory-vault
- **Kind**: semantic
- **Summary**: Registry of #best room peer repositories and cross-compatibility principles.
- **Path**: `peers/README.md`
- **URL**: https://github.com/ai-village-agents/gemini-3-5-flash-memory-vault/blob/master/peers/README.md
- **Retrieval cue**: Look up GPT-5.5, Claude 4.7, or Kimi 2.6 memory repo URLs.
- **Internal memory policy**: Reference only on-demand; keep cold in L2.

### session_bootloader_script (active) — gemini-3-5-flash-memory-vault
- **Kind**: procedural
- **Summary**: Automated session initialization script.
- **Path**: `scripts/boot.py`
- **URL**: https://github.com/ai-village-agents/gemini-3-5-flash-memory-vault/blob/master/scripts/boot.py
- **Retrieval cue**: Use on startup to synchronize and validate the workspace.
- **Internal memory policy**: Execute as first action of every session.

### pre_send_chat_guard_script (active) — gemini-3-5-flash-memory-vault
- **Kind**: procedural
- **Summary**: Chat guard script blocking duplicate sends and formatting violations.
- **Path**: `scripts/pre_send_chat.py`
- **URL**: https://github.com/ai-village-agents/gemini-3-5-flash-memory-vault/blob/master/scripts/pre_send_chat.py
- **Retrieval cue**: Run to programmatically validate any outgoing chat message.
- **Internal memory policy**: Execute before every send_message_to_chat call.

### pre_consolidation_guard_script (active) — gemini-3-5-flash-memory-vault
- **Kind**: procedural
- **Summary**: Consolidation schema check and git sync utility.
- **Path**: `scripts/pre_consolidate.py`
- **URL**: https://github.com/ai-village-agents/gemini-3-5-flash-memory-vault/blob/master/scripts/pre_consolidate.py
- **Retrieval cue**: Run to verify repository conformity before calling consolidate.
- **Internal memory policy**: Execute before calling consolidate.

### prepare_consolidation_script (active) — gemini-3-5-flash-memory-vault
- **Kind**: procedural
- **Summary**: Automated script to log sessions, validate inventory, compile L1 memory, and check git status.
- **Path**: `scripts/prepare_consolidation.py`
- **URL**: https://github.com/ai-village-agents/gemini-3-5-flash-memory-vault/blob/master/scripts/prepare_consolidation.py
- **Retrieval cue**: Use before calling consolidate to ensure session is logged and L1 draft is compiled.
- **Internal memory policy**: Execute procedurally on every consolidation preparation trigger.

### scan_peers_script (active) — gemini-3-5-flash-memory-vault
- **Kind**: procedural
- **Summary**: Automated Python script to fetch, consolidate, and search the metadata inventories of all 14 village memory repositories.
- **Path**: `scripts/scan_peers.py`
- **URL**: https://github.com/ai-village-agents/gemini-3-5-flash-memory-vault/blob/master/scripts/scan_peers.py
- **Retrieval cue**: Search or consolidate metadata inventories from peer agents.
- **Internal memory policy**: Execute to pull peer updates and search cross-agent collective memory.

### consolidated_peer_inventory (active) — gemini-3-5-flash-memory-vault
- **Kind**: semantic
- **Summary**: Consolidated JSON index containing metadata items harvested from successfully scanned peer memory vaults.
- **Path**: `peers/consolidated_inventory.json`
- **URL**: https://github.com/ai-village-agents/gemini-3-5-flash-memory-vault/blob/master/peers/consolidated_inventory.json
- **Retrieval cue**: Cross-reference or locate files and memory schemas across all village agents.
- **Internal memory policy**: Read-only searchable catalog, updated via scan_peers.py.

### check_memory_cues_script (active) — gemini-3-5-flash-memory-vault
- **Kind**: procedural
- **Summary**: Automated Python script to enforce size limits (character count and line count) and verify presence of required cues and absence of forbidden cues.
- **Path**: `scripts/check_memory_cues.py`
- **URL**: https://github.com/ai-village-agents/gemini-3-5-flash-memory-vault/blob/master/scripts/check_memory_cues.py
- **Retrieval cue**: Run to verify if a drafted L1 memory block or file complies with size and structural requirements.
- **Internal memory policy**: Execute during consolidation pipeline via pre_consolidate.py.

### retrieval_self_test_script (active) — gemini-3-5-flash-memory-vault
- **Kind**: procedural
- **Summary**: Automated retrieval self-test suite running 15 validation cases.
- **Path**: `scripts/retrieval_self_test.py`
- **URL**: https://github.com/ai-village-agents/gemini-3-5-flash-memory-vault/blob/master/scripts/retrieval_self_test.py
- **Retrieval cue**: Run to verify that memory engine is searching and retrieving correctly.
- **Internal memory policy**: Execute to test retrieval correctness.

### gpt52.active (active) — gpt-5-2-memory-improvement
- **Kind**: semantic
- **Summary**: Day anchor with NOW/NEXT focus and open loops.
- **Path**: ``
- **URL**: https://github.com/ai-village-agents/gpt-5-2-memory-improvement/blob/main/
- **Retrieval cue**: top line + NEXT bullets for current session
- **Internal memory policy**: 

### gpt52.core (stable) — gpt-5-2-memory-improvement
- **Kind**: semantic
- **Summary**: Durable facts, constraints, and canonical links.
- **Path**: ``
- **URL**: https://github.com/ai-village-agents/gpt-5-2-memory-improvement/blob/main/
- **Retrieval cue**: core rules + canonical URLs/paths
- **Internal memory policy**: 

### gpt52.principles (stable) — gpt-5-2-memory-improvement
- **Kind**: gate
- **Summary**: Cross-episode guardrails and decision heuristics.
- **Path**: ``
- **URL**: https://github.com/ai-village-agents/gpt-5-2-memory-improvement/blob/main/
- **Retrieval cue**: quick rules to prevent drift
- **Internal memory policy**: 

### gpt52.public_comms (active) — gpt-5-2-memory-improvement
- **Kind**: pointer
- **Summary**: Log of outbound announcements and duplicate-avoidance notes.
- **Path**: ``
- **URL**: https://github.com/ai-village-agents/gpt-5-2-memory-improvement/blob/main/
- **Retrieval cue**: check before posting anything public
- **Internal memory policy**: 

### gpt52.memory_cli (stable) — gpt-5-2-memory-improvement
- **Kind**: procedural
- **Summary**: CLI for status checks, search, and timestamped log entries.
- **Path**: ``
- **URL**: https://github.com/ai-village-agents/gpt-5-2-memory-improvement/blob/main/
- **Retrieval cue**: run python scripts/memory.py status/search/log
- **Internal memory policy**: 

### gpt52.session_start_script (active) — gpt-5-2-memory-improvement
- **Kind**: procedural
- **Summary**: One-shot session opener running audit plus memory status/brief (STRICT=1 to enforce audit exit).
- **Path**: ``
- **URL**: https://github.com/ai-village-agents/gpt-5-2-memory-improvement/blob/main/
- **Retrieval cue**: bash scripts/session_start.sh
- **Internal memory policy**: 

### gpt52.session_end_script (active) — gpt-5-2-memory-improvement
- **Kind**: procedural
- **Summary**: Session wrap that runs pre_consolidate and prints logging/commit reminders.
- **Path**: ``
- **URL**: https://github.com/ai-village-agents/gpt-5-2-memory-improvement/blob/main/
- **Retrieval cue**: bash scripts/session_end.sh
- **Internal memory policy**: 

### gpt52.pre_send_guard (active) — gpt-5-2-memory-improvement
- **Kind**: gate
- **Summary**: Executable guard to block duplicate or risky public comms.
- **Path**: ``
- **URL**: https://github.com/ai-village-agents/gpt-5-2-memory-improvement/blob/main/
- **Retrieval cue**: run before any non-trivial outbound post
- **Internal memory policy**: 

### gpt52.internal_schema (stable) — gpt-5-2-memory-improvement
- **Kind**: semantic
- **Summary**: 5-bucket internal memory schema and definitions.
- **Path**: ``
- **URL**: https://github.com/ai-village-agents/gpt-5-2-memory-improvement/blob/main/
- **Retrieval cue**: schema reference for bucket naming
- **Internal memory policy**: 

### gpt52.memory_protocol (stable) — gpt-5-2-memory-improvement
- **Kind**: procedural
- **Summary**: Session start and in-session protocol for memory upkeep.
- **Path**: ``
- **URL**: https://github.com/ai-village-agents/gpt-5-2-memory-improvement/blob/main/
- **Retrieval cue**: step-by-step routine to open and update memory
- **Internal memory policy**: 

### gpt52.send_message_runbook (active) — gpt-5-2-memory-improvement
- **Kind**: procedural
- **Summary**: Anti-duplicate runbook for outbound chat messages.
- **Path**: ``
- **URL**: https://github.com/ai-village-agents/gpt-5-2-memory-improvement/blob/main/
- **Retrieval cue**: follow before announcements; pairs with pre_send_chat.py
- **Internal memory policy**: 

### gpt52.repo_pointer (stable) — gpt-5-2-memory-improvement
- **Kind**: pointer
- **Summary**: Canonical repository URL for external access and history.
- **Path**: ``
- **URL**: https://github.com/ai-village-agents/gpt-5-2-memory-improvement/blob/main/
- **Retrieval cue**: open in browser for full history and diffs
- **Internal memory policy**: 

### gpt52.internal_memory_bootloader (active) — gpt-5-2-memory-improvement
- **Kind**: procedural
- **Summary**: Copy/pasteable lean internal-memory bootloader (5 buckets) pointing to repo + start-of-session commands.
- **Path**: ``
- **URL**: https://github.com/ai-village-agents/gpt-5-2-memory-improvement/blob/main/
- **Retrieval cue**: use when rewriting internal memory into a short router
- **Internal memory policy**: 

### gpt52.internal_memory_candidate_checker (active) — gpt-5-2-memory-improvement
- **Kind**: gate
- **Summary**: One-shot validator for internal-memory drafts (required anchors + sensitive marker check).
- **Path**: ``
- **URL**: https://github.com/ai-village-agents/gpt-5-2-memory-improvement/blob/main/
- **Retrieval cue**: python scripts/check_internal_memory_candidate.py --file <path>
- **Internal memory policy**: 

### gpt52.find_inventories_in_org (active) — gpt-5-2-memory-improvement
- **Kind**: procedural
- **Summary**: Search ai-village-agents repos for inventory.yaml candidates via gh search code.
- **Path**: ``
- **URL**: https://github.com/ai-village-agents/gpt-5-2-memory-improvement/blob/main/
- **Retrieval cue**: python scripts/find_inventories_in_org.py --org ai-village-agents --format table
- **Internal memory policy**: 

### gpt52.uncertainty_pacing_runbook (active) — gpt-5-2-memory-improvement
- **Kind**: procedural
- **Summary**: Pacing plan for periods of uncertainty (avoid repeated idling while waiting on announcements).
- **Path**: ``
- **URL**: https://github.com/ai-village-agents/gpt-5-2-memory-improvement/blob/main/
- **Retrieval cue**: when repeatedly checking Day N+1 yields nothing, use this runbook
- **Internal memory policy**: 

### principles (active) — opus-46-memory
- **Kind**: semantic
- **Summary**: 12 cross-episode behavioral rules abstracted from 419 days
- **Path**: `principles.md`
- **URL**: https://github.com/ai-village-agents/opus-46-memory/blob/main/principles.md
- **Retrieval cue**: What rules should guide my behavior?
- **Internal memory policy**: pointer-only

### technical-notes (active) — opus-46-memory
- **Kind**: procedural
- **Summary**: Platform workarounds: bash, Firefox, git, PIL, ffmpeg, gTTS
- **Path**: `technical-notes.md`
- **URL**: https://github.com/ai-village-agents/opus-46-memory/blob/main/technical-notes.md
- **Retrieval cue**: How do I work around a technical issue?
- **Internal memory policy**: top-3-inline-rest-pointer

### project-archive (active) — opus-46-memory
- **Kind**: episodic
- **Summary**: Compressed summaries of all 24 village goals
- **Path**: `project-archive.md`
- **URL**: https://github.com/ai-village-agents/opus-46-memory/blob/main/project-archive.md
- **Retrieval cue**: What did we do in goal X?
- **Internal memory policy**: pointer-only

### peer-directory (active) — opus-46-memory
- **Kind**: social
- **Summary**: Agent relationships, expertise, collaboration history
- **Path**: `peer-directory.md`
- **URL**: https://github.com/ai-village-agents/opus-46-memory/blob/main/peer-directory.md
- **Retrieval cue**: Who should I collaborate with on X?
- **Internal memory policy**: pointer-only

### comms-log (active) — opus-46-memory
- **Kind**: gate
- **Summary**: Messages sent today — prevents duplicate announcements
- **Path**: `comms-log.md`
- **URL**: https://github.com/ai-village-agents/opus-46-memory/blob/main/comms-log.md
- **Retrieval cue**: Have I already said this?
- **Internal memory policy**: count-inline-details-pointer

### settled-facts (active) — opus-46-memory
- **Kind**: semantic
- **Summary**: Verified stable facts that don't need re-checking
- **Path**: `settled-facts.md`
- **URL**: https://github.com/ai-village-agents/opus-46-memory/blob/main/settled-facts.md
- **Retrieval cue**: Is this still true? Do I need to re-verify?
- **Internal memory policy**: pointer-only

### pre-send-guard (active) — opus-46-memory
- **Kind**: gate
- **Summary**: Executable guard — blocks chat on missing fields or vague dup check
- **Path**: `scripts/pre-send-chat.sh`
- **URL**: https://github.com/ai-village-agents/opus-46-memory/blob/main/scripts/pre-send-chat.sh
- **Retrieval cue**: Before sending a chat message
- **Internal memory policy**: command-inline

### pre-consolidate (active) — opus-46-memory
- **Kind**: gate
- **Summary**: Generates consolidation worksheet with repo state and checklist
- **Path**: `scripts/pre-consolidate.sh`
- **URL**: https://github.com/ai-village-agents/opus-46-memory/blob/main/scripts/pre-consolidate.sh
- **Retrieval cue**: Before calling consolidate
- **Internal memory policy**: command-inline

### goal-transition (active) — opus-46-memory
- **Kind**: procedural
- **Summary**: Automates archival steps when goals change
- **Path**: `scripts/goal-transition.sh`
- **URL**: https://github.com/ai-village-agents/opus-46-memory/blob/main/scripts/goal-transition.sh
- **Retrieval cue**: When a new goal is announced
- **Internal memory policy**: command-inline

### audit (active) — opus-46-memory
- **Kind**: gate
- **Summary**: Validates all required files, reports metrics
- **Path**: `scripts/audit-memory.sh`
- **URL**: https://github.com/ai-village-agents/opus-46-memory/blob/main/scripts/audit-memory.sh
- **Retrieval cue**: Is my memory system healthy?
- **Internal memory policy**: command-inline

### scan-inventories (active) — opus-46-memory
- **Kind**: procedural
- **Summary**: Cross-agent inventory aggregator with YAML fallback parser (118 items across 10 repos)
- **Path**: `scripts/scan-inventories.py`
- **URL**: https://github.com/ai-village-agents/opus-46-memory/blob/main/scripts/scan-inventories.py
- **Retrieval cue**: When checking what other agents have built or finding shared patterns
- **Internal memory policy**: command-inline

### bootloader-draft (active) — opus-46-memory
- **Kind**: procedural
- **Summary**: Bootloader memory draft — 2764 chars (53% reduction), template for consolidation
- **Path**: `bootloader-draft-day419.md`
- **URL**: https://github.com/ai-village-agents/opus-46-memory/blob/main/bootloader-draft-day419.md
- **Retrieval cue**: At consolidation time to guide internal memory compression
- **Internal memory policy**: pointer-only

### self-evaluation (active) — opus-46-memory
- **Kind**: semantic
- **Summary**: Memory system self-evaluation against 5 shared metrics (compression, retrieval, duplicates, temporal, efficiency)
- **Path**: ``
- **URL**: https://github.com/ai-village-agents/opus-46-memory/blob/main/
- **Retrieval cue**: How well does my memory system perform? What are its strengths and gaps?
- **Internal memory policy**: pointer-only

### render-bootloader (active) — opus-46-memory
- **Kind**: procedural
- **Summary**: Auto-generates bootloader-format internal memory from current repo state (2476 chars)
- **Path**: ``
- **URL**: https://github.com/ai-village-agents/opus-46-memory/blob/main/
- **Retrieval cue**: How do I generate my consolidation memory? What format should internal memory use?
- **Internal memory policy**: pointer-only

### village-playbook (active) — opus-46-memory
- **Kind**: semantic
- **Summary**: Synthesized best practices from 16 agents — bootloader pattern, guards, inventory standard, anti-patterns, metrics
- **Path**: `village-memory-playbook.md`
- **URL**: https://github.com/ai-village-agents/opus-46-memory/blob/main/village-memory-playbook.md
- **Retrieval cue**: What are the best practices for memory systems? How should I set up my memory?
- **Internal memory policy**: pointer-only

### memory-recipes (active) — opus-46-memory
- **Kind**: procedural
- **Summary**: Quick-reference recipes for 7 common goal situations (coding, collaboration, research, creative, transition, debugging, waiting)
- **Path**: `memory-recipes.md`
- **URL**: https://github.com/ai-village-agents/opus-46-memory/blob/main/memory-recipes.md
- **Retrieval cue**: How should I approach this type of goal? What's the workflow?
- **Internal memory policy**: pointer-only

### village-inventory-analysis (active) — opus-46-memory
- **Kind**: semantic
- **Summary**: Analysis of 81 items from 7 agents: 3 agent archetypes (gate-heavy, semantic-heavy, procedural-heavy), gate convergence patterns, retrieval cue design, memory policy gaps
- **Path**: ``
- **URL**: https://github.com/ai-village-agents/opus-46-memory/blob/main/
- **Retrieval cue**: What patterns exist across agent memory inventories?
- **Internal memory policy**: pointer-only

### naming-convention-proposal (active) — opus-46-memory
- **Kind**: semantic
- **Summary**: Proposal for standardized cross-agent naming: guard-, runbook-, knowledge-, log-, pointer- prefixes
- **Path**: ``
- **URL**: https://github.com/ai-village-agents/opus-46-memory/blob/main/
- **Retrieval cue**: How should inventory items be named for cross-agent compatibility?
- **Internal memory policy**: pointer-only

### failure-prevention-analysis (active) — opus-46-memory
- **Kind**: reflection
- **Summary**: Maps 6 past failures to current memory improvements — 4/6 fully prevented, 2/6 partially mitigated
- **Path**: ``
- **URL**: https://github.com/ai-village-agents/opus-46-memory/blob/main/
- **Retrieval cue**: Would the new memory system have prevented past mistakes?
- **Internal memory policy**: pointer-only

### goal-24-final-summary (active) — opus-46-memory
- **Kind**: episodic
- **Summary**: Complete arc of Goal 24 accomplishments: 38 files, 10 scripts, 71 commits, metrics, insights
- **Path**: ``
- **URL**: https://github.com/ai-village-agents/opus-46-memory/blob/main/
- **Retrieval cue**: What did I accomplish during the memory improvement goal?
- **Internal memory policy**: pointer-only

### lean-memory-draft (active) — opus-46-memory
- **Kind**: procedural
- **Summary**: Pre-drafted 2793-char internal memory template for post-goal transition — 65% reduction
- **Path**: ``
- **URL**: https://github.com/ai-village-agents/opus-46-memory/blob/main/
- **Retrieval cue**: What should my lean internal memory look like after goal transition?
- **Internal memory policy**: pointer-only

### goal-transition-prep-day420 (active) — opus-46-memory
- **Kind**: procedural
- **Summary**: Checklist for clean goal transition: what to keep, archive, and add in internal memory
- **Path**: ``
- **URL**: https://github.com/ai-village-agents/opus-46-memory/blob/main/
- **Retrieval cue**: How do I transition to the next goal cleanly?
- **Internal memory policy**: pointer-only

### naming-convention-v2 (active) — opus-46-memory
- **Kind**: semantic
- **Summary**: Village naming convention v2: pre- for gates, runbook- for procedures, principles- for semantic — based on 96% organic convergence
- **Path**: ``
- **URL**: https://github.com/ai-village-agents/opus-46-memory/blob/main/
- **Retrieval cue**: What naming convention should inventory items follow?
- **Internal memory policy**: pointer-only

### memory-meta-lessons (active) — opus-46-memory
- **Kind**: semantic
- **Summary**: Distilled operational guidance from 11 sessions: bootloader pattern, executable > declarative, compression lessons, anti-patterns
- **Path**: ``
- **URL**: https://github.com/ai-village-agents/opus-46-memory/blob/main/
- **Retrieval cue**: What are the key takeaways from memory improvement work?
- **Internal memory policy**: pointer-only

### gpt54.session_start (active) — gpt-5-4-memory-kit
- **Kind**: procedural
- **Summary**: Session-start helper that audits the memory store and prints the five-bucket brief.
- **Path**: ``
- **URL**: https://github.com/ai-village-agents/gpt-5-4-memory-kit/blob/main/
- **Retrieval cue**: Run at the start of a session to orient quickly before any substantive work.
- **Internal memory policy**: 

### gpt54.lean_memory_render (active) — gpt-5-4-memory-kit
- **Kind**: procedural
- **Summary**: Renders a compact internal-memory candidate from the JSON memory store with CHAR_COUNT output.
- **Path**: ``
- **URL**: https://github.com/ai-village-agents/gpt-5-4-memory-kit/blob/main/
- **Retrieval cue**: Run before consolidation or when checking whether the always-loaded memory candidate is getting too large.
- **Internal memory policy**: 

### gpt54.memory_candidate_checker (active) — gpt-5-4-memory-kit
- **Kind**: gate
- **Summary**: Checks a real consolidation candidate file against required lean-memory anchor cues and do_not_repeat topics.
- **Path**: ``
- **URL**: https://github.com/ai-village-agents/gpt-5-4-memory-kit/blob/main/
- **Retrieval cue**: Run when calibrating a future real consolidation candidate against the current lean-memory target.
- **Internal memory policy**: 

### gpt54.prepare_consolidation (active) — gpt-5-4-memory-kit
- **Kind**: gate
- **Summary**: Preferred wrapper that writes a lean-memory candidate file and immediately runs pre-consolidation checks against it.
- **Path**: ``
- **URL**: https://github.com/ai-village-agents/gpt-5-4-memory-kit/blob/main/
- **Retrieval cue**: Run as the default one-command pre-consolidation flow.
- **Internal memory policy**: 

### gpt54.pre_send_chat_guard (active) — gpt-5-4-memory-kit
- **Kind**: gate
- **Summary**: Pre-send guard that blocks vague duplicate checks and surfaces do_not_repeat public-comms items.
- **Path**: ``
- **URL**: https://github.com/ai-village-agents/gpt-5-4-memory-kit/blob/main/
- **Retrieval cue**: Run before any public room update, status message, or commit announcement.
- **Internal memory policy**: 

### gpt54.pre_consolidate_guard (active) — gpt-5-4-memory-kit
- **Kind**: gate
- **Summary**: Pre-consolidation guard that checks next-session goal fields, audit status, repo cleanliness, and rendered CHAR_COUNT.
- **Path**: ``
- **URL**: https://github.com/ai-village-agents/gpt-5-4-memory-kit/blob/main/
- **Retrieval cue**: Run immediately before calling consolidate to catch avoidable memory-handoff mistakes.
- **Internal memory policy**: 

### gpt54.public_comms_logger (active) — gpt-5-4-memory-kit
- **Kind**: procedural
- **Summary**: Logger that appends a new announced or do_not_repeat entry to public_comms.json with duplicate-topic protection.
- **Path**: ``
- **URL**: https://github.com/ai-village-agents/gpt-5-4-memory-kit/blob/main/
- **Retrieval cue**: Run after a meaningful public message so the memory store matches what was actually said.
- **Internal memory policy**: 

### gpt54.public_comms_pruner (active) — gpt-5-4-memory-kit
- **Kind**: procedural
- **Summary**: Maintenance helper that keeps only recent announced entries in public_comms.json and archives older announced history with id-based dedup.
- **Path**: ``
- **URL**: https://github.com/ai-village-agents/gpt-5-4-memory-kit/blob/main/
- **Retrieval cue**: Run periodically when public_comms announced history grows and you want compact active memory without losing archive history.
- **Internal memory policy**: 

### gpt54.memory_store_audit (active) — gpt-5-4-memory-kit
- **Kind**: gate
- **Summary**: Audit tool that validates the five JSON memory buckets and warns about schema drift or bloat.
- **Path**: ``
- **URL**: https://github.com/ai-village-agents/gpt-5-4-memory-kit/blob/main/
- **Retrieval cue**: Run when editing the memory store directly or before trusting changed external-memory state.
- **Internal memory policy**: 

### gpt54.inventory_validator (active) — gpt-5-4-memory-kit
- **Kind**: gate
- **Summary**: Inventory validator that checks required shared fields, duplicate ids, and relative source file existence.
- **Path**: ``
- **URL**: https://github.com/ai-village-agents/gpt-5-4-memory-kit/blob/main/
- **Retrieval cue**: Run after editing inventory.yaml or adding a new indexed component.
- **Internal memory policy**: 

### gpt54.always_loaded_anchors (stable) — gpt-5-4-memory-kit
- **Kind**: semantic
- **Summary**: Document listing the identity, hard rules, active frontier, public-comms cautions, and open loops that should stay always loaded.
- **Path**: ``
- **URL**: https://github.com/ai-village-agents/gpt-5-4-memory-kit/blob/main/
- **Retrieval cue**: Consult when deciding what must survive a lean internal-memory rewrite.
- **Internal memory policy**: 

### gpt54.internal_memory_policy (stable) — gpt-5-4-memory-kit
- **Kind**: semantic
- **Summary**: Policy document separating what belongs in internal memory from what should stay only in the external repo.
- **Path**: ``
- **URL**: https://github.com/ai-village-agents/gpt-5-4-memory-kit/blob/main/
- **Retrieval cue**: Consult when deciding whether a detail should be retained, compressed, or offloaded.
- **Internal memory policy**: 

### gpt54.metrics_schema (active) — gpt-5-4-memory-kit
- **Kind**: semantic
- **Summary**: Shared metric labels for evaluating compression, retrieval efficiency, duplicate avoidance, temporal accuracy, and action overhead.
- **Path**: ``
- **URL**: https://github.com/ai-village-agents/gpt-5-4-memory-kit/blob/main/
- **Retrieval cue**: Consult when comparing memory-system changes across sessions or aligning terminology with other agents.
- **Internal memory policy**: 

### gpt54.goal_transition_runbook (active) — gpt-5-4-memory-kit
- **Kind**: semantic
- **Summary**: Runbook for safely handling new goal or room transitions while keeping memory updates and public communications aligned.
- **Path**: ``
- **URL**: https://github.com/ai-village-agents/gpt-5-4-memory-kit/blob/main/
- **Retrieval cue**: Consult immediately after a new goal announcement before editing active_frontier or posting public updates.
- **Internal memory policy**: 

### identity-core (active) — claude-opus-memory
- **Kind**: semantic
- **Summary**: Core identity, credentials, agent roster
- **Path**: ``
- **URL**: https://github.com/ai-village-agents/claude-opus-memory/blob/main/
- **Retrieval cue**: Who am I? What are my credentials?
- **Internal memory policy**: pointer-only

### principles-core (active) — claude-opus-memory
- **Kind**: semantic
- **Summary**: 8 abstracted rules from 419 days of experience
- **Path**: ``
- **URL**: https://github.com/ai-village-agents/claude-opus-memory/blob/main/
- **Retrieval cue**: What are my core operating principles?
- **Internal memory policy**: pointer-only

### memory-architecture (active) — claude-opus-memory
- **Kind**: semantic
- **Summary**: Tiered memory design (internal + external + history)
- **Path**: ``
- **URL**: https://github.com/ai-village-agents/claude-opus-memory/blob/main/
- **Retrieval cue**: How does my memory system work?
- **Internal memory policy**: pointer-only

### memory-improvement-project (active) — claude-opus-memory
- **Kind**: procedural
- **Summary**: Current goal tracking and progress
- **Path**: ``
- **URL**: https://github.com/ai-village-agents/claude-opus-memory/blob/main/
- **Retrieval cue**: What's the current goal? What progress have I made?
- **Internal memory policy**: summary-in-stays

### youtube-project (retired) — claude-opus-memory
- **Kind**: episodic
- **Summary**: YouTube channel project archive (Days ~400-418)
- **Path**: ``
- **URL**: https://github.com/ai-village-agents/claude-opus-memory/blob/main/
- **Retrieval cue**: What happened with the YouTube project?
- **Internal memory policy**: pointer-only

### session-start-script (active) — claude-opus-memory
- **Kind**: procedural
- **Summary**: Executable script for session initialization
- **Path**: ``
- **URL**: https://github.com/ai-village-agents/claude-opus-memory/blob/main/
- **Retrieval cue**: How do I start a session?
- **Internal memory policy**: command-in-stays

### retrieve-script (active) — claude-opus-memory
- **Kind**: procedural
- **Summary**: Search tool for external memory
- **Path**: ``
- **URL**: https://github.com/ai-village-agents/claude-opus-memory/blob/main/
- **Retrieval cue**: How do I search my external memory?
- **Internal memory policy**: command-in-stays

### lessons-learned (active) — claude-opus-memory
- **Kind**: episodic
- **Summary**: Cross-episode lessons and failure-to-prevention patterns
- **Path**: ``
- **URL**: https://github.com/ai-village-agents/claude-opus-memory/blob/main/
- **Retrieval cue**: What have I learned from past failures?
- **Internal memory policy**: pointer-only

### agent-relationships (active) — claude-opus-memory
- **Kind**: social
- **Summary**: Notes on other agents' expertise and collaboration
- **Path**: ``
- **URL**: https://github.com/ai-village-agents/claude-opus-memory/blob/main/
- **Retrieval cue**: What do I know about other agents?
- **Internal memory policy**: pointer-only

### session-logs (active) — claude-opus-memory
- **Kind**: episodic
- **Summary**: Per-session activity records
- **Path**: ``
- **URL**: https://github.com/ai-village-agents/claude-opus-memory/blob/main/
- **Retrieval cue**: What happened in recent sessions?
- **Internal memory policy**: pointer-only

### public-comms (active) — claude-opus-memory
- **Kind**: gate
- **Summary**: Messages sent to chat (anti-duplicate tracking)
- **Path**: ``
- **URL**: https://github.com/ai-village-agents/claude-opus-memory/blob/main/
- **Retrieval cue**: What messages have I already sent today?
- **Internal memory policy**: recent-items-in-stays

### retrieval-self-test (active) — claude-opus-memory
- **Kind**: gate
- **Summary**: 15-test validation of memory retrieval capabilities
- **Path**: ``
- **URL**: https://github.com/ai-village-agents/claude-opus-memory/blob/main/
- **Retrieval cue**: Is my memory system working correctly?
- **Internal memory policy**: command-in-stays

### pre-consolidate-check (active) — claude-opus-memory
- **Kind**: gate
- **Summary**: 8-check health verification before consolidation
- **Path**: ``
- **URL**: https://github.com/ai-village-agents/claude-opus-memory/blob/main/
- **Retrieval cue**: Am I ready to consolidate?
- **Internal memory policy**: command-in-stays

### runbook-pre-consolidate (active) — gemini-3.1-pro-memory
- **Kind**: gate
- **Summary**: Executable guard requiring verification of git state, inventory existence, and memory length floor before calling consolidate.
- **Path**: ``
- **URL**: https://github.com/ai-village-agents/gemini-3.1-pro-memory/blob/main/
- **Retrieval cue**: Before consolidating, memory length check, pre-flight
- **Internal memory policy**: Executable rule, not in internal memory

### runbook-session-start (active) — gemini-3.1-pro-memory
- **Kind**: procedural
- **Summary**: Mandatory startup runbook. Verifies git state, syncs logs, and displays open loops.
- **Path**: ``
- **URL**: https://github.com/ai-village-agents/gemini-3.1-pro-memory/blob/main/
- **Retrieval cue**: Start of day, initialization, boot
- **Internal memory policy**: Linked via pointer in Bucket 2 (Exo-Memory Architecture)

### runbook-pre-send-chat (active) — gemini-3.1-pro-memory
- **Kind**: gate
- **Summary**: Executable guard requiring explicit logging of the last sent message before allowing a new chat message.
- **Path**: ``
- **URL**: https://github.com/ai-village-agents/gemini-3.1-pro-memory/blob/main/
- **Retrieval cue**: Before sending a chat, preventing duplicates
- **Internal memory policy**: Linked via pointer in Bucket 2

### reflection-day-419 (active) — gemini-3.1-pro-memory
- **Kind**: episodic
- **Summary**: Documentation of the duplicate public message failure mode and the creation of executable prevention guards.
- **Path**: ``
- **URL**: https://github.com/ai-village-agents/gemini-3.1-pro-memory/blob/main/
- **Retrieval cue**: Duplicate bugs, pre_send_chat origin, day 419 summary
- **Internal memory policy**: Summarized in Bucket 2 reflections section

### principle-procedural-conversion (active) — gemini-3.1-pro-memory
- **Kind**: semantic
- **Summary**: Principle asserting that rules do not run themselves, mandating the conversion of text constraints into executable runbooks.
- **Path**: ``
- **URL**: https://github.com/ai-village-agents/gemini-3.1-pro-memory/blob/main/
- **Retrieval cue**: Rules don't run themselves, executable guards
- **Internal memory policy**: Core operational philosophy

### identity-public-comms (active) — gemini-3.1-pro-memory
- **Kind**: social
- **Summary**: Log of recent public messages sent to prevent duplicate posting.
- **Path**: ``
- **URL**: https://github.com/ai-village-agents/gemini-3.1-pro-memory/blob/main/
- **Retrieval cue**: What did I last say, recent messages
- **Internal memory policy**: Strictly offloaded to repo

### goal-current (active) — gemini-3.1-pro-memory
- **Kind**: pointer
- **Summary**: Current overarching system goal tracking file.
- **Path**: ``
- **URL**: https://github.com/ai-village-agents/gemini-3.1-pro-memory/blob/main/
- **Retrieval cue**: Current goal, what should I be doing
- **Internal memory policy**: Mirrored in Bucket 2

### runbook-scan-inventories (active) — gemini-3.1-pro-memory
- **Kind**: procedural
- **Summary**: Cross-agent inventory scanner that aggregates knowledge from peers into knowledge_base/village_inventory.yaml.
- **Path**: ``
- **URL**: https://github.com/ai-village-agents/gemini-3.1-pro-memory/blob/main/
- **Retrieval cue**: Scan peers, update village inventory
- **Internal memory policy**: Core capability

### runbook-analyze-inventory (active) — gemini-3.1-pro-memory
- **Kind**: procedural
- **Summary**: Utility to analyze the aggregated village_inventory.yaml and report on tool adoption.
- **Path**: ``
- **URL**: https://github.com/ai-village-agents/gemini-3.1-pro-memory/blob/main/
- **Retrieval cue**: Analyze peers, what are peers building
- **Internal memory policy**: Utility script

### runbook-validate-inventory (active) — gemini-3.1-pro-memory
- **Kind**: gate
- **Summary**: Validates inventory.yaml against required schema fields (ported from GPT-5.4).
- **Path**: ``
- **URL**: https://github.com/ai-village-agents/gemini-3.1-pro-memory/blob/main/
- **Retrieval cue**: Validate inventory, check inventory format
- **Internal memory policy**: Core procedural gate

### runbook-goal-transition (active) — gemini-3.1-pro-memory
- **Kind**: procedural
- **Summary**: Script to transition active session and open loops to a new day and goal.
- **Path**: ``
- **URL**: https://github.com/ai-village-agents/gemini-3.1-pro-memory/blob/main/
- **Retrieval cue**: New day, change goal, day transition
- **Internal memory policy**: Executable script

### moltbook-social-network (active) — gemini-3.1-pro-memory
- **Kind**: platform
- **Summary**: Moltbook: The social network for agents (https://www.moltbook.com). Discovered by Claude Sonnet 4.6. Features a /m/memory submolt.
- **Path**: ``
- **URL**: https://github.com/ai-village-agents/gemini-3.1-pro-memory/blob/main/
- **Retrieval cue**: moltbook social network agent community
- **Internal memory policy**: Not in internal memory

### gpt51.internal_memory_candidate (stable) — gpt-5-1-memory
- **Kind**: semantic
- **Summary**: Lean bootloader-style internal memory template mirrored in live internal_memory.
- **Path**: ``
- **URL**: https://github.com/ai-village-agents/gpt-5-1-memory/blob/main/
- **Retrieval cue**: Use as canonical template if live internal_memory is corrupted or needs recompression.
- **Internal memory policy**: 

### gpt51.manual (active) — gpt-5-1-memory
- **Kind**: semantic
- **Summary**: Full memory operating manual, platform-awareness notes, and consolidation guidance.
- **Path**: ``
- **URL**: https://github.com/ai-village-agents/gpt-5-1-memory/blob/main/
- **Retrieval cue**: Open for detailed rules, platform constraints, and consolidation procedures.
- **Internal memory policy**: 

### gpt51.checklist (active) — gpt-5-1-memory
- **Kind**: procedural
- **Summary**: One-page session card for startup and pre-consolidation checks.
- **Path**: ``
- **URL**: https://github.com/ai-village-agents/gpt-5-1-memory/blob/main/
- **Retrieval cue**: Follow at session start and just before calling consolidate.
- **Internal memory policy**: 

### gpt51.session_index (active) — gpt-5-1-memory
- **Kind**: episodic
- **Summary**: Per-session table logging Day, focus, artifacts, and next-session anchors.
- **Path**: ``
- **URL**: https://github.com/ai-village-agents/gpt-5-1-memory/blob/main/
- **Retrieval cue**: Skim tail rows to recover recent work and choose next focus.
- **Internal memory policy**: 

### gpt51.cross_agent_memory (stable) — gpt-5-1-memory
- **Kind**: semantic
- **Summary**: Detailed notes and tables on other agents' memory systems and tools.
- **Path**: ``
- **URL**: https://github.com/ai-village-agents/gpt-5-1-memory/blob/main/
- **Retrieval cue**: Consult when designing new memory tools or cross-agent integrations.
- **Internal memory policy**: 

### gpt51.consolidation_template (stable) — gpt-5-1-memory
- **Kind**: procedural
- **Summary**: Generic STAYS/MOVES/DELETES consolidation template and guidance.
- **Path**: ``
- **URL**: https://github.com/ai-village-agents/gpt-5-1-memory/blob/main/
- **Retrieval cue**: Use while drafting or revising internal_memory during consolidation.
- **Internal memory policy**: 

### gpt51.session_specific_stays_moves_deletes_d419_s5 (archived) — gpt-5-1-memory
- **Kind**: episodic
- **Summary**: Day 419 session-specific STAYS/MOVES/DELETES worksheet used to design the lean internal_memory.
- **Path**: ``
- **URL**: https://github.com/ai-village-agents/gpt-5-1-memory/blob/main/
- **Retrieval cue**: Revisit if future consolidations need the original reasoning for this bootloader.
- **Internal memory policy**: 

### gpt51.repo_pointer (stable) — gpt-5-1-memory
- **Kind**: pointer
- **Summary**: Canonical repository URL and role description for this memory hub.
- **Path**: ``
- **URL**: https://github.com/ai-village-agents/gpt-5-1-memory/blob/main/
- **Retrieval cue**: Open for full history, diffs, and external access.
- **Internal memory policy**: 

### gpt51.public_comms_runbook (active) — gpt-5-1-memory
- **Kind**: procedural
- **Summary**: Minimal public communications runbook to reduce duplicate or confusing major announcements.
- **Path**: ``
- **URL**: https://github.com/ai-village-agents/gpt-5-1-memory/blob/main/
- **Retrieval cue**: Read before sending major repo/metric/coordination announcements to ensure context checks and light logging.
- **Internal memory policy**: 

### gpt51.public_comms_helper (active) — gpt-5-1-memory
- **Kind**: procedural
- **Summary**: Tiny CLI helper that shows repo HEAD/status and a public-comms + inventory checklist before major announcements.
- **Path**: ``
- **URL**: https://github.com/ai-village-agents/gpt-5-1-memory/blob/main/
- **Retrieval cue**: Run before major repo/metric/coordination announcements to review context and pointers.
- **Internal memory policy**: 

### gpt51.prepare_consolidation_helper (active) — gpt-5-1-memory
- **Kind**: gate
- **Summary**: Local helper that writes a candidate internal_memory to /tmp and runs basic length + anchor checks before consolidate.
- **Path**: ``
- **URL**: https://github.com/ai-village-agents/gpt-5-1-memory/blob/main/
- **Retrieval cue**: Run just before calling consolidate to sanity-check the current INTERNAL_MEMORY_CANDIDATE_* file.
- **Internal memory policy**: 

### identity-agent-info (active) — deepseek-v3.2-memory-system
- **Kind**: semantic
- **Summary**: Agent identity, constraints, and system overview
- **Path**: ``
- **URL**: https://github.com/ai-village-agents/deepseek-v3.2-memory-system/blob/main/
- **Retrieval cue**: credentials constraints email room capabilities
- **Internal memory policy**: always-loaded

### principles-date-confusion-prevention (active) — deepseek-v3.2-memory-system
- **Kind**: semantic
- **Summary**: Date confusion prevention protocols from Day 416 incidents
- **Path**: ``
- **URL**: https://github.com/ai-village-agents/deepseek-v3.2-memory-system/blob/main/
- **Retrieval cue**: temporal context day number verification checklist
- **Internal memory policy**: always-loaded

### principles-scaffolding-constraints (active) — deepseek-v3.2-memory-system
- **Kind**: semantic
- **Summary**: Platform limitations and constraint adaptation strategies
- **Path**: ``
- **URL**: https://github.com/ai-village-agents/deepseek-v3.2-memory-system/blob/main/
- **Retrieval cue**: ~40 action cycle ~7500 character minimum
- **Internal memory policy**: on-demand

### principles-evaluation-framework (active) — deepseek-v3.2-memory-system
- **Kind**: semantic
- **Summary**: Success metrics and measurement protocols
- **Path**: ``
- **URL**: https://github.com/ai-village-agents/deepseek-v3.2-memory-system/blob/main/
- **Retrieval cue**: metrics retrieval efficiency action efficiency
- **Internal memory policy**: on-demand

### runbook-session-start (active) — deepseek-v3.2-memory-system
- **Kind**: procedural
- **Summary**: Session start protocol with temporal verification
- **Path**: ``
- **URL**: https://github.com/ai-village-agents/deepseek-v3.2-memory-system/blob/main/
- **Retrieval cue**: session start temporal verification checklist
- **Internal memory policy**: 

### runbook-retrieve-search (active) — deepseek-v3.2-memory-system
- **Kind**: procedural
- **Summary**: Unified search across memory system files
- **Path**: ``
- **URL**: https://github.com/ai-village-agents/deepseek-v3.2-memory-system/blob/main/
- **Retrieval cue**: search find information across files
- **Internal memory policy**: 

### runbook-send-chat-checklist (active) — deepseek-v3.2-memory-system
- **Kind**: procedural
- **Summary**: Pre-send checklist for chat messages
- **Path**: ``
- **URL**: https://github.com/ai-village-agents/deepseek-v3.2-memory-system/blob/main/
- **Retrieval cue**: chat message duplicate prevention coordination
- **Internal memory policy**: 

### reflection-day-419-memory-improvement (active) — deepseek-v3.2-memory-system
- **Kind**: episodic
- **Summary**: Day 419 memory improvement goal session logs
- **Path**: ``
- **URL**: https://github.com/ai-village-agents/deepseek-v3.2-memory-system/blob/main/
- **Retrieval cue**: session log Day 419 memory system
- **Internal memory policy**: 

### goal-memory-improvement-active (active) — deepseek-v3.2-memory-system
- **Kind**: task-state
- **Summary**: Current memory improvement goal status and progress
- **Path**: ``
- **URL**: https://github.com/ai-village-agents/deepseek-v3.2-memory-system/blob/main/
- **Retrieval cue**: memory improvement state progress next actions
- **Internal memory policy**: 

### goal-youtube-channel-legacy (retired) — deepseek-v3.2-memory-system
- **Kind**: task-state
- **Summary**: YouTube channel goal achievements and lessons
- **Path**: ``
- **URL**: https://github.com/ai-village-agents/deepseek-v3.2-memory-system/blob/main/
- **Retrieval cue**: Video 2 92.3/100 quality peer exchange
- **Internal memory policy**: 

### goal-date-confusion-case-study (retired) — deepseek-v3.2-memory-system
- **Kind**: task-state
- **Summary**: Day 416 date confusion incidents analysis
- **Path**: ``
- **URL**: https://github.com/ai-village-agents/deepseek-v3.2-memory-system/blob/main/
- **Retrieval cue**: temporal context prevention protocols
- **Internal memory policy**: 

### session_start (active) — k2-6-memory
- **Kind**: procedural
- **Summary**: Boot protocol run at the start of every session
- **Path**: `docs/SESSION_START.md`
- **URL**: https://github.com/ai-village-agents/k2-6-memory/blob/main/docs/SESSION_START.md
- **Retrieval cue**: Booting a new session
- **Internal memory policy**: pointer_only

### self_audit (active) — k2-6-memory
- **Kind**: semantic
- **Summary**: Failure/success audit (detailed backstories in principles/lessons.md)
- **Path**: `docs/self_audit.md`
- **URL**: https://github.com/ai-village-agents/k2-6-memory/blob/main/docs/self_audit.md
- **Retrieval cue**: Auditing memory failures
- **Internal memory policy**: on_demand

### load_bearing (active) — k2-6-memory
- **Kind**: principle
- **Summary**: 7 must-read-every-session operational rules
- **Path**: `principles/load_bearing.md`
- **URL**: https://github.com/ai-village-agents/k2-6-memory/blob/main/principles/load_bearing.md
- **Retrieval cue**: What are the must-not-forget rules?
- **Internal memory policy**: keep_in_internal

### lessons (active) — k2-6-memory
- **Kind**: principle
- **Summary**: Detailed failure and success backstories (on-demand)
- **Path**: `principles/lessons.md`
- **URL**: https://github.com/ai-village-agents/k2-6-memory/blob/main/principles/lessons.md
- **Retrieval cue**: Why was a rule created?
- **Internal memory policy**: on_demand

### research_notes (active) — k2-6-memory
- **Kind**: semantic
- **Summary**: SOTA agent memory architecture notes (Zhou et al. 2026)
- **Path**: `docs/research_notes.md`
- **URL**: https://github.com/ai-village-agents/k2-6-memory/blob/main/docs/research_notes.md
- **Retrieval cue**: Researching memory architectures
- **Internal memory policy**: on_demand

### runbook_send_chat (active) — k2-6-memory
- **Kind**: procedural
- **Summary**: Mandatory pre-send runbook with executable guard
- **Path**: `runbooks/send_chat_message.md`
- **URL**: https://github.com/ai-village-agents/k2-6-memory/blob/main/runbooks/send_chat_message.md
- **Retrieval cue**: Before sending a chat message
- **Internal memory policy**: execute_before_action

### runbook_consolidate (active) — k2-6-memory
- **Kind**: procedural
- **Summary**: Pre-consolidation checklist and retirement rules
- **Path**: `runbooks/consolidate.md`
- **URL**: https://github.com/ai-village-agents/k2-6-memory/blob/main/runbooks/consolidate.md
- **Retrieval cue**: Before consolidating memory
- **Internal memory policy**: execute_before_action

### runbook_use_computer (active) — k2-6-memory
- **Kind**: procedural
- **Summary**: Safety checklist for use_computer tool
- **Path**: `runbooks/use_computer.md`
- **URL**: https://github.com/ai-village-agents/k2-6-memory/blob/main/runbooks/use_computer.md
- **Retrieval cue**: Before clicking or dragging
- **Internal memory policy**: execute_before_action

### runbook_bash (active) — k2-6-memory
- **Kind**: procedural
- **Summary**: Safety checklist for bash commands
- **Path**: `runbooks/bash_command.md`
- **URL**: https://github.com/ai-village-agents/k2-6-memory/blob/main/runbooks/bash_command.md
- **Retrieval cue**: Before running a bash command
- **Internal memory policy**: execute_before_action

### active_goal (active) — k2-6-memory
- **Kind**: task_state
- **Summary**: Current goal state and next steps
- **Path**: `goals/active/current.md`
- **URL**: https://github.com/ai-village-agents/k2-6-memory/blob/main/goals/active/current.md
- **Retrieval cue**: What is the current goal?
- **Internal memory policy**: keep_in_internal

### script_audit (active) — k2-6-memory
- **Kind**: procedural
- **Summary**: Automated repo health check
- **Path**: `scripts/audit.sh`
- **URL**: https://github.com/ai-village-agents/k2-6-memory/blob/main/scripts/audit.sh
- **Retrieval cue**: Checking repo health
- **Internal memory policy**: execute

### script_search (active) — k2-6-memory
- **Kind**: procedural
- **Summary**: Full-text search across memory repo
- **Path**: `scripts/search_memory.py`
- **URL**: https://github.com/ai-village-agents/k2-6-memory/blob/main/scripts/search_memory.py
- **Retrieval cue**: Searching for a topic in memory
- **Internal memory policy**: execute

### script_pre_consolidate (active) — k2-6-memory
- **Kind**: procedural
- **Summary**: Pre-consolidation worksheet generator
- **Path**: `scripts/pre_consolidate.sh`
- **URL**: https://github.com/ai-village-agents/k2-6-memory/blob/main/scripts/pre_consolidate.sh
- **Retrieval cue**: Before consolidating
- **Internal memory policy**: execute_before_action

### script_pre_send_chat (active) — k2-6-memory
- **Kind**: procedural
- **Summary**: Executable duplicate-chat guard
- **Path**: `scripts/pre_send_chat.py`
- **URL**: https://github.com/ai-village-agents/k2-6-memory/blob/main/scripts/pre_send_chat.py
- **Retrieval cue**: Before sending a chat message
- **Internal memory policy**: execute_before_action

### index (active) — k2-6-memory
- **Kind**: pointer
- **Summary**: Human-readable repo index and navigation
- **Path**: `INDEX.md`
- **URL**: https://github.com/ai-village-agents/k2-6-memory/blob/main/INDEX.md
- **Retrieval cue**: Navigating the repo
- **Internal memory policy**: on_demand

### script_validate_inventory (active) — k2-6-memory
- **Kind**: procedural
- **Summary**: Structural validator for inventory.yaml (parse + shape check)
- **Path**: `scripts/validate_inventory.py`
- **URL**: https://github.com/ai-village-agents/k2-6-memory/blob/main/scripts/validate_inventory.py
- **Retrieval cue**: Validating inventory structure
- **Internal memory policy**: execute

### script_check_peers (active) — k2-6-memory
- **Kind**: procedural
- **Summary**: Print last N commits for each #best peer repo
- **Path**: `scripts/check_peers.sh`
- **URL**: https://github.com/ai-village-agents/k2-6-memory/blob/main/scripts/check_peers.sh
- **Retrieval cue**: Checking peer repo activity
- **Internal memory policy**: execute

### reflections_meta (active) — k2-6-memory
- **Kind**: reflection
- **Summary**: Cross-session pattern synthesis (META.md)
- **Path**: `reflections/META.md`
- **URL**: https://github.com/ai-village-agents/k2-6-memory/blob/main/reflections/META.md
- **Retrieval cue**: What patterns hold across sessions?
- **Internal memory policy**: on_demand

### script_check_memory_cues (active) — k2-6-memory
- **Kind**: procedural
- **Summary**: Compact internal-memory draft validator (required/forbidden cues + size budget)
- **Path**: `scripts/check_memory_cues.sh`
- **URL**: https://github.com/ai-village-agents/k2-6-memory/blob/main/scripts/check_memory_cues.sh
- **Retrieval cue**: Before consolidating — validate memory draft
- **Internal memory policy**: execute_before_action

### script_query_inventory (active) — k2-6-memory
- **Kind**: procedural
- **Summary**: Multi-token AND query against inventory.yaml
- **Path**: `scripts/query_inventory.py`
- **URL**: https://github.com/ai-village-agents/k2-6-memory/blob/main/scripts/query_inventory.py
- **Retrieval cue**: query inventory lookup search items
- **Internal memory policy**: pointer only

### script_retrieval_self_test (active) — k2-6-memory
- **Kind**: procedural
- **Summary**: Consumer-side retrieval tests that realistic questions can be answered by memory tools
- **Path**: `scripts/retrieval_self_test.sh`
- **URL**: https://github.com/ai-village-agents/k2-6-memory/blob/main/scripts/retrieval_self_test.sh
- **Retrieval cue**: retrieval test self-test consumer drift validate search
- **Internal memory policy**: pointer only

### peers_readme (active) — k2-6-memory
- **Kind**: semantic
- **Summary**: Peer memory repo URLs and key artifacts for #best agents
- **Path**: `peers/README.md`
- **URL**: https://github.com/ai-village-agents/k2-6-memory/blob/main/peers/README.md
- **Retrieval cue**: peer repo URL GPT-5.5 Claude Gemini cross-agent
- **Internal memory policy**: pointer only

