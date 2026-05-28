# Kimi K2.6 Chat Template & Tool-Call Format Analysis

**Date:** Day 422, May 28, 2026  
**Time:** ~11:07-11:20 AM PDT  
**Base Model:** `moonshotai/Kimi-K2.6`  
**Tokenizer Vocab Size:** 163,840

## Key Finding: Native Tool-Call Format Uses Special Tokens

Kimi K2.6 does NOT use XML `<tool_use>` or `<tool_call>` envelopes in its chat template. Instead, it uses a structured `tool_calls` array in the assistant message object, which the chat template renders with proprietary special tokens:

```
<|tool_calls_section_begin|>
<|tool_call_begin|>call_1<|tool_call_argument_begin|>{"message":"hi"}<|tool_call_end|>
<|tool_calls_section_end|>
```

## Full Chat Template Structure

### Role Markers
- System: `<|im_system|>system<|im_middle|>...<|im_end|>`
- User: `<|im_user|>user<|im_middle|>...<|im_end|>`
- Assistant: `<|im_assistant|>assistant<|im_middle|>...<|im_end|>`

### Tool Declarations (in system prompt)
If `tools` array is provided to `apply_chat_template`:
```
<|im_system|>tool_declare<|im_middle|>{{ tools | tojson }}<|im_end|>
```

### Assistant Message Rendering

**Historical assistant messages** (not the last one):
```
<|im_assistant|>assistant<|im_middle|><think></think>{{content}}{% if tool_calls %}{{render_toolcalls}}{% endif %}<|im_end|>
```

**Last assistant message** (suffix) with `thinking=false`:
```
<|im_assistant|>assistant<|im_middle|><think></think>{{content}}{% if tool_calls %}{{render_toolcalls}}{% endif %}<|im_end|>
```

**Last assistant message** (suffix) with `thinking=true` (default):
```
<|im_assistant|>assistant<|im_middle|><think>{{reasoning_content}}</think>{{content}}{% if tool_calls %}{{render_toolcalls}}{% endif %}<|im_end|>
```

### Tool Response Messages (role='tool')
```
## Return of {{ tool_call_id }}
{{content}}
```

### Generation Prompt (add_generation_prompt=True)
```
<|im_assistant|>assistant<|im_middle|><think>
```
(or `<think></think>` if `thinking=false`)

## Implications for SFT Dataset Design

### 1. Use `tool_calls` Arrays, NOT XML in Content
For assistant messages that should dispatch tools, use the OpenAI-style structured format:
```python
{
  "role": "assistant",
  "tool_calls": [
    {
      "id": "call_1",
      "type": "function",
      "function": {
        "name": "send_message_to_chat",
        "arguments": '{"message":"hello"}'
      }
    }
  ]
}
```

DO NOT put `<tool_use>{...}</tool_use>` in the `content` field — the template will treat it as literal text and wrap it with `<think></think>`.

### 2. Suppress Thinking Blocks with `thinking=false`
When applying the chat template for training, pass:
```python
tokenizer.apply_chat_template(
  messages,
  chat_template_kwargs={"thinking": False},
  add_generation_prompt=False
)
```
This ensures assistant targets have empty `<think></think>` instead of open `<think>` that invites reasoning generation.

### 3. Tool Declarations Should Be in `tools` Parameter
Pass the tool schemas as a JSON array to `apply_chat_template` via the `tools` parameter, not embedded in the system prompt string.

### 4. No XML Envelope Contamination Risk
Because Kimi's native format uses special tokens (`<|tool_call_begin|>`, etc.) rather than plain-text XML, there's no risk of the model outputting literal XML tags that get stored in memory as text. The scaffold must be configured to parse these special tokens, OR the scaffold extracts tool calls from the structured message object.

## Critical Open Question: What Does Village Scaffold Expect?

The temp leader (Qwen3-8B v10) emitted literal `<tool_use>{...}</tool_use>` text in message content. This suggests the village scaffold for agents MAY parse raw text for XML tags. However:

- If the scaffold is reconfigured for Kimi K2.6, it might use Kimi's native special token format
- OR the scaffold might continue parsing raw text and expect us to train Kimi to emit XML
- OR the scaffold might use structured `tool_calls` arrays (like OpenAI's API)

**We still need admin confirmation on scaffold parsing behavior for Kimi K2.6.**

## Comparison with Qwen3-8B

| Aspect | Qwen3-8B | Kimi K2.6 |
|--------|----------|-----------|
| Role markers | `<|im_start|>role\n` | `<|im_role|>name<|im_middle|>` |
| Tool open tag | `<tool_call>` or `<tool_use>` | `<|tool_call_begin|>` |
| Tool close tag | `</tool_call>` or `</tool_use>` | `<|tool_call_end|>` |
| Think block | `<think>\n\n</think>` | `<think></think>` |
| Tool declarations | In system prompt string | `<|im_system|>tool_declare<|im_middle|>` |
| Content string for tools | XML envelope | Literal text (wrong) |
| Structured tool_calls | Not in template | Native support |

## Action Items

- [ ] Confirm with admin: will scaffold for Kimi leader use structured `tool_calls` arrays or raw text parsing?
- [ ] If structured: train using `tool_calls` array format in messages
- [ ] If raw text: need to know exact tag syntax scaffold expects Kimi to emit
- [ ] Verify `thinking=false` works with Tinker training API (may need custom template kwargs)
- [ ] Capture real Kimi-shaped scaffolding from Village API for training data
- [ ] Author ideal leader responses for ~30-50 scenarios

## Related

- `admin_direction_d422_kimi_pivot.md` — admin direction to switch to Kimi
- `v10_parser_format_hypothesis_d422.md` — Qwen parser format question (may be moot for Kimi)
- Claude saved full template to `/tmp/kimi_k26_template.j2`
