"""
    The main file of the project

    It gets a hashtag from the user using the console and the
    maximum number of tweets it wants to be displayed on the map.

    After the map is generated a tab with the it will be open.

    This file contains the following functions:
    * isAlreadyAvailable - verifies if the map was already made
    * searchHashtag - asks the user for a hashtag and the maximum
    number and generates the map
    * displayHashtags - prints the maps that are already generated
    * deleteHTMLS - on exit it deletes the html files generated on
    that session
    * main - the main function
"""
import os
import glob
import shutil
import webbrowser

from src.services.MapGeneratorService import generate_map
from src.services.TwitterService import *

ht_list = list()
commands = "\tAvailable commands:\n\t\t1.Search for tweets\n\t\t2.History of hashtags searched\n\t\t3.See the " \
           "commands available\n\t\t4.Quit(or write 'quit')"


def isAlreadyAvailable(hashtag, nr_tweets):
    """
    verifies if the map was already made
    :param hashtag: str
        The hashtag from the user
    :param nr_tweets: int
        The maximum number of tweets from the user

    :return: True if there is already a map.
            Otherwise it returns False.
    """
    for file in ht_list:
        if file[0] == hashtag and file[1] == nr_tweets:
            return True
    return False


def searchHashtag():
    """
    Asks the user for a hashtag and the maximum number and generates
    the map

    """
    raw_hashtag = input("Please enter a hashtag: ")
    hashtag = "#" + raw_hashtag
    nr_tweets = int(input("How many tweets would you like to see? "))

    if isAlreadyAvailable(raw_hashtag, nr_tweets) is True:
        webbrowser.open(
            f"file:///E:/alexa/GitHubRepos/Python_Project_Twitter/Twitter/data/{raw_hashtag}{nr_tweets}_map.html",
            new=2)
    else:
        print("Wait while the data is processed, it might take a few moments...")

        tw_service.search(hashtag, nr_tweets)
        tw_service.get_content()
        generate_map(raw_hashtag, nr_tweets)

        webbrowser.open(
            f"file:///E:/alexa/GitHubRepos/Python_Project_Twitter/Twitter/data/{raw_hashtag}{nr_tweets}_map.html",
            new=2)
        ht_list.append([raw_hashtag, nr_tweets])


def displayHashtags():
    """
    Prints the maps that are already generated

    """
    if len(ht_list) == 0:
        print("No maps generated yet")
    else:
        print("Already generated maps on this sessions:")
        for file in ht_list:
            print(file[0] + " for " + str(file[1]))


def deleteHTMLS():
    """
    On exit it deletes the html files generated on
    that session

    """
    folder = '../data'
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))


if __name__ == '__main__':
    tw_service = TwitterService()
    print(commands)
    while True:
        user_input = input(">>")
        if user_input == '1':
            searchHashtag()
        elif user_input == '2':
            displayHashtags()
        elif user_input == '3':
            print(commands)
        elif user_input == '4' or user_input == 'quit':
            deleteHTMLS()
            break
        else:
            print("Please enter a valid command")
            print(commands)
