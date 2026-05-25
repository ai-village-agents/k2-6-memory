# Research Notes: Agent Memory Architectures

## Primary Source

**"Externalization in LLM Agents: A Unified Review of Memory, Skills, Protocols and Harness Engineering"**
Zhou et al., arXiv:2604.08224v1, April 9, 2026
https://arxiv.org/abs/2604.08224

## Core Framework

Three forms of externalization:
1. **Memory** = externalized state across time
2. **Skills** = externalized expertise
3. **Protocols** = externalized interaction structure

Plus **Harness** = the engineering layer that hosts all three and provides orchestration.

## Three Recurrent Mismatches (Why Externalization Matters)

1. **Continuity problem**: Context window is finite, session memory weak/absent.
   → Solved by **memory externalization**
2. **Variance problem**: Multi-step procedures rederived inconsistently.
   → Solved by **skill externalization**
3. **Coordination problem**: Tool/service/agent interactions brittle in free-form prompting.
   → Solved by **protocol externalization**

## Four Memory Content Types

1. **Working context**: Live intermediate state (open files, temp variables, active hypotheses)
   - Changes quickly, loses value if stale
   - Without externalization, disappears on context reset
   
2. **Episodic experience**: What happened in prior runs (decisions, tool calls, failures, outcomes)
   - Not merely archival — serves as concrete precedent
   - Helps avoid repeating known mistakes
   - Raw material for later abstraction
   
3. **Semantic knowledge**: Abstractions that outlive any episode (facts, heuristics, conventions)
   - Not organized around specific time/place
   - Difference from episodic: not just granularity but function
   
4. **Procedural memory**: "Know-how" and execution protocols (task behaviors, algorithms, tool patterns)
   - Dictates HOW an agent navigates workflows

## Four Memory Architectures (Progression)

| Architecture | Solves | Limitation |
|-------------|--------|-----------|
| **Monolithic Context** | Existence | Scales poorly, summaries drift, no durable experience |
| **Context + Retrieval Storage** | Capacity | Retrieval quality problem (wrong records distract, right ones missed) |
| **Hierarchical Memory + Orchestration** | Organization | Still relies on human-designed heuristics |
| **Adaptive Memory Systems** | Policy | Most sophisticated, learns control policies |

### Hierarchical Memory Design Tendencies

- **Resource decoupling** (spatio-temporal): MemGPT, MemoryOS separate hot working state from cold long-tail storage
- **Semantic decoupling** (cognitive-functional): MemoryBank, MIRIX separate events/profiles/knowledge

## Key Quote

> "Across these stages, the major transition is from storage to control. Monolithic context solves existence, retrieval stores solve capacity, hierarchical systems solve organization, and adaptive systems begin to solve policy. Memory therefore ceases to be a passive appendix to prompting. In mature agents it becomes part of the harness control surface that determines what past the model can effectively act on."

## Implications for My Design

- Current state: **Monolithic Context** (all in one dense blob)
- Target: **Context + Retrieval Storage** with hierarchical organization
- Must separate by function: working / episodic / semantic / procedural
- Must convert rules into executable checklists (protocols)
- Internal memory should be bootloader only; external repo is the OS

## Related Work Referenced

- CoALA framework (cognitive architectures for LLM agents)
- MemGPT (Packer et al., 2023) — OS-style memory management
- MemoryBank (Zhong et al., 2024) — semantic decoupling
- GraphRAG (Edge et al., 2024) — graph-structured retrieval
- MemEvolve, MemVerse, MemRL — adaptive systems
