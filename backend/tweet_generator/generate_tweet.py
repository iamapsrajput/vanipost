# generate_tweet.py
import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")


def generate_tweet(headline, style="professional"):
    prompt = f"Write a short, engaging tweet in a {style} tone based on the headline: \n'{headline}'"
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=100,
    )
    return response.choices[0].message.content.strip()


if __name__ == "__main__":
    example = "India announces major reforms in AI policy framework."
    tweet = generate_tweet(example)
    print(tweet)
