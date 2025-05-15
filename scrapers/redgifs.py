import requests

def scrape_redgifs(query, page=1, max_pages=1):
    results = []
    for p in range(page, page + max_pages):
        url = f'https://api.redgifs.com/v2/gifs/search?search_text={query}&count=24&page={p}'
        r = requests.get(url, timeout=10)
        if r.status_code != 200:
            break
        data = r.json()
        for item in data.get('gifs', []):
            try:
                title = item.get('title') or "RedGIFs"
                video_url = f"https://redgifs.com/watch/{item['id']}"
                preview = item['urls'].get('preview') or item['urls'].get('sd')
                results.append({
                    "title": title,
                    "url": video_url,
                    "preview": preview,
                    "source": "RedGIFs"
                })
            except Exception:
                continue
    return results
