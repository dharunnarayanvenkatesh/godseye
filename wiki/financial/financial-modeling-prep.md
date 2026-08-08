# Financial Modeling Prep

## Summary

Company fundamentals, statements, ownership, market data, and calendars.

## Access Methods

- **Primary access**: API key; free and paid tiers
- **Homepage/docs**: https://site.financialmodelingprep.com/developer/docs

## Data Schema

Schema varies by endpoint, export, or vendor package. Capture source-specific
identifiers, entity names, aliases, addresses, dates, relationship fields,
provenance, and source URLs before transforming records.

## Coverage

- **Jurisdiction**: Global public markets
- **Time range**: Varies by source and endpoint
- **Update frequency**: Varies by source
- **Volume**: Varies by source

## Cross-Reference Potential

- **Alpha Vantage**: join on names, identifiers, domains, addresses, dates, or source-specific IDs where available.
- **SEC EDGAR**: join on names, identifiers, domains, addresses, dates, or source-specific IDs where available.
- **OpenFIGI**: join on names, identifiers, domains, addresses, dates, or source-specific IDs where available.

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

- https://site.financialmodelingprep.com/developer/docs
