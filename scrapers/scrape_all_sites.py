from . import SCRAPER_FUNCS

def scrape_all_sites(query, mode="straight", page=1):
    results = []
    for scraper in SCRAPER_FUNCS:
        try:
            r = scraper(query, mode, page)
            if r and isinstance(r, list):
                results.extend(r)
        except Exception as e:
            print(f"[!] Error in {scraper.__name__}: {e}")
            results.append({
                "title": f"{scraper.__name__} error",
                "url": "#",
                "preview": "",
                "source": scraper.__name__,
                "error": str(e),
            })
    return results
