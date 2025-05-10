
import requests

def scrape_redgifs(query, max_pages=10):
    results = []
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Referer": "https://www.redgifs.com/",
        "Accept": "application/json"
    }

    for page in range(1, max_pages + 1):
        url = f"https://api.redgifs.com/v2/gifs/search?search_text={query}&count=20&page={page}"
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            break

        data = response.json().get("gifs", [])
        for item in data:
            try:
                title = item["title"]
                video_url = "https://redgifs.com/watch/" + item["id"]
                preview = item["urls"]["poster"]

                results.append({
                    "title": title,
                    "url": video_url,
                    "preview": preview,
                    "source": "redgifs"
                })
            except:
                continue

    return results
