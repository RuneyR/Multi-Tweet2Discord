import threading
import random
import requests.exceptions
import tweepy
import time
import queue
import logging
import TwitterFollowers

DEFAULT_WEBHOOK_VALUE_IN_TEXT = TwitterFollowers.REPLACE_WEBHOOK_LINE
logging.basicConfig(filename='app.log', level=logging.INFO)
chars = '0123456789ABCDEF'


# Posts to Discord. The
def discordWebhook(tweet, un, avatarURL, twitter_dict: dict, twitterID):
    from discord_webhook import DiscordWebhook
    valueInDict = list(twitter_dict.get(twitterID))
    try:
        if valueInDict[0] != DEFAULT_WEBHOOK_VALUE_IN_TEXT or valueInDict[0] != "IGNORE":
            webhook = DiscordWebhook(url=valueInDict, username=un, content=tweet, avatar_url=avatarURL, rate_limit_retry=True)

            webhook.execute()
            time.sleep(1)
    except requests.exceptions.MissingSchema:
        print("Invalid Webhook URL at " + un + "! \n Please update. Setting " + twitterID + " to ignore.")
        twitter_dict.update({twitterID: "IGNORE"})


def printInfo(currentStatus, wasTrunc: bool):
    print(currentStatus.created_at)
    print(currentStatus.user.screen_name)
    if wasTrunc:
        print(currentStatus.full_text)
    else:
        print(currentStatus.text)
    print("<<<_______________>>>")


def postToDiscord(currentStatus, twitter_dict):
    discordWebhook(
        'https://twitter.com/' + currentStatus.user.screen_name + '/status/' + currentStatus.id_str,
        currentStatus.user.screen_name, currentStatus.user.profile_image_url,
        twitter_dict, currentStatus.user.id_str)


class Queue:
    def __init__(self, twitter_dict: dict, tweeter: tweepy.API):
        self.twitter_dict = twitter_dict
        self.statusQueue = queue.Queue(maxsize=0)
        self.tweeter = tweeter

    def setDict(self, new_dict):
        self.twitter_dict = new_dict

    def beginThread(self):
        queueThread = threading.Thread(target=self.checkStatusThenPost)
        queueThread.daemon = True
        queueThread.start()

    def checkStatusThenPost(self):
        currentStatus = None
        is_not_original_tweet = False
        while True:
            try:
                if self.statusQueue.empty():
                    time.sleep(5)
                else:
                    currentStatus = self.statusQueue.get()
                    # Check to see if Truncated. If it is, get the extended version...
                    wasTrunc = False
                    if currentStatus.truncated:
                        currentStatus = self.tweeter.get_status(currentStatus.id, tweet_mode='extended')
                        wasTrunc = True
                    if hasattr(currentStatus, "retweeted_status") or hasattr(currentStatus,
                                                                             "quoted_status") or currentStatus.in_reply_to_screen_name != None:
                        is_not_original_tweet = True
                    # if status.user.id_str == userID and not is_retweet:
                    elif not is_not_original_tweet:
                        print(currentStatus.id)
                        if wasTrunc and hasattr(currentStatus, "extended_entities"):
                            if 'media' in currentStatus.extended_entities:
                                printInfo(currentStatus, wasTrunc)
                                postToDiscord(currentStatus, self.twitter_dict)
                        else:
                            if 'media' in currentStatus.entities:
                                printInfo(currentStatus, wasTrunc)
                                postToDiscord(currentStatus, self.twitter_dict)
                            else:
                                print("Skipping Tweet, no media!")

                        # if wasTrunc and hasattr(currentStatus, "extended_entities"):
                        #     if 'media' in currentStatus.extended_entities:
                        #         printInfo(currentStatus, wasTrunc)
                        #         media = currentStatus.extended_entities.get('media')
                        #         link_str = []
                        #         for x in range(len(media)):
                        #             link_str.append(media[x].get("media_url"))
                        #         postToDiscord(currentStatus, self.twitter_dict, link_str)
                        # else:
                        #     if 'media' in currentStatus.entities:
                        #         printInfo(currentStatus, wasTrunc)
                        #         media = currentStatus.entities.get('media')
                        #         link_str = []
                        #         for x in range(len(media)):
                        #             link_str.append(media[x].get("media_url"))
                        #         postToDiscord(currentStatus, self.twitter_dict, link_str)
                    is_not_original_tweet = False
            except Exception as e:
                print("WE GOT AN ERROR!: -------------------------")
                print(e)
                print(currentStatus.id)
                continue
