import requests
from bs4 import BeautifulSoup

def scrape_eporner(query):
    url = f"https://www.eporner.com/search/{query}/"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")

    results = []
    for vid in soup.select("div.mb h3 a"):
        title = vid.text.strip()
        link = "https://www.eporner.com" + vid["href"]
        thumb = vid.find_parent("div.mb").select_one("img")["src"]

        results.append({
            "title": title,
            "url": link,
            "preview": thumb,
            "source": "Eporner"
        })

    return results
