import tweepy
from pipe import pipe
from utils import Util


class TwitterStreamListener(tweepy.StreamListener):

    def __init__(self):
        self.pipe = pipe()

    def on_data(self, data):
        text_i = data.find('"text"')
        source_i = data.find("source")
        text = data[text_i + 8:source_i]
        self.pipe.add(Util.normalize(text))

    def on_error(self, status_code):
        if status_code == 420:
            return False
