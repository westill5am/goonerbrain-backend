import requests
from bs4 import BeautifulSoup

def scrape_pornhub(query, page=1, max_pages=1):
    results = []
    headers = {'User-Agent': 'Mozilla/5.0', 'Accept-Language': 'en-US,en;q=0.9'}
    for p in range(page, page + max_pages):
        url = f"https://www.pornhub.com/video/search?search={query}&page={p}"
        r = requests.get(url, headers=headers, timeout=10)
        if r.status_code != 200 or 'captcha' in r.text.lower():
            break
        soup = BeautifulSoup(r.content, 'html.parser')
        videos = soup.select('.pcVideoListItem') or soup.select('li.videoBox')
        for video in videos:
            try:
                a = video.select_one('.title a')
                if not a:
                    continue
                title = a.text.strip()
                video_url = "https://www.pornhub.com" + a['href']
                preview_img = video.select_one('img')
                preview = preview_img.get('data-thumb_url') or preview_img.get('src')
                if preview and preview.startswith('//'):
                    preview = 'https:' + preview
                elif not preview:
                    continue
                results.append({
                    "title": title,
                    "url": video_url,
                    "preview": preview,
                    "source": "Pornhub"
                })
            except Exception:
                continue
    return results
