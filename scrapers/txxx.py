import requests
from bs4 import BeautifulSoup

def scrape_txxx(query):
    url = f"https://www.txxx.com/search/{query}/"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")

    results = []
    for video in soup.select(".thumb"):
        a = video.select_one("a")
        title = a["title"]
        link = "https://www.txxx.com" + a["href"]
        preview = a.select_one("img")["data-original"]

        results.append({
            "title": title,
            "url": link,
            "preview": preview,
            "source": "TXXX"
        })

    return results
