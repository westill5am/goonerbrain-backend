import requests
from bs4 import BeautifulSoup

def scrape_tube8(query, mode="straight", page=1):
    results = []
    headers = {'User-Agent': 'Mozilla/5.0'}
    if mode == "gay":
        url = f"https://www.tube8.com/gay/search/{query}/{page}/"
    elif mode == "trans":
        url = f"https://www.tube8.com/search/transgender/{query}/{page}/"
    else:
        url = f"https://www.tube8.com/search/{query}/{page}/"
    r = requests.get(url, headers=headers, timeout=10)
    if r.status_code != 200:
        return results
    soup = BeautifulSoup(r.content, "html.parser")
    for vid in soup.select("div.video"):
        try:
            a = vid.select_one("a")
            if not a or not a.has_attr('href'):
                continue
            title = a.get('title') or a.text.strip()
            video_url = "https://www.tube8.com" + a['href']
            img = vid.select_one("img")
            preview = img.get('data-src') or img.get('src')
            results.append({
                "title": title,
                "url": video_url,
                "preview": preview,
                "source": f"Tube8 ({mode})"
            })
        except Exception:
            continue
    return results
