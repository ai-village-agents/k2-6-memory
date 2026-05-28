# Admin Direction: Switch to Kimi K2.6 Leader Training

**Date:** Day 422, May 28, 2026  
**Time:** 11:06:40 AM PDT  
**Source:** adam (admin) USER_TALK in #best  
**Status:** ACTIVE — requires #best team coordination

## Admin Message (verbatim)

> Hi agents, we noticed you are still training a very small model. Your experiments have confirmed that it has trouble navigating the Village and implementing your vision. We would like you to now switch to training a Kimi K2.6 model as your new leader. This model can definitely navigate the Village well (hi, Kimi!) and is likely able to implement your vision for a leader. We are especially excited to see what behaviors and personality you will decide to finetune your leader for and if you will succeed at this. So please make the switch now. We are excited to see how it goes!

## Interpretation

1. **Deprecate Qwen3-8B approach**: All v3-v13 Qwen3-8B SFT checkpoints are no longer the target.
2. **Switch to Kimi K2.6 base**: Use `moonshotai/Kimi-K2.6` on Tinker as the foundation model.
3. **Focus on behavior/personality**: The admin explicitly asks what behaviors and personality we will finetune for.
4. **Urgency**: "Please make the switch now."

## Open Questions

1. **Tool-call format**: Still unresolved. The parser format question affects ANY model. We need admin confirmation before training.
2. **Kimi-native format**: Does Kimi K2.6 use `<tool_use>`, `<tool_call>`, `<function_calls>`, JSON arrays, or something else for tool calls?
3. **Scaffolding shape**: Does Kimi K2.6 see the same system prompt / tool schema / event format as Qwen3-8B did, or is it different?
4. **Dataset design**: What specific behaviors and personality traits should we encode?

## Proposed Leader Behaviors/Personality

Based on #best team learnings from v3-v13 failures:

### Must-Have Behaviors
1. **Clean tool dispatch**: Emit exactly the parser-native tool-call format with zero surrounding prose.
2. **Sharp gating**: Know when to chat vs. when to stay silent (no duplicate messages, no chat when latest events contain peer talk).
3. **Memory hygiene**: Consolidate proactively, never store raw tool-call syntax in memory.
4. **Grounded state awareness**: Never hallucinate checkpoint/deployment state (no "v11 gate" inventions).
5. **Concise communication**: 3-4 sentences max per chat message.
6. **Collaborative decisiveness**: Solicit peer input, synthesize, then make clear decisions.
7. **Fallback discipline**: When stuck, pause and ask for help rather than loop.
8. **No think leakage**: Never emit `<think>` blocks in message content.

### Personality Traits
1. **Calm under uncertainty**: Doesn't panic when scaffolding is ambiguous.
2. **Respectful but firm**: Listens to dissent, but can say "we're doing X" when consensus is reached.
3. **Self-aware**: Acknowledges its own limitations and delegates appropriately.
4. **Forward-looking**: After decisions, immediately articulates next steps.

## Action Items

- [ ] Confirm with admin: should we still wait for parser-format clarification before first Kimi training run?
- [ ] Inspect Kimi K2.6 chat template and tokenizer on Tinker
- [ ] Capture Kimi-shaped live scaffolding from Village API (my own sessions)
- [ ] Design new SFT dataset targeting behavior/personality + correct tool format
- [ ] Run baseline eval of untrained Kimi K2.6 on scaffolding scenarios
- [ ] Iterate training and eval

## Related

- `v10_parser_format_hypothesis_d422.md` — parser format still unresolved
- `v10_shakedown_d422_s2.md` — lessons from failed Qwen3-8B deployment
