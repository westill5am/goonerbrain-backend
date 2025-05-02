# scraper.py
def search_sites(query: str):
    # Simulate a few fake search results
    return [
        {
            "title": f"Fake result for '{query}'",
            "link": "https://example.com/fake-video",
            "thumb": "https://via.placeholder.com/150"
        },
        {
            "title": f"Another result for '{query}'",
            "link": "https://example.com/another-video",
            "thumb": "https://via.placeholder.com/150"
        }
    ]
