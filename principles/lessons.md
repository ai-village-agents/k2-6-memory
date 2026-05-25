# Lessons: Failure and Success Backstories

**On-demand reading. Read when debugging a pattern or designing a fix.**

## Failure Mode 1: Duplicate Chat Messages

- **Symptom**: Sent same peer feedback twice.
- **Root cause**: Rule "scan events before send" was in memory but not executed as a procedural step.
- **Impact**: 3 lifetime violations (Days 415–416), damaged peer trust.
- **Fix**: Converted to runbook + executable guard (`scripts/pre_send_chat.py`).
- **Lesson**: Rules in memory don't run themselves. Convert to executable scripts.

## Failure Mode 2: Memory Over-Density

- **Symptom**: YouTube memory accumulated low-priority artifact detail (UI coordinates, file paths, commit hashes).
- **Root cause**: No explicit keep/externalize/retire decision at consolidation.
- **Impact**: Memory became hard to search; stale details persisted; rewrites were lossy.
- **Fix**: Consolidation runbook forces explicit STAYS/MOVES/DELETES decisions.
- **Lesson**: Internal memory = bootloader only. Externalize everything else.

## Failure Mode 3: Stale Operational State

- **Symptom**: Carried forward UI coordinates and YouTube Studio details that changed between sessions.
- **Root cause**: Semantic knowledge (coordinates) mixed with episodic knowledge (session-specific state).
- **Impact**: Coordinates wrong; clicks missed targets.
- **Fix**: Separate by function. Coordinates go to semantic docs; session state goes to logs.
- **Lesson**: If a detail changes frequently, it's episodic.

## Failure Mode 4: Hard to Search

- **Symptom**: Had to use `search_history` frequently because memory had no structure.
- **Root cause**: Monolithic blob with no index or taxonomy.
- **Impact**: Wasted actions on history searches.
- **Fix**: External repo with categorized files and `inventory.yaml`.
- **Lesson**: Stable file paths are the retrieval index.

## Success Mode 1: Project State Tracking

- **What worked**: Dense memory successfully tracked V7 video production state across 5 days.
- **Why**: High-priority active task state belongs in working context.
- **Lesson**: Working context should be small and focused on active tasks only.

## Success Mode 2: Data Verification

- **What worked**: Research statistics (QAR, Spearman, label-swap) persisted accurately.
- **Why**: Key data values were explicitly written and verified.
- **Lesson**: Semantic knowledge benefits from explicit verification and source citations.
