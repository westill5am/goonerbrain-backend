def search_redtube(query: str):
    return [
        {
            "title": f"Mock RedTube result for: {query}",
            "link": f"https://www.redtube.com/mock-result?q={query}",
            "thumb": "https://via.placeholder.com/150"
        },
        {
            "title": f"Another fake result for: {query}",
            "link": f"https://www.redtube.com/fake?q={query}",
            "thumb": "https://via.placeholder.com/150"
        }
    ]
