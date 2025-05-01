import requests
from bs4 import BeautifulSoup

def search_redtube(query: str):
    url = f"https://www.redtube.com/?search={query}"
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, "html.parser")
    
    results = []
    for video in soup.select(".video"):
        title = video.select_one(".title").text.strip()
        thumb = video.select_one("img")["src"]
        link = "https://www.redtube.com" + video.select_one("a")["href"]
        results.append({"title": title, "thumb": thumb, "link": link})
    
    return results
