import os
import sys
import tweepy

TWITTER_FOLLOWER_FILE = "FRIENDS.txt"

global isFileEmpty


def checkFile(tweeter: tweepy.API):
    global isFileEmpty
    try:
        isFileEmpty = os.stat(TWITTER_FOLLOWER_FILE).st_size == 0
        print("read file here")
    except OSError:
        print("Twitter file not found.Creating " + TWITTER_FOLLOWER_FILE + ". Make sure to edit it.\n")
        consumerFileWrite = open(TWITTER_FOLLOWER_FILE, "w")
        consumerFileWrite.close()
        populateTwitterFile(tweeter)


def populateTwitterFile(tweeter: tweepy.API):
    followers = tweeter.get_friends()
    textToWrite = ''
    for account in followers:
        textToWrite += account.screen_name + '\n' + str(account.id) + '\n'
        textToWrite += "Replace with Discord Webhook URL. New line for every new webhook.\n"
        textToWrite += "END\n"
    consumerFileWrite = open(TWITTER_FOLLOWER_FILE, "a")
    consumerFileWrite.write(textToWrite)
    consumerFileWrite.close()
    sys.exit("Edit the generated file. Instructions are in the README text file.")
