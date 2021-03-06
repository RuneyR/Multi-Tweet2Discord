import os
import sys
import tweepy

TWITTER_FOLLOWER_FILE = "FRIENDS.txt"
REPLACE_WEBHOOK_LINE = "Replace with Discord Webhook URL. New line for every new webhook.\n"
global isFileEmpty


def checkFile(tweeter: tweepy.API):
    global isFileEmpty, TWITTER_FOLLOWER_FILE
    try:
        if len(sys.argv) > 1:
            if sys.argv[1] == '--reprint' or sys.argv[1] == '--rp':
                TWITTER_FOLLOWER_FILE = "reprint" + TWITTER_FOLLOWER_FILE
                raise OSError
        isFileEmpty = os.stat(TWITTER_FOLLOWER_FILE).st_size == 0
        contents = readFile()
        return setStage(contents)
    except OSError:
        print("Twitter file not found.Creating " + TWITTER_FOLLOWER_FILE + ". Make sure to edit it.\n")
        consumerFileWrite = open(TWITTER_FOLLOWER_FILE, "w")
        consumerFileWrite.close()
        populateTwitterFile(tweeter)


def populateTwitterFile(tweeter: tweepy.API):
    followers = tweeter.get_friends(count=200)
    textToWrite = ''
    for account in followers:
        textToWrite += account.screen_name + '\n' + str(account.id) + '\n'
        textToWrite += REPLACE_WEBHOOK_LINE
        textToWrite += "END\n"
    consumerFileWrite = open(TWITTER_FOLLOWER_FILE, "a")
    consumerFileWrite.write(textToWrite)
    consumerFileWrite.close()
    sys.exit("Edit the generated file. Instructions are in the README text file.")


# Iterate throughout the Friend.txt in a specific order. Add the userid as a key, and a LIST of discord webhooks as
# its value. Since python sets are referenced, make a unique copy at key assignment so its value are assigned properly.
def setStage(contents):
    cursor = 1
    userDict = dict()
    key = ''
    value = set()
    try:
        while cursor < len(contents):
            key = contents[cursor]
            cursor += 1
            while contents[cursor] != "END":
                value.add(contents[cursor])
                cursor += 1
            userDict[key] = value.copy()
            key = ''
            value.clear()
            cursor += 2
    except IndexError:
        return userDict
    return userDict


def readFile():
    cfr = open(TWITTER_FOLLOWER_FILE, "r")
    ck = cfr.read().split("\n")
    cfr.close()
    return ck
