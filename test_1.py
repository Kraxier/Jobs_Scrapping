r'''
Research on 
    How to Not get Blocked just By Starting the Project?
    How Can Website Notice my Script?

Reading the Term and Condition in Jobstreet.ph is very not good 



Breaking the TOS 
Breaking a website's Terms of Service (ToS) for web scraping—even if the data is public—carries legal, ethical, and technical risks. Here’s a clear breakdown:

1. Legal Risks
Violation of ToS: If a website explicitly forbids scraping in its ToS (e.g., "automated data collection is prohibited"), scraping violates a binding contract. Courts in the US and EU have ruled this can lead to lawsuits (e.g., hiQ Labs v. LinkedIn had mixed outcomes).

Copyright/Database Laws: Public data ≠ free to scrape. Compilations of data may be protected (e.g., EU’s Database Directive). Copying entire datasets could infringe copyright.

CFAA (US): Bypassing technical barriers (e.g., login walls) may be deemed "unauthorized access," risking federal charges under the Computer Fraud and Abuse Act.

2. Ethical Concerns
Server Impact: Scraping can overload servers, harming the site for other users.

Privacy: "Public" data (e.g., social media posts) might still have ethical privacy boundaries.

Fairness: If the site offers a paid API, scraping undermines their business model.

3. When "Public Data" Isn’t a Free Pass
Robots.txt/ToS: Ignoring these signals is unethical and may escalate to legal action.

Jurisdiction: Laws vary (e.g., GDPR in Europe restricts scraping personal data, even if public).

Precedent: Courts increasingly side with websites (e.g., Facebook v. Power Ventures).

Safer Alternatives ✅
Respect ToS/robots.txt: Check both before scraping.

Use Official APIs: Always prefer sanctioned methods (e.g., Twitter/X API).

Request Permission: Contact the site for written consent.

Public Datasets: Use government portals (data.gov), academic repositories, or licensed datasets.

Limit Scale/Aggression: Avoid disrupting services; use rate limiting.

Bottom Line
"Public" doesn’t mean "unregulated." While some cases (e.g., non-commercial research) may have fair-use arguments, violating ToS remains risky. Consult a lawyer for critical projects. When in doubt: prioritize ethics, legality, and transparency.

Note: This is not legal advice. Laws evolve—always seek expert counsel.
'''


from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://example.com")
    print(page.title())
    browser.close()
