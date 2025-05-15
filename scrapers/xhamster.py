import requests
from bs4 import BeautifulSoup

def scrape_xhamster(query, mode="straight", page=1):
    results = []
    base_url = "https://xhamster.com"
    if mode == "gay":
        search_url = f"{base_url}/gay/search/{query}/{page}"
    elif mode == "trans":
        search_url = f"{base_url}/trans/search/{query}/{page}"
    else:
        search_url = f"{base_url}/search/{query}/{page}"
    headers = {'User-Agent': 'Mozilla/5.0'}
    r = requests.get(search_url, headers=headers, timeout=10)
    soup = BeautifulSoup(r.content, "html.parser")
    for vid in soup.select("div.video-thumb-info"):
        try:
            a = vid.find_parent("a", href=True)
            if not a:
                continue
            title = a.get("title") or vid.text.strip()
            video_url = base_url + a["href"]
            img = vid.find_previous("img")
            preview = img.get("src") if img else ""
            results.append({
                "title": title,
                "url": video_url,
                "preview": preview,
                "source": f"XHamster ({mode})"
            })
        except Exception:
            continue
    return results
