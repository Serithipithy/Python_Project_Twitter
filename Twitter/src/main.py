"""
    The main file of the project

    It gets a hashtag from the user using the console and the number
    maximum number of tweets it wants to be displayed on the map.

    After the map is generated a tab with the it will be open.

"""
import webbrowser

from src.services.MapGeneratorService import generate_map
from src.services.TwitterService import *

if __name__ == '__main__':
    tw_service = TwitterService()
    hashtag = "#" + input("Please enter a hashtag you wanna see: ")
    nr_tweets = int(input("How many tweets would you like to see? "))

    print("Wait while the data is processed, it might take a few moments...")

    tw_service.search(hashtag, nr_tweets)
    tw_service.get_content()
    generate_map()

    webbrowser.open("file:///E:/alexa/GitHubRepos/Python_Project_Twitter/Twitter/data/tweets_map.html", new=2)
