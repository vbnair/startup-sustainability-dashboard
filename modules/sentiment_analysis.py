import requests
from transformers import pipeline
from time import sleep

def fetch_latest_headline(startup, api_key):
    url = "https://newsapi.org/v2/everything"
    params = {"q": startup, "apiKey": api_key, "language": "en", "sortBy": "publishedAt", "pageSize": 1}
    try:
        response = requests.get(url, params=params)
        if response.status_code != 200:
            return None
        data = response.json()
        if "articles" in data and data["articles"]:
            return data["articles"][0]["title"]
        return None
    except Exception:
        return None

def run_sentiment_analysis(df, api_key):
    sentiment_model = pipeline("sentiment-analysis")
    headlines, sentiments = [], []
    print("\nFetching headlines and running sentiment analysis...")
    for startup in df['Startup']:
        print(f"Processing: {startup}")
        headline = fetch_latest_headline(startup, api_key)
        if headline:
            sentiment = sentiment_model(headline)[0]['label']
        else:
            sentiment = "Not Available"
        headlines.append(headline if headline else "No recent news found")
        sentiments.append(sentiment)
        sleep(1)  # avoid API rate limit
    df['Latest Headline'] = headlines
    df['Media Sentiment'] = sentiments
    return df
