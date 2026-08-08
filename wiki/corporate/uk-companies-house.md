# UK Companies House

## Summary

UK company profiles, officers, PSC beneficial ownership records, filings, and charges.

## Access Methods

- **Primary access**: public API; API key required
- **Homepage/docs**: https://developer.company-information.service.gov.uk/

## Data Schema

Schema varies by endpoint, export, or vendor package. Capture source-specific
identifiers, entity names, aliases, addresses, dates, relationship fields,
provenance, and source URLs before transforming records.

## Coverage

- **Jurisdiction**: United Kingdom
- **Time range**: Varies by source and endpoint
- **Update frequency**: Varies by source
- **Volume**: Varies by source

## Cross-Reference Potential

- **OpenCorporates**: join on names, identifiers, domains, addresses, dates, or source-specific IDs where available.
- **OpenOwnership Register**: join on names, identifiers, domains, addresses, dates, or source-specific IDs where available.
- **Companies House bulk data**: join on names, identifiers, domains, addresses, dates, or source-specific IDs where available.

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

- https://developer.company-information.service.gov.uk/
