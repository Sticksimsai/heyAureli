import tweepy
from dataclasses import dataclass

@dataclass
class PostResult:
    id: int
    text: str

class TwitterClient:
    def __init__(self, api_key, api_secret, access_token, access_secret):
        auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_secret)
        self.api = tweepy.API(auth)

    def post(self, text, in_reply_to_status_id=None):
        status = self.api.update_status(status=text[:280], in_reply_to_status_id=in_reply_to_status_id)
        return PostResult(id=status.id, text=status.text)

    def mentions(self, count=5):
        return self.api.mentions_timeline(count=count, tweet_mode="extended")
