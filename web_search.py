import requests
from bs4 import BeautifulSoup
import urllib.parse

def search_company_news(company, max_results=3):
    query = f"{company} latest news"
    url = f"https://html.duckduckgo.com/html/?q={urllib.parse.quote(query)}"
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    results = []
    for link in soup.find_all("a", class_="result__a", href=True):
        # DuckDuckGo's real URL is in the "uddg=" query param
        raw = link['href']
        parsed = urllib.parse.urlparse(raw)
        qs = urllib.parse.parse_qs(parsed.query)
        actual_url = qs.get('uddg', [None])[0]
        if actual_url:
            results.append(actual_url)
        if len(results) >= max_results:
            break

    return results
