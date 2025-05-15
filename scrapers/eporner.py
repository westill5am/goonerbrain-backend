import requests
from bs4 import BeautifulSoup

def scrape_eporner(query, mode="straight", page=1):
    results = []
    headers = {'User-Agent': 'Mozilla/5.0'}
    # No gay subdomain, but you can bias keywords
    if mode == "gay":
        url = f"https://www.eporner.com/search/{page}/?q=gay+{query}"
    elif mode == "trans":
        url = f"https://www.eporner.com/search/{page}/?q=trans+{query}"
    else:
        url = f"https://www.eporner.com/search/{page}/?q={query}"
    r = requests.get(url, headers=headers, timeout=10)
    if r.status_code != 200:
        return results
    soup = BeautifulSoup(r.content, "html.parser")
    for vid in soup.select("div.mb-video"):
        try:
            a = vid.select_one("a")
            if not a or not a.has_attr('href'):
                continue
            title = a.get('title') or a.text.strip()
            video_url = "https://www.eporner.com" + a['href']
            img = vid.select_one("img")
            preview = img.get('data-src') or img.get('src')
            results.append({
                "title": title,
                "url": video_url,
                "preview": preview,
                "source": f"Eporner ({mode})"
            })
        except Exception:
            continue
    return results
