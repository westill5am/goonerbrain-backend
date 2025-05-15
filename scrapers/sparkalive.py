# scrapers/sparkalive.py
import requests
from bs4 import BeautifulSoup

def scrape_sparkalive(query: str, mode: str, page: int):
    """
    Scrapes the SparkAlive website for video results based on the search query, mode (straight, gay, trans), and page.
    Returns a list of search results (video title, URL, preview image).
    """
    base_url = "https://sparkalive.com"
    search_url = f"{base_url}/search?q={query}&page={page}&mode={mode}"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    try:
        # Send a GET request to the search URL
        response = requests.get(search_url, headers=headers)
        response.raise_for_status()  # Raise an error if the status code is not 200
        
        # Parse the response HTML
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all video results (adjust the selector based on the actual HTML structure)
        results = []
        video_cards = soup.find_all('div', class_='video-card')  # Example selector; update according to the actual HTML structure
        for card in video_cards:
            title = card.find('h3').text.strip() if card.find('h3') else "No title"
            url = card.find('a')['href'] if card.find('a') else None
            preview_img = card.find('img')['src'] if card.find('img') else None
            
            # Ensure valid URL and preview image
            if url and preview_img:
                results.append({
                    'title': title,
                    'url': base_url + url,  # Ensure the full URL is used
                    'preview': preview_img
                })
        
        return results

    except requests.exceptions.RequestException as e:
        print(f"[ERROR] Failed to fetch data from SparkAlive: {e}")
        return []
