import os
from dotenv import load_dotenv

import tweepy

load_dotenv()

api_key = os.environ.get("API_KEY", "")
api_secret = os.environ.get("API_SECRET", "")
bearer_token = os.environ.get("BEARER_TOKEN", "")
access_token = os.environ.get("ACCESS_TOKEN", "")
access_token_secret = os.environ.get("ACCESS_TOKEN_SECRET", "")

client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)

auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)

reply_tweet = "Congratulations on taking your first step towards your goals 💪. " \
              "Now, just wait for the right person to reach out to you 👀"


class MyStream(tweepy.StreamingClient):

    def on_tweet(self, tweet):
        print(tweet.text)
        try:
            client.retweet(tweet.id)
            client.create_tweet(in_reply_to_tweet_id=tweet.id, text=reply_tweet)
        except Exception as error:
            print(error)


stream = MyStream(bearer_token=bearer_token)

rule = tweepy.StreamRule("(@Hey_CountMeIn) (-is:retweet -is:reply)")

stream.add_rules(rule)

stream.filter()
