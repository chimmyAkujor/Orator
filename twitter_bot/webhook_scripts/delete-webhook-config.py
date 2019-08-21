import os
import requests
from requests_oauthlib import OAuth1

CONSUMER_KEY = os.environ.get('TWITTER_CONSUMER_KEY')
CONSUMER_SECRET = os.environ.get('TWITTER_CONSUMER_SECRET')
ACCESS_KEY = os.environ.get('TWITTER_ACCESS_TOKEN')
ACCESS_SECRET = os.environ.get('TWITTER_ACCESS_TOKEN_SECRET')


url = "https://api.twitter.com/1.1/account_activity/all/prod/webhooks.json"

auth = OAuth1(CONSUMER_KEY, CONSUMER_SECRET,ACCESS_KEY, ACCESS_SECRET)

response = requests.get(url,auth=auth)
webhook_id = response.json()[0]['id']

url = "https://api.twitter.com/1.1/account_activity/all/prod/webhooks/" + webhook_id + ".json"
response = requests.delete(url,auth=auth)

print(response.text)