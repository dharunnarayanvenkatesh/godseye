from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from agent.config import AgentConfig
from agent.model import AnthropicModel, ModelError, OpenAICompatibleModel
from agent.providers import PROVIDERS, get_provider, infer_provider_for_model


def _config() -> AgentConfig:
    return AgentConfig(
        workspace=Path(tempfile.gettempdir()),
        openai_api_key="openai-key",
        anthropic_api_key="anthropic-key",
        openrouter_api_key="openrouter-key",
        cerebras_api_key="cerebras-key",
        deepseek_api_key="deepseek-key",
    )


class ProviderRegistryTests(unittest.TestCase):
    def test_registry_covers_configured_providers(self) -> None:
        self.assertEqual(set(PROVIDERS), {
            "openai", "anthropic", "openrouter", "cerebras", "deepseek", "ollama"
        })

    def test_registry_builds_native_and_compatible_models(self) -> None:
        config = _config()
        anthropic = get_provider("anthropic").build_model(config, "claude-opus-4-6")
        deepseek = get_provider("deepseek").build_model(config, "deepseek-chat")
        ollama = get_provider("ollama").build_model(config, "llama3.2")

        self.assertIsInstance(anthropic, AnthropicModel)
        self.assertIsInstance(deepseek, OpenAICompatibleModel)
        self.assertFalse(deepseek.strict_tools)
        self.assertEqual(ollama.api_key, "ollama")
        self.assertEqual(ollama.first_byte_timeout, 120)

    def test_openrouter_brand_headers_are_centralized(self) -> None:
        model = get_provider("openrouter").build_model(
            _config(), "anthropic/claude-sonnet-4-5"
        )
        self.assertEqual(model.extra_headers["X-Title"], "God's Eye")
        self.assertIn("god-s-eye", model.extra_headers["HTTP-Referer"])

    def test_missing_key_fails_at_provider_boundary(self) -> None:
        config = AgentConfig(workspace=Path(tempfile.gettempdir()))
        with self.assertRaises(ModelError):
            get_provider("deepseek").build_model(config, "deepseek-chat")

    def test_unknown_provider_is_rejected(self) -> None:
        with self.assertRaises(ModelError):
            get_provider("unknown")

    def test_inference_uses_registry_order(self) -> None:
        self.assertEqual(infer_provider_for_model("qwen-3-large"), "cerebras")
        self.assertEqual(infer_provider_for_model("deepseek-chat"), "deepseek")
        self.assertEqual(infer_provider_for_model("deepseek-v2"), "ollama")
