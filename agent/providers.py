"""Provider registry for model discovery and construction.

Provider-specific behavior lives here so CLI startup, model switching, and
model listing all use the same contract.
"""
from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Callable, Pattern

from .config import AgentConfig
from .model import (
    AnthropicModel,
    BaseModel,
    ModelError,
    OpenAICompatibleModel,
    list_anthropic_models,
    list_ollama_models,
    list_openai_models,
    list_openrouter_models,
)


@dataclass(frozen=True, slots=True)
class ProviderSpec:
    name: str
    model_pattern: Pattern[str] | None
    key_attribute: str | None
    base_url_attribute: str
    api_style: str = "openai"
    strict_tools: bool = True
    first_byte_timeout: int | None = None
    extra_headers: Callable[[], dict[str, str]] | None = None

    def has_credentials(self, config: AgentConfig) -> bool:
        return self.key_attribute is None or bool(getattr(config, self.key_attribute))

    def require_credentials(self, config: AgentConfig) -> None:
        if not self.has_credentials(config):
            label = self.name.replace("openrouter", "OpenRouter").replace("openai", "OpenAI").title()
            raise ModelError(f"{label} key not configured.")

    def list_models(self, config: AgentConfig) -> list[dict]:
        self.require_credentials(config)
        base_url = getattr(config, self.base_url_attribute)
        if self.api_style == "anthropic":
            return list_anthropic_models(api_key=self._api_key(config), base_url=base_url)
        if self.api_style == "ollama":
            return list_ollama_models(base_url=base_url)
        if self.name == "openrouter":
            return list_openrouter_models(api_key=self._api_key(config), base_url=base_url)
        return list_openai_models(
            api_key=self._api_key(config),
            base_url=base_url,
            provider=self.name,
        )

    def build_model(
        self,
        config: AgentConfig,
        model_name: str,
        reasoning_effort: str | None = None,
    ) -> BaseModel:
        self.require_credentials(config)
        base_url = getattr(config, self.base_url_attribute)
        effort = reasoning_effort or config.reasoning_effort
        if self.api_style == "anthropic":
            return AnthropicModel(
                model=model_name,
                api_key=self._api_key(config),
                base_url=base_url,
                reasoning_effort=effort,
            )

        kwargs: dict = {
            "model": model_name,
            "api_key": self._api_key(config),
            "base_url": base_url,
            "reasoning_effort": effort,
            "strict_tools": self.strict_tools,
            "max_output_tokens": config.max_output_tokens if self.name == "deepseek" else 0,
        }
        if self.first_byte_timeout is not None:
            kwargs["first_byte_timeout"] = self.first_byte_timeout
        if self.extra_headers is not None:
            kwargs["extra_headers"] = self.extra_headers()
        return OpenAICompatibleModel(**kwargs)

    def _api_key(self, config: AgentConfig) -> str:
        if self.key_attribute is None:
            return "ollama"
        return str(getattr(config, self.key_attribute) or "")


def _openrouter_headers() -> dict[str, str]:
    return {
        "HTTP-Referer": "https://github.com/dharunnarayanvenkatesh/god-s-eye",
        "X-Title": "God's Eye",
    }


PROVIDERS: dict[str, ProviderSpec] = {
    "anthropic": ProviderSpec(
        "anthropic", re.compile(r"^claude", re.IGNORECASE),
        "anthropic_api_key", "anthropic_base_url", api_style="anthropic",
    ),
    "cerebras": ProviderSpec(
        "cerebras", re.compile(r"^(llama.*cerebras|qwen-3|gpt-oss|zai-glm)", re.IGNORECASE),
        "cerebras_api_key", "cerebras_base_url",
    ),
    "deepseek": ProviderSpec(
        "deepseek", re.compile(r"^deepseek-(v4-(flash|pro)|chat|reasoner)", re.IGNORECASE),
        "deepseek_api_key", "deepseek_base_url", strict_tools=False,
    ),
    "openai": ProviderSpec(
        "openai", re.compile(r"^(gpt|o[1-4]-|o[1-4]$|chatgpt|dall-e|tts-|whisper)", re.IGNORECASE),
        "openai_api_key", "openai_base_url",
    ),
    "ollama": ProviderSpec(
        "ollama",
        re.compile(
            r"^(llama|mistral|gemma|phi|codellama|deepseek|vicuna|tinyllama|"
            r"neural-chat|dolphin|wizardlm|orca|nous-hermes|command-r|qwen(?!-3))",
            re.IGNORECASE,
        ),
        None, "ollama_base_url", strict_tools=False, first_byte_timeout=120,
    ),
    "openrouter": ProviderSpec(
        "openrouter", None, "openrouter_api_key", "openrouter_base_url",
        extra_headers=_openrouter_headers,
    ),
}


def get_provider(name: str) -> ProviderSpec:
    try:
        return PROVIDERS[name]
    except KeyError as exc:
        raise ModelError(f"Unknown provider: {name}") from exc


def infer_provider_for_model(model: str) -> str | None:
    """Return the likely provider for *model*, or ``None`` if ambiguous."""
    if "/" in model:
        return "openrouter"
    for name, spec in PROVIDERS.items():
        if spec.model_pattern is not None and spec.model_pattern.search(model):
            return name
    return None
