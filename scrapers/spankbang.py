import requests
from bs4 import BeautifulSoup

def scrape_spankbang(query):
    results = []
    url = f"https://spankbang.com/s/{query}/"
    headers = {'User-Agent': 'Mozilla/5.0'}

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    videos = soup.select('.video-item')

    for video in videos[:10]:
        title = video.select_one('a.n').text
        video_url = "https://spankbang.com" + video.select_one('a.n')['href']
        preview_img = video.select_one('img')['data-src']

        results.append({
            "title": title,
            "url": video_url,
            "preview": preview_img,
            "source": "spankbang"
        })

    return results
