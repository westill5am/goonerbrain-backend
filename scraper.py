import asyncio

# Fake placeholder scrapers — replace these with your real modules later
async def pornhub_scrape(query):
    return [{
        "title": f"Pornhub Result for '{query}'",
        "url": "https://pornhub.com",
        "preview": "",
        "source": "Pornhub"
    }]

async def xvideos_scrape(query):
    return [{
        "title": f"Xvideos Result for '{query}'",
        "url": "https://xvideos.com",
        "preview": "",
        "source": "Xvideos"
    }]

async def scrape_sites(query: str):
    tasks = [
        pornhub_scrape(query),
        xvideos_scrape(query)
    ]
    results = await asyncio.gather(*tasks, return_exceptions=True)

    final_results = []
    for result in results:
        if isinstance(result, list):
            final_results.extend(result)
    return final_results
