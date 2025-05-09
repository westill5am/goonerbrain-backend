import requests
from bs4 import BeautifulSoup

def scrape_xhamster(query):
    url = f"https://xhamster.com/search/{query.replace(' ', '%20')}"
    res = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(res.text, "html.parser")

    results = []
    for card in soup.select("div.video-thumb__image-container > a"):
        img = card.find("img")
        if img and card.get("href"):
            results.append({
                "title": f"XHamster Result for '{query}'",
                "url": "https://xhamster.com" + card["href"],
                "preview": img.get("src", ""),
                "source": "XHamster"
            })
    return results
