from .pornhub import scrape_pornhub
from .xvideos import scrape_xvideos
from .spankbang import scrape_spankbang
from .redgifs import scrape_redgifs

def scrape_all_sites(query, mode="straight", page=1):
    results = []
    scrapers = [
        ("Pornhub", scrape_pornhub),
        ("Xvideos", scrape_xvideos),
        ("SpankBang", scrape_spankbang),
        ("RedGIFs", scrape_redgifs)
    ]
    for name, scraper in scrapers:
        try:
            # You can adjust max_pages per scraper if you want
            results += scraper(query, page=page, max_pages=1)
        except Exception as e:
            results.append({
                "title": "Error",
                "url": "#",
                "preview": "",
                "source": name,
                "error": str(e)
            })
    return results
