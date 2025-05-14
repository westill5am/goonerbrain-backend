from .spankbang import scrape as scrape_spankbang
from .redgifs import scrape as scrape_redgifs

def scrape_all_sites(query: str, mode: str = "straight", page: int = 1):
    results = []
    try:
        results += scrape_spankbang(query, mode=mode, page=page)
    except Exception as e:
        results.append({"source": "SpankBang", "title": "Error", "url": "#", "preview": "", "error": str(e)})
    try:
        results += scrape_redgifs(query, mode=mode, page=page)
    except Exception as e:
        results.append({"source": "RedGIFs", "title": "Error", "url": "#", "preview": "", "error": str(e)})
    return results
