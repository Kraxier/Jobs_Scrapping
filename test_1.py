
# Website i can Try: https://ph.jora.com/ 
r'''
I think this site is a Third Party Man Website Because it Stated that It comes from the Other Website But this is a Good Practice Site for me 
'''

# from playwright.sync_api import sync_playwright

# with sync_playwright() as p:
#     browser = p.chromium.launch(headless=False)
#     page = browser.new_page()
#     page.goto("https://example.com")
#     print(page.title())
#     browser.close()


# Trying the Simple BS4 and Request 
# import requests
# from bs4 import BeautifulSoup

# url = "https://ph.jora.com/j?sp=homepage&trigger_source=homepage&q=Mechatronics&l="
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:119.0) Gecko/20100101 Firefox/119.0',
#     'Accept-Language': 'en-US,en;q=0.9',
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
#     'Referer': 'https://ph.jora.com/',
#     'Connection': 'keep-alive',
# }

# session = requests.Session()
# response = session.get(url, headers=headers)

# if response.status_code == 200:
#     soup = BeautifulSoup(response.text, 'html.parser')
#     title = soup.find('h1', class_='search-results-title')
#     if title:
#         print("Search result heading:", title.get_text(strip=True))
#     else:
#         print("Search result heading not found.")
# else:
#     print(f"Failed to fetch page. Status code: {response.status_code}")


# Results: Failed to fetch page. Status code: 403 "🚫 The server understood your request, but refuses to authorize it."

from playwright.sync_api import sync_playwright

def scrape_jora_title():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        url = "https://ph.jora.com/j?sp=homepage&trigger_source=homepage&q=Mechatronics&l="
        page.goto(url, timeout=60000)

        # Wait until the title tag is present
        page.wait_for_load_state('domcontentloaded')

        # Extract the title tag content
        page_title = page.title()

        print("Page Title:", page_title)

        input()
        browser.close()

if __name__ == "__main__":
    scrape_jora_title()

# Finally it's working 


r'''

Understanding Why BS4 and Request Didn't Work while the playwright work 

    context = browser.new_context(
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
        viewport={"width": 1280, "height": 800},
        locale="en-US"
    )

🔴 Why requests + BeautifulSoup Didn't Work
Jora uses JavaScript to render content:

When you use requests, you're only downloading the raw HTML of the page.

Many modern websites (like Jora) render job listings, counts, and even headers dynamically using JavaScript after the page loads.

requests can’t execute JavaScript — so you're missing most of the actual content.

Bot protection and 403 Forbidden:

Jora likely uses Cloudflare or similar tools to block bots.

It checks for things like:

Real browser behavior

JavaScript execution

Valid cookies, sessions, or even mouse movement

requests is easily fingerprinted as a bot.

from this i think it is the 403 Method 


'''