import requests
from bs4 import BeautifulSoup

def scrape_beeg(query, mode="straight", page=1):
    results = []
    # Beeg doesn't really have gay/trans filter, bias query
    if mode == "gay":
        query = f"gay {query}"
    elif mode == "trans":
        query = f"trans {query}"
    url = f"https://beeg.com/search?q={query}&page={page}"
    headers = {'User-Agent': 'Mozilla/5.0'}
    r = requests.get(url, headers=headers, timeout=10)
    soup = BeautifulSoup(r.content, "html.parser")
    for vid in soup.select("div.video-item"):
        try:
            a = vid.select_one("a")
            if not a or not a.has_attr("href"):
                continue
            title = a.get('title') or a.text.strip()
            video_url = "https://beeg.com" + a['href']
            img = vid.select_one("img")
            preview = img.get("src") if img else ""
            results.append({
                "title": title,
                "url": video_url,
                "preview": preview,
                "source": f"Beeg ({mode})"
            })
        except Exception:
            continue
    return results
