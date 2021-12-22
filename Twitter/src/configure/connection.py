import tweepy

from src.configure.__all__ import *


def auth_twitter():
    try:
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

        api = tweepy.API(auth, wait_on_rate_limit=True)

        # print("Authentification Succesfull")
        return api
    except KeyError :
        print("Error: Authentication Failed")
        return None
