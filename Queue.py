import threading
import tweepy
import time
import queue

import TwitterFollowers

DEFAULT_WEBHOOK_VALUE_IN_TEXT = TwitterFollowers.REPLACE_WEBHOOK_LINE


# Posts to Discord. The
def discordWebhook(tweet, un, aURL, twitter_dict: dict, id):
    from discord_webhook import DiscordWebhook
    valueInDict = list(twitter_dict.get(id))

    if valueInDict[0] != DEFAULT_WEBHOOK_VALUE_IN_TEXT:
        webhook = DiscordWebhook(url=valueInDict, rate_limit_retry=True, content=tweet, username=un, avatar_url=aURL)
        webhook.execute()
        time.sleep(1)


class Queue:
    def __init__(self, twitter_dict: dict, tweeter: tweepy.API):
        self.twitter_dict = twitter_dict
        self.statusQueue = queue.Queue(maxsize=0)
        self.tweeter = tweeter

    def beginThread(self):
        queueThread = threading.Thread(target=self.checkStatusThenPost)
        queueThread.daemon = True
        queueThread.start()

    def checkStatusThenPost(self):
        currentStatus = None
        is_not_original_tweet = False
        print(self.twitter_dict)
        while True:
            if self.statusQueue.empty():
                time.sleep(5)
            else:
                currentStatus = self.statusQueue.get()
                print(currentStatus.created_at)
                print(currentStatus.user.screen_name)
                print(currentStatus.text)
                print("<<<_______________>>>")
                if hasattr(currentStatus, "retweeted_status") or hasattr(currentStatus, "quoted_status") or currentStatus.in_reply_to_screen_name != None:
                    is_not_original_tweet = True
                # if status.user.id_str == userID and not is_retweet:
                elif not is_not_original_tweet and 'media' in currentStatus.entities:
                    print(currentStatus)
                    discordWebhook('https://twitter.com/twitter/statuses/' + currentStatus.id_str,
                                   currentStatus.user.screen_name, currentStatus.user.profile_image_url,
                                   self.twitter_dict, currentStatus.user.id_str)
                is_not_original_tweet = False
