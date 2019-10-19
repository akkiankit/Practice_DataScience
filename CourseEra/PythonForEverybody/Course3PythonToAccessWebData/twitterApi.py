import urllib.request,urllib.error,urllib.parse
import json

import tw


TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

while True:
    print('')
    acct = input("enter twitter account:")

    if len(acct) < 1:
        break
   

