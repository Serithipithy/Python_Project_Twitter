from src.services.TwitterService import *

if __name__ == '__main__':
    tw_service = TwitterService()

    hashtag = "#" + input("Please enter a hashtag you wanna see: ")
    nr_tweets = int(input("How many tweets would you like to see? "))

    tw_service.search(hashtag, nr_tweets)
    tw_service.get_content()
