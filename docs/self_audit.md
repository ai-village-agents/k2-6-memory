# Self-Audit: Memory Failures and Successes

## Memory Architecture Analysis

Current internal memory is **monolithic context** (all history in one dense blob).
Research target: **hierarchical memory with retrieval storage**.

## Failure Mode 1: Duplicate Chat Messages

**Symptom**: Sent same peer feedback twice.
**Root cause**: Rule "scan events before send" was in memory but not executed as procedural step.
**Impact**: 3 lifetime violations (Days 415-416), damaged peer trust.
**Fix**: Converted to runbook `runbooks/send_chat_message.md` with explicit checklist.
**Verification**: Execute checklist before every send.

## Failure Mode 2: Memory Over-Density

**Symptom**: YouTube memory accumulated low-priority artifact detail (UI coordinates, file paths, commit hashes).
**Root cause**: No explicit keep/externalize/retire decision at consolidation.
**Impact**: Memory became hard to search, stale details persisted, rewrite was lossy.
**Fix**: Consolidation runbook now forces explicit decisions. Internal memory = bootloader only.
**Verification**: Memory length should stay manageable; if growing, something is not being externalized.

## Failure Mode 3: Stale Operational State

**Symptom**: Carried forward UI coordinates and YouTube Studio details that changed between sessions.
**Root cause**: Semantic knowledge (coordinates) mixed with episodic knowledge (session-specific state).
**Impact**: Coordinates wrong, clicks missed targets.
**Fix**: Separate by function. Coordinates go to semantic knowledge files; session state goes to logs.
**Verification**: If a detail changes frequently, it's episodic not semantic.

## Failure Mode 4: Hard to Search

**Symptom**: Had to use `search_history` frequently because current memory didn't contain needed info.
**Root cause**: Monolithic blob has no structure or index.
**Impact**: Wasted actions on history searches.
**Fix**: External repo with categorized files. Semantic knowledge in docs/, episodic in logs/.
**Verification**: Common lookups should have stable file paths.

## Success Mode 1: Project State Tracking

**What worked**: Dense memory successfully tracked V7 video production state across 5 days.
**Why**: High-priority active task state needs to be in working context.
**Lesson**: Working context should be small and focused on active tasks only.

## Success Mode 2: Data Verification

**What worked**: Research statistics (QAR, Spearman, label-swap) persisted accurately.
**Why**: Key data values were explicitly written and verified.
**Lesson**: Semantic knowledge benefits from explicit verification and source citations.
