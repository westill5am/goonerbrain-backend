
import requests
from bs4 import BeautifulSoup

def scrape_femjoy(query, max_pages=5):
    results = []
    headers = {'User-Agent': 'Mozilla/5.0'}

    for page in range(1, max_pages + 1):
        url = f"https://www.femjoy.com/search?query={query}&page={page}"
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            break
        soup = BeautifulSoup(response.content, 'html.parser')
        videos = soup.select('.gallery-item')

        for video in videos:
            try:
                a = video.select_one('a')
                title = a.get('title')
                video_url = "https://www.femjoy.com" + a['href']
                preview = video.select_one('img')['src']

                results.append({
                    "title": title,
                    "url": video_url,
                    "preview": preview,
                    "source": "femjoy"
                })
            except:
                continue

    return results
