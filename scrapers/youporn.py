
import requests
from bs4 import BeautifulSoup

def scrape_youporn(query, max_pages=10):
    results = []
    headers = {'User-Agent': 'Mozilla/5.0'}

    for page in range(1, max_pages + 1):
        url = f"https://www.youporn.com/search/?query={query}&page={page}"
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            break

        soup = BeautifulSoup(response.content, 'html.parser')
        videos = soup.select('.video-box')

        for video in videos:
            try:
                title = video.select_one(".video-title").text.strip()
                video_url = "https://www.youporn.com" + video.select_one("a")["href"]
                preview = video.select_one("img")["data-thumbnail"]

                results.append({
                    "title": title,
                    "url": video_url,
                    "preview": preview,
                    "source": "youporn"
                })
            except:
                continue

    return results
