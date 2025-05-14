def scrape_all_sites(query):
    return [
        {
            "title": f"Test Match: {query} #{i+1}",
            "url": f"https://example.com/watch?id={i}",
            "preview": f"https://via.placeholder.com/300x160?text={query}+{i+1}",
            "source": "mock"
        }
        for i in range(5)
    ]
