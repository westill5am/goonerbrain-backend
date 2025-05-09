import requests
from bs4 import BeautifulSoup

def scrape_youporn(query):
    url = f"https://www.youporn.com/search/?query={query}"
    res = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(res.text, "html.parser")

    results = []
    for video in soup.select("div.video-box"):
        a = video.find("a", href=True)
        img = video.find("img")
        if a and img:
            results.append({
                "title": f"YouPorn Result for '{query}'",
                "url": "https://www.youporn.com" + a["href"],
                "preview": img.get("data-thumb_url") or img.get("src"),
                "source": "YouPorn"
            })
    return results
