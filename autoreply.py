from models.api import keys
from pycoingecko import CoinGeckoAPI
import tweepy

consumer_key = str(keys[0])
consumer_secret_key = str(keys[1])
access_token = str(keys[2])
access_token_secret = str(keys[3])
auth=tweepy.OAuthHandler(consumer_key,consumer_secret_key)
auth.set_access_token(access_token,access_token_secret)
api = tweepy.API(auth)
cg = CoinGeckoAPI()

def auto_reply(cg,api):
    mention = tweepy.Cursor(api.search, q='@cryptobotO_').items(1)
    for tweet in mention :
        tweet_id = tweet.id
        tweet_text = tweet.text
        crypto = str(tweet_text.replace("@cryptobotO_ ",""))
        print(crypto)
        price = cg.get_price(ids=[crypto],vs_currencies=["usd"])
        print(price)
        str_price = str(price[crypto]["usd"])
        new_tweet = "The price of " + crypto + " is currently " + str_price + "$USD \n dont forget to follow"
        api.update_status(status=new_tweet,in_reply_to_status_id=tweet_id,auto_populate_reply_metadata=True)
        return tweet_id

while True : 
    auto_reply(cg,api)
    break