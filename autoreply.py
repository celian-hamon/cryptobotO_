from models.api import keys
from pycoingecko import CoinGeckoAPI
from time import sleep
from os import remove
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
    with open("temp.txt","r") as fichier:
        last_id = fichier.readline()
    mention = tweepy.Cursor(api.search, q='@cryptobotO_').items(1)
    for tweet in mention :
        tweet_id = tweet.id
        last_id = int(last_id)
        if tweet_id == last_id:
            print("echec")
            return tweet_id
        tweet_text = tweet.text
        crypto = str(tweet_text.replace("@cryptobotO_ ",""))
        price = cg.get_price(ids=[crypto],vs_currencies=["usd"])
        str_price = str(price[crypto]["usd"])
        new_tweet = "The price of " + crypto + " is currently " + str_price + "$USD \n dont forget to follow"
        api.update_status(status=new_tweet,in_reply_to_status_id=tweet_id,auto_populate_reply_metadata=True)
        print("sucess")
        remove("temp.txt")
        with open("temp.txt","a") as fichier:
            fichier.write(str(tweet_id))
        return tweet_id


while True : 
    try :
        auto_reply(cg,api)
    except :
        print("echec2")
        pass
    sleep(30)