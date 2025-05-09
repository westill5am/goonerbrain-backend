import requests
from bs4 import BeautifulSoup

def scrape_pornhub(query):
    results = []
    url = f"https://www.pornhub.com/video/search?search={query}"
    headers = {'User-Agent': 'Mozilla/5.0'}

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    videos = soup.select('.pcVideoListItem')

    for video in videos[:10]:
        title = video.select_one('.title a').text.strip()
        video_url = 'https://www.pornhub.com' + video.select_one('.title a')['href']
        preview_img = video.select_one('img')['data-thumb_url']

        results.append({
            "title": title,
            "url": video_url,
            "preview": preview_img,
            "source": "pornhub"
        })
    
    return results
