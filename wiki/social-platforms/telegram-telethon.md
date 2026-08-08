# Telegram public channels through Telethon

## Summary

Collection from public Telegram channels and groups visible to an authorized account.

## Access Methods

- **Primary access**: Telegram API credentials and Telethon client
- **Homepage/docs**: https://docs.telethon.dev/
- **Access caution**: Collect only public or authorized communities and comply with platform rules.

## Data Schema

Schema varies by endpoint, export, or vendor package. Capture source-specific
identifiers, entity names, aliases, addresses, dates, relationship fields,
provenance, and source URLs before transforming records.

## Coverage

- **Jurisdiction**: Telegram
- **Time range**: Varies by source and endpoint
- **Update frequency**: Varies by source
- **Volume**: Varies by source

## Cross-Reference Potential

- **RSS and Atom feeds**: join on names, identifiers, domains, addresses, dates, or source-specific IDs where available.
- **GDELT**: join on names, identifiers, domains, addresses, dates, or source-specific IDs where available.
- **SerpAPI**: join on names, identifiers, domains, addresses, dates, or source-specific IDs where available.

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

- https://docs.telethon.dev/
