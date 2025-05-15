import requests
from bs4 import BeautifulSoup

def scrape_youporn(query, mode="straight", page=1):
    results = []
    if mode == "gay":
        query = f"gay {query}"
    elif mode == "trans":
        query = f"trans {query}"

    url = f"https://www.youporn.com/results/?search={query}&page={page}"
    headers = {'User-Agent': 'Mozilla/5.0'}

    try:
        r = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(r.content, "html.parser")

        for video in soup.select("div.video-box"):
            try:
                a = video.select_one("a.video-box-image")
                if not a or not a.has_attr("href"):
                    continue

                video_url = "https://www.youporn.com" + a['href']
                title = a.get("title") or video.select_one("div.ellipsis").text.strip()
                img = a.select_one("img")
                preview = img.get("src") or img.get("data-src") or ""

                if not preview or "placeholder" in preview:
                    continue

                results.append({
                    "title": title.strip(),
                    "url": video_url,
                    "preview": preview.strip(),
                    "source": f"YouPorn ({mode})"
                })
            except:
                continue
    except Exception as e:
        print(f"[YouPorn] Error: {e}")
    return results
