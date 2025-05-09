import requests
from bs4 import BeautifulSoup

def scrape_youporn(query):
    results = []
    url = f"https://www.youporn.com/search/?query={query}"
    headers = {'User-Agent': 'Mozilla/5.0'}

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    videos = soup.select('.video-box')

    for video in videos[:10]:
        title = video.select_one('.video-title').text.strip()
        video_url = "https://www.youporn.com" + video.select_one('a')['href']
        preview_img = video.select_one('img')['data-thumbnail']

        results.append({
            "title": title,
            "url": video_url,
            "preview": preview_img,
            "source": "youporn"
        })

    return results
