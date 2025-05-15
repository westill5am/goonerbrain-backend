import requests
from bs4 import BeautifulSoup

def scrape_fux(query, mode="straight", page=1):
    results = []
    if mode == "gay":
        query = f"gay {query}"
    elif mode == "trans":
        query = f"trans {query}"
    url = f"https://www.fux.com/search/videos/{query}/?page={page}"
    headers = {'User-Agent': 'Mozilla/5.0'}
    r = requests.get(url, headers=headers, timeout=10)
    soup = BeautifulSoup(r.content, "html.parser")
    for vid in soup.select("div.item"):
        try:
            a = vid.select_one("a")
            if not a or not a.has_attr("href"):
                continue
            title = a.get('title') or a.text.strip()
            video_url = "https://www.fux.com" + a['href']
            img = vid.select_one("img")
            preview = img.get("data-src") or img.get("src")
            results.append({
                "title": title,
                "url": video_url,
                "preview": preview,
                "source": f"Fux ({mode})"
            })
        except Exception:
            continue
    return results
