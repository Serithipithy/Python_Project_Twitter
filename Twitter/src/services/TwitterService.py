from src.configure.connection import *


class TwitterService:
    api = None
    searched_tweets = None
    content = None

    def __init__(self):
        self.api = auth_twitter()

    def search(self, query: str, max_tweets: int):
        self.max_tweets=max_tweets
        self.searched_tweets = tweepy.Cursor(self.api.search_tweets,
                                             q=query,
                                             result_type="recent",
                                             count=max_tweets)

    def get_content(self):
        for tweet in self.searched_tweets.items(self.max_tweets):
            # print(tweet.text)
            print(tweet.coordinates)
