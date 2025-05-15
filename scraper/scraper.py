from . import SCRAPER_FUNCS  # <-- This imports all your scraper functions from __init__.py

def scrape_all_sites(query, mode="straight", page=1):
    all_results = []
    for scraper in SCRAPER_FUNCS:
        try:
            results = scraper(query, mode=mode, page=page)
            if isinstance(results, list):
                all_results.extend(results)
            elif results:
                all_results.append(results)
        except Exception as e:
            all_results.append({
                "title": f"Error from {scraper.__name__}",
                "url": "#",
                "preview": "",
                "source": scraper.__name__,
                "error": str(e),
            })
    return all_results
