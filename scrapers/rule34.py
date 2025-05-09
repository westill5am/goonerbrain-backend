import requests
from bs4 import BeautifulSoup

def scrape_rule34(query):
    url = f"https://rule34.xxx/index.php?page=post&s=list&tags={query}"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    
    results = []
    for thumb in soup.select(".thumb > a"):
        img = thumb.find("img")
        if img and img.has_attr("src"):
            results.append({
                "title": f"Rule34 Result for '{query}'",
                "url": "https://rule34.xxx" + thumb["href"],
                "preview": "https:" + img["src"] if img["src"].startswith("//") else img["src"],
                "source": "Rule34"
            })
    return results
