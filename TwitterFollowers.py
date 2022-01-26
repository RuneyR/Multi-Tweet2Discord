import os
import sys
import tweepy

TWITTER_FOLLOWER_FILE = "FRIENDS.txt"

global isFileEmpty


def checkFile(tweeter: tweepy.API):
    global isFileEmpty
    try:
        isFileEmpty = os.stat(TWITTER_FOLLOWER_FILE).st_size == 0
        contents = readFile()
        print(setStage(contents))
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


# Iterate throughout the Friend.txt in a specific order. Add the username as a key, and a LIST of discord webhooks as
# its value. Since python sets are referenced, make a unique copy at key assignment so its value are assigned properly.
def setStage(contents):
    cursor = 0
    userDict = dict()
    key = ''
    value = set()
    try:
        while cursor < len(contents):
            key = contents[cursor]
            cursor += 2
            while contents[cursor] != "END":
                value.add(contents[cursor])
                cursor += 1
            userDict[key] = value.copy()
            key = ''
            value.clear()
            cursor += 1
    except IndexError:
        return userDict
    return userDict


def readFile():
    cfr = open(TWITTER_FOLLOWER_FILE, "r")
    ck = cfr.read().split("\n")
    cfr.close()
    return ck
