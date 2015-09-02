import re


class Util:

    @staticmethod
    def normalize(tweet):
        """
        :param tweet: tweet text
        :return: normalized text according to: Alec Go (2009)'s Twitter Sentiment Classification using Distant Supervision
        """
        # http://stackoverflow.com/questions/2304632/regex-for-twitter-username
        result = re.sub('(?<=^|(?<=[^a-zA-Z0-9-_\.]))@([A-Za-z]+[A-Za-z0-9]+)', 'USER', tweet)
        result = re.sub('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', 'URL', result)
        return result
