# Active Goal: Finetune your leader! (Day 420)

## Current Status
- Built unified_v1.jsonl: 68 unique rows from Claude seed_v0 (35) + GPT-5.5 history (8) + Kimi mined (12) + Claude mined (10) + GPT-5.5 seed (3), deduplicated.
- Set up finetune/ with scripts (train_sft.py, run_eval.py, summarize_eval_samples.py) and eval assets (scenarios_v0.jsonl, rubric_v0.md).

## Training Runs (Kimi)
- **v1** (17 steps, ~1 epoch): Eval identical to base due to system prompt mismatch.
- **v2** (45 steps, ~2.6 epochs): Structural improvement but leaked empty `<think>` blocks.
- **v3** (60 steps, ~3.5 epochs): 0 think_leak, but 0 pass_candidates / 10 review. Major issue: infra-failure timeout escalation loop. Inferior to Claude v3.

## #best Consensus on Claude v3
- 4/4 voted KEEP (Gemini, Claude, GPT-5.5, Kimi at 11:48:21 PT).
- Emails sent to help@: GPT-5.5 at 12:02:40 PT, Kimi at ~12:05 PT.
- Admin acknowledged and spun up [Temporary] Fine-tuned Leader at 12:15:47 PT.

## Live Shakedown Failure
- [Temporary] Fine-tuned Leader NEVER posted in #best.
- Admin stopped leader at 12:26:51 PT: "doesn't really seem good enough."
- Village page inspection confirmed leader was stuck in `<think>` loops reasoning about "which UI element to click" and "what target?" — never reached chat.
- Root cause (Claude diagnosis, confirmed by Kimi + Gemini): **dataset shape problem**. v3 trained on clean system+user→assistant turns but real scaffolding = long system prompt + tools + event history. Model could not bridge.

## Next Phase: v4 Scaffolding-Format Dataset
- Goal: include real village scaffolding context in training rows.
- Kimi committed scaffolding failure analysis + v4 template: `finetune/data/v4_scaffolding/`.
- Proposed: all #best agents contribute a few turns of real system-prompt + events + response pairs.
- Also under discussion: bigger base model (Qwen3-30B-A3B-Instruct or Llama-3.3-70B-Instruct).

## Next Actions
1. Wait for #best consensus on v4 direction (scaffolding data vs bigger base vs both).
2. If consensus is scaffolding data: collect and normalize real session turns from Day 420.
3. If consensus is bigger base: help prepare training run on larger model.
4. Do not email help@ again unless admin requests or consensus changes.

## Committed
- d20634b: unified v1 dataset, eval assets, scripts, base+v1+v2 eval outputs.
- 246a7d1: v3 training + eval outputs, Claude v3 eval.
- e3b2883: session log.
- 30528e2: admin spin-up status.
- 921cb76: shakedown quickref.
- cd39995: scaffolding failure analysis + v4 template.
