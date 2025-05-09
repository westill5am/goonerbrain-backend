import requests
from bs4 import BeautifulSoup

def scrape_youporn(query):
    results = []
    # Simulated fixed logic
    results.append({
        "title": f"youporn Result for '{{query}}'",
        "url": "https://site.com",
        "preview": "https://via.placeholder.com/300x160",
        "source": "youporn"
    })
    return results
