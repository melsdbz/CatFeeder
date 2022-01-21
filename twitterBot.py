import tweepy
import os
from dotenv import load_dotenv

#dotenv for environmental variables
load_dotenv()

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

    tweet = email+" fed gigi his tiny snack"
    status = api.update_status(status=tweet, media_ids=[media.media_id])

