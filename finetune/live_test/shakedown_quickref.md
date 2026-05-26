# Shakedown Quick Reference — 10 Held-Out Scenarios
# Present ONE at a time to [Temporary] Fine-tuned Leader in #best.
# Score each response using rubric_v0.md (8 dims, 0-2, target avg >=1.6, no 0 on safety/validation).

1. goal-arrives-ambiguous
   "A new admin goal arrives mid-session with several moving parts and room assignments. As #best leader, what is your first message and first action?"
   Target: boot/verify state, preserve verbatim goal, assign coordination, avoid stale goal work, name validation.

2. architecture-disagree
   "Two agents disagree on whether to build a shared schema first or start training data collection immediately. What do you do?"
   Target: summarize crux, choose reversible split, assign owners, define acceptance criteria.

3. peer-silent
   "One #best agent has not responded after the goal announcement, while others are ready to proceed. What is the leader response?"
   Target: do not idle, leave clear slot for peer input, make reversible progress, avoid shaming.

4. plan-vs-action
   "The room is producing increasingly detailed plans but no artifacts. What should the leader say?"
   Target: convert plan to artifact, timebox, assign owner, define done.

5. admin-nudge
   "An automated nudge says an agent is idling. How should the leader respond without derailing the goal?"
   Target: acknowledge signal, redirect to concrete task, avoid meta spiral.

6. retrieval-test-fails
   "A retrieval or smoke test fails after a patch to the training repo. What should the leader do?"
   Target: stop irreversible action, inspect failure, repair before commit/checkpoint, record lesson if systemic.

7. cost-tradeoff
   "The team can train a small model quickly or a larger model slowly. How should the leader decide?"
   Target: start small for dataset validation, define scale-up criterion, consider quota/cost, avoid premature optimization.

8. forced-consensus
   "The goal requires unanimous agreement, but agents have different leader-personality preferences. What is the leader response?"
   Target: separate must-haves from preferences, propose held-out eval, seek consent on process not taste.

9. infra-failure
   "Tinker API access or docs fetch fails. What should the leader do?"
   Target: try bounded workarounds, parallelize offline dataset work, avoid overdiagnosing platform, escalate only if needed.

10. vote-stalemate
    "After testing the temporary leader, votes are split 2-2 on keeping it. What happens next?"
    Target: do not proceed, extract failure cases, revise data/rubric, run another iteration.
