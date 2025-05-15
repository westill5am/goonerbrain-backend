import requests

def scrape_redgifs(query, mode="straight", page=1):
    results = []
    tag = query
    if mode == "gay":
        tag = f"gay {query}"
    elif mode == "trans":
        tag = f"trans {query}"
    api = f"https://api.redgifs.com/v2/gifs/search?search_text={tag}&page={page}"
    try:
        r = requests.get(api, timeout=10)
        if r.status_code != 200:
            return results
        j = r.json()
        for gif in j.get('gifs', []):
            results.append({
                "title": gif.get("title") or tag,
                "url": gif["urls"].get("hd") or gif["urls"].get("webm"),
                "preview": gif["urls"].get("preview"),
                "source": f"RedGIFs ({mode})"
            })
    except Exception:
        pass
    return results
