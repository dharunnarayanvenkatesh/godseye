#!/usr/bin/env python
"""Search or seed God's Eye's curated source catalog."""
from __future__ import annotations

import argparse
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from agent.source_catalog import CATALOG, SourceCatalogEntry, categories, search_catalog


def _slug(display: str) -> str:
    return display.strip().lower().replace(" & ", "-").replace(" ", "-")


def _render_entry(entry: SourceCatalogEntry) -> str:
    refs = "\n".join(f"- **{ref}**: join on names, identifiers, domains, addresses, dates, or source-specific IDs where available." for ref in entry.cross_refs)
    if not refs:
        refs = "- No preferred cross-references documented yet."

    caution = f"\n- **Access caution**: {entry.caution}" if entry.caution else ""

    return f"""# {entry.name}

## Summary

{entry.notes}

## Access Methods

- **Primary access**: {entry.access}
- **Homepage/docs**: {entry.homepage}{caution}

## Data Schema

Schema varies by endpoint, export, or vendor package. Capture source-specific
identifiers, entity names, aliases, addresses, dates, relationship fields,
provenance, and source URLs before transforming records.

## Coverage

- **Jurisdiction**: {entry.jurisdiction}
- **Time range**: Varies by source and endpoint
- **Update frequency**: Varies by source
- **Volume**: Varies by source

## Cross-Reference Potential

{refs}

## Data Quality

Expect name variants, missing identifiers, inconsistent dates, duplicate
entities, jurisdiction-specific terms, and access-tier differences. Preserve raw
records and record match confidence separately from confirmed facts.

## Acquisition Script

No dedicated fetch script yet. Use `scripts/search_source_catalog.py` to discover
the source, then create a source-specific fetcher that caches raw responses,
records provenance, respects rate limits, and keeps paid or restricted data out
of committed fixtures.

## Legal & Licensing

Review the source's terms, license, privacy rules, and jurisdiction-specific
legal restrictions before collection or redistribution. Commercial and paid
sources require valid licensed access.

## References

- {entry.homepage}
"""


def _existing_index_entries(index_text: str) -> set[str]:
    names: set[str] = set()
    for line in index_text.splitlines():
        if not line.startswith("|"):
            continue
        parts = [part.strip() for part in line.strip().strip("|").split("|")]
        if len(parts) >= 3 and parts[0] not in {"Source", "--------"}:
            names.add(parts[0])
    return names


def seed_wiki(wiki_dir: Path) -> int:
    wiki_dir.mkdir(parents=True, exist_ok=True)
    index_path = wiki_dir / "index.md"
    index_text = index_path.read_text(encoding="utf-8") if index_path.exists() else "# Data Sources Wiki\n"
    existing_names = _existing_index_entries(index_text)

    created = 0
    for entry in CATALOG:
        target = wiki_dir / entry.path
        if not target.exists():
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(_render_entry(entry), encoding="utf-8")
            created += 1

    new_entries = [entry for entry in CATALOG if entry.name not in existing_names]
    if new_entries:
        if "## Expanded OSINT Source Catalog" not in index_text:
            index_text = index_text.rstrip() + "\n\n## Expanded OSINT Source Catalog\n"
        additions: list[str] = []
        by_category: dict[str, list[SourceCatalogEntry]] = {}
        for entry in new_entries:
            by_category.setdefault(entry.category, []).append(entry)
        for category in sorted(by_category):
            additions.append(f"\n### {category}\n")
            additions.append("| Source | Jurisdiction | Link |\n")
            additions.append("|--------|-------------|------|\n")
            for entry in sorted(by_category[category], key=lambda item: item.name.casefold()):
                filename = Path(entry.path).name
                additions.append(f"| {entry.name} | {entry.jurisdiction} | [{filename}]({entry.path}) |\n")
        index_path.write_text(index_text.rstrip() + "\n" + "".join(additions), encoding="utf-8")

    return created


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("query", nargs="?", default="", help="Search text. Empty query lists all catalog entries.")
    parser.add_argument("--category", help="Restrict search to a category substring.")
    parser.add_argument("--categories", action="store_true", help="List catalog categories.")
    parser.add_argument("--write-wiki", action="store_true", help="Create missing wiki pages and index rows from the catalog.")
    parser.add_argument("--wiki-dir", default=str(ROOT / "wiki"), help="Wiki directory to update when --write-wiki is used.")
    args = parser.parse_args()

    if args.categories:
        for category in categories():
            print(category)
        return 0

    if args.write_wiki:
        created = seed_wiki(Path(args.wiki_dir))
        print(f"Seeded {created} missing wiki page(s) in {args.wiki_dir}")
        return 0

    matches = search_catalog(args.query, category=args.category)
    for entry in matches:
        print(f"{entry.name}\t{entry.category}\t{entry.jurisdiction}\t{entry.access}\t{entry.homepage}")
    return 0 if matches else 1


if __name__ == "__main__":
    raise SystemExit(main())
