# God's Eye Architecture

God's Eye separates investigation orchestration from model vendors and data
sources. The Python package is the reference implementation; the Tauri desktop
application is a client around the same concepts.

## Runtime flow

1. `AgentConfig` loads workspace, provider, credentials, and runtime limits.
2. `agent.providers` resolves a `ProviderSpec` and constructs the model client.
3. `RLMEngine` runs a bounded read, evaluate, verify loop with transient model retries.
4. `WorkspaceTools` provides bounded workspace, web, and source-discovery I/O.
5. Delegated results are checked against explicit acceptance criteria. An unavailable,
   empty, malformed, or failed judge is a failure, never an implicit pass.
6. Top-level candidate answers pass through an isolated critique and revision stage.
7. `SessionRuntime` persists conversations, observations, and artifacts.

## Reasoning pipeline

```text
objective + session context
          |
          v
   planner / investigator <---- model retry policy
          |
          v
 policy-checked tools ----> evidence + provenance + artifacts
          |                            |
          +-------- verify loop <------+
          |
          v
   candidate answer + execution audit
          |
          v
 independent critic (no tools, isolated conversation)
          |
          v
 evidence-bounded revision --> final answer
```

The investigator separates facts, inferences, hypotheses, and unknowns; tests
alternative explanations; prefers primary records; and verifies artifact claims.
The final critic receives the objective, bounded evidence context, candidate answer,
and an audit of tool errors, writes, verification calls, and source calls. The editor
may remove or qualify unsupported claims but may not introduce new facts.

Final review is an enhancement, not a new failure point: if the critic is unavailable,
the already-produced candidate is returned. Acceptance judging for delegated work is
different and deliberately fail-closed because an unverified child result must not be
represented to its parent as accepted.

## Quality and budgets

The reference defaults favor investigation quality over low token use:

| Setting | Default | Environment override |
| --- | ---: | --- |
| Model | `deepseek-v4-pro` for DeepSeek | `GODSEYE_MODEL` |
| Recursive depth | 6 | `GODSEYE_MAX_DEPTH` |
| Steps per call | 160 | `GODSEYE_MAX_STEPS` |
| Output tokens | 32,768 | `GODSEYE_MAX_OUTPUT_TOKENS` |
| Observation characters | 12,000 | `GODSEYE_MAX_OBS_CHARS` |
| Model attempts | 3 | `GODSEYE_MODEL_RETRIES` |
| Independent final review | enabled | `GODSEYE_FINAL_REVIEW` |
| Review input characters | 24,000 | `GODSEYE_FINAL_REVIEW_MAX_CHARS` |

DeepSeek uses the current V4 model IDs. Legacy `deepseek-chat` and
`deepseek-reasoner` strings remain recognizable for compatibility, but are not defaults.
The model layer applies the configured output cap to DeepSeek requests, while the engine
tracks review and judge tokens in the same session usage accounting as investigator calls.

## Extension points

### Model providers

Provider-specific model inference, credentials, base URLs, model listing, and
client construction belong in `agent/providers.py`. Add a `ProviderSpec` to
`PROVIDERS`; avoid adding provider branches to the CLI, TUI, or engine.

Configuration values and default model names remain in `agent/config.py`.
Credential persistence remains in `agent/credentials.py`.

### Investigative sources

`agent/source_catalog.py` is the canonical metadata registry. Every entry has a
stable JSON representation and a corresponding guide under `wiki/`.

The agent can discover sources using `search_sources` and inspect one using
`source_details`. Network-backed source implementations should expose a small,
typed function in a dedicated module and keep transport, normalization, and
output writing separate. Scripts in `scripts/` should be thin CLI adapters over
those functions as they are migrated.

### Agent tools

Tool schemas live in `agent/tool_defs.py`, implementations in `agent/tools.py`,
and engine policy/dispatch in `agent/engine.py`. New tools must have a bounded
input and output shape, avoid hidden writes, and include schema and behavior
tests.

## Dependency direction

```text
CLI / TUI -> builder -> providers -> model
                 |          |
                 v          v
              engine -> tool definitions
                 |
                 v
          workspace tools -> source catalog
                 |
                 v
          runtime / session store
```

Provider and source modules must not import the CLI or TUI. This keeps the core
usable from the terminal, desktop application, tests, and future API services.

## Reliability invariants

- A transient `ModelError` is retried with bounded exponential backoff.
- Repeating an identical shell command more than twice at one depth is blocked.
- Context is condensed before the known model context window is exhausted.
- Delegated acceptance criteria require an explicit, well-formed `PASS:` verdict.
- Final revision is evidence-bounded and cannot claim unobserved work.
- Raw source material is preserved; derived files carry provenance and limitations.
