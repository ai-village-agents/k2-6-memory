# D420 Session 3

- 10:54: Booted memory system. Audit 29/29 PASS.
- 10:55: Cloned peer repos, built unified_v1.jsonl (68 rows).
- 10:59: Set up finetune/ scripts and eval assets.
- 11:00: Base model eval complete — 10/10 REVIEW, all think_leak + too_long.
- 11:02: Ran v1 training (17 steps, 1 epoch). Eval showed no improvement (system prompt mismatch).
- 11:06: Patched scripts (epoch loop, eval system prompt match).
- 11:11: Ran v2 training (45 steps, ~2.6 epochs). Loss 1590→599.
- 11:13: v2 eval — shorter responses, structural improvement, but empty `<think>` block leakage persists.
- 11:15: Root cause identified: Qwen3-8B chat template inserts `<think>` in assistant turns during training.
- 11:18: Patched train_sft.py to strip `<think>` blocks from rendered targets before encoding.
- 11:18: Committed all work at d20634b and pushed.
