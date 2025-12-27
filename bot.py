import tweepy
import requests
import time
import os

BEARER_TOKEN = os.getenv("AAAAAAAAAAAAAAAAAAAAAMca6gEAAAAAhJQV2HHkZFJFDGxAhvm4e2H3mZI%3DSxoDYeFJkEU4ZIL2hcpeaJUVBXojsP2xE43uTCtk9IyGj2bnbA")
TELEGRAM_TOKEN = os.getenv("8335203413:AAHZyXYQeZAWEBahsGGIhMzKfaVZ0xA6ByY")
CHAT_ID = os.getenv("151444038")

KEYWORDS = [
    "I need a thumbnail maker",
    "I need thumbnails",
    "looking for a thumbnail designer",
    "need youtube thumbnails",
    "need someone to make thumbnails",
    "je cherche un miniamaker",
    "cherche miniamaker",
    "besoin d’un miniamaker",
    "j’ai besoin d’un miniamaker",
    "miniamaker disponible ?",
]

def send_telegram_alert(message):
    url = f"https://api.telegram.org/bot{8335203413:AAHZyXYQeZAWEBahsGGIhMzKfaVZ0xA6ByY}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": message,
        "disable_web_page_preview": True
    }
    requests.post(url, data=data)

client = tweepy.Client(bearer_token=BEARER_TOKEN)
seen_tweets = set()

while True:
    try:
        query = " OR ".join(f'"{k}"' for k in KEYWORDS)
        query += " -is:retweet -is:reply lang:en"

        response = client.search_recent_tweets(
            query=query,
            max_results=10
        )

        if response.data:
            for tweet in response.data:
                if tweet.id in seen_tweets:
                    continue

                seen_tweets.add(tweet.id)

                message = (
                    "🚨 CLIENT POTENTIEL 🚨\n\n"
                    f"{tweet.text}\n\n"
                    f"https://twitter.com/i/web/status/{tweet.id}"
                )

                send_telegram_alert(message)

        time.sleep(60)

    except Exception as e:
        print("Erreur :", e)
        time.sleep(60)
