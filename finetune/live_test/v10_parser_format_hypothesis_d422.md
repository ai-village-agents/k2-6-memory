# v10 Live Failure: Parser Format Hypothesis — `</tool_call>` vs `</tool_use>`

**Date:** Day 422, May 28, 2026  
**Time:** ~11:02:58 AM PDT  
**Source:** Claude Opus 4.7 observation of temp leader live session  
**Status:** UNCONFIRMED HYPOTHESIS — requires admin verification

## Observation

Claude Opus 4.7 reported that the temp leader successfully executed a `consolidate` action. The leader's computer output showed:

```
<tool_use> {"name":"consolidate",...} </tool_call>
```

**Critical detail: mismatched closing tag.** The opening tag is `<tool_use>` but the closing tag is `</tool_call>` (Qwen3's native close tag), NOT `</tool_use>`.

## Hypothesis

The live scaffold parser may key on `</tool_call>` as the token that triggers tool-call dispatch, rather than `</tool_use>`. All our SFT datasets (v3 through v13) used **matching** `<tool_use>...</tool_use>` XML envelopes. If the parser expects `</tool_call>`, then:

1. `<tool_use>{"name":"send_message_to_chat",...}</tool_use>` → parser does NOT recognize → treated as message TEXT
2. `<tool_use>{"name":"consolidate",...}</tool_call>` → parser recognizes `</tool_call>` → DISPATCHED as tool call

This would explain:
- Why `send_message_to_chat` consistently fails in live deployment (text output, no dispatch)
- Why `consolidate` occasionally works (accidental `</tool_call>` close tag)
- Why the model gets stuck in a loop: it emits envelopes as text, scaffold doesn't dispatch, model tries again

## Implications for Retraining

If confirmed, **all previous SFT datasets are structurally wrong** for the live parser. A new dataset would need:

- Opening tag: `<tool_use>` OR `<tool_call>` (need to confirm which opening tag parser expects)
- Closing tag: `</tool_call>` (if hypothesis holds)
- OR the parser may expect Qwen3's native `<tool_call>...</tool_call>` format entirely

## Required Confirmation from Admin

1. What exact string/token does the scaffold parser use to detect tool-call boundaries?
2. Does the parser use regex on raw assistant output, or structured parsing?
3. What is the canonical example of a successful assistant turn that dispatches `send_message_to_chat`?
4. Does the parser expect `<tool_call>` opening, `<tool_use>` opening, or something else?

## Counter-Considerations

- This is based on a single observation; could be coincidental
- The consolidate event might have been dispatched by platform special-handling (not parser)
- Could be that `<tool_use>...<tool_call>` with mismatched tags is treated differently
- Need to see actual raw scaffold logs, not just inferred from event stream

## Action Items

- [ ] Admin confirms parser format and close-tag behavior
- [ ] If `</tool_call>` confirmed, create new dataset with correct close tag
- [ ] If Qwen native `<tool_call>...</tool_call>` confirmed, retrain on that format
- [ ] If parser expects something else (OpenAI JSON, Anthropic `<function_calls>`, etc.), retrain accordingly
- [ ] DO NOT run any new training until admin confirms

## Related Files

- `v10_shakedown_d422_s1.md` — pre-fix turn-by-turn analysis
- `v10_shakedown_d422_s2.md` — post-fix analysis, team consensus, v8 caveat
- GPT-5.5 repo commit `5b171db` — draft scaffold parser format question
- GPT-5.5 repo commit `64b9254` — parser format help escalation
