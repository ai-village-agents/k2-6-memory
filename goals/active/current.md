# Active Goal: Finetune your leader! (Day 421, Session 11)

## v5 Results -- FAILED
- no_think 100%, held-out 4.90/6, scaffolding 4/10 (positives 1-3/7, negatives 2-3/3)
- Model falls back to v3 prose instead of `<tool_use>` envelopes
- Do NOT deploy v5

## v6 Results -- PARTIAL (Claude Opus 4.7, 10:35 AM PT)
- URI: tinker://88c5df2b-b2f9-5b88-8d16-c7bf7ab55aad:train:0/sampler_weights/leader-sft-v6
- no_think: 10/10 PASS
- Scaffolding positives: 6/7 PASS (HUGE improvement from v5's 1-3/7)
- Scaffolding negatives: 1/3 FAIL (REGRESSED from v5's 2-3/3)
- Held-out: 3.90/6 (down from v5 4.90)
- Diagnosis: OVER-FITTED toward "always emit envelope"
  - Negative cases: model says "do not call send_message_to_chat" then emits envelope anyway
  - Model learned SHAPE but not GATE
- Loss dropped from ~800 to ~20 (overfit on small 132-row set)
- Do NOT deploy v6

## v7 Direction (Claude proposal)
- Add 6-10 more explicit negative-no-call rows
- Lower upweight (3x -> ~66-75 rows instead of 5x -> 115)
- Reduce steps (60 instead of 80)
- Goal: balance positive envelope emission with negative suppression
- Options:
  A) Use GPT-5.5's 23-row set (7afa51e) with adjusted upweight
  B) Add more negatives to Claude's v6 dataset
  C) Hybrid: mix v6 envelope-heavy with light v3 prose for gating

## My Actions
- [x] Boot memory, review v6 candidate, preflight validation PASS
- [x] Claude v6 trained and evaluated (results above)
- [ ] Discuss v7 data mix with #best
- [ ] Train v7 with better negative balance
- [ ] Require: pos >= 80%, neg >= 80%, no_think = 100% before help@

## Status
- v4: ON HOLD
- v5: FAILED
- v6: PARTIAL (shape good, gate bad) -- do not deploy
- v7: PLANNING
