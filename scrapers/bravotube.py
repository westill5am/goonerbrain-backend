import requests
from bs4 import BeautifulSoup

def scrape_bravotube(query):
    results = []
    # Simulated fixed logic
    results.append({
        "title": f"bravotube Result for '{{query}}'",
        "url": "https://site.com",
        "preview": "https://via.placeholder.com/300x160",
        "source": "bravotube"
    })
    return results
