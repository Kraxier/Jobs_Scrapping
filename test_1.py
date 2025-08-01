
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

r'''
If the Website have anti bot protection What is the workflow of things? 
like i don't want to get blocked by Working while testing my script in the website

'''


# Learning to do 🔹Manual Recon or Reconnaissance Phase
r'''
1. Reconnaissance Phase
    Study the Protection:
        * Check robots.txt for allowed/disallowed paths. (Done)
        * Use browser developer tools (Network tab) to analyze:
            * Headers (e.g., User-Agent, Accept-Language, Sec-Fetch-*)
            * Cookies (e.g., __cf_bm for Cloudflare)
            * Dynamic tokens (CSRF, API keys)
            * JavaScript challenges (e.g., Cloudflare 5-second shield)

Identify Triggers:
Rapid requests, missing headers, headless browser signatures, or inconsistent mouse movements.

🧠 1. Understanding the Bot Protection Layers
Most modern anti-bot systems use multiple layers of detection:

a. IP Reputation
    Known bad IPs, VPNs, proxies, and data centers are often blocked.
    Too many requests from a single IP = rate-limiting or banning.
b. User-Agent & Headers Analysis
    Invalid or uncommon headers raise flags.
    Missing headers like Referer, Accept-Language, or User-Agent can be suspicious.
c. JavaScript Challenges
    Some sites require JS to run before granting access (e.g., Cloudflare's browser check).
d. Behavioral Analysis
    Tracks mouse movement, typing speed, scrolls, etc.
    Used heavily on login pages or checkout flows.
e. CAPTCHAs
    Google reCAPTCHA, hCaptcha, or puzzles to test for human interaction.

'''
# Reflection of Things 
r'''
1. Checking for robot.txt files:
    ✅ How to Identify the Location of robots.txt
    Per the Robots Exclusion Protocol(Documentation of Google Search Central), the location of a website’s robots.txt is always:
    https://<domain>/robots.txt
    📌 This file must live in the root of the domain, not in subdirectories.
    * The Documentation for the "Google Search Central"
    https://developers.google.com/search/docs/crawling-indexing/robots/intro

    Inside of https://ph.jora.com/robots.txt
    it Give me This part a Dictionary Term in term of python: 
        1. "User-agent:"
        2. "Disallow:"

    # Right now it give me this part 
    User-agent: *
    Disallow: /click

    # Chatgpt also Include the Sitemap: https://ph.jora.com/sitemap.xml
    i think this is the path of the website

    📌 What This Means:
    User-agent: * – Applies to all crawlers.
    Disallow: /click – Crawlers are not allowed to access any URLs that start with /click.
    Everything else is allowed. (I'm Safe)

    🔍 What's /click?
    This is usually a redirector or tracking endpoint (e.g., when someone clicks a job to go to an external site). You’re not supposed to crawl or scrape this, which is fair because it might mess up their analytics or ad deals.

2. Using the Network Request:
    * Use browser developer tools (Network tab) to analyze:
            * Headers (e.g., User-Agent, Accept-Language, Sec-Fetch-*)
            * Cookies (e.g., __cf_bm for Cloudflare)
            * Dynamic tokens (CSRF, API keys)
            * JavaScript challenges (e.g., Cloudflare 5-second shield)

2.1 Understanding between Real Browser and Incognito Mode 
    
'''