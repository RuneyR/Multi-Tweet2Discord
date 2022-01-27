import tweepy
import time

from urllib3.exceptions import ProtocolError

import Queue

Que_Thread = None


class twitterStream:
    def __init__(self, twitterFriendDict: dict, thread: Queue, cons_key: str, cons_sec: str, access_key: str,
                 access_sec: str):
        self.twitterFriendDict = twitterFriendDict
        self.cK = cons_key
        self.cS = cons_sec
        self.aK = access_key
        self.aS = access_sec
        self.stream = None
        global Que_Thread
        Que_Thread = thread

    def listen(self):
        self.stream = MyStreamListener(self.cK, self.cS, self.aK, self.aS)
        while True:
            try:
                myList = list(self.twitterFriendDict.keys())
                self.stream.filter(follow=myList, stall_warnings=True)

            except (ProtocolError, AttributeError):
                print(time.ctime() + ": Lib probably crashed, restarting now")
                continue

            except Exception as e:
                print(e)
                print(time.ctime() + ": Something went wrong.")
                time.sleep(10)
                continue


class MyStreamListener(tweepy.Stream):
    def on_status(self, status):
        Que_Thread.statusQueue.put(status)

    def on_limit(self, track):
        print("Being rate limited. Standby...")
        time.sleep(10)
        return True
