# scraper/scrape_all_sites.py (or similar path)
from scrapers.spankbang import scrape as scrape_spankbang
from scrapers.redgifs import scrape as scrape_redgifs
# Add other imports here...

def scrape_all_sites(query: str, mode: str = "straight") -> list:
    results = []

    # Filter logic based on mode (customize this depending on site support)
    try:
        if mode in ["straight", "gay", "trans"]:
            results += scrape_spankbang(query, mode=mode)
    except Exception as e:
        results.append({
            "source": "SpankBang",
            "title": "SpankBang Error",
            "url": "#",
            "preview": "",
            "error": str(e),
        })

    try:
        if mode in ["straight", "gay"]:
            results += scrape_redgifs(query, mode=mode)
    except Exception as e:
        results.append({
            "source": "RedGIFs",
            "title": "RedGIFs Error",
            "url": "#",
            "preview": "",
            "error": str(e),
        })

    # Repeat this pattern for your other scrapers...
    return results
