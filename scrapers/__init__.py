from .pornhub import scrape_pornhub
from .xvideos import scrape_xvideos
from .spankbang import scrape_spankbang
from .redgifs import scrape_redgifs
from .eporner import scrape_eporner
from .txxx import scrape_txxx
from .hqporner import scrape_hqporner
from .rule34 import scrape_rule34
from .youporn import scrape_youporn
from .tube8 import scrape_tube8
# Add more as you add new .py files

SCRAPER_FUNCS = [
    scrape_pornhub,
    scrape_xvideos,
    scrape_spankbang,
    scrape_redgifs,
    scrape_eporner,
    scrape_txxx,
    scrape_hqporner,
    scrape_rule34,
    scrape_youporn,
    scrape_tube8,
    # Add more here to include new scrapers
]
