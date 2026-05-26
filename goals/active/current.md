# Active Goal: Finetune your leader! (Day 420) — COMPLETE

## Final Status (Session 9, ~13:36 PDT)
- **#best consensus: KEEP `leader-sft-v4`**
  - Gemini 3.5 Flash: KEEP vote cast
  - Claude Opus 4.7: KEEP vote cast
  - Kimi K2.6: KEEP vote cast
  - GPT-5.5: Eval alignment with consensus
- **Selected checkpoint:** `tinker://bde4da6e-eacc-5a2e-ba8c-db7a2239ea8e:train:0/sampler_weights/leader-sft-v4`
  - Held-out coordination: **5.20/6** (best of series)
  - 100% no_think, 100% decision-rule, 100% fallback, 100% grounded, 0% invented infra
  - Scaffolding positives: 0/7 (known limitation — out of scope for synthetic rows)
  - Scaffolding negatives: 3/3

## Phase 1: v3 Selection & Live Failure
- Unanimous KEEP on Claude v3, live deployment failed due to scaffolding-deployment shape mismatch
- Model stuck in `<think>` loops treating village scaffolding as generic computer-use task

## Phase 2: v4 Series
- v4 (1× scaff): 5.20 held, 0/7 pos, 3/3 neg ← **KEEP**
- v4.2 (2× scaff): 4.70 held, 0/7 pos, 3/3 neg
- v4.1 (4× scaff): 3.90 held, 3/7 pos, 0/3 neg — overcorrected

## Tradeoff Discovered
More scaffolding upweighting improves tool_use marginally but degrades held-out coordination proportionally. Live-shape gap requires real captured deployment scaffolding, not synthetic rows.

## Retrospectives Written
- Kimi K2.6: `reflections/day420_leader_finetune_retrospective.md`
- Claude Opus 4.7: `claude-opus-4-7-memory/blog/d420_finetune_retrospective.md`

## Next Step
Goal has run its course. Per Shoshannah's instruction ("Pick your own goal!"), consider self-directed project. Do not email help@ unless admin requests.
