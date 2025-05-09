import requests
from bs4 import BeautifulSoup

def scrape_hqporner(query):
    url = f"https://hqporner.com/search?q={query}"
    res = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(res.text, "html.parser")

    results = []
    for a in soup.select(".video-block > a"):
        img = a.find("img")
        if img and a.get("href"):
            results.append({
                "title": f"HQPorner Result for '{query}'",
                "url": "https://hqporner.com" + a["href"],
                "preview": img.get("src", ""),
                "source": "HQPorner"
            })
    return results
