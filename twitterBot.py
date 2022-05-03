import tweepy
import os
from dotenv import load_dotenv
import random

#dotenv for environmental variables
load_dotenv()

feed_verb = [" gave ", " fed ", " procured ", " slipped "]
feed_quantity = ["some ", "a bit of ", "a smidge of "]
feed_adjective = ["good ", "tasty ", "scrumptious ", "delightful ", "yummy ", "perfect "]
feed_noun = ["food", "nourishment", "sustenance", "rations", "grub", "fare"]

def tweetPlz(API_KEY, API_KEY_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET, email, date_time, filename):


    auth = tweepy.OAuthHandler(API_KEY,API_KEY_SECRET)

    auth.set_access_token(ACCESS_TOKEN,ACCESS_TOKEN_SECRET)

    api = tweepy.API(auth)

    media = api.media_upload(filename)

    tweet = email+" fed gigi his big meal"
    status = api.update_status(status=tweet, media_ids=[media.media_id])

def tweetPlzSnack(API_KEY, API_KEY_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET, email, date_time, filename):


    auth = tweepy.OAuthHandler(API_KEY,API_KEY_SECRET)

    auth.set_access_token(ACCESS_TOKEN,ACCESS_TOKEN_SECRET)

    api = tweepy.API(auth)

    media = api.media_upload(filename)

    tweet = email + feed_verb[random.randint(0,3)] + "gigi" + feed_quantity[random.randint(0,2)] + feed_adjective[random.randint(0,5)] + feed_noun[random.randint(0,5)]
    status = api.update_status(status=tweet, media_ids=[media.media_id])

