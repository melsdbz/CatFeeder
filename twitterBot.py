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

    tweet = email+" fed gigi at "+date_time
    status = api.update_status(tweet, media_ids=[media.media_id])

if __name__ == "__main__":
    tweetPlz()