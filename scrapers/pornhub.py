import requests
from bs4 import BeautifulSoup

def scrape_pornhub(query, max_pages=3):
    results = []
    headers = {
        'User-Agent': 'Mozilla/5.0',
        'Accept-Language': 'en-US,en;q=0.9',
    }
    
    for page in range(1, max_pages + 1):
        url = f"https://www.pornhub.com/video/search?search={query}&page={page}"
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code != 200 or 'captcha' in response.text.lower():
            break

        soup = BeautifulSoup(response.content, 'html.parser')
        # Try multiple selectors for reliability
        videos = soup.select('.pcVideoListItem') or soup.select('li.videoBox')

        if not videos:
            break

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
                    "source": "pornhub"
                })
            except Exception as e:
                # Optional: print(e)
                continue

    return results
