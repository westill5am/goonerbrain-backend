
import requests
from bs4 import BeautifulSoup

def scrape_pornhub(query, max_pages=10):
    results = []
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    for page in range(1, max_pages + 1):
        url = f"https://www.pornhub.com/video/search?search={query}&page={page}"
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            break

        soup = BeautifulSoup(response.content, 'html.parser')
        videos = soup.select('.pcVideoListItem')

        if not videos:
            break

        for video in videos:
            try:
                a = video.select_one('.title a')
                title = a.text.strip()
                video_url = "https://www.pornhub.com" + a['href']
                preview_img = video.select_one('img')
                preview = preview_img.get('data-thumb_url') or preview_img.get('src')
                if not preview or preview.startswith('//'):
                    preview = 'https:' + preview

                results.append({
                    "title": title,
                    "url": video_url,
                    "preview": preview,
                    "source": "pornhub"
                })
            except:
                continue

    return results
