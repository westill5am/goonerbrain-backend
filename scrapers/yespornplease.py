
import requests
from bs4 import BeautifulSoup

def scrape_yespornplease(query, max_pages=10):
    results = []
    headers = {'User-Agent': 'Mozilla/5.0'}

    for page in range(1, max_pages + 1):
        url = f"https://yespornplease.se/?s={query}&paged={page}"
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            break

        soup = BeautifulSoup(response.content, 'html.parser')
        videos = soup.select('div.result-item')

        for video in videos:
            try:
                a = video.select_one('a')
                title = a.get('title', '').strip()
                video_url = a['href']
                preview = video.select_one('img')['src']

                results.append({
                    "title": title,
                    "url": video_url,
                    "preview": preview,
                    "source": "yespornplease"
                })
            except:
                continue

    return results
