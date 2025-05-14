from scrapers.pornhub import scrape_pornhub
from scrapers.xvideos import scrape_xvideos
from scrapers.redgifs import scrape_redgifs
# Add as needed...

def scrape_all_sites(query):
    return (
        scrape_pornhub(query) +
        scrape_xvideos(query) +
        scrape_redgifs(query)
        # Add more here
    )
