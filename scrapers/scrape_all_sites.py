# scrapers/scrape_all_sites.py

from . import SCRAPER_FUNCS

def scrape_all_sites(query: str, mode: str = "straight", page: int = 1):
    """
    Run each scraper in SCRAPER_FUNCS against (query, mode, page),
    concatenate all their results into a single list.
    Each scraper must have signature: fn(query, mode, page) -> List[dict]
    """
    all_results = []

    for fn in SCRAPER_FUNCS:
        try:
            results = fn(query, mode, page)
            if results:
                all_results.extend(results)
        except Exception as e:
            # Log scraper failure and keep going
            print(f"[scrape_all_sites] {fn.__name__} failed:", e)

    return all_results
