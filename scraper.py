import requests
from bs4 import BeautifulSoup

def scrape_ph(query):
    return [{
        "title": f"Pornhub Result for '{query}'",
        "url": "https://pornhub.com",
        "preview": "",
        "source": "Pornhub"
    }]

def scrape_xv(query):
    return [{
        "title": f"Xvideos Result for '{query}'",
        "url": "https://xvideos.com",
        "preview": "",
        "source": "Xvideos"
    }]

def scrape_spankbang(query):
    try:
        from spankbang_api import SpankBang
        sb = SpankBang()
        results = sb.search(query)
        return [{
            "title": v.title,
            "url": v.url,
            "preview": v.thumbnail,
            "source": "SpankBang"
        } for v in results[:5]]
    except Exception as e:
        return [{"title": "SpankBang Error", "url": "", "preview": "", "source": str(e)}]

def scrape_redgifs(query):
    try:
        from redgifs import RedGifs
        rg = RedGifs()
        results = rg.search_gifs(query)
        return [{
            "title": gif.title or f"RedGIF: {query}",
            "url": gif.url,
            "preview": gif.preview_url or gif.thumbnail_url,
            "source": "RedGIFs"
        } for gif in results[:5]]
    except Exception as e:
        return [{"title": "RedGIFs Error", "url": "", "preview": "", "source": str(e)}]

def scrape_all_sites(query):
    return (
        scrape_ph(query) +
        scrape_xv(query) +
        scrape_spankbang(query) +
        scrape_redgifs(query)
    )
