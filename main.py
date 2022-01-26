import tweepy

import KeysTokens as tokenRead
from TweepyAPI import TweepyAPI
import TwitterFollowers as TF

consumer_key, consumer_secret, access_key, access_secret = None, None, None, None
tweeter = None


def assign_keys():
    global consumer_key, consumer_secret, access_key, access_secret
    tokenRead.check_files()
    our_keys = tokenRead.get_api_variables()
    consumer_key = our_keys[1]
    consumer_secret = our_keys[3]
    our_keys = tokenRead.get_access_variables()
    access_key = our_keys[1]
    access_secret = our_keys[3]


def authorize():
    callAPI = TweepyAPI(consumer_key, consumer_secret, access_key, access_secret)
    global tweeter
    tweeter = callAPI.authorize()


if __name__ == '__main__':
    assign_keys()
    authorize()
    TF.checkFile(tweeter)

