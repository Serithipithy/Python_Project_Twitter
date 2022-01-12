"""Connection

This script gives the access to the Twitter API

This file can also be imported as a module and contains the following
functions:

    * auth_twitter - authenticates to the Twitter API
"""
import tweepy

from src.configure.__all__ import *


def auth_twitter():
    """
    Authenticates to the Twitter API

    :return: API | None
    """
    try:
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

        api = tweepy.API(auth, wait_on_rate_limit=True)

        # print("Authentication Succesfull")
        return api
    except KeyError :
        print("Error: Authentication Failed")
        return None
