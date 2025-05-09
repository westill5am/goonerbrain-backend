import requests
from bs4 import BeautifulSoup

def scrape_spankbang(query):
    url = f"https://spankbang.com/s/{query}/1"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")

    results = []
    for vid in soup.select("div.video-item"):
        a = vid.select_one("a")
        title = a["title"]
        link = "https://spankbang.com" + a["href"]
        thumb = vid.select_one("img")
        preview = thumb.get("data-src", "")

        results.append({
            "title": title,
            "url": link,
            "preview": preview,
            "source": "SpankBang"
        })

    return results
