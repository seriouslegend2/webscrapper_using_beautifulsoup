import requests
from bs4 import BeautifulSoup
import time

url = 'https://www.amazon.in/s?k=iphone&crid=2U8YUNE0U4H9S&sprefix=iphon%2Caps%2C343&ref=nb_sb_noss_2'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
}

def fetch_page(url, headers, retries=3):
    session = requests.Session()
    for _ in range(retries):
        response = session.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        elif response.status_code == 503:
            print("Server unavailable (503). Retrying...")
            time.sleep(3)  # Wait before retrying
        else:
            print(f"Failed to retrieve the page. Status code: {response.status_code}")
            return None
    return None

page_content = fetch_page(url, headers)
if page_content:
    soup = BeautifulSoup(page_content, 'html.parser')

    # Debugging: Print part of the HTML content to check the structure
    print("Soup content:", soup.prettify()[:1000])  # Print the first 1000 characters for inspection

    # Update selectors based on the current HTML structure
    spans = soup.select("span.a-size-medium.a-color-base.a-text-normal")
    prices = soup.select("span.a-price-whole")

    print("Product Names:")
    for span in spans:
        print(span.get_text(strip=True))

    print("\nProduct Prices:")
    for price in prices:
        print(price.get_text(strip=True))
else:
    print("Failed to retrieve the page after multiple attempts.")
