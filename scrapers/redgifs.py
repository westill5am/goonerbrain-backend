import requests

def scrape_redgifs(query):
    results = []
    api = f"https://api.redgifs.com/v2/gifs/search?search_text={query}&count=10"
    res = requests.get(api)
    data = res.json().get("gifs", [])

    for item in data:
        results.append({
            "title": item["title"] or "RedGIF",
            "url": f"https://redgifs.com/watch/{item['id']}",
            "preview": item["urls"].get("thumbnail", ""),
            "source": "RedGIFs"
        })

    return results
