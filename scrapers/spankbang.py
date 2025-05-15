import requests
from bs4 import BeautifulSoup

def scrape_spankbang(query, page=1, max_pages=1):
    results = []
    headers = {'User-Agent': 'Mozilla/5.0', 'Accept-Language': 'en-US,en;q=0.9'}
    for p in range(page, page + max_pages):
        url = f"https://spankbang.com/s/{query}/{p}/?o=all"
        r = requests.get(url, headers=headers, timeout=10)
        if r.status_code != 200:
            break
        soup = BeautifulSoup(r.content, 'html.parser')
        videos = soup.select('div.video-item')
        for video in videos:
            try:
                a = video.select_one('.video-title')
                link = video.select_one('a')
                img = video.select_one('img')
                if not a or not link or not img:
                    continue
                title = a.text.strip()
                video_url = "https://spankbang.com" + link['href']
                preview = img.get('src')
                if preview and preview.startswith('//'):
                    preview = 'https:' + preview
                elif not preview:
                    continue
                results.append({
                    "title": title,
                    "url": video_url,
                    "preview": preview,
                    "source": "SpankBang"
                })
            except Exception:
                continue
    return results
