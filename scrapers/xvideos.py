import requests
from bs4 import BeautifulSoup

def scrape_xvideos(query):
    url = f"https://www.xvideos.com/?k={query}"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")

    results = []
    for video in soup.select("div.thumb-block"):
        a_tag = video.select_one("a")
        title = a_tag["title"]
        link = "https://www.xvideos.com" + a_tag["href"]
        img = video.select_one("img")
        preview = img.get("data-src") or img.get("src", "")

        results.append({
            "title": title,
            "url": link,
            "preview": preview,
            "source": "Xvideos"
        })

    return results
