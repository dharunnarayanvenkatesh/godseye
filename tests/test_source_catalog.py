from __future__ import annotations

import json
from pathlib import Path

from agent.source_catalog import CATALOG, categories, get_source, search_catalog
from agent.tools import WorkspaceTools
from agent.wiki_graph import CATEGORY_COLORS, parse_index
from scripts.search_source_catalog import seed_wiki


def test_catalog_contains_requested_source_families() -> None:
    names = {entry.name for entry in CATALOG}
    expected = {
        "OCCRP Aleph",
        "OpenCorporates",
        "OpenSanctions",
        "GLEIF LEI data",
        "UK Companies House",
        "Open Contracting Data Standard",
        "EU TED",
        "CourtListener",
        "RDAP",
        "crt.sh",
        "VirusTotal",
        "Sherlock",
        "GHunt",
        "GDELT",
        "Common Crawl",
        "Internet Archive",
        "Brave Search API",
        "Telegram public channels through Telethon",
        "Public Discord communities",
    }
    assert expected <= names


def test_search_catalog_matches_cross_reference_text() -> None:
    results = search_catalog("passive dns")
    names = {entry.name for entry in results}
    assert "CIRCL Passive DNS" in names
    assert "Farsight DNSDB" in names


def test_catalog_categories_have_graph_colors() -> None:
    missing = {_category_slug(category) for category in categories()} - set(CATEGORY_COLORS)
    assert missing == set()


def test_exact_source_lookup_and_serialization() -> None:
    source = get_source("sec edgar")
    assert source is not None
    payload = source.as_dict()
    assert payload["name"] == "SEC EDGAR"
    assert payload["wiki_path"] == "wiki/corporate/sec-edgar.md"
    assert isinstance(payload["cross_refs"], list)


def test_workspace_tools_expose_catalog(tmp_path: Path) -> None:
    tools = WorkspaceTools(root=tmp_path)
    result = json.loads(tools.search_sources("beneficial ownership", limit=3))
    assert result["count"] > 0
    assert result["count"] <= 3
    assert result["available_categories"]

    details = json.loads(tools.source_details("SEC EDGAR"))
    assert details["homepage"].startswith("https://www.sec.gov/")


def test_unknown_source_returns_structured_error(tmp_path: Path) -> None:
    tools = WorkspaceTools(root=tmp_path)
    result = json.loads(tools.source_details("not a real database"))
    assert "error" in result


def test_seed_wiki_creates_pages_and_index(tmp_path: Path) -> None:
    wiki_dir = tmp_path / "wiki"
    created = seed_wiki(wiki_dir)
    assert created >= len(CATALOG)
    entries = parse_index(wiki_dir)
    names = {entry.name for entry in entries}
    assert "OCCRP Aleph" in names
    assert "VirusTotal" in names
    assert (wiki_dir / "threat-intel" / "virustotal.md").exists()


def _category_slug(display_name: str) -> str:
    return display_name.strip().lower().replace(" & ", "-").replace(" ", "-")
