import tweepy
import os
import time
import random
from os import environ
import requests
import urllib

consumer_key = environ['consumer_key']
consumer_secret = environ['consumer_secret']

key = environ['key']
secret = environ['secret']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

api = tweepy.API(auth, wait_on_rate_limit=True)
user = api.me()

j = 0
lines = []
# texts = []
with open('images1.txt') as f:
    lines = f.read().splitlines()


# with open('twttext.txt') as h:
#   texts = h.read().splitlines()
def uploadpictures(pictures, message):
    media_ids = []
    try:
        for i in range(len(pictures)):
            urllib.request.urlretrieve(pictures[i], 'im{}.png'.format(i))
            media_ids.append(api.media_upload('im{}.png'.format(i)).media_id_string)

        api.update_status(status=message, media_ids=media_ids)
    except:
        pass
    for i in range(len(pictures)):
        os.remove('im{}.png'.format(i))


def case_study():
    global j
    # global texts
    global lines
    url = []
    # msg = texts[j]
    msg = ''
    url = lines[j].split()
    uploadpictures(pictures=url, message=msg)
    j = j + 1


def reply():
    global j
    if (j > 242):
        j = 0
    case_study()


while True:
    reply()
    time.sleep(3600)
