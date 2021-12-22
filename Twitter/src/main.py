import webbrowser

from src.services.MapGeneratorService import generate_map
from src.services.TwitterService import *

if __name__ == '__main__':
    hashtag = "#" + input("Please enter a hashtag you wanna see: ")
    nr_tweets = int(input("How many tweets would you like to see? "))

    tw_service = TwitterService()
    print("Wait while the data is processed, it might take a few moments...")

    tw_service.search(hashtag, nr_tweets)
    tw_service.get_content()
    generate_map()

    webbrowser.open("file:///E:/alexa/GitHubRepos/Python_Project_Twitter/Twitter/data/tweets_map.html", new=2)
