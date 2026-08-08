/** Category color map for graph nodes. */
export const CATEGORY_COLORS: Record<string, string> = {
  "campaign-finance": "#f97583",
  "contracts": "#79c0ff",
  "corporate": "#56d364",
  "corporate-registries": "#56d364",
  "developer-footprints": "#79c0ff",
  "domain-dns-intel": "#39c5cf",
  "financial": "#d2a8ff",
  "identity-intel": "#e3b341",
  "influence-networks": "#ff7b72",
  "infrastructure": "#ffa657",
  "investigative-archives": "#c9d1d9",
  "international": "#ff7b72",
  "legal-court-records": "#b392f0",
  "lobbying": "#e3b341",
  "market-financial-data": "#d2a8ff",
  "news-web-archives": "#a5d6ff",
  "nonprofits": "#a5d6ff",
  "procurement": "#79c0ff",
  "reference-data": "#c9d1d9",
  "regulatory": "#7ee787",
  "regulatory-enforcement": "#7ee787",
  "sanctions": "#f778ba",
  "search-apis": "#7ee787",
  "social-identity-intel": "#f778ba",
  "social-platforms": "#a5d6ff",
  "threat-intelligence": "#ff7b72",
  "trade-supply-chain": "#ffa657",
  "web-technology-intel": "#39c5cf",
  "media": "#c9d1d9",
  "legal": "#b392f0",
};

export function getCategoryColor(category: string): string {
  return CATEGORY_COLORS[category] ?? "#8b949e";
}
