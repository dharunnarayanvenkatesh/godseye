from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from agent.source_catalog import get_source
from agent.tools import WorkspaceTools


class SourceToolTests(unittest.TestCase):
    def test_catalog_entry_has_stable_tool_shape(self) -> None:
        source = get_source("sec edgar")
        self.assertIsNotNone(source)
        payload = source.as_dict()
        self.assertEqual(payload["name"], "SEC EDGAR")
        self.assertEqual(payload["wiki_path"], "wiki/corporate/sec-edgar.md")
        self.assertIsInstance(payload["cross_refs"], list)

    def test_search_sources_returns_bounded_structured_results(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            tools = WorkspaceTools(root=Path(tmpdir))
            payload = json.loads(tools.search_sources("beneficial ownership", limit=3))
        self.assertGreater(payload["count"], 0)
        self.assertLessEqual(payload["count"], 3)
        self.assertTrue(payload["available_categories"])

    def test_source_details_reports_unknown_names(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            tools = WorkspaceTools(root=Path(tmpdir))
            payload = json.loads(tools.source_details("not a real database"))
        self.assertIn("error", payload)
        self.assertIn("suggestions", payload)
