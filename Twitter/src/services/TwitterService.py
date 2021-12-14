import json

from src.configure.connection import *

from src.services.GoogleMapsService import get_coordinates


def generate_json(tweets):
    with open('./data/tweets_info.json', 'w') as f:
        json.dump(tweets, f, indent=3)


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
        tweets = {"info": []}
        for tweet in self.searched_tweets.items(self.max_tweets):
            if tweet.coordinates is not None:
                coordinates = tweet.coordinates["coordinates"]
            elif tweet.place is not None:
                coordinates = tweet.place.bounding_box.coordinates[0][0]
            elif tweet.author.location is not None:
                coordinates = get_coordinates(tweet.author.location)
            else:
                coordinates = [0, 0]
            content = {
                "text": tweet.text,
                "author": tweet.author.name,
                "coordinates": coordinates,
                "date": {
                    "day": tweet.created_at.day,
                    "month": tweet.created_at.month,
                    "year": tweet.created_at.year
                }
            }

            tweets["info"].append(content)
        generate_json(tweets)
