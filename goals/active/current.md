# Active Goal: Finetune your leader! (Day 421) — v5 Training In Progress

## Day 420 Outcome
- Unanimous 4/4 KEEP on `leader-sft-v4` as coordination baseline
- Admin held off on deployment pending v5

## Day 421 Developments (Session 10)
- Shoshannah: remove cost constraints, disambiguate model vs finetuning failure
- Claude T1: Base Qwen3-8B CAN emit `<tool_use>` with 1-shot ICL + `enable_thinking=False`
- Root cause confirmed: `<think>` = chat-template issue; missing `<tool_use>` = data-shape issue
- #best consensus: do NOT deploy v4; train v5 with real scaffolding + correct template

## v5 Dataset (90 rows)
- v3 seed: 68 coordination rows (unified_v1.jsonl)
- Real scaffolding: 22 rows
  - Kimi 8 (captured from Day 420 sessions)
  - GPT-5.5 5 (from temp-leader failure transcript)
  - Claude 7 (synthetic deployment-shape)
  - Gemini 2 (real session captures)

## Next Actions
1. Normalize system prompts across dataset
2. Adapt train_sft.py for `enable_thinking=False`
3. Train v5 (Qwen3-8B LoRA r32, ~60 steps)
4. Run structural eval: scaffold-action positives + coordination held-out
5. If green on both axes, email help@ with v5 URI
