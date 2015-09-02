import tweepy
import utils


class TwitterStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        print(status.text)
        utils.Util.normalize(status.text)

    def on_error(self, status_code):
        if status_code == 420:
            return False