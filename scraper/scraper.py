import redtube

def search_sites(query: str):
    # Safely call redtube search
    try:
        results = redtube.search_redtube(query)
        return results or [{"title": "No redtube results", "link": "", "thumb": ""}]
    except Exception as e:
        return [{"title": f"Scraper error: {str(e)}", "link": "", "thumb": ""}]
