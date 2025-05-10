
import requests
from bs4 import BeautifulSoup

def scrape_xvideos(query, max_pages=10):
    results = []
    headers = {'User-Agent': 'Mozilla/5.0'}

    for page in range(1, max_pages + 1):
        url = f"https://www.xvideos.com/?k={query}&p={page}"
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            break

        soup = BeautifulSoup(response.content, 'html.parser')
        videos = soup.select('.thumb-block')

        if not videos:
            break

        for video in videos:
            try:
                a = video.select_one('p.title a')
                title = a.text.strip()
                video_url = "https://www.xvideos.com" + a['href']
                preview = video.select_one('img')['data-src']
                results.append({
                    "title": title,
                    "url": video_url,
                    "preview": preview,
                    "source": "xvideos"
                })
            except:
                continue

    return results
