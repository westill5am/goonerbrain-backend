import requests
from bs4 import BeautifulSoup

def scrape_spankbang(query, mode="straight", page=1):
    results = []
    headers = {'User-Agent': 'Mozilla/5.0'}
    if mode == "gay":
        url = f"https://www.spankbang.com/gay/search?query={query}&p={page}"
    elif mode == "trans":
        url = f"https://www.spankbang.com/search?query=trans+{query}&p={page}"
    else:
        url = f"https://www.spankbang.com/search?query={query}&p={page}"
    r = requests.get(url, headers=headers, timeout=10)
    if r.status_code != 200:
        return results
    soup = BeautifulSoup(r.content, "html.parser")
    for vid in soup.select("div.video-item, .video"):
        try:
            a = vid.select_one("a")
            if not a or not a.has_attr('href'):
                continue
            title = a['title'] if a.has_attr('title') else a.text.strip()
            video_url = "https://www.spankbang.com" + a['href']
            img = vid.select_one("img")
            preview = img.get("src") if img else ""
            results.append({
                "title": title,
                "url": video_url,
                "preview": preview,
                "source": f"SpankBang ({mode})"
            })
        except Exception:
            continue
    return results
