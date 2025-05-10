
import requests
from bs4 import BeautifulSoup

def scrape_motherless(query, max_pages=10):
    results = []
    headers = {'User-Agent': 'Mozilla/5.0'}

    for page in range(1, max_pages + 1):
        url = f"https://motherless.com/videos/{query}/{page}"
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            break

        soup = BeautifulSoup(response.content, 'html.parser')
        videos = soup.select("div.thumb")

        for video in videos:
            try:
                a_tag = video.select_one("a")
                title = a_tag.get("title", "").strip()
                video_url = "https://motherless.com" + a_tag["href"]
                preview = video.select_one("img")["src"]

                results.append({
                    "title": title,
                    "url": video_url,
                    "preview": preview,
                    "source": "motherless"
                })
            except:
                continue

    return results
