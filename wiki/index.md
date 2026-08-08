# Data Sources Wiki

Reference documentation for every dataset God's Eye can ingest. Each entry follows a [standardized template](template.md) so agents and contributors can quickly understand access methods, schema, and cross-reference potential.

## Sources by Category

### Campaign Finance

| Source | Jurisdiction | Link |
|--------|-------------|------|
| Massachusetts OCPF | MA state & local | [massachusetts-ocpf.md](campaign-finance/massachusetts-ocpf.md) |
| FEC Federal Campaign Finance | US federal | [fec-federal.md](campaign-finance/fec-federal.md) |

### Government Contracts

| Source | Jurisdiction | Link |
|--------|-------------|------|
| Boston Open Checkbook | City of Boston | [boston-open-checkbook.md](contracts/boston-open-checkbook.md) |
| USASpending.gov | US federal | [usaspending.md](contracts/usaspending.md) |
| SAM.gov | US federal | [sam-gov.md](contracts/sam-gov.md) |

### Corporate Registries

| Source | Jurisdiction | Link |
|--------|-------------|------|
| MA Secretary of Commonwealth | Massachusetts | [massachusetts-soc.md](corporate/massachusetts-soc.md) |
| SEC EDGAR | US public companies | [sec-edgar.md](corporate/sec-edgar.md) |

### Financial

| Source | Jurisdiction | Link |
|--------|-------------|------|
| FDIC BankFind | US banks & thrifts | [fdic-bankfind.md](financial/fdic-bankfind.md) |

### Lobbying

| Source | Jurisdiction | Link |
|--------|-------------|------|
| Senate Lobbying Disclosures (LD-1/LD-2) | US federal | [senate-ld.md](lobbying/senate-ld.md) |

### Nonprofits

| Source | Jurisdiction | Link |
|--------|-------------|------|
| ProPublica Nonprofit Explorer / IRS 990 | US nationwide | [propublica-990.md](nonprofits/propublica-990.md) |

### Regulatory & Enforcement

| Source | Jurisdiction | Link |
|--------|-------------|------|
| EPA ECHO | US nationwide | [epa-echo.md](regulatory/epa-echo.md) |
| OSHA Inspections | US nationwide | [osha-inspections.md](regulatory/osha-inspections.md) |

### Sanctions

| Source | Jurisdiction | Link |
|--------|-------------|------|
| OFAC SDN List | International | [ofac-sdn.md](sanctions/ofac-sdn.md) |

### International

| Source | Jurisdiction | Link |
|--------|-------------|------|
| ICIJ Offshore Leaks Database | Global | [icij-offshore-leaks.md](international/icij-offshore-leaks.md) |

### Infrastructure

| Source | Jurisdiction | Link |
|--------|-------------|------|
| US Census Bureau ACS | US nationwide | [census-acs.md](infrastructure/census-acs.md) |

## Contributing

To add a new data source, copy [template.md](template.md) into the appropriate category folder and fill in each section. Link it from this index when complete.

## Expanded OSINT Source Catalog

### Campaign Finance
| Source | Jurisdiction | Link |
|--------|-------------|------|
| FollowTheMoney | United States | [followthemoney.md](campaign-finance/followthemoney.md) |
| National election and political-finance databases | National/state/local | [national-election-political-finance.md](campaign-finance/national-election-political-finance.md) |

### Corporate Registries
| Source | Jurisdiction | Link |
|--------|-------------|------|
| Companies House bulk data | United Kingdom | [companies-house-bulk-data.md](corporate/companies-house-bulk-data.md) |
| EU business registries | European Union | [eu-business-registries.md](corporate/eu-business-registries.md) |
| GLEIF LEI data | Global | [gleif-lei.md](corporate/gleif-lei.md) |
| National company registries | National | [national-company-registries.md](corporate/national-company-registries.md) |
| OpenCorporates | Global | [opencorporates.md](corporate/opencorporates.md) |
| OpenOwnership Register | Global | [openownership-register.md](corporate/openownership-register.md) |
| Orbis | Global | [orbis.md](corporate/orbis.md) |
| Sayari | Global | [sayari.md](corporate/sayari.md) |
| UK Companies House | United Kingdom | [uk-companies-house.md](corporate/uk-companies-house.md) |

### Developer Footprints
| Source | Jurisdiction | Link |
|--------|-------------|------|
| GitFive | GitHub | [gitfive.md](developer/gitfive.md) |
| GitGraber | GitHub | [gitgraber.md](developer/gitgraber.md) |
| GitHub and GitLab APIs | Global | [github-gitlab-apis.md](developer/github-gitlab-apis.md) |
| GitLeaks | Repositories | [gitleaks.md](developer/gitleaks.md) |

### Domain & DNS Intel
| Source | Jurisdiction | Link |
|--------|-------------|------|
| Amass | Global | [amass.md](domain/amass.md) |
| Assetfinder | Global | [assetfinder.md](domain/assetfinder.md) |
| Certificate Transparency logs | Global | [certificate-transparency-logs.md](domain/certificate-transparency-logs.md) |
| crt.sh | Global | [crtsh.md](domain/crtsh.md) |
| DNSDumpster | Global | [dnsdumpster.md](domain/dnsdumpster.md) |
| DNSTwist | Global | [dnstwist.md](domain/dnstwist.md) |
| DNSViz | Global | [dnsviz.md](domain/dnsviz.md) |
| dnsx | Global | [dnsx.md](domain/dnsx.md) |
| DomainTools | Global | [domaintools.md](domain/domaintools.md) |
| httpx | Global | [httpx.md](domain/httpx.md) |
| ICANN Lookup | Global | [icann-lookup.md](domain/icann-lookup.md) |
| MXToolbox | Global | [mxtoolbox.md](domain/mxtoolbox.md) |
| RDAP | Global | [rdap.md](domain/rdap.md) |
| SecurityTrails | Global | [securitytrails.md](domain/securitytrails.md) |
| Subfinder | Global | [subfinder.md](domain/subfinder.md) |
| theHarvester | Global | [theharvester.md](domain/theharvester.md) |
| URLCrazy | Global | [urlcrazy.md](domain/urlcrazy.md) |
| ViewDNS | Global | [viewdns.md](domain/viewdns.md) |
| WHOIS | Global | [whois.md](domain/whois.md) |

### Identity Intel
| Source | Jurisdiction | Link |
|--------|-------------|------|
| Email2phonenumber-style utilities | Global | [email2phonenumber-style-utilities.md](identity/email2phonenumber-style-utilities.md) |
| EmailRep | Global | [emailrep.md](identity/emailrep.md) |
| Epieos | Global | [epieos.md](identity/epieos.md) |
| Gravatar lookup | Global | [gravatar-lookup.md](identity/gravatar-lookup.md) |
| Have I Been Pwned | Breach-notification corpus | [hibp.md](identity/hibp.md) |
| Holehe | Global | [holehe.md](identity/holehe.md) |
| Hunter | Global | [hunter.md](identity/hunter.md) |
| Keybase | Global | [keybase.md](identity/keybase.md) |
| PGP key servers | Global | [pgp-key-servers.md](identity/pgp-key-servers.md) |

### Influence Networks
| Source | Jurisdiction | Link |
|--------|-------------|------|
| LittleSis | US and global | [littlesis.md](influence/littlesis.md) |

### Investigative Archives
| Source | Jurisdiction | Link |
|--------|-------------|------|
| OCCRP Aleph | Global | [occrp-aleph.md](investigative/occrp-aleph.md) |

### Legal & Court Records
| Source | Jurisdiction | Link |
|--------|-------------|------|
| CourtListener | United States | [courtlistener.md](legal/courtlistener.md) |
| PACER | United States | [pacer.md](legal/pacer.md) |
| RECAP | United States | [recap.md](legal/recap.md) |

### Market & Financial Data
| Source | Jurisdiction | Link |
|--------|-------------|------|
| Alpha Vantage | Global public markets | [alpha-vantage.md](financial/alpha-vantage.md) |
| Crunchbase | Global startups and investors | [crunchbase.md](financial/crunchbase.md) |
| Financial Modeling Prep | Global public markets | [financial-modeling-prep.md](financial/financial-modeling-prep.md) |
| OpenFIGI | Global securities | [openfigi.md](financial/openfigi.md) |
| PitchBook | Global private markets | [pitchbook.md](financial/pitchbook.md) |

### News & Web Archives
| Source | Jurisdiction | Link |
|--------|-------------|------|
| Common Crawl | Web | [common-crawl.md](media/common-crawl.md) |
| Event Registry | Global | [event-registry.md](media/event-registry.md) |
| GDELT | Global | [gdelt.md](media/gdelt.md) |
| Internet Archive | Web | [internet-archive.md](media/internet-archive.md) |
| Media Cloud | Global | [media-cloud.md](media/media-cloud.md) |
| MediaStack | Global | [mediastack.md](media/mediastack.md) |
| Memento | Web archives | [memento.md](media/memento.md) |
| NewsAPI | Global | [newsapi.md](media/newsapi.md) |
| RSS and Atom feeds | Web | [rss-atom-feeds.md](media/rss-atom-feeds.md) |
| Wikinews | Global | [wikinews.md](media/wikinews.md) |

### Procurement
| Source | Jurisdiction | Link |
|--------|-------------|------|
| EU TED | European Union | [eu-ted.md](procurement/eu-ted.md) |
| Open Contracting Data Standard | Global | [ocds.md](procurement/ocds.md) |
| OpenTender | Europe | [opentender.md](procurement/opentender.md) |
| UN procurement data | Global | [un-procurement.md](procurement/un-procurement.md) |
| World Bank procurement data | Global | [world-bank-procurement.md](procurement/world-bank-procurement.md) |

### Reference Data
| Source | Jurisdiction | Link |
|--------|-------------|------|
| Wikidata | Global | [wikidata.md](reference/wikidata.md) |
| Wikimedia APIs | Wikimedia projects | [wikimedia-apis.md](reference/wikimedia-apis.md) |

### Sanctions
| Source | Jurisdiction | Link |
|--------|-------------|------|
| OpenSanctions | Global | [opensanctions.md](sanctions/opensanctions.md) |

### Search APIs
| Source | Jurisdiction | Link |
|--------|-------------|------|
| Bing Web Search | Web | [bing-web-search.md](search/bing-web-search.md) |
| Brave Search API | Web | [brave-search-api.md](search/brave-search-api.md) |
| Google Programmable Search | Web | [google-programmable-search.md](search/google-programmable-search.md) |
| SerpAPI | Global web/search engines | [serpapi.md](search/serpapi.md) |

### Social & Identity Intel
| Source | Jurisdiction | Link |
|--------|-------------|------|
| Blackbird | Global | [blackbird.md](social/blackbird.md) |
| Bluesky directory tools | Bluesky/AT Protocol | [bluesky-directory-tools.md](social/bluesky-directory-tools.md) |
| GHunt | Google accounts | [ghunt.md](identity/ghunt.md) |
| KnowEm | Global | [knowem.md](social/knowem.md) |
| Maigret | Global | [maigret.md](social/maigret.md) |
| Mastodon account search | Fediverse | [mastodon-account-search.md](social/mastodon-account-search.md) |
| Namechk | Global | [namechk.md](social/namechk.md) |
| Sherlock | Global | [sherlock.md](social/sherlock.md) |
| Snoop | Global | [snoop.md](social/snoop.md) |
| Social Analyzer | Global | [social-analyzer.md](social/social-analyzer.md) |
| Steam public-profile tools | Steam | [steam-public-profile-tools.md](social/steam-public-profile-tools.md) |
| WhatsMyName | Global | [whatsmyname.md](social/whatsmyname.md) |
| WhatsMyName Web | Global | [whatsmyname-web.md](social/whatsmyname-web.md) |

### Social Platforms
| Source | Jurisdiction | Link |
|--------|-------------|------|
| Bluesky firehose | Bluesky/AT Protocol | [bluesky-firehose.md](social-platforms/bluesky-firehose.md) |
| Mastodon APIs | Fediverse | [mastodon-apis.md](social-platforms/mastodon-apis.md) |
| Public Discord communities | Discord | [public-discord-communities.md](social-platforms/public-discord-communities.md) |
| Reddit API | Reddit | [reddit-api.md](social-platforms/reddit-api.md) |
| Telegram public channels through Telethon | Telegram | [telegram-telethon.md](social-platforms/telegram-telethon.md) |
| YouTube Data API | YouTube | [youtube-data-api.md](social-platforms/youtube-data-api.md) |

### Threat Intelligence
| Source | Jurisdiction | Link |
|--------|-------------|------|
| AbuseIPDB | Global | [abuseipdb.md](threat-intel/abuseipdb.md) |
| AlienVault OTX | Global | [alienvault-otx.md](threat-intel/alienvault-otx.md) |
| CIRCL Passive DNS | Global | [circl-passive-dns.md](threat-intel/circl-passive-dns.md) |
| Farsight DNSDB | Global | [farsight-dnsdb.md](threat-intel/farsight-dnsdb.md) |
| GreyNoise | Internet-wide sensors | [greynoise.md](threat-intel/greynoise.md) |
| OpenPhish | Global | [openphish.md](threat-intel/openphish.md) |
| PhishTank | Global | [phishtank.md](threat-intel/phishtank.md) |
| RiskIQ PassiveTotal | Global | [riskiq-passivetotal.md](threat-intel/riskiq-passivetotal.md) |
| Spamhaus | Global | [spamhaus.md](threat-intel/spamhaus.md) |
| URLScan | Global | [urlscan.md](threat-intel/urlscan.md) |
| VirusTotal | Global | [virustotal.md](threat-intel/virustotal.md) |

### Trade & Supply Chain
| Source | Jurisdiction | Link |
|--------|-------------|------|
| ImportYeti | United States importers | [importyeti.md](trade/importyeti.md) |
| Panjiva | Global | [panjiva.md](trade/panjiva.md) |

### Web Technology Intel
| Source | Jurisdiction | Link |
|--------|-------------|------|
| BuiltWith | Global | [builtwith.md](web-tech/builtwith.md) |
| Wappalyzer | Global | [wappalyzer.md](web-tech/wappalyzer.md) |
| WhatWeb | Global | [whatweb.md](web-tech/whatweb.md) |
