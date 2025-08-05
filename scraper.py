import requests
import trafilatura
from newspaper import Article

def extract_article_text(url):
    # Try newspaper3k first
    try:
        article = Article(url)
        article.download()
        article.parse()
        if article.text.strip():
            return article.text
    except:
        pass

    # If newspaper fails, fallback to trafilatura
    try:
        downloaded = trafilatura.fetch_url(url)
        if downloaded:
            extracted = trafilatura.extract(downloaded, include_comments=False, include_tables=False)
            if extracted:
                return extracted
    except:
        pass

    return None  # final fallback
