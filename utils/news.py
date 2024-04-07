import requests
import pyttsx3

engine = pyttsx3.init()


def get_news(api_key, category='general', country='in'):
    # News API endpoint URL
    endpoint = 'https://newsapi.org/v2/top-headlines'

    # Parameters for the API request
    params = {
        'country': country,
        'category': category,
        'apiKey': api_key,
    }

    try:
        # Make the API request
        news = requests.get(endpoint, params=params)
        data = news.json()

        # Check if the request was successful
        if news.status_code == 200:
            articles = data.get('articles', [])
            for news, article in enumerate(articles, start=1):
                engine.say(f"\n{news}. {article['title']}")
                engine.runAndWait()
                engine.say(f"   {article['description']}")
                engine.runAndWait()
        else:
            print(f"Error {news.status_code}: {data.get('message', 'Unknown error')}")
    except Exception as e:
        print(f"An error occurred: {e}")
