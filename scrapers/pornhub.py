import requests
from bs4 import BeautifulSoup

def scrape_pornhub(query):
    url = f"https://www.pornhub.com/video/search?search={query}"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")

    results = []
    for video in soup.select("li.videoBox"):
        title = video.select_one("span.title").text.strip()
        link = "https://www.pornhub.com" + video.a["href"]
        thumbnail = video.img["data-thumb_url"] if video.img.has_attr("data-thumb_url") else video.img.get("src", "")

        results.append({
            "title": title,
            "url": link,
            "preview": thumbnail,
            "source": "Pornhub"
        })

    return results
