# scrapers/milftzy.py

import requests
from bs4 import BeautifulSoup

def scrape_milftzy(query: str, mode: str, page: int):
    """
    Scrape Milftzy search results.

    Args:
      query: the search term
      mode: one of "straight", "gay", "trans" (ignore for Milftzy)
      page: page number (1-based)

    Returns:
      A list of dicts, each with keys: title, url, preview, source
    """
    base_url = "https://milftzy.com"
    # Milftzy uses a URL like /search/<term>/?page=<n>
    search_url = f"{base_url}/search/{requests.utils.quote(query)}/?page={page}"

    headers = {
        "User-Agent": "Mozilla/5.0 (compatible; GoonerBrain/1.0; +https://goonerbrain.com)"
    }
    resp = requests.get(search_url, headers=headers, timeout=10)
    resp.raise_for_status()

    soup = BeautifulSoup(resp.text, "html.parser")
    results = []

    # Each result on Milftzy is wrapped in an element with class "video-item"
    for card in soup.select(".video-item"):
        # title link
        a = card.select_one("a.thumb")
        href = a["href"]
        # make a full URL
        url = href if href.startswith("http") else base_url + href

        # thumbnail image
        img = a.select_one("img")
        preview = img["src"]
        preview = preview if preview.startswith("http") else base_url + preview

        # title text
        title_el = card.select_one(".video-title")
        title = title_el.text.strip() if title_el else "Milftzy Video"

        results.append({
            "title": title,
            "url": url,
            "preview": preview,
            "source": "Milftzy"
        })

    return results
