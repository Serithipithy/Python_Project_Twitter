import json

from src.configure.connection import *

from src.services.GoogleMapsService import get_coordinates


def generate_json(tweets):
    """
    Generate the json file

    Parameters
    ----------
    :param tweets:
         The list that will be converted into a json file
     :type tweets: list

     :return: None
    """
    with open('./data/tweets_info.json', 'w') as f:
        json.dump(tweets, f, indent=3)


class TwitterService:
    """
    A class used to represent the service for Twitter

    ...

    Attributes
    ----------
    api :
        an instance of API class from tweepy
    searched_tweets : str
        the tweets retrieved from the Twitter API
    content : list
        the content of tweets needed to be plotted on the map after the searched_tweets is filtered
    max_tweets : int
        the maximum number of tweets

    Methods
    -------
    Constructor:
        Establishes the connection to the Twitter API
    search(query: str, max_tweets: int):
        Searches for the tweets based on a query/word
    get_content():
        Filters the searched_tweets in order to make a json with all the tweets info
    """
    api = None
    searched_tweets = None
    content = None
    max_tweets = None

    def __init__(self):
        self.api = auth_twitter()

    def search(self, query: str, max_tweets: int):
        """
        Searches for the tweets based on a query/word

        Parameters
        ----------
        :param query:
            The word that search will be based on
        :type query: str
        :param max_tweets:
            The maximum number of tweets that will be searched
        :type max_tweets: int

        :return: None
        """
        self.max_tweets = max_tweets
        self.searched_tweets = tweepy.Cursor(self.api.search_tweets,
                                             q=query,
                                             result_type="recent",
                                             count=max_tweets,
                                             include_entities="include_entities")

    def get_content(self):
        """
        Filters the searched_tweets in order to generate a json file with all the tweets info needed.
        """
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
                "id_str": tweet.id_str,
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
