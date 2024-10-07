# web_scrape.py

import requests
from bs4 import BeautifulSoup

print("\n=== Web Scraping ===")
url = 'https://www.realtor.ca/real-estate/27402693/369-rosegate-way-oakville-uptown-core-uptown-core'

# Set headers to mimic a browser request
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Look for <h1> elements
    titles = soup.find_all('h1')
    if titles:
        for title in titles:
            print(title.get_text())
    else:
        print("No <h1> titles found.")
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
