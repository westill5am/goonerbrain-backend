# scrapers/__init__.py

from .pornhub import scrape_pornhub
from .xvideos import scrape_xvideos
from .redgifs import scrape_redgifs
from .spankbang import scrape_spankbang
from .eporner import scrape_eporner
from .txxx import scrape_txxx
from .hqporner import scrape_hqporner
from .rule34 import scrape_rule34
from .youporn import scrape_youporn
from .tube8 import scrape_tube8
from .motherless import scrape_motherless
from .erome import scrape_erome
from .xhamster import scrape_xhamster
from .fux import scrape_fux
from .beeg import scrape_beeg
from .bravotube import scrape_bravotube

# Add more as modules are created

def scrape_all_sites(query):
    results = []
    for scraper in [
        scrape_pornhub,
        scrape_xvideos,
        scrape_redgifs,
        scrape_spankbang,
        scrape_eporner,
        scrape_txxx,
        scrape_hqporner,
        scrape_rule34,
        scrape_youporn,
        scrape_tube8,
        scrape_motherless,
        scrape_erome,
        scrape_xhamster,
        scrape_fux,
        scrape_beeg,
        scrape_bravotube,
        # Add more scrapers here
    ]:
        try:
            results.extend(scraper(query))
        except Exception as e:
            print(f"[!] Error in {scraper.__name__}: {e}")
    return results
