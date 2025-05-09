import requests
from bs4 import BeautifulSoup

def scrape_hqporner(query, max_pages=20):
    results = []
    headers = {'User-Agent': 'Mozilla/5.0'}

    for page in range(1, max_pages + 1):
        url = f"https://hqporner.com/search/{query}/{page}.html"
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            break

        soup = BeautifulSoup(response.content, 'html.parser')
        videos = soup.select('div.video')

        if not videos:
            break

        for video in videos:
            a_tag = video.select_one('a')
            title = a_tag['title']
            video_url = "https://hqporner.com" + a_tag['href']
            preview_img = video.select_one('img')['src']

            results.append({
                "title": title,
                "url": video_url,
                "preview": preview_img,
                "source": "hqporner"
            })

    return results
