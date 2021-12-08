from src.configure.connection import *
import json


class TwitterService:
    api = None
    searched_tweets = None
    content = None
    max_tweets = None

    def __init__(self):
        self.api = auth_twitter()

    def search(self, query: str, max_tweets: int):
        self.max_tweets = max_tweets
        self.searched_tweets = tweepy.Cursor(self.api.search_tweets,
                                             q=query,
                                             result_type="recent",
                                             count=max_tweets,
                                             include_entities="include_entities")

    def get_content(self):
        tweets = list()
        for tweet in self.searched_tweets.items(self.max_tweets):
            content = {
                "text": tweet.text,
                "author": tweet.author.name,
                "author_location": tweet.author.location,
                "coordinates": tweet.coordinates,
                "place": tweet.place,
                "geo": tweet.geo
            }

            tweets.append(content)
        for line in tweets:
            print(line["author_place"])
