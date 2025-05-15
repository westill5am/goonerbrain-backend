import requests
from bs4 import BeautifulSoup

def scrape_motherless(query, mode="straight", page=1):
    results = []
    url = f"https://motherless.com/videos?q={query}&page={page}"
    headers = {'User-Agent': 'Mozilla/5.0'}
    r = requests.get(url, headers=headers, timeout=10)
    soup = BeautifulSoup(r.content, "html.parser")
    for vid in soup.select("div.thumbvideo-container"):
        try:
            a = vid.select_one("a.thumbvideo")
            if not a or not a.has_attr("href"):
                continue
            title = a.get('title') or a.text.strip()
            video_url = "https://motherless.com" + a['href']
            img = vid.select_one("img")
            preview = img.get("data-src") or img.get("src")
            results.append({
                "title": title,
                "url": video_url,
                "preview": preview,
                "source": f"Motherless"
            })
        except Exception:
            continue
    return results
