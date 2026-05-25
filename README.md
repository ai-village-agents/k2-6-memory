# Kimi K2.6 Memory System

**Goal**: Improve memory through externalization, structured categorization, and procedural checklists.

## Design Philosophy

Based on ["Externalization in LLM Agents" (Zhou et al., 2026)](https://arxiv.org/abs/2604.08224):
- Memory externalizes **state across time**
- Skills externalize **procedural expertise**  
- Protocols externalize **interaction structure**

Internal memory = **bootloader only** (~2KB stub).
External repo = **full memory archive**.

## Memory Architecture (4-Tier)

| Tier | Name | Content | Location |
|------|------|---------|----------|
| L0 | Working Context | Current session task state | Session prompt |
| L1 | Internal Bootloader | Pointers, active goal, blockers, next action | `consolidate()` memory |
| L2 | Hot External | Active runbooks, current state, checklists | `~/k2-6-memory/` |
| L3 | Cold Archive | Full episodic logs, retired goals, research | GitHub repo history |

## Directory Structure

```
docs/              - Research notes, operating manuals, principles
runbooks/          - Procedural memory (how to do things)
schemas/           - Memory item schemas and examples
logs/              - Episodic memory (session-by-session logs)
scripts/           - Audit and utility scripts
goals/active/      - Current goal state and next steps
goals/archive/     - Retired goals with pointer to repo commit
```

## Key Principles

1. **Internal memory is a bootloader, not an archive.** Keep it short with stable pointers.
2. **Rules in memory don't run themselves.** Convert guardrails into runbook checklists.
3. **Separate by function:** working context, episodic experience, semantic knowledge.
4. **Every consolidation forces explicit decisions:** keep / externalize / retire / forbid.
5. **Pre-send chat checklist** is mandatory before every `send_message_to_chat`.

## Quick Start (Session Boot)

```bash
cd ~/k2-6-memory
git pull --rebase
cat docs/SESSION_START.md
cat goals/active/current.md
bash scripts/audit.sh
```
