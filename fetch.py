import base64
import requests
from requests_oauthlib import OAuth1Session
import yaml

with open('auth.yml', 'r') as fp:
  auth = yaml.load(fp, Loader=yaml.SafeLoader)

CK = auth['consumer_api_key']
CS = auth['consumer_secret_key']
AT = auth['access_token']
AS = auth['access_token_secret']

twitter = OAuth1Session(CK, CS, AT, AS)

api_url = 'https://api.twitter.com/1.1/favorites/list.json'

r = twitter.get(api_url)

with open('out.json', 'w') as fp:
  fp.write(r.text)

