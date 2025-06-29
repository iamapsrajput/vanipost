# run_pipeline.py
from news_fetcher.fetch_news import fetch_top_headlines
from tweet_generator.generate_tweet import generate_tweet

if __name__ == "__main__":
    headlines = fetch_top_headlines(country="us", category="technology")
    if not headlines:
        print("No headlines fetched.")
    else:
        for i, headline in enumerate(headlines, 1):
            tweet = generate_tweet(headline)
            print(f"\nHeadline {i}: {headline}\nGenerated Tweet: {tweet}\n")
