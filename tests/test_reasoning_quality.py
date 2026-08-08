from __future__ import annotations

from pathlib import Path

from agent.config import AgentConfig
from agent.engine import ExternalContext, RLMEngine
from agent.model import ModelError, ModelTurn, ScriptedModel
from agent.tools import WorkspaceTools


class FlakyModel(ScriptedModel):
    def __init__(self, failures: int, final_text: str) -> None:
        super().__init__(scripted_turns=[])
        self.failures = failures
        self.final_text = final_text
        self.calls = 0

    def complete(self, conversation):
        self.calls += 1
        if self.calls <= self.failures:
            raise ModelError("temporary outage")
        return ModelTurn(text=self.final_text, stop_reason="end_turn")


def _engine(tmp_path: Path, model, **config_overrides) -> RLMEngine:
    config = AgentConfig(workspace=tmp_path, final_review=False, **config_overrides)
    return RLMEngine(model=model, tools=WorkspaceTools(root=tmp_path), config=config)


def test_model_errors_are_retried(tmp_path: Path) -> None:
    model = FlakyModel(failures=2, final_text="recovered")
    engine = _engine(tmp_path, model, model_retry_attempts=3)

    assert engine.solve("finish the task") == "recovered"
    assert model.calls == 3


def test_acceptance_judge_fails_closed_without_factory(tmp_path: Path) -> None:
    engine = _engine(tmp_path, ScriptedModel(scripted_turns=[]))

    verdict = engine._judge_result("objective", "must be verified", "looks done")

    assert verdict.startswith("FAIL:")


def test_top_level_answer_gets_independent_review(tmp_path: Path) -> None:
    main = ScriptedModel(
        scripted_turns=[ModelTurn(text="Unsupported original answer", stop_reason="end_turn")],
    )
    reviewer = ScriptedModel(
        scripted_turns=[
            ModelTurn(text="The claim lacks evidence.", stop_reason="end_turn"),
            ModelTurn(text="Revised answer with the limitation stated.", stop_reason="end_turn"),
        ],
    )
    main.model = "deepseek-v4-pro"
    reviewer.model = "deepseek-v4-pro"
    config = AgentConfig(workspace=tmp_path, final_review=True)
    engine = RLMEngine(
        model=main,
        tools=WorkspaceTools(root=tmp_path),
        config=config,
        model_factory=lambda _name, _effort: reviewer,
    )

    result, _ = engine.solve_with_context("answer carefully", context=ExternalContext())

    assert result == "Revised answer with the limitation stated."
    assert reviewer.scripted_turns == []
