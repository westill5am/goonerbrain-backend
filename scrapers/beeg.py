import requests
from bs4 import BeautifulSoup

def scrape_beeg(query):
    results = []
    url = f"https://beeg.com/search/{query}"
    headers = {'User-Agent': 'Mozilla/5.0'}

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    videos = soup.select('.video-thumb')

    for video in videos[:10]:
        title = video.get('title', 'No title')
        video_url = "https://beeg.com" + video.get('href')
        preview_img = video.select_one('img')['data-src']

        results.append({
            "title": title,
            "url": video_url,
            "preview": preview_img,
            "source": "beeg"
        })

    return results
