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


🟢 1. Government-Sanctioned Portal (Recommended)
PhilJobNet (philjobnet.gov.ph)

Status: Official PH government platform under the Department of Labor and Employment (DOLE). Explicitly encourages public access to job data for employment matching 9.

Scraping Permissions:

Free public access to job listings, employer details, and labor market information.

No prohibitions against automated data collection in ToS (unlike commercial sites).

Designed as a national "one-stop shop" for job data 9.

Data Fields: Job titles, companies, locations, posting dates, employment types, application URLs.

⚠️ 2. Free Job Boards with Implied Consent
These sites host publicly posted jobs but lack explicit scraping policies. Proceed cautiously:

Jora Philippines (jora.com/ph): Aggregates jobs from multiple sources; lightweight interface 6.

Pinoy Jobs: Local job board emphasizing "safe hiring," likely tolerant of non-invasive scraping 6.

GradPhilippines: Targets students/graduates; job data is publicly listed for applicants 6.

Bossjob: Focuses on job matching; public listings suggest permissive use 6.
Guidelines:

Check robots.txt (e.g., User-agent: * allows scraping).

Avoid high-frequency requests to prevent server strain.
'''



# Website i can Try: https://ph.jora.com/ 
r'''
I think this site is a Third Party Man Website Because it Stated that It comes from the Other Website But this is a Good Practice Site for me 
'''

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://example.com")
    print(page.title())
    browser.close()
