import requests
from bs4 import BeautifulSoup

def scrape_porndoe(query, mode="straight", page=1):
    results = []
    if mode == "gay":
        query = f"gay {query}"
    elif mode == "trans":
        query = f"trans {query}"

    url = f"https://www.porndoe.com/search/videos/{query}/page/{page}/"
    headers = {'User-Agent': 'Mozilla/5.0'}
    try:
        r = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(r.content, "html.parser")

        for vid in soup.select("div.video-item"):
            try:
                a = vid.select_one("a[href]")
                img = vid.select_one("img")

                title = a.get('title') or a.text.strip()
                video_url = "https://www.porndoe.com" + a['href']
                preview = img.get("src") or img.get("data-src") or ""

                if not preview or "placeholder" in preview:
                    continue

                results.append({
                    "title": title.strip(),
                    "url": video_url,
                    "preview": preview.strip(),
                    "source": f"Porndoe ({mode})"
                })
            except:
                continue
    except Exception as e:
        print(f"[Porndoe] Error: {e}")
    return results
