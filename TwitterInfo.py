#!/usr/bin/env python


import tweepy
from tweepy import *
from tweepy import OAuthHandler
import time
import os

# fill in values with your own keys - dev.twitter.com
CONSUMER_KEY = 'value'
CONSUMER_SECRET = 'value'
ACCESS_KEY = 'value'
ACCESS_SECRET = 'value'

auth = OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
api = tweepy.API(auth)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

# Array of twitter IDs. Fill in the actual user IDs
ids = []

for i in ids:
    user = api.get_user(i)
    uid = user.id
    screen = user.screen_name.encode("utf-8")
    desc = user.description.encode("utf-8")
    followcount = user.followers_count
    statuscount = user.statuses_count
    url = user.url
    if user.protected:
        protected = "protected"
    elif not user.protected:
        protected = "not protected"
    created = user.created_at
    location = user.location.encode("utf-8")
    lang = user.lang
    with open("results.txt", "a") as outfile:
        outfile.write(str(uid)+",,"+str(screen)+",,"+str(desc)+",,"+str(followcount)+",,"+str(statuscount)+",,"+str(url)+",,"+str(protected)+",,"+str(created)+",,"+str(location)+",,"+str(lang)+"\n")
    continue
