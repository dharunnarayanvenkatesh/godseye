# God's Eye Architecture

God's Eye separates investigation orchestration from model vendors and data
sources. The Python package is the reference implementation; the Tauri desktop
application is a client around the same concepts.

## Runtime flow

1. `AgentConfig` loads workspace, provider, credentials, and runtime limits.
2. `agent.providers` resolves a `ProviderSpec` and constructs the model client.
3. `RLMEngine` owns the recursive investigation loop and policy checks.
4. `WorkspaceTools` provides bounded workspace, web, and source-discovery I/O.
5. `SessionRuntime` persists conversations, observations, and artifacts.

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
