def search_sites(query: str):
    print(f"✅ Backend hit with query: {query}")
    return [
        {
            "title": f"Test result for {query}",
            "link": "https://example.com/test",
            "thumb": "https://via.placeholder.com/150"
        },
        {
            "title": f"Another result for {query}",
            "link": "https://example.com/test2",
            "thumb": "https://via.placeholder.com/150"
        }
    ]
