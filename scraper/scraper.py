import redtube

def search_sites(query: str):
    try:
        results = redtube.search_redtube(query)
        return results if results else [{"title": "No results", "link": "", "thumb": ""}]
    except Exception as e:
        return [{"title": f"Error: {str(e)}", "link": "", "thumb": ""}]
