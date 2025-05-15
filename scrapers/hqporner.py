import requests
from bs4 import BeautifulSoup

def scrape_hqporner(query, mode="straight", page=1):
    results = []
    headers = {'User-Agent': 'Mozilla/5.0'}
    if mode == "gay":
        url = f"https://hqporner.com/search/gay/{query}.html?page={page}"
    elif mode == "trans":
        url = f"https://hqporner.com/search/transgender/{query}.html?page={page}"
    else:
        url = f"https://hqporner.com/search/{query}.html?page={page}"
    r = requests.get(url, headers=headers, timeout=10)
    if r.status_code != 200:
        return results
    soup = BeautifulSoup(r.content, "html.parser")
    for vid in soup.select("div.videoblock"):
        try:
            a = vid.select_one("a")
            if not a or not a.has_attr('href'):
                continue
            title = a.get('title') or a.text.strip()
            video_url = "https://hqporner.com" + a['href']
            img = vid.select_one("img")
            preview = img.get('src')
            results.append({
                "title": title,
                "url": video_url,
                "preview": preview,
                "source": f"HQPorner ({mode})"
            })
        except Exception:
            continue
    return results
