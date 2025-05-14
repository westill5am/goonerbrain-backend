def scrape_all_sites(query):
    return [
        {
            "title": f"Pornhub Result for '{query}'",
            "url": "https://pornhub.com",
            "preview": f"https://via.placeholder.com/300x160?text=Pornhub+{query}",
            "source": "Pornhub"
        },
        {
            "title": f"Xvideos Result for '{query}'",
            "url": "https://xvideos.com",
            "preview": f"https://via.placeholder.com/300x160?text=Xvideos+{query}",
            "source": "Xvideos"
        },
        {
            "title": f"SpankBang Result for '{query}'",
            "url": "https://spankbang.com",
            "preview": f"https://via.placeholder.com/300x160?text=SpankBang+{query}",
            "source": "SpankBang"
        },
        {
            "title": f"RedGIFs Result for '{query}'",
            "url": "https://redgifs.com",
            "preview": f"https://via.placeholder.com/300x160?text=RedGIFs+{query}",
            "source": "RedGIFs"
        }
    ]
