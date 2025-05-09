# scraper.py
import asyncio

# Example placeholder functions (replace with actual imports)
async def pornhub_scrape(query):
    return [{"title": f"Pornhub: {query}", "url": "https://pornhub.com", "preview": "", "source": "Pornhub"}]

async def xvideos_scrape(query):
    return [{"title": f"Xvideos: {query}", "url": "https://xvideos.com", "preview": "", "source": "Xvideos"}]

async def scrape_sites(query: str):
    tasks = [pornhub_scrape(query), xvideos_scrape(query)]
    results = await asyncio.gather(*tasks, return_exceptions=True)

    output = []
    for res in results:
        if isinstance(res, list):
            output.extend(res)
    return output
