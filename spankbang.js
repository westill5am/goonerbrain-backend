import httpx
from bs4 import BeautifulSoup

async def scrape_spankbang(query: str):
    url = f"https://spankbang.party/s/{query}"
    results = []

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    async with httpx.AsyncClient() as client:
        r = await client.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(r.text, 'html.parser')

        for a in soup.select("div.video-list > a"):
            href = a.get("href")
            title = a.select_one(".title")
            duration = a.select_one(".dur")
            img = a.find("img")

            if not href or not title or not img:
                continue

            preview = img.get("data-src") or img.get("src")
            results.append({
                "title": title.text.strip(),
                "url": f"https://spankbang.party{href}",
                "preview": f"https:{preview}" if preview and not preview.startswith("http") else preview,
                "duration": duration.text.strip() if duration else "N/A",
                "source": "SpankBang"
            })

    return results
