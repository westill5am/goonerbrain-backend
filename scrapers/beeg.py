import requests
from bs4 import BeautifulSoup

def scrape_beeg(query):
    url = f"https://beeg.com/search?q={query}"
    res = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(res.text, "html.parser")

    results = []
    for item in soup.select("a[data-href]"):
        img = item.find("img")
        if img:
            results.append({
                "title": f"Beeg Result for '{query}'",
                "url": "https://beeg.com" + item["data-href"],
                "preview": img.get("src", ""),
                "source": "Beeg"
            })
    return results
