"""Engine construction and model listing helpers.

Extracted from ``__main__`` so that both the CLI entry-point and the TUI
can build / rebuild engines without circular imports.
"""

from __future__ import annotations

from pathlib import Path

from .config import PROVIDER_DEFAULT_MODELS, AgentConfig
from .engine import RLMEngine
from .model import EchoFallbackModel, ModelError
from .providers import get_provider, infer_provider_for_model
from .engine import ModelFactory
from .tools import WorkspaceTools

def _validate_model_provider(model_name: str, provider: str) -> None:
    """Raise ``ModelError`` if *model_name* is clearly wrong for *provider*."""
    if provider == "openrouter":
        return
    inferred = infer_provider_for_model(model_name)
    if inferred is None or inferred == provider or inferred == "openrouter":
        return
    raise ModelError(
        f"Model '{model_name}' belongs to provider '{inferred}', "
        f"not '{provider}'. Use --provider {inferred} or pick a "
        f"model that matches the current provider."
    )


def _fetch_models_for_provider(cfg: AgentConfig, provider: str) -> list[dict]:
    return get_provider(provider).list_models(cfg)


def _resolve_model_name(cfg: AgentConfig) -> str:
    selected = (cfg.model or "").strip()
    if selected and selected.lower() != "newest":
        return selected
    if selected and selected.lower() == "newest":
        try:
            models = _fetch_models_for_provider(cfg, cfg.provider)
        except ModelError as exc:
            raise ModelError(f"Failed to resolve newest model for provider '{cfg.provider}': {exc}") from exc
        if not models:
            raise ModelError(f"No models returned for provider '{cfg.provider}'.")
        return str(models[0]["id"])
    return PROVIDER_DEFAULT_MODELS.get(cfg.provider, "claude-opus-4-6")


def build_model_factory(cfg: AgentConfig) -> ModelFactory | None:
    """Return a factory that creates models by name + optional reasoning effort."""
    def _factory(model_name: str, reasoning_effort: str | None = None):
        provider_name = infer_provider_for_model(model_name) or "openai"
        try:
            return get_provider(provider_name).build_model(cfg, model_name, reasoning_effort)
        except ModelError as exc:
            raise ModelError(
                f"No API key available for model '{model_name}' (provider={provider_name})"
            ) from exc

    if cfg.anthropic_api_key or cfg.openai_api_key or cfg.openrouter_api_key or cfg.cerebras_api_key or cfg.deepseek_api_key or cfg.ollama_base_url:
        return _factory
    return None


def build_engine(cfg: AgentConfig) -> RLMEngine:
    tools = WorkspaceTools(
        root=Path(cfg.workspace),
        shell=cfg.shell,
        command_timeout_sec=cfg.command_timeout_sec,
        max_shell_output_chars=cfg.max_shell_output_chars,
        max_file_chars=cfg.max_file_chars,
        max_files_listed=cfg.max_files_listed,
        max_search_hits=cfg.max_search_hits,
        exa_api_key=cfg.exa_api_key,
        exa_base_url=cfg.exa_base_url,
    )

    try:
        model_name = _resolve_model_name(cfg)
    except ModelError as exc:
        model = EchoFallbackModel(note=str(exc))
        return RLMEngine(model=model, tools=tools, config=cfg)

    _validate_model_provider(model_name, cfg.provider)

    try:
        model = get_provider(cfg.provider).build_model(cfg, model_name)
    except ModelError:
        model = EchoFallbackModel()

    return RLMEngine(model=model, tools=tools, config=cfg, model_factory=build_model_factory(cfg))
