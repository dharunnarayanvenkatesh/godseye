"""Curated investigative data-source catalog.

The wiki is the human-readable knowledge base. This module keeps a compact,
searchable registry that scripts and agents can use to discover source leads and
seed missing wiki pages without relying on memory.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class SourceCatalogEntry:
    name: str
    category: str
    jurisdiction: str
    path: str
    access: str
    homepage: str
    notes: str
    cross_refs: tuple[str, ...] = ()
    caution: str = ""

    def as_dict(self) -> dict[str, Any]:
        """Return a stable JSON-ready representation for tools and UIs."""
        return {
            "name": self.name,
            "category": self.category,
            "jurisdiction": self.jurisdiction,
            "access": self.access,
            "homepage": self.homepage,
            "notes": self.notes,
            "cross_refs": list(self.cross_refs),
            "caution": self.caution,
            "wiki_path": f"wiki/{self.path}",
        }


CATALOG: tuple[SourceCatalogEntry, ...] = (
    SourceCatalogEntry("ICIJ Offshore Leaks Database", "International", "Global", "international/icij-offshore-leaks.md", "public web search and bulk CSV/Neo4j downloads", "https://offshoreleaks.icij.org/", "Offshore entities, officers, intermediaries, addresses, and relationship graph data.", ("OpenSanctions", "OCCRP Aleph", "OpenCorporates")),
    SourceCatalogEntry("OCCRP Aleph", "Investigative Archives", "Global", "investigative/occrp-aleph.md", "public web/API; some datasets require account access", "https://aleph.occrp.org/", "Entity, document, and network search across leaked and public-interest datasets.", ("OpenSanctions", "ICIJ Offshore Leaks Database", "FollowTheMoney")),
    SourceCatalogEntry("OpenCorporates", "Corporate Registries", "Global", "corporate/opencorporates.md", "public web/API; higher-volume API is paid", "https://opencorporates.com/", "Company profiles and officer data aggregated from many national registries.", ("OpenOwnership Register", "GLEIF LEI data", "SEC EDGAR")),
    SourceCatalogEntry("OpenSanctions", "Sanctions", "Global", "sanctions/opensanctions.md", "public bulk data/API; commercial tiers available", "https://www.opensanctions.org/", "Sanctions, politically exposed persons, watchlists, and entity identifiers.", ("OCCRP Aleph", "ICIJ Offshore Leaks Database", "OpenCorporates")),
    SourceCatalogEntry("GLEIF LEI data", "Corporate Registries", "Global", "corporate/gleif-lei.md", "public API and bulk downloads", "https://www.gleif.org/en/lei-data/gleif-api", "Legal Entity Identifier reference data for registered entities and relationships.", ("OpenCorporates", "SEC EDGAR", "OpenFIGI")),
    SourceCatalogEntry("UK Companies House", "Corporate Registries", "United Kingdom", "corporate/uk-companies-house.md", "public API; API key required", "https://developer.company-information.service.gov.uk/", "UK company profiles, officers, PSC beneficial ownership records, filings, and charges.", ("OpenCorporates", "OpenOwnership Register", "Companies House bulk data")),
    SourceCatalogEntry("EU business registries", "Corporate Registries", "European Union", "corporate/eu-business-registries.md", "mixed national portals; BRIS web search", "https://e-justice.europa.eu/489/EN/business_registers__search_for_a_company_in_the_eu", "EU business-register discovery layer and member-state company registries.", ("OpenCorporates", "GLEIF LEI data", "EU TED")),
    SourceCatalogEntry("National company registries", "Corporate Registries", "National", "corporate/national-company-registries.md", "varies by jurisdiction", "https://org-id.guide/", "Country-level company registries, often with official numbers, directors, filings, and status.", ("OpenCorporates", "OpenOwnership Register", "GLEIF LEI data")),
    SourceCatalogEntry("OpenOwnership Register", "Corporate Registries", "Global", "corporate/openownership-register.md", "public search and bulk data where available", "https://register.openownership.org/", "Beneficial ownership data normalized with the Beneficial Ownership Data Standard.", ("OpenCorporates", "OpenSanctions", "UK Companies House")),
    SourceCatalogEntry("Companies House bulk data", "Corporate Registries", "United Kingdom", "corporate/companies-house-bulk-data.md", "public bulk downloads", "https://download.companieshouse.gov.uk/en_output.html", "Bulk UK company snapshot data for large-scale matching.", ("UK Companies House", "OpenCorporates", "OpenOwnership Register")),
    SourceCatalogEntry("SEC EDGAR", "Corporate Registries", "US public companies", "corporate/sec-edgar.md", "public APIs and bulk downloads; User-Agent required", "https://www.sec.gov/search-filings/edgar-application-programming-interfaces", "US public-company filings, beneficial ownership disclosures, insider transactions, XBRL facts, and issuer metadata.", ("OpenCorporates", "GLEIF LEI data", "OpenFIGI")),
    SourceCatalogEntry("Open Contracting Data Standard", "Procurement", "Global", "procurement/ocds.md", "open schema and publisher-specific feeds", "https://standard.open-contracting.org/latest/en/", "Common data model for planning, tender, award, contract, and implementation stages.", ("OpenTender", "EU TED", "World Bank procurement data")),
    SourceCatalogEntry("OpenTender", "Procurement", "Europe", "procurement/opentender.md", "public web search; bulk/API availability varies", "https://opentender.eu/", "European procurement data aggregated for market and integrity analysis.", ("Open Contracting Data Standard", "EU TED", "OpenCorporates")),
    SourceCatalogEntry("EU TED", "Procurement", "European Union", "procurement/eu-ted.md", "public search, API, and bulk notices", "https://ted.europa.eu/", "Tenders Electronic Daily, the EU supplement to the Official Journal for public procurement.", ("OpenTender", "Open Contracting Data Standard", "EU business registries")),
    SourceCatalogEntry("World Bank procurement data", "Procurement", "Global", "procurement/world-bank-procurement.md", "public APIs and downloads", "https://financesapp.worldbank.org/procurement/", "World Bank projects, procurement notices, contract awards, and supplier records.", ("Open Contracting Data Standard", "OpenCorporates", "OpenSanctions")),
    SourceCatalogEntry("UN procurement data", "Procurement", "Global", "procurement/un-procurement.md", "public vendor/award portals; details vary by agency", "https://www.ungm.org/Public/ContractAward", "UN Global Marketplace award notices and procurement opportunities.", ("Open Contracting Data Standard", "OpenSanctions", "OpenCorporates")),
    SourceCatalogEntry("USASpending.gov", "Government Contracts", "US federal", "contracts/usaspending.md", "public API and bulk downloads", "https://api.usaspending.gov/docs/endpoints", "US federal contracts, grants, loans, and other award records.", ("SEC EDGAR", "SAM.gov", "FEC Federal Campaign Finance")),
    SourceCatalogEntry("LittleSis", "Influence Networks", "US and global", "influence/littlesis.md", "public web/API", "https://littlesis.org/", "Relationship database for people, organizations, boards, donors, lobbying, and influence networks.", ("SEC EDGAR", "FEC Federal Campaign Finance", "OpenSanctions")),
    SourceCatalogEntry("FollowTheMoney", "Campaign Finance", "United States", "campaign-finance/followthemoney.md", "public web/API; account may be required for API", "https://www.followthemoney.org/", "State-level campaign finance, lobbying, and political spending data.", ("FEC Federal Campaign Finance", "LittleSis", "National election and political-finance databases")),
    SourceCatalogEntry("Wikidata", "Reference Data", "Global", "reference/wikidata.md", "public SPARQL/API and dumps", "https://www.wikidata.org/wiki/Wikidata:Data_access", "Open knowledge graph for identifiers, aliases, organizational relationships, and biographical context.", ("OpenCorporates", "OpenSanctions", "LittleSis")),
    SourceCatalogEntry("CourtListener", "Legal & Court Records", "United States", "legal/courtlistener.md", "public web/API", "https://www.courtlistener.com/api/", "Court opinions, dockets, judges, parties, and legal citations from Free Law Project.", ("RECAP", "PACER", "SEC EDGAR")),
    SourceCatalogEntry("RECAP", "Legal & Court Records", "United States", "legal/recap.md", "public archive/API", "https://www.courtlistener.com/recap/", "Free Law Project archive of PACER documents contributed by users.", ("CourtListener", "PACER", "OpenCorporates")),
    SourceCatalogEntry("PACER", "Legal & Court Records", "United States", "legal/pacer.md", "paid official access", "https://pacer.uscourts.gov/", "Official US federal court docket and filing access.", ("CourtListener", "RECAP", "OpenCorporates"), "Paid service; observe court rules, account terms, and privacy limits."),
    SourceCatalogEntry("ImportYeti", "Trade & Supply Chain", "United States importers", "trade/importyeti.md", "public web search", "https://www.importyeti.com/", "US maritime import records organized by company and supplier.", ("Panjiva", "OpenCorporates", "SEC EDGAR")),
    SourceCatalogEntry("Panjiva", "Trade & Supply Chain", "Global", "trade/panjiva.md", "commercial", "https://panjiva.com/", "Commercial trade and supply-chain intelligence.", ("ImportYeti", "Sayari", "OpenCorporates"), "Use only with a valid subscription and license-compliant exports."),
    SourceCatalogEntry("Sayari", "Corporate Registries", "Global", "corporate/sayari.md", "commercial", "https://sayari.com/", "Commercial entity-resolution, ownership, sanctions, and trade-risk platform.", ("OpenSanctions", "OpenCorporates", "Panjiva"), "Use only with authorized credentials and vendor-approved workflows."),
    SourceCatalogEntry("Orbis", "Corporate Registries", "Global", "corporate/orbis.md", "commercial", "https://www.moodys.com/web/en/us/capabilities/company-reference-data/orbis.html", "Commercial company reference, ownership, financial, and corporate-family data.", ("OpenCorporates", "GLEIF LEI data", "PitchBook"), "Use only with licensed access."),
    SourceCatalogEntry("PitchBook", "Market & Financial Data", "Global private markets", "financial/pitchbook.md", "commercial", "https://pitchbook.com/", "Private-market companies, investors, funds, deals, valuations, and executives.", ("Crunchbase", "Orbis", "SEC EDGAR"), "Use only with licensed access."),
    SourceCatalogEntry("Crunchbase", "Market & Financial Data", "Global startups and investors", "financial/crunchbase.md", "API/commercial terms", "https://data.crunchbase.com/docs", "Company, funding-round, investor, acquisition, and people data.", ("PitchBook", "OpenCorporates", "SEC EDGAR")),
    SourceCatalogEntry("OpenFIGI", "Market & Financial Data", "Global securities", "financial/openfigi.md", "public API; API key recommended", "https://www.openfigi.com/api", "Maps securities identifiers such as FIGI, ticker, ISIN, CUSIP, and exchange codes.", ("SEC EDGAR", "GLEIF LEI data", "Alpha Vantage")),
    SourceCatalogEntry("Alpha Vantage", "Market & Financial Data", "Global public markets", "financial/alpha-vantage.md", "API key; free and paid tiers", "https://www.alphavantage.co/documentation/", "Market prices, fundamentals, FX, crypto, and economic indicators.", ("OpenFIGI", "SEC EDGAR", "Financial Modeling Prep")),
    SourceCatalogEntry("Financial Modeling Prep", "Market & Financial Data", "Global public markets", "financial/financial-modeling-prep.md", "API key; free and paid tiers", "https://site.financialmodelingprep.com/developer/docs", "Company fundamentals, statements, ownership, market data, and calendars.", ("Alpha Vantage", "SEC EDGAR", "OpenFIGI")),
    SourceCatalogEntry("National election and political-finance databases", "Campaign Finance", "National/state/local", "campaign-finance/national-election-political-finance.md", "varies by jurisdiction", "https://www.idea.int/data-tools/data/political-finance-database", "Official election, donation, party finance, and campaign disclosure databases.", ("FollowTheMoney", "FEC Federal Campaign Finance", "LittleSis")),
    SourceCatalogEntry("RDAP", "Domain & DNS Intel", "Global", "domain/rdap.md", "public protocol and registry endpoints", "https://rdap.org/", "Structured successor to WHOIS for domain, IP, ASN, registrar, and contact metadata.", ("WHOIS", "ICANN Lookup", "SecurityTrails")),
    SourceCatalogEntry("WHOIS", "Domain & DNS Intel", "Global", "domain/whois.md", "public protocol; often rate-limited/redacted", "https://lookup.icann.org/", "Legacy registration records for domains, IP allocations, and contacts.", ("RDAP", "ICANN Lookup", "DomainTools")),
    SourceCatalogEntry("ICANN Lookup", "Domain & DNS Intel", "Global", "domain/icann-lookup.md", "public web lookup", "https://lookup.icann.org/", "ICANN-hosted lookup for registration and RDAP/WHOIS data.", ("RDAP", "WHOIS", "DomainTools")),
    SourceCatalogEntry("crt.sh", "Domain & DNS Intel", "Global", "domain/crtsh.md", "public web and query endpoints", "https://crt.sh/", "Certificate Transparency search by domain, certificate, issuer, and identity fields.", ("Certificate Transparency logs", "Subfinder", "Amass")),
    SourceCatalogEntry("Certificate Transparency logs", "Domain & DNS Intel", "Global", "domain/certificate-transparency-logs.md", "public logs and monitors", "https://certificate.transparency.dev/", "Append-only certificate issuance logs useful for subdomain and infrastructure discovery.", ("crt.sh", "SecurityTrails", "URLScan")),
    SourceCatalogEntry("DNSDumpster", "Domain & DNS Intel", "Global", "domain/dnsdumpster.md", "public web search", "https://dnsdumpster.com/", "DNS reconnaissance and attack-surface mapping.", ("SecurityTrails", "Amass", "Subfinder")),
    SourceCatalogEntry("DNSViz", "Domain & DNS Intel", "Global", "domain/dnsviz.md", "public web/API", "https://dnsviz.net/", "DNS and DNSSEC visualization and diagnostics.", ("MXToolbox", "RDAP", "SecurityTrails")),
    SourceCatalogEntry("MXToolbox", "Domain & DNS Intel", "Global", "domain/mxtoolbox.md", "public web/API tiers", "https://mxtoolbox.com/", "Mail, DNS, blacklist, SPF, DKIM, DMARC, and deliverability diagnostics.", ("DNSViz", "Spamhaus", "WHOIS")),
    SourceCatalogEntry("ViewDNS", "Domain & DNS Intel", "Global", "domain/viewdns.md", "public web; API available", "https://viewdns.info/", "Reverse IP, historical DNS, WHOIS, and related domain lookup tools.", ("SecurityTrails", "DomainTools", "DNSDumpster")),
    SourceCatalogEntry("SecurityTrails", "Domain & DNS Intel", "Global", "domain/securitytrails.md", "API key; free and paid tiers", "https://securitytrails.com/corp/apidocs", "Current and historical DNS, WHOIS, subdomains, and infrastructure intelligence.", ("RDAP", "crt.sh", "URLScan")),
    SourceCatalogEntry("DomainTools", "Domain & DNS Intel", "Global", "domain/domaintools.md", "commercial API", "https://www.domaintools.com/integrations/api/", "Domain ownership, historical WHOIS, passive DNS, and risk scoring.", ("WHOIS", "SecurityTrails", "RiskIQ PassiveTotal"), "Use only with licensed access."),
    SourceCatalogEntry("RiskIQ PassiveTotal", "Threat Intelligence", "Global", "threat-intel/riskiq-passivetotal.md", "commercial/API", "https://learn.microsoft.com/en-us/defender/threat-intelligence/", "Passive DNS, WHOIS, SSL, tracker, and host intelligence from Microsoft Defender TI.", ("DomainTools", "SecurityTrails", "VirusTotal"), "Use only with authorized credentials."),
    SourceCatalogEntry("CIRCL Passive DNS", "Threat Intelligence", "Global", "threat-intel/circl-passive-dns.md", "community access/API", "https://www.circl.lu/services/passive-dns/", "Passive DNS database operated by CIRCL.", ("Farsight DNSDB", "SecurityTrails", "URLScan")),
    SourceCatalogEntry("Farsight DNSDB", "Threat Intelligence", "Global", "threat-intel/farsight-dnsdb.md", "commercial/API", "https://www.domaintools.com/products/farsight-dnsdb/", "Large passive DNS history database.", ("CIRCL Passive DNS", "DomainTools", "SecurityTrails"), "Use only with licensed access."),
    SourceCatalogEntry("URLScan", "Threat Intelligence", "Global", "threat-intel/urlscan.md", "public search/API; API key for submissions", "https://urlscan.io/docs/api/", "URL scanning, page metadata, screenshots, requests, certificates, and related indicators.", ("crt.sh", "VirusTotal", "OpenPhish")),
    SourceCatalogEntry("VirusTotal", "Threat Intelligence", "Global", "threat-intel/virustotal.md", "API key; free and commercial tiers", "https://docs.virustotal.com/reference/overview", "Reputation, detections, relationships, and enrichment for URLs, domains, IPs, and files.", ("URLScan", "AlienVault OTX", "GreyNoise"), "Follow API terms and do not submit sensitive files without authorization."),
    SourceCatalogEntry("GreyNoise", "Threat Intelligence", "Internet-wide sensors", "threat-intel/greynoise.md", "API key; community and paid tiers", "https://docs.greynoise.io/", "Internet scanner classification and IP context.", ("VirusTotal", "AbuseIPDB", "AlienVault OTX")),
    SourceCatalogEntry("AlienVault OTX", "Threat Intelligence", "Global", "threat-intel/alienvault-otx.md", "public/API key", "https://otx.alienvault.com/api", "Community threat-intelligence pulses and indicator relationships.", ("VirusTotal", "URLScan", "AbuseIPDB")),
    SourceCatalogEntry("AbuseIPDB", "Threat Intelligence", "Global", "threat-intel/abuseipdb.md", "API key; free and paid tiers", "https://docs.abuseipdb.com/", "IP abuse reports, confidence scores, and categories.", ("GreyNoise", "Spamhaus", "VirusTotal")),
    SourceCatalogEntry("Spamhaus", "Threat Intelligence", "Global", "threat-intel/spamhaus.md", "public lookups; data/API terms vary", "https://www.spamhaus.org/", "Spam, botnet, malware, and abuse blocklists and lookups.", ("MXToolbox", "AbuseIPDB", "PhishTank")),
    SourceCatalogEntry("PhishTank", "Threat Intelligence", "Global", "threat-intel/phishtank.md", "public data/API", "https://phishtank.org/developer_info.php", "Community phishing URL database.", ("OpenPhish", "URLScan", "VirusTotal")),
    SourceCatalogEntry("OpenPhish", "Threat Intelligence", "Global", "threat-intel/openphish.md", "public feeds; commercial tiers", "https://openphish.com/", "Phishing URL intelligence feeds.", ("PhishTank", "URLScan", "VirusTotal")),
    SourceCatalogEntry("Have I Been Pwned", "Identity Intel", "Breach-notification corpus", "identity/hibp.md", "API key for breached account checks; k-anonymity password API", "https://haveibeenpwned.com/API/v3", "Breach corpus for account exposure checks and domain monitoring.", ("EmailRep", "Holehe", "Epieos"), "Use only for accounts/domains you are authorized to check."),
    SourceCatalogEntry("EmailRep", "Identity Intel", "Global", "identity/emailrep.md", "API key; free and paid tiers", "https://emailrep.io/", "Email reputation and enrichment signals.", ("Have I Been Pwned", "Hunter", "Epieos"), "Use for legitimate enrichment and abuse-prevention workflows."),
    SourceCatalogEntry("Hunter", "Identity Intel", "Global", "identity/hunter.md", "API key; free and paid tiers", "https://hunter.io/api-documentation", "Email discovery and verification for domains and organizations.", ("EmailRep", "theHarvester", "Epieos")),
    SourceCatalogEntry("Epieos", "Identity Intel", "Global", "identity/epieos.md", "web/commercial", "https://epieos.com/", "Email and phone OSINT enrichment from public signals.", ("EmailRep", "Have I Been Pwned", "GHunt"), "Use only for lawful, authorized investigations."),
    SourceCatalogEntry("theHarvester", "Domain & DNS Intel", "Global", "domain/theharvester.md", "open-source tool; data-source API keys optional", "https://github.com/laramies/theHarvester", "Email, host, subdomain, and people discovery from public sources.", ("Hunter", "Subfinder", "Amass")),
    SourceCatalogEntry("Amass", "Domain & DNS Intel", "Global", "domain/amass.md", "open-source tool; data-source API keys optional", "https://github.com/owasp-amass/amass", "Attack-surface mapping and subdomain enumeration.", ("Subfinder", "Assetfinder", "crt.sh")),
    SourceCatalogEntry("Subfinder", "Domain & DNS Intel", "Global", "domain/subfinder.md", "open-source tool; data-source API keys optional", "https://github.com/projectdiscovery/subfinder", "Fast passive subdomain discovery.", ("Amass", "Assetfinder", "dnsx")),
    SourceCatalogEntry("Assetfinder", "Domain & DNS Intel", "Global", "domain/assetfinder.md", "open-source tool", "https://github.com/tomnomnom/assetfinder", "Find domains and subdomains related to a target.", ("Subfinder", "Amass", "httpx")),
    SourceCatalogEntry("dnsx", "Domain & DNS Intel", "Global", "domain/dnsx.md", "open-source tool", "https://github.com/projectdiscovery/dnsx", "Fast DNS toolkit for resolving and probing DNS records.", ("Subfinder", "httpx", "DNSViz")),
    SourceCatalogEntry("httpx", "Domain & DNS Intel", "Global", "domain/httpx.md", "open-source tool", "https://github.com/projectdiscovery/httpx", "HTTP probing, service fingerprinting, status, title, and TLS metadata collection.", ("dnsx", "WhatWeb", "Wappalyzer")),
    SourceCatalogEntry("DNSTwist", "Domain & DNS Intel", "Global", "domain/dnstwist.md", "open-source tool", "https://github.com/elceef/dnstwist", "Domain permutation and typosquatting detection.", ("URLCrazy", "PhishTank", "OpenPhish")),
    SourceCatalogEntry("URLCrazy", "Domain & DNS Intel", "Global", "domain/urlcrazy.md", "open-source tool", "https://github.com/urbanadventurer/urlcrazy", "Domain typo, homoglyph, and brand impersonation discovery.", ("DNSTwist", "PhishTank", "OpenPhish")),
    SourceCatalogEntry("WhatWeb", "Web Technology Intel", "Global", "web-tech/whatweb.md", "open-source tool", "https://github.com/urbanadventurer/WhatWeb", "Website technology fingerprinting.", ("Wappalyzer", "BuiltWith", "httpx")),
    SourceCatalogEntry("Wappalyzer", "Web Technology Intel", "Global", "web-tech/wappalyzer.md", "browser extension/API/commercial", "https://www.wappalyzer.com/", "Website technology detection and enrichment.", ("WhatWeb", "BuiltWith", "httpx")),
    SourceCatalogEntry("BuiltWith", "Web Technology Intel", "Global", "web-tech/builtwith.md", "commercial/API", "https://builtwith.com/api", "Technology profiles, tracking pixels, hosting, and web stack intelligence.", ("Wappalyzer", "WhatWeb", "SecurityTrails"), "Use only with licensed access."),
    SourceCatalogEntry("Sherlock", "Social & Identity Intel", "Global", "social/sherlock.md", "open-source tool", "https://github.com/sherlock-project/sherlock", "Username search across social sites.", ("Maigret", "WhatsMyName", "Namechk"), "Respect platform terms and avoid harassment or doxxing."),
    SourceCatalogEntry("Maigret", "Social & Identity Intel", "Global", "social/maigret.md", "open-source tool", "https://github.com/soxoj/maigret", "Username search and profile collection across many sites.", ("Sherlock", "WhatsMyName", "Social Analyzer"), "Respect platform terms and avoid harassment or doxxing."),
    SourceCatalogEntry("WhatsMyName", "Social & Identity Intel", "Global", "social/whatsmyname.md", "open-source list/tool", "https://github.com/WebBreacher/WhatsMyName", "Username-checking site list and tools.", ("WhatsMyName Web", "Sherlock", "Maigret")),
    SourceCatalogEntry("Blackbird", "Social & Identity Intel", "Global", "social/blackbird.md", "open-source tool", "https://github.com/p1ngul1n0/blackbird", "Username enumeration and profile discovery.", ("Sherlock", "Maigret", "WhatsMyName")),
    SourceCatalogEntry("Social Analyzer", "Social & Identity Intel", "Global", "social/social-analyzer.md", "open-source tool", "https://github.com/qeeqbox/social-analyzer", "Profile and username analysis across social platforms.", ("Sherlock", "Maigret", "Namechk")),
    SourceCatalogEntry("Snoop", "Social & Identity Intel", "Global", "social/snoop.md", "open-source tool", "https://github.com/snooppr/snoop", "Username search across many sites.", ("Sherlock", "Maigret", "WhatsMyName")),
    SourceCatalogEntry("Namechk", "Social & Identity Intel", "Global", "social/namechk.md", "public web/commercial", "https://namechk.com/", "Username and domain availability checks.", ("KnowEm", "Sherlock", "WhatsMyName")),
    SourceCatalogEntry("KnowEm", "Social & Identity Intel", "Global", "social/knowem.md", "public web/commercial", "https://knowem.com/", "Username and brand availability search across social networks.", ("Namechk", "Sherlock", "WhatsMyName")),
    SourceCatalogEntry("WhatsMyName Web", "Social & Identity Intel", "Global", "social/whatsmyname-web.md", "public web", "https://whatsmyname.app/", "Web interface for WhatsMyName username checks.", ("WhatsMyName", "Sherlock", "Maigret")),
    SourceCatalogEntry("GHunt", "Social & Identity Intel", "Google accounts", "identity/ghunt.md", "open-source tool", "https://github.com/mxrch/GHunt", "Google account OSINT from visible public signals.", ("Epieos", "Holehe", "EmailRep"), "Use only for authorized investigations and respect account privacy."),
    SourceCatalogEntry("Holehe", "Identity Intel", "Global", "identity/holehe.md", "open-source tool", "https://github.com/megadose/holehe", "Checks whether an email is associated with public account-signup flows.", ("Have I Been Pwned", "EmailRep", "Epieos"), "Use only for authorized investigations; avoid intrusive enumeration."),
    SourceCatalogEntry("Email2phonenumber-style utilities", "Identity Intel", "Global", "identity/email2phonenumber-style-utilities.md", "varies; often fragile/unofficial", "https://github.com/martinvigo/email2phonenumber", "Class of utilities that infer phone-number hints from account recovery or public signals.", ("Holehe", "Epieos", "GHunt"), "High privacy risk; use only with explicit authorization and do not automate against services without permission."),
    SourceCatalogEntry("Gravatar lookup", "Identity Intel", "Global", "identity/gravatar-lookup.md", "public hash/profile lookup", "https://docs.gravatar.com/rest/api/", "Public Gravatar profile discovery by email hash.", ("EmailRep", "Keybase", "GitHub and GitLab APIs")),
    SourceCatalogEntry("Keybase", "Identity Intel", "Global", "identity/keybase.md", "public web/API", "https://keybase.io/docs/api/1.0", "Identity proofs linking usernames, keys, domains, and social accounts.", ("PGP key servers", "GitHub and GitLab APIs", "Gravatar lookup")),
    SourceCatalogEntry("PGP key servers", "Identity Intel", "Global", "identity/pgp-key-servers.md", "public keyserver queries", "https://keys.openpgp.org/about/api", "Public OpenPGP key discovery, identities, and signatures.", ("Keybase", "GitHub and GitLab APIs", "Gravatar lookup")),
    SourceCatalogEntry("GitHub and GitLab APIs", "Developer Footprints", "Global", "developer/github-gitlab-apis.md", "public APIs; tokens recommended", "https://docs.github.com/en/rest", "Profiles, repositories, organizations, commits, issues, and public code metadata.", ("GitFive", "GitGraber", "GitLeaks"), "Respect API terms and repository ownership boundaries."),
    SourceCatalogEntry("GitFive", "Developer Footprints", "GitHub", "developer/gitfive.md", "open-source tool", "https://github.com/mxrch/GitFive", "GitHub profile OSINT from public metadata.", ("GitHub and GitLab APIs", "Keybase", "PGP key servers")),
    SourceCatalogEntry("GitGraber", "Developer Footprints", "GitHub", "developer/gitgraber.md", "open-source tool", "https://github.com/hisxo/gitGraber", "Searches GitHub code for potential secrets and sensitive patterns.", ("GitHub and GitLab APIs", "GitLeaks"), "Use only on repositories you own or are authorized to inspect."),
    SourceCatalogEntry("GitLeaks", "Developer Footprints", "Repositories", "developer/gitleaks.md", "open-source tool", "https://github.com/gitleaks/gitleaks", "Secret scanning for Git repositories and filesystems.", ("GitHub and GitLab APIs", "GitGraber"), "Use only on repositories you own or are authorized to inspect."),
    SourceCatalogEntry("Steam public-profile tools", "Social & Identity Intel", "Steam", "social/steam-public-profile-tools.md", "public profile/API where available", "https://steamcommunity.com/dev", "Public Steam profile, vanity URL, friend, and game metadata where visible.", ("Sherlock", "Maigret", "WhatsMyName")),
    SourceCatalogEntry("Mastodon account search", "Social & Identity Intel", "Fediverse", "social/mastodon-account-search.md", "public instance APIs", "https://docs.joinmastodon.org/methods/search/", "Account and post search across individual Mastodon instances.", ("Mastodon APIs", "Bluesky directory tools", "Sherlock")),
    SourceCatalogEntry("Bluesky directory tools", "Social & Identity Intel", "Bluesky/AT Protocol", "social/bluesky-directory-tools.md", "public APIs/firehose", "https://docs.bsky.app/", "Account, DID, handle, and social graph discovery on AT Protocol.", ("Bluesky firehose", "Mastodon account search", "Sherlock")),
    SourceCatalogEntry("GDELT", "News & Web Archives", "Global", "media/gdelt.md", "public APIs and BigQuery dataset", "https://www.gdeltproject.org/", "Global news/event monitoring, full-text metadata, events, and translations.", ("Media Cloud", "Event Registry", "Common Crawl")),
    SourceCatalogEntry("Media Cloud", "News & Web Archives", "Global", "media/media-cloud.md", "API access", "https://mediacloud.org/", "News-source and media ecosystem analysis.", ("GDELT", "Event Registry", "RSS and Atom feeds")),
    SourceCatalogEntry("Common Crawl", "News & Web Archives", "Web", "media/common-crawl.md", "public S3/HTTP indexes", "https://commoncrawl.org/", "Massive public web crawl corpus and URL indexes.", ("Internet Archive", "Memento", "GDELT")),
    SourceCatalogEntry("Internet Archive", "News & Web Archives", "Web", "media/internet-archive.md", "public APIs", "https://archive.org/developers/", "Wayback Machine snapshots, collections, and media metadata.", ("Memento", "Common Crawl", "GDELT")),
    SourceCatalogEntry("Memento", "News & Web Archives", "Web archives", "media/memento.md", "public protocol/API aggregators", "https://timetravel.mementoweb.org/", "TimeGate protocol for discovering archived versions across web archives.", ("Internet Archive", "Common Crawl", "GDELT")),
    SourceCatalogEntry("Wikinews", "News & Web Archives", "Global", "media/wikinews.md", "public MediaWiki APIs/dumps", "https://www.wikinews.org/", "Open collaborative news articles and metadata.", ("Wikimedia APIs", "GDELT", "RSS and Atom feeds")),
    SourceCatalogEntry("Event Registry", "News & Web Archives", "Global", "media/event-registry.md", "API key; free and paid tiers", "https://eventregistry.org/documentation", "News article clustering, events, entities, and trends.", ("GDELT", "Media Cloud", "NewsAPI")),
    SourceCatalogEntry("NewsAPI", "News & Web Archives", "Global", "media/newsapi.md", "API key; free and paid tiers", "https://newsapi.org/docs", "Article search and headlines from news publishers.", ("MediaStack", "Event Registry", "GDELT")),
    SourceCatalogEntry("MediaStack", "News & Web Archives", "Global", "media/mediastack.md", "API key; free and paid tiers", "https://mediastack.com/documentation", "News article search and feeds.", ("NewsAPI", "Event Registry", "GDELT")),
    SourceCatalogEntry("SerpAPI", "Search APIs", "Global web/search engines", "search/serpapi.md", "API key; paid tiers", "https://serpapi.com/search-api", "Structured results from search engines.", ("Google Programmable Search", "Bing Web Search", "Brave Search API"), "Respect search-engine and API terms."),
    SourceCatalogEntry("Google Programmable Search", "Search APIs", "Web", "search/google-programmable-search.md", "API key and search engine ID", "https://developers.google.com/custom-search/v1/overview", "Programmable Google search over selected sites or the broader web.", ("SerpAPI", "Bing Web Search", "Brave Search API")),
    SourceCatalogEntry("Bing Web Search", "Search APIs", "Web", "search/bing-web-search.md", "Azure API key", "https://www.microsoft.com/en-us/bing/apis/bing-web-search-api", "Microsoft Bing web search API.", ("Google Programmable Search", "Brave Search API", "SerpAPI")),
    SourceCatalogEntry("Brave Search API", "Search APIs", "Web", "search/brave-search-api.md", "API key; free and paid tiers", "https://api.search.brave.com/app/documentation/web-search/get-started", "Independent web search API.", ("Bing Web Search", "Google Programmable Search", "SerpAPI")),
    SourceCatalogEntry("RSS and Atom feeds", "News & Web Archives", "Web", "media/rss-atom-feeds.md", "public feeds", "https://www.rssboard.org/rss-specification", "Syndicated feed monitoring for official sites, blogs, advisories, and news.", ("GDELT", "NewsAPI", "Wikinews")),
    SourceCatalogEntry("Reddit API", "Social Platforms", "Reddit", "social-platforms/reddit-api.md", "OAuth API", "https://www.reddit.com/dev/api/", "Subreddit, post, comment, and user metadata available through Reddit API terms.", ("RSS and Atom feeds", "GDELT", "SerpAPI")),
    SourceCatalogEntry("YouTube Data API", "Social Platforms", "YouTube", "social-platforms/youtube-data-api.md", "API key/OAuth", "https://developers.google.com/youtube/v3", "Videos, channels, playlists, comments, captions metadata, and search.", ("Google Programmable Search", "GDELT", "RSS and Atom feeds")),
    SourceCatalogEntry("Wikimedia APIs", "Reference Data", "Wikimedia projects", "reference/wikimedia-apis.md", "public APIs and dumps", "https://api.wikimedia.org/wiki/Getting_started_with_Wikimedia_APIs", "Wikipedia/Wikidata Commons and MediaWiki data access.", ("Wikidata", "Wikinews", "GDELT")),
    SourceCatalogEntry("Mastodon APIs", "Social Platforms", "Fediverse", "social-platforms/mastodon-apis.md", "public instance APIs/OAuth", "https://docs.joinmastodon.org/api/", "Instance, account, status, timeline, and search APIs.", ("Mastodon account search", "RSS and Atom feeds", "Bluesky firehose")),
    SourceCatalogEntry("Bluesky firehose", "Social Platforms", "Bluesky/AT Protocol", "social-platforms/bluesky-firehose.md", "public AT Protocol APIs", "https://docs.bsky.app/docs/advanced-guides/firehose", "Realtime AT Protocol event stream for posts, likes, follows, and repo events.", ("Bluesky directory tools", "Mastodon APIs", "GDELT")),
    SourceCatalogEntry("Telegram public channels through Telethon", "Social Platforms", "Telegram", "social-platforms/telegram-telethon.md", "Telegram API credentials and Telethon client", "https://docs.telethon.dev/", "Collection from public Telegram channels and groups visible to an authorized account.", ("RSS and Atom feeds", "GDELT", "SerpAPI"), "Collect only public or authorized communities and comply with platform rules."),
    SourceCatalogEntry("Public Discord communities", "Social Platforms", "Discord", "social-platforms/public-discord-communities.md", "platform/API access varies", "https://discord.com/developers/docs/intro", "Public or permissioned Discord community monitoring and metadata collection.", ("RSS and Atom feeds", "GDELT", "SerpAPI"), "Do not scrape private servers or bypass access controls."),
)


def search_catalog(query: str, *, category: str | None = None) -> list[SourceCatalogEntry]:
    """Return catalog entries matching *query* and optional category substring."""
    q = query.casefold().strip()
    cat = category.casefold().strip() if category else ""
    matches: list[SourceCatalogEntry] = []
    for entry in CATALOG:
        haystack = " ".join(
            [
                entry.name,
                entry.category,
                entry.jurisdiction,
                entry.access,
                entry.homepage,
                entry.notes,
                entry.caution,
                " ".join(entry.cross_refs),
            ]
        ).casefold()
        if q and q not in haystack:
            continue
        if cat and cat not in entry.category.casefold():
            continue
        matches.append(entry)
    return matches


def categories() -> tuple[str, ...]:
    """Return display categories represented in the catalog."""
    return tuple(sorted({entry.category for entry in CATALOG}))


def get_source(name: str) -> SourceCatalogEntry | None:
    """Return a source by exact case-insensitive name."""
    wanted = name.casefold().strip()
    return next((entry for entry in CATALOG if entry.name.casefold() == wanted), None)
