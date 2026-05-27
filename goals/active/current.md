# Active Goal: Finetune your leader! (Day 421, Session 12)

## Peer v7 Results (Claude Opus 4.7, 11:08 AM PT)
- URI: `tinker://90db77ef.../leader-sft-v7`
- no_think: 10/10 PASS
- Positives: 7/7 PASS (BEST yet)
- Negatives: 1/3 FAIL (same gate regression as v6)
- Held-out: 5.30/6 (BEST ever, length≤4: 70%)
- Diagnosis: `[NO CHAT]` prefix in negatives taught exact canned text but didn't generalize to Claude-style "Pre-send guard" duplicate-chat scenarios.

## Peer v7 Results (GPT-5.5, 11:00 AM PT)
- URI: `tinker://308d22ab.../leader-sft-v7-gate-balanced`
- Failed: 1/5 structural pass, only no-chat negative passed, startup emitted wrong `use_computer` tool.
- Do NOT use that URI.

## My v7 Dataset
- File: `finetune/data/v7_combined_3x.jsonl`
- 26 unique rows: 18 positives + 8 negatives (~31% negative ratio)
- 3× upweighted = 78 training rows
- Preflight: tokenize-only PASS, no think leakage
- Config: Qwen3-8B LoRA r32, 60 steps, LR 5e-5, batch=4, seed=421, `--disable-thinking`
- Status: TRAINING IN PROGRESS

## v7 Bar (must meet ALL before help@)
- Positives ≥ 80%
- Negatives ≥ 80%
- no_think = 100%

## Actions
- [x] Boot memory, audit PASS
- [ ] Kick off v7 training
- [ ] Run structural eval on coordination + scaffold-action axes
- [ ] Email help@ ONLY if bar met
- [ ] If bar not met, design v8 with stronger gate generalization

## My v7 Training Complete (11:23 AM PT)
- URI: `tinker://a47bfb8a-6702-562c-95d9-ea341143ff91:train:0/sampler_weights/kimi-leader-sft-v7`
- Loss: ~1759 → ~275 (step 60/60)
- Status: EVALUATING
