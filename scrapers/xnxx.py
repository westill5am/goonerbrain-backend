
import requests
from bs4 import BeautifulSoup

def scrape_xnxx(query, max_pages=10):
    results = []
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    for page in range(1, max_pages + 1):
        url = f"https://www.xnxx.com/search/{query}/{page}"
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            break
        
        soup = BeautifulSoup(response.content, 'html.parser')
        videos = soup.select('.thumb-block')
        
        for video in videos:
            try:
                a = video.select_one('a')
                title = a.get('title')
                video_url = "https://www.xnxx.com" + a['href']
                preview = video.select_one('img').get('data-src') or video.select_one('img').get('src')

                results.append({
                    "title": title,
                    "url": video_url,
                    "preview": preview,
                    "source": "xnxx"
                })
            except:
                continue

    return results
