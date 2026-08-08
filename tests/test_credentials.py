from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from agent.credentials import (
    CredentialBundle,
    CredentialStore,
    discover_env_candidates,
    parse_env_file,
)
from agent.builder import infer_provider_for_model
from agent.config import PROVIDER_DEFAULT_MODELS


class CredentialTests(unittest.TestCase):
    def test_deepseek_provider_defaults_and_inference(self) -> None:
        self.assertEqual(PROVIDER_DEFAULT_MODELS["deepseek"], "deepseek-chat")
        self.assertEqual(infer_provider_for_model("deepseek-chat"), "deepseek")
        self.assertEqual(infer_provider_for_model("deepseek-reasoner"), "deepseek")

    def test_parse_env_file_extracts_supported_keys(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            env_path = Path(tmpdir) / ".env"
            env_path.write_text(
                "\n".join(
                    [
                        "OPENAI_API_KEY=oa-key",
                        "ANTHROPIC_API_KEY=an-key",
                        "OPENROUTER_API_KEY=or-key",
                        "DEEPSEEK_API_KEY=ds-key",
                        "EXA_API_KEY=exa-key",
                    ]
                ),
                encoding="utf-8",
            )
            creds = parse_env_file(env_path)
            self.assertEqual(creds.openai_api_key, "oa-key")
            self.assertEqual(creds.anthropic_api_key, "an-key")
            self.assertEqual(creds.openrouter_api_key, "or-key")
            self.assertEqual(creds.deepseek_api_key, "ds-key")
            self.assertEqual(creds.exa_api_key, "exa-key")

    def test_store_roundtrip(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            store = CredentialStore(workspace=root, session_root_dir=".godseye")
            creds = CredentialBundle(
                openai_api_key="oa",
                anthropic_api_key="an",
                openrouter_api_key="or",
                deepseek_api_key="ds",
                exa_api_key="exa",
            )
            store.save(creds)
            loaded = store.load()
            self.assertEqual(loaded, creds)

    def test_discover_env_candidates_includes_workspace_env(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            workspace = Path(tmpdir) / "RLMCode"
            workspace.mkdir(parents=True, exist_ok=True)
            candidates = discover_env_candidates(workspace)
            self.assertGreaterEqual(len(candidates), 1)
            self.assertEqual(candidates[0].resolve(), (workspace / ".env").resolve())


if __name__ == "__main__":
    unittest.main()
