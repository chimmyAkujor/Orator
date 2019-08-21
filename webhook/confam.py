import os
import requests
import tweepy

CONSUMER_KEY = os.environ.get('TWITTER_CONSUMER_KEY')
CONSUMER_SECRET = os.environ.get('TWITTER_CONSUMER_SECRET')
ACCESS_KEY = os.environ.get('TWITTER_ACCESS_TOKEN')
ACCESS_SECRET = os.environ.get('TWITTER_ACCESS_TOKEN_SECRET')
RAPID_API_KEY = os.environ.get('RAPID_API_KEY')



auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

print(api.mentions_timeline(count=1))


def getMotivationalQuote():
    url = "https://quotable-quotes.p.rapidapi.com/randomQuotes"
    headers = {'X-RapidAPI-Host':"quotable-quotes.p.rapidapi.com",
                'X-RapidAPI-Key':RAPID_API_KEY,
                'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36',
                }
    response=requests.get(url, headers=headers).json()
    print(str(response['quote']+' - '+response['author']))
    return str(response['quote']+' - '+response['author'])

