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
k = 0
lines = []
jump = []
#texts = []
with open('images.txt') as f:
    lines = f.read().splitlines()
with open('imgnum.txt') as g:
    jump = g.read().splitlines()
#with open('twttext.txt') as h:
 #   texts = h.read().splitlines()

def fourpictures(url, message):
    urllib.request.urlretrieve(url[0],'im1.png')
    urllib.request.urlretrieve(url[1],'im2.png')
    urllib.request.urlretrieve(url[2],'im3.png')
    urllib.request.urlretrieve(url[3],'im4.png')
    images = ('im1.png', 'im2.png', 'im3.png', 'im4.png')
    media_ids = [api.media_upload(i).media_id_string for i in images]
    api.update_status(status=message, media_ids=media_ids)
    os.remove('im1.png')
    os.remove('im2.png')
    os.remove('im3.png')
    os.remove('im4.png')

def twopictures(url, message):
    urllib.request.urlretrieve(url[0],'im1.png')
    urllib.request.urlretrieve(url[1],'im2.png')
    images = ('im1.png', 'im2.png')
    media_ids = [api.media_upload(i).media_id_string for i in images]
    api.update_status(status=message, media_ids=media_ids)
    os.remove('im1.png')
    os.remove('im2.png')

def singlepic(url, message):
    filename = 'temp.jpg'
    request = requests.get(url[0], stream=True)
    if request.status_code == 200:
        with open(filename, 'wb') as image:
            for chunk in request:
                image.write(chunk)

        api.update_with_media(filename, status=message)
        os.remove(filename)
    else:
        print("Unable to download image")

def case_study():
    global j
    global k
   # global texts
    global jump
    global lines
    url = []
    b = int(jump[j])
   # msg = texts[j]
    msg = ''
    for i in range(int(jump[j])):
        url.append(lines[k])
        k = k + 1
    if(b == 1):
        singlepic(url,msg)
    elif(b==2):
        twopictures(url,msg)
    elif(b==4):
        fourpictures(url,msg)
    j = j + 1



def reply():
    global j
    global k
    if(j>242):
        k = 0
        j = 0
    case_study()
    for follower in tweepy.Cursor(api.followers).items():
        follower.follow()

while True:
    reply()
    time.sleep(3600)