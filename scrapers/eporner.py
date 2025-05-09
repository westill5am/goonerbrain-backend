import requests
from bs4 import BeautifulSoup

def scrape_eporner(query):
    results = []
    url = f"https://www.eporner.com/search/{query}/"
    headers = {'User-Agent': 'Mozilla/5.0'}

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    videos = soup.select('.mb')

    for video in videos[:10]:
        title = video.select_one('a.mb')['title']
        video_url = "https://www.eporner.com" + video.select_one('a.mb')['href']
        preview_img = video.select_one('img')['src']

        results.append({
            "title": title,
            "url": video_url,
            "preview": preview_img,
            "source": "eporner"
        })

    return results
