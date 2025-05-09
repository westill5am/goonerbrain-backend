import requests
from bs4 import BeautifulSoup

def scrape_xvideos(query):
    results = []
    url = f"https://www.xvideos.com/?k={query}"
    headers = {'User-Agent': 'Mozilla/5.0'}

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    videos = soup.select('.thumb-block')

    for video in videos[:10]:
        title = video.select_one('p.title a').text.strip()
        video_url = "https://www.xvideos.com" + video.select_one('p.title a')['href']
        preview_img = video.select_one('img')['data-src']

        results.append({
            "title": title,
            "url": video_url,
            "preview": preview_img,
            "source": "xvideos"
        })

    return results
