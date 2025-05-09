# scrapers/__init__.py

from .pornhub import scrape_pornhub
from .xvideos import scrape_xvideos
from .redgifs import scrape_redgifs
from .spankbang import scrape_spankbang

# Add more as modules are created

def scrape_all_sites(query):
    results = []
    for scraper in [
        scrape_pornhub,
        scrape_xvideos,
        scrape_redgifs,
        scrape_spankbang,
        # Add more scrapers here
    ]:
        try:
            results.extend(scraper(query))
        except Exception as e:
            print(f"[!] Error in {scraper.__name__}: {e}")
    return results
