
import requests
from bs4 import BeautifulSoup

def scrape_javhd(query, max_pages=10):
    results = []
    headers = {'User-Agent': 'Mozilla/5.0'}

    for page in range(1, max_pages + 1):
        url = f"https://www.javhd.com/search/{query}?page={page}"
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            break
        soup = BeautifulSoup(response.content, 'html.parser')
        videos = soup.select('.video-box')

        for video in videos:
            try:
                a = video.select_one('a')
                title = a['title']
                video_url = "https://www.javhd.com" + a['href']
                preview = video.select_one('img')['src']

                results.append({
                    "title": title,
                    "url": video_url,
                    "preview": preview,
                    "source": "javhd"
                })
            except:
                continue

    return results
