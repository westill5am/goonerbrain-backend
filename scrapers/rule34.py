import requests
from bs4 import BeautifulSoup

def scrape_rule34(query, mode="straight", page=1):
    results = []
    tag = query
    if mode == "gay":
        tag = f"gay {query}"
    elif mode == "trans":
        tag = f"trans {query}"
    url = f"https://rule34.xxx/index.php?page=post&s=list&tags={tag}&pid={(page-1)*42}"
    r = requests.get(url, timeout=10)
    soup = BeautifulSoup(r.content, "html.parser")
    for img in soup.select("span.thumb > a"):
        try:
            href = img['href']
            full_url = f"https://rule34.xxx{href}"
            img_el = img.select_one("img")
            preview = img_el['src'] if img_el else ""
            results.append({
                "title": img_el.get('alt', 'rule34') if img_el else 'rule34',
                "url": full_url,
                "preview": preview,
                "source": f"Rule34 ({mode})"
            })
        except Exception:
            continue
    return results
