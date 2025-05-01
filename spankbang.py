# spankbang.py
import aiohttp
from bs4 import BeautifulSoup

async def scrape_spankbang(query):
    search_url = f"https://spankbang.com/s/{query.replace(' ', '+')}/1/"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    async with aiohttp.ClientSession() as session:
        async with session.get(search_url, headers=headers) as response:
            if response.status != 200:
                return []
            html = await response.text()
            soup = BeautifulSoup(html, "html.parser")
            results = []
            for video in soup.select(".video-item"):
                title_tag = video.select_one(".title")
                if not title_tag:
                    continue
                title = title_tag.get_text(strip=True)
                href = video.get("href")
                preview = video.select_one("img")["src"] if video.select_one("img") else ""
                results.append({
                    "title": title,
                    "url": f"https://spankbang.com{href}",
                    "preview": preview
                })
            return results
