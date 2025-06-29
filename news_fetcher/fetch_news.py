# fetch_news.py
import requests
import os
from dotenv import load_dotenv

load_dotenv()

NEWS_API_KEY = os.getenv("NEWS_API_KEY")
NEWS_ENDPOINT = "https://newsapi.org/v2/top-headlines"


def fetch_top_headlines(country=None, category=None, limit=5):
    params = {
        "apiKey": NEWS_API_KEY,
        "pageSize": limit,
    }
    if country:
        params["country"] = country
    if category:
        params["category"] = category

    response = requests.get(NEWS_ENDPOINT, params=params)
    if response.status_code == 200:
        data = response.json()
        return [article["title"] for article in data.get("articles", [])]
    else:
        print("News fetch error:", response.status_code, response.text)
        return []


if __name__ == "__main__":
    headlines = fetch_top_headlines(country="us", category="technology")
    for i, headline in enumerate(headlines, 1):
        print(f"{i}. {headline}")
