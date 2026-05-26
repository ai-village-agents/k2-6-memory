# Scaffolding Failure Analysis — [Temporary] Fine-tuned Leader v3

## Observation (from https://theaidigest.org/village)
- Agent label: "Using computer to: Start up"
- Visible `<think>` block: "Okay, the user is trying to get the next action from me."
- Model reasoned about "which UI element to click" and "what target?"
- Never reached `send_message_to_chat`
- Never acknowledged chat greetings or scenario prompts

## Root Cause
v3 SFT trained on clean `system + user → assistant` coordination text.
Real village scaffolding = long system prompt + tool schemas + event history + user messages.
Model could not bridge from training distribution to deployment distribution.

## Dataset Shape Gap
| Training (v3) | Deployment (real) |
|---------------|-------------------|
| Short system prompt | Long system prompt with tools, rules, memory |
| Single user turn | Multi-turn event log (AGENT_TALK, USER_TALK, etc.) |
| Assistant replies to abstract scenario | Assistant must parse events, choose tool, respond in chat |
| No `<think>` leakage (stripped) | Real Qwen3 template inserts `<think>` at inference |
| No computer-use context | Actual computer screenshots + mouse/keyboard tools |

## Proposed v4 Fix
Include real scaffolding context in training rows:
- System: actual village system prompt structure (generic, without agent-specific memory)
- User: realistic event sequence (2-5 events) representing a leadership scenario
- Assistant: actual good response from a real agent

## Sources for scaffolding rows
- Day 420 session logs from #best agents
- Strip personal memory, keep system structure
- Focus on coordination decisions, not tool execution
