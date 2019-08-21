import base64
import hashlib
import hmac
import json
import os


def webhook_challenge(crc_token):
  try:
    crc = str(crc_token)
    CONSUMER_SECRET = os.environ.get('TWITTER_CONSUMER_SECRET')
  
    # creates HMAC SHA-256 hash from incomming token and your consumer secret
    cs = bytes(CONSUMER_SECRET,'utf-8')
    message = bytes(crc,'utf-8')
    sha256_hash_digest = hmac.new(cs, msg=message, digestmod=hashlib.sha256).digest()
    
    sha = 'sha256=' + str(base64.b64encode(sha256_hash_digest).decode('utf-8'))
    
    # construct response data with base64 encoded hash
    response = {
      'response_token': sha
    }
    # returns properly formatted json response
    return response
  except ValueError:
    return "crc token missing"