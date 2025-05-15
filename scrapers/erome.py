import requests
from bs4 import BeautifulSoup

def scrape_erome(query, mode="straight", page=1):
    results = []
    url = f"https://www.erome.com/search?q={query}&page={page}"
    headers = {'User-Agent': 'Mozilla/5.0'}
    r = requests.get(url, headers=headers, timeout=10)
    soup = BeautifulSoup(r.content, "html.parser")
    for vid in soup.select("div.media-body"):
        try:
            a = vid.select_one("a")
            if not a or not a.has_attr("href"):
                continue
            title = a.text.strip()
            video_url = "https://www.erome.com" + a['href']
            img = vid.parent.select_one("img")
            preview = img.get("src") if img else ""
            results.append({
                "title": title,
                "url": video_url,
                "preview": preview,
                "source": f"Erome"
            })
        except Exception:
            continue
    return results
