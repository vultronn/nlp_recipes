#%%
# import nltk 
# import spacy
# #%%
# !pip install tweepy
# # %%
# nltk.download()
# spacy.load('en')

# %%
import numpy as np
import tweepy
import json
import pandas as pd
from tweepy import OAuthHandler

#%%
# credentials

consumer_key = "VczHo4q1Wmzry59sdeJtKPWxC"
consumer_secret = "StvLf2f8DRMehOmpimKyrI9oZgcfkYAZzs2F5p5uKVItRfJoOB"
access_token = "1136763472384069632-aKpagfplOTCJgRSCjBUgxnqLRbn6LK"
access_token_secret = "JkkUutf659EydO5I5kYQqvdOPRPw3xqwBWzPgqbXWOWeT"

# calling API

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
# %%
# Provide the query you want to pull the data. For example, pulling data for the mobile phone ABC

query ="ABC"

# Fetching tweets

Tweets = api.search(query, count = 10,lang='en',exclude='retweets',tweet_mode='extended')
# %%
