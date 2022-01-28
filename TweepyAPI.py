import tweepy


class TweepyAPI:
    def __init__(self, consumer_Key: str, consumer_Secret: str, access_Key: str, access_Secret: str):
        self.CK = consumer_Key
        self.CS = consumer_Secret
        self.AK = access_Key
        self.AS = access_Secret

    def authorize(self):
        auth = tweepy.OAuthHandler(self.CK, self.CS)
        auth.set_access_token(self.AK, self.AS)
        tweeter = tweepy.API(auth, wait_on_rate_limit=True)
        return tweeter
