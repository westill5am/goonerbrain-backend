import requests
from bs4 import BeautifulSoup

def scrape_bravotube(query):
    results = []
    url = f"https://www.bravotube.net/videos/{query}/"
    headers = {'User-Agent': 'Mozilla/5.0'}

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    videos = soup.select('.video_block')

    for video in videos[:10]:
        title = video.select_one('img')['alt']
        video_url = "https://www.bravotube.net" + video.select_one('a')['href']
        preview_img = video.select_one('img')['src']

        results.append({
            "title": title,
            "url": video_url,
            "preview": preview_img,
            "source": "bravotube"
        })

    return results
