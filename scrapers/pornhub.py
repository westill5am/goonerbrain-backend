import requests
from bs4 import BeautifulSoup

def scrape_pornhub(query, mode="straight", page=1):
    results = []
    headers = {'User-Agent': 'Mozilla/5.0'}
    if mode == "gay":
        url = f"https://www.pornhub.com/gay/video/search?search={query}&page={page}"
    elif mode == "trans":
        url = f"https://www.pornhub.com/transgender/video/search?search={query}&page={page}"
    else:
        url = f"https://www.pornhub.com/video/search?search={query}&page={page}"
    response = requests.get(url, headers=headers, timeout=10)
    if response.status_code != 200:
        return results
    soup = BeautifulSoup(response.content, 'html.parser')
    for video in soup.select('.pcVideoListItem, .search-video-preview'):
        try:
            a = video.select_one('.title a')
            if not a:
                continue
            title = a.text.strip()
            video_url = "https://www.pornhub.com" + a['href']
            img = video.select_one('img')
            preview = img.get('data-thumb_url') or img.get('src')
            if preview and preview.startswith('//'):
                preview = 'https:' + preview
            results.append({
                "title": title,
                "url": video_url,
                "preview": preview,
                "source": f"Pornhub ({mode})"
            })
        except Exception:
            continue
    return results
