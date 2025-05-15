import requests
from bs4 import BeautifulSoup

def scrape_xvideos(query, mode="straight", page=1):
    results = []
    headers = {'User-Agent': 'Mozilla/5.0'}
    if mode == "gay":
        url = f"https://www.gayxvideos.com/?k={query}&p={page}"
    elif mode == "trans":
        url = f"https://www.xvideos.com/?k=transgender+{query}&p={page}"
    else:
        url = f"https://www.xvideos.com/?k={query}&p={page}"
    r = requests.get(url, headers=headers, timeout=10)
    if r.status_code != 200:
        return results
    soup = BeautifulSoup(r.content, "html.parser")
    for vid in soup.select("div.thumb-block"):
        try:
            a = vid.select_one("a")
            if not a or not a.has_attr("title"):
                continue
            title = a['title']
            video_url = "https://www.xvideos.com" + a['href']
            img = vid.select_one("img")
            preview = img.get("data-src") or img.get("src")
            results.append({
                "title": title,
                "url": video_url,
                "preview": preview,
                "source": f"Xvideos ({mode})"
            })
        except Exception:
            continue
    return results
