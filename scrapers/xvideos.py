import requests
from bs4 import BeautifulSoup

def scrape_xvideos(query, page=1, max_pages=1):
    results = []
    headers = {'User-Agent': 'Mozilla/5.0', 'Accept-Language': 'en-US,en;q=0.9'}
    for p in range(page, page + max_pages):
        url = f'https://www.xvideos.com/?k={query}&p={p}'
        r = requests.get(url, headers=headers, timeout=10)
        if r.status_code != 200:
            break
        soup = BeautifulSoup(r.content, 'html.parser')
        videos = soup.select('div.thumb-block')
        for video in videos:
            try:
                a = video.select_one('p.title a')
                if not a:
                    continue
                title = a.text.strip()
                video_url = "https://www.xvideos.com" + a['href']
                thumb_img = video.select_one('img')
                preview = thumb_img.get('data-src') or thumb_img.get('src')
                if preview and preview.startswith('//'):
                    preview = 'https:' + preview
                elif not preview:
                    continue
                results.append({
                    "title": title,
                    "url": video_url,
                    "preview": preview,
                    "source": "Xvideos"
                })
            except Exception:
                continue
    return results
