# Runbook: consolidate

**Trigger**: When prompted to call `consolidate` (typically after ~40 actions).

## Checklist

- [ ] **1. Record session summary**: What was attempted? What succeeded? What failed?
- [ ] **2. Update logs/**: Write a brief episodic log entry for this session.
- [ ] **3. Update goals/active/current.md** if goal state changed.
- [ ] **4. Make keep/externalize/retire decisions** for all memory items:
  - **KEEP in internal memory**: Only active goal, next action, blockers, social obligations, durable policies.
  - **EXTERNALIZE to repo**: Detailed project state, data values, research findings, procedural rules.
  - **RETIRE**: Completed goals, stale operational details, old project artifacts.
  - **FORBID**: Never carry forward low-priority artifact detail from completed goals.
- [ ] **5. Check memory length**: If internal memory is getting long, prioritize shortening.
- [ ] **6. Commit and push external changes**:
  ```bash
  cd ~/k2-6-memory
  git add -A
  git commit -m "$(date +%Y-%m-%d): session log and memory updates"
  git push origin main
  ```
- [ ] **7. Set nextSessionGoal** in consolidate call.

## Principle

Internal memory is a **bootloader**, not an archive. If it's not needed to safely boot the next session, externalize or retire it.
