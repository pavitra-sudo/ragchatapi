import requests
from bs4 import BeautifulSoup


def scrape_url(url:str) -> str:
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}
        response = requests.get(url, headers=headers, timeout=30)  # Set a timeout for the request
        response.raise_for_status()  # Check if the request was successful
        soup = BeautifulSoup(response.text, 'html.parser')
        
        for tag in soup(['script', 'style']):
            tag.decompose()  # Remove script and style elements
            
        return soup.get_text(separator=' ', strip=True)  # Get text with spaces and remove leading/trailing whitespace
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return ""