import requests
from bs4 import BeautifulSoup

def scrape_bravotube(query, mode="straight", page=1):
    results = []
    if mode == "gay":
        query = f"gay {query}"
    elif mode == "trans":
        query = f"trans {query}"
    url = f"https://www.bravotube.net/search/{query}/{page}/"
    headers = {'User-Agent': 'Mozilla/5.0'}
    r = requests.get(url, headers=headers, timeout=10)
    soup = BeautifulSoup(r.content, "html.parser")
    for vid in soup.select("div.video"):
        try:
            a = vid.select_one("a")
            if not a or not a.has_attr("href"):
                continue
            title = a.get('title') or a.text.strip()
            video_url = "https://www.bravotube.net" + a['href']
            img = vid.select_one("img")
            preview = img.get("src") if img else ""
            results.append({
                "title": title,
                "url": video_url,
                "preview": preview,
                "source": f"BravoTube ({mode})"
            })
        except Exception:
            continue
    return results
