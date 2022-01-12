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
commands = "\tAvailable commands:\n\t\t1.Search for tweets (or add)\n\t\t2.History of hashtags searched in " \
           "chronologic order\n\t\t3.See the commands available\n\t\t4.Quit(or write 'quit')\n "
incorrectInput="Please enter valid input!\n> A hashtag must me a word\n> The number of tweets must be an integer and " \
               "greater than 0 \n"


def isAlreadyAvailable(hashtag, nr_tweets):
    """
    verifies if the map was already made
    :param hashtag:
        The hashtag from the user
    :type hashtag:  str
    :param nr_tweets:
        The maximum number of tweets from the user
    :type nr_tweets: int

    :return: Boolean
    """
    for file in ht_list:
        if file[0] == hashtag and file[1] == nr_tweets:
            return True
    return False


def searchHashtag():
    """
    Asks the user for a hashtag and the maximum number and generates
    the map
    :return: None
    """
    raw_hashtag = input("Your hashtag: ")
    hashtag = "#" + raw_hashtag
    nr_tweets = input("Maximum number of tweets: ")

    if len(raw_hashtag) == 0 or len(nr_tweets) == 0:
        print(incorrectInput)
        searchHashtag()
    nr_tweets = int(nr_tweets)

    if nr_tweets < 1:
        print(incorrectInput)
        searchHashtag()

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

    :return: None
    """
    if len(ht_list) == 0:
        print("No maps generated yet")
    else:
        print("Already generated maps on this sessions:")
        for file in ht_list:
            print(file[0] + " for " + str(file[1]))
        print("If you want to see the map that was at a certain moment in this session, you can simply press 1 and \n"
              "after that, in the input, put again the hashtag and the number corresponding to the one you choose \n"
              "that is already in this list.")


def deleteFiles(path):
    """
        On exit it deletes the html files generated on that session

    :param path: str
        folder path
    :type path: str
    :return: None

    """
    folder = path
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
            deleteFiles('../data')
            deleteFiles('./data')
            break
        else:
            print("Please enter a valid command")
            print(commands)
