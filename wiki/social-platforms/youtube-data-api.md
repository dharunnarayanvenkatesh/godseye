# YouTube Data API

## Summary

Videos, channels, playlists, comments, captions metadata, and search.

## Access Methods

- **Primary access**: API key/OAuth
- **Homepage/docs**: https://developers.google.com/youtube/v3

## Data Schema

Schema varies by endpoint, export, or vendor package. Capture source-specific
identifiers, entity names, aliases, addresses, dates, relationship fields,
provenance, and source URLs before transforming records.

## Coverage

- **Jurisdiction**: YouTube
- **Time range**: Varies by source and endpoint
- **Update frequency**: Varies by source
- **Volume**: Varies by source

## Cross-Reference Potential

- **Google Programmable Search**: join on names, identifiers, domains, addresses, dates, or source-specific IDs where available.
- **GDELT**: join on names, identifiers, domains, addresses, dates, or source-specific IDs where available.
- **RSS and Atom feeds**: join on names, identifiers, domains, addresses, dates, or source-specific IDs where available.

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

- https://developers.google.com/youtube/v3
