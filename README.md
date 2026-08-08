# God's Eye

Architecture and extension points are documented in [ARCHITECTURE.md](ARCHITECTURE.md).

A recursive-language-model investigation agent with a desktop GUI and terminal interface. God's Eye ingests heterogeneous datasets — corporate registries, campaign finance records, lobbying disclosures, government contracts, and more — resolves entities across them, and surfaces non-obvious connections through evidence-backed analysis. It operates autonomously with file I/O, shell execution, web search, and recursive sub-agent delegation.

## Download

Source and releases live at [dharunnarayanvenkatesh/god-s-eye](https://github.com/dharunnarayanvenkatesh/god-s-eye):

- **macOS** — `.dmg`
- **Windows** — `.msi`
- **Linux** — `.AppImage`

## Desktop App

The desktop app (`godseye-desktop/`) is a Tauri 2 application with a three-pane layout:

- **Sidebar** — Session management, provider/model settings, and API credential status
- **Chat pane** — Conversational interface showing the agent's objectives, reasoning steps, tool calls, and findings with syntax-highlighted code blocks
- **Knowledge graph** — Interactive Cytoscape.js visualization of entities and relationships discovered during investigation. Nodes are color-coded by category (corporate, campaign-finance, lobbying, contracts, sanctions, etc.). Click a source node to open a slide-out drawer with the full rendered wiki document.

### Features

- **Live knowledge graph** — Entities and connections render in real time as the agent works. Switch between force-directed, hierarchical, and circular layouts. Search and filter by category.
- **Wiki source drawer** — Click any source node to read the full markdown document in a slide-out panel. Internal wiki links navigate between documents and focus the corresponding graph node.
- **Session persistence** — Investigations are saved automatically. Resume previous sessions or start new ones from the sidebar.
- **Background wiki curator** — A lightweight agent runs in the background to keep wiki documents consistent and cross-linked.
- **Multi-provider support** — Switch between OpenAI, Anthropic, OpenRouter, Cerebras, DeepSeek, and Ollama (local) from the sidebar.

### Building from Source

```bash
cd godseye-desktop

# Install frontend dependencies
cd frontend && npm install && cd ..

# Run in development mode
cargo tauri dev

# Build distributable binary
cargo tauri build
```

Requires: Rust stable, Node.js 20+, and platform-specific Tauri dependencies ([see Tauri prerequisites](https://v2.tauri.app/start/prerequisites/)).

## CLI Agent

The Python CLI agent can be used independently of the desktop app.

### Quickstart

```bash
# Install
pip install -e .

# Configure API keys (interactive prompt)
godseye-agent --configure-keys

# Launch the TUI
godseye-agent --workspace /path/to/your/project
```

Or run a single task headlessly:

```bash
godseye-agent --task "Cross-reference vendor payments against lobbying disclosures and flag overlaps" --workspace ./data
```

### Docker

```bash
# Add your API keys to .env, then:
docker compose up
```

The container mounts `./workspace` as the agent's working directory.

## Supported Providers

| Provider | Default Model | Env Var |
|----------|---------------|---------|
| OpenAI | `gpt-5.2` | `OPENAI_API_KEY` |
| Anthropic | `claude-opus-4-6` | `ANTHROPIC_API_KEY` |
| OpenRouter | `anthropic/claude-sonnet-4-5` | `OPENROUTER_API_KEY` |
| Cerebras | `qwen-3-235b-a22b-instruct-2507` | `CEREBRAS_API_KEY` |
| DeepSeek | `deepseek-chat` | `DEEPSEEK_API_KEY` |
| Ollama | `llama3.2` | (none — local) |

### Local Models (Ollama)

[Ollama](https://ollama.com) runs models locally with no API key. Install Ollama, pull a model (`ollama pull llama3.2`), then:

```bash
godseye-agent --provider ollama
godseye-agent --provider ollama --model mistral
godseye-agent --provider ollama --list-models
```

The base URL defaults to `http://localhost:11434/v1` and can be overridden with `GODSEYE_OLLAMA_BASE_URL` or `--base-url`. The first request may be slow while Ollama loads the model into memory; a 120-second first-byte timeout is used automatically.

Run with DeepSeek:

```bash
godseye-agent --provider deepseek --model deepseek-chat
godseye-agent --provider deepseek --model deepseek-reasoner
```

Additional service keys: `EXA_API_KEY` (web search), `VOYAGE_API_KEY` (embeddings).

All keys can also be set with an `GODSEYE_` prefix (e.g. `GODSEYE_OPENAI_API_KEY`), via `.env` files in the workspace, or via CLI flags.

## Agent Tools

The agent has access to 19 tools, organized around its investigation workflow:

**Dataset ingestion & workspace** — `list_files`, `search_files`, `repo_map`, `read_file`, `write_file`, `edit_file`, `hashline_edit`, `apply_patch` — load, inspect, and transform source datasets; write structured findings.

**Shell execution** — `run_shell`, `run_shell_bg`, `check_shell_bg`, `kill_shell_bg` — run analysis scripts, data pipelines, and validation checks.

**Web** — `web_search` (Exa), `fetch_url` — pull public records, verify entities, and retrieve supplementary data.

**Planning & delegation** — `think`, `subtask`, `execute`, `list_artifacts`, `read_artifact` — decompose investigations into focused sub-tasks, each with acceptance criteria and independent verification.

In **recursive mode** (the default), the agent spawns sub-agents via `subtask` and `execute` to parallelize entity resolution, cross-dataset linking, and evidence-chain construction across large investigations.

## Source Catalog

God's Eye ships with a curated OSINT source catalog covering corporate
registries, beneficial ownership, sanctions, procurement, court records, domain
and DNS intelligence, threat intelligence, social/user discovery, developer
footprints, market data, media archives, and public search APIs. Search it with:

```bash
python scripts/search_source_catalog.py "passive dns"
python scripts/search_source_catalog.py --category "Threat Intelligence"
python scripts/search_source_catalog.py --categories
```

To seed missing source pages into the wiki index:

```bash
python scripts/search_source_catalog.py --write-wiki
```

## CLI Reference

```
godseye-agent [options]
```

### Workspace & Session

| Flag | Description |
|------|-------------|
| `--workspace DIR` | Workspace root (default: `.`) |
| `--session-id ID` | Use a specific session ID |
| `--resume` | Resume the latest (or specified) session |
| `--list-sessions` | List saved sessions and exit |

### Model Selection

| Flag | Description |
|------|-------------|
| `--provider NAME` | `auto`, `openai`, `anthropic`, `openrouter`, `cerebras`, `deepseek`, `ollama` |
| `--model NAME` | Model name or `newest` to auto-select |
| `--reasoning-effort LEVEL` | `low`, `medium`, `high`, or `none` |
| `--list-models` | Fetch available models from the provider API |

### Execution

| Flag | Description |
|------|-------------|
| `--task OBJECTIVE` | Run a single task and exit (headless) |
| `--recursive` | Enable recursive sub-agent delegation |
| `--acceptance-criteria` | Judge subtask results with a lightweight model |
| `--max-depth N` | Maximum recursion depth (default: 4) |
| `--max-steps N` | Maximum steps per call (default: 100) |
| `--timeout N` | Shell command timeout in seconds (default: 45) |

### UI

| Flag | Description |
|------|-------------|
| `--no-tui` | Plain REPL (no colors or spinner) |
| `--headless` | Non-interactive mode (for CI) |
| `--demo` | Censor entity names and workspace paths in output |

### Persistent Defaults

Use `--default-model`, `--default-reasoning-effort`, or per-provider variants like `--default-model-openai` to save workspace defaults to `.godseye/settings.json`. View them with `--show-settings`.

## Configuration

Keys are resolved in this priority order (highest wins):

1. CLI flags (`--openai-api-key`, etc.)
2. Environment variables (`OPENAI_API_KEY` or `GODSEYE_OPENAI_API_KEY`)
3. `.env` file in the workspace
4. Workspace credential store (`.godseye/credentials.json`)
5. User credential store (`~/.godseye/credentials.json`)

All runtime settings can also be set via `GODSEYE_*` environment variables (e.g. `GODSEYE_MAX_DEPTH=8`).

## Project Structure

```
godseye-desktop/         Tauri 2 desktop application
  crates/
    godseye-tauri/            Tauri backend (Rust)
      src/commands/           IPC command handlers (agent, wiki, config)
    godseye-core/             Shared core library
  frontend/                   TypeScript/Vite frontend
    src/components/           UI components (ChatPane, GraphPane, InputBar, Sidebar)
    src/graph/                Cytoscape.js graph rendering
    src/api/                  Tauri IPC wrappers
    e2e/                      Playwright E2E tests

agent/                        Python CLI agent
  __main__.py                 CLI entry point and REPL
  engine.py                   Recursive language model engine
  runtime.py                  Session persistence and lifecycle
  model.py                    Provider-agnostic LLM abstraction
  builder.py                  Engine/model factory
  tools.py                    Workspace tool implementations
  tool_defs.py                Tool JSON schemas
  prompts.py                  System prompt construction
  config.py                   Configuration dataclass
  credentials.py              Credential management
  tui.py                      Rich terminal UI
  demo.py                     Demo mode (output censoring)
  patching.py                 File patching utilities
  settings.py                 Persistent settings

tests/                        Unit and integration tests
```

## Development

### Desktop App

```bash
cd godseye-desktop

# Development mode (hot-reload)
cargo tauri dev

# Frontend tests
cd frontend && npm test

# E2E tests (Playwright)
cd frontend && npm run test:e2e

# Backend tests
cargo test
```

### CLI Agent

```bash
# Install in editable mode
pip install -e .

# Run tests
python -m pytest tests/

# Skip live API tests
python -m pytest tests/ --ignore=tests/test_live_models.py --ignore=tests/test_integration_live.py
```

Requires Python 3.10+. Dependencies: `rich`, `prompt_toolkit`, `pyfiglet`.

## License

MIT — see [LICENSE](LICENSE) for details.
