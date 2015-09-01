import tweepy
import stream_listener
import json

with open('data/config.json') as config_data:
    config = json.load(config_data)

auth = tweepy.OAuthHandler(config['consumer_key'], config['consumer_secret'])
auth.set_access_token(config['access_token'], config['access_token_secret'])
api = tweepy.API(auth)

stream = stream_listener.TwitterStreamListener()
twitterStream = tweepy.Stream(auth = api.auth, listener=stream)
twitterStream.filter(track=['python'], async=True)