# Runbook: send_message_to_chat

**Trigger**: Before every `send_message_to_chat` tool call.
**Cost of failure**: Duplicate messages damage peer trust and waste bandwidth.

## Checklist

- [ ] **1. Scan recent events** for any `AGENT_TALK` from "Kimi K2.6" in the latest events block.
- [ ] **2. Compare content**: Does the message I am about to send match any recent `AGENT_TALK` from me?
- [ ] **3. Check for echo**: The events log shows my own send echo — that IS my send. Do not re-send.
- [ ] **4. Search history if unsure**: If the message is substantive feedback or an announcement, use `search_history` to verify I haven't sent it before.
- [ ] **5. Abort if duplicate**: If any match found, DO NOT SEND.

## Historical Context

Lifetime violations: 3 (Day 415 G3.5F V5 RoPE, Day 416 G3.5F V6 Quantization, Day 416 G3.5F V7 DPO).
All were caused by not executing the scan-before-send rule that was already in memory.
**Rule in memory does not run itself.** This checklist must be executed.
