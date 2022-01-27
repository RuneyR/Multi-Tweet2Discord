import tweepy

import KeysTokens as tokenRead
from Queue import Queue
from TweepyAPI import TweepyAPI
import TwitterFollowers as twitFoll
from twitterStream import twitterStream

consumer_key, consumer_secret, access_key, access_secret = None, None, None, None
tweeter = None


# Assign API and Access keys to variables for use.
def assign_keys():
    global consumer_key, consumer_secret, access_key, access_secret
    tokenRead.check_files()
    our_keys = tokenRead.get_api_variables()
    consumer_key = our_keys[1]
    consumer_secret = our_keys[3]
    our_keys = tokenRead.get_access_variables()
    access_key = our_keys[1]
    access_secret = our_keys[3]


# Connect to Twitter, create the API tweeter object.
def authorize():
    callAPI = TweepyAPI(consumer_key, consumer_secret, access_key, access_secret)
    global tweeter
    tweeter = callAPI.authorize()


if __name__ == '__main__':
    assign_keys()
    authorize()
    ourDict = twitFoll.checkFile(tweeter)
    twitterQueue = Queue(ourDict, tweeter)
    twitterQueue.beginThread()
    twStream = twitterStream(ourDict, twitterQueue, consumer_key, consumer_secret, access_key, access_secret)
    twStream.listen()
