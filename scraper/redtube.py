def search_redtube(query: str):
    return [
        {
            "title": f"Fake RedTube Result 1 for '{query}'",
            "link": f"https://www.redtube.com/fake1?q={query}",
            "thumb": "https://via.placeholder.com/150"
        },
        {
            "title": f"Fake RedTube Result 2 for '{query}'",
            "link": f"https://www.redtube.com/fake2?q={query}",
            "thumb": "https://via.placeholder.com/150"
        }
    ]
