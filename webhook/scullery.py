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


def getMotivationalQuote():
    url = "https://quotable-quotes.p.rapidapi.com/randomQuotes"
    headers = {'X-RapidAPI-Host':"quotable-quotes.p.rapidapi.com",
                'X-RapidAPI-Key':RAPID_API_KEY,
                'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36',
                }
    response=requests.get(url, headers=headers).json()
    return str(response['quote']+' - '+response['author'])

def getStarWarsQuote():
    url = 'http://swquotesapi.digitaljedi.dk/api/SWQuote/RandomStarWarsQuote'
    reponse = requests.get(url).json()
    return str(reponse['starWarsQuote'])

def getGotQuote():
    url = 'https://got-quotes.herokuapp.com/quotes'
    reponse = requests.get(url).json()
    return str(reponse['quote']+' - '+reponse['character'])

def getYeQuote():
    url = 'https://api.kanye.rest/'
    reponse = requests.get(url).json()
    return str(reponse['quote']+' - Kanye')

def inspiredFactory(mention, mentionId):
    if '#motivate' in mention.lower():
        quote = getMotivationalQuote()
        api.update_status(quote,in_reply_to_status_id=mentionId,auto_populate_reply_metadata=True)
        print('reply successful')
        
    if '#starwars' in mention.lower():
        quote = getStarWarsQuote()
        api.update_status(quote,in_reply_to_status_id=mentionId,auto_populate_reply_metadata=True)
        print('reply successful')

    if '#got' in mention.lower():
        quote = getGotQuote()
        api.update_status(quote,in_reply_to_status_id=mentionId,auto_populate_reply_metadata=True)
        print('reply successful')

    if '#kanye' in mention.lower():
        quote = getYeQuote()
        api.update_status(quote,in_reply_to_status_id=mentionId,auto_populate_reply_metadata=True)
        print('reply successful')
