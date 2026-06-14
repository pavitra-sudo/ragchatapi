from app.rag import ingest_text, chat_with_context
from app.scraper import scrape_url

def main():
    print("Scraping...")
    text = scrape_url("https://example.com")
    print(f"Scraped {len(text)} characters.")
    
    print("Ingesting...")
    ingest_text(text)
    print("Ingested.")
    
    print("Chatting...")
    ans = chat_with_context("What domain is this for?")
    print(f"Answer: {ans}")

if __name__ == "__main__":
    main()
