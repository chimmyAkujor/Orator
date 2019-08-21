import os
import requests
from requests_oauthlib import OAuth1

CONSUMER_KEY = os.environ.get('TWITTER_CONSUMER_KEY')
CONSUMER_SECRET = os.environ.get('TWITTER_CONSUMER_SECRET')
ACCESS_KEY = os.environ.get('TWITTER_ACCESS_TOKEN')
ACCESS_SECRET = os.environ.get('TWITTER_ACCESS_TOKEN_SECRET')


url = "https://api.twitter.com/1.1/account_activity/all/prod/webhooks.json"

auth = OAuth1(CONSUMER_KEY, CONSUMER_SECRET,ACCESS_KEY, ACCESS_SECRET)

payload = {'url':'https://62ce9fb5.ngrok.io/webhook/twitter'}

response = requests.post(url,auth=auth,params = payload)

print(response.text)