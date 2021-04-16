from time import sleep
from pycoingecko import CoinGeckoAPI
from random import randint
from licto import lictoo,emoj
from merge import get_img_lead
from PIL import Image
import tweepy

consumer_key = 'bgwMY7ETrRQtUJXQW50a4HFsr'
consumer_secret_key = 'gUpSnJGMTL2mTs7oEyznrT0iUvP7IGaZgXvwl2aLetu4WfFEUs'
access_token = '1382241545554948097-eQ4vy2hft8Od7kiONNG0JlzaXpTR08'
access_token_secret = 'fDQUMFFyizVKtQCmKOi5bK5QJjHyWHwkdWkeTPzijPykO'
auth=tweepy.OAuthHandler(consumer_key,consumer_secret_key)
auth.set_access_token(access_token,access_token_secret)
api = tweepy.API(auth)
cg = CoinGeckoAPI()

# return random emojie if param == 1 ,if param == 2 return random sentence
def rand(param):
    if param == 1 :
        return emoj[randint(0,len(emoj)-1)]
    if param == 2 :
        return lictoo[randint(0,len(lictoo)-1)]

# tweet hourly current price of one btc and one eth in usd
def crypto_weather(cg):
    price = cg.get_price(ids=['bitcoin','ethereum'], vs_currencies='usd')
    print(price)
    price_btc = str(price["bitcoin"]['usd'])
    price_eth = str(price["ethereum"]['usd'])
    print(price_btc,price_eth)
    tweet_wth= rand(1) + "Crypto Weather" + rand(1) + "\nThe current price of #Bitcoin is " + price_btc + "$USD\nThe current price of #Ethereum is " + price_eth + "$USD\n" + rand(2) + "\n$ETH $BTC\n" + rand(1) + "End of report" + rand(1)
    print(tweet_wth)
    return tweet_wth

#return the number of crypto in the api :61
def nbelt(cg):
    nombre_de_crypto = 0
    all = cg.get_supported_vs_currencies()
    for _ in all:
        nombre_de_crypto += 1
    print("nombre de crypto :",nombre_de_crypto)
    return nombre_de_crypto

# tweet on a weekly schedule the crypto_leaderboard wich is the 5 crypto wich have the highest market cap (nmbr of token * cost of token) currently btc,eth,binance,ripple,doge
def leaderboard(cg):
    market = cg.get_coins_markets(vs_currency='usd',per_page=5)
    premiere_crypto = str(market[0]['id'])
    deuxieme_crypto = str(market[1]['id'])
    troisieme_crypto = str(market[2]['id'])
    quatrieme_crypto = str(market[3]['id'])
    cinquieme_crypto = str(market[4]['id'])
    s1 = str(market[0]['symbol'])
    s2 = str(market[1]['symbol'])
    s3 = str(market[2]['symbol'])
    s4 = str(market[3]['symbol'])
    s5 = str(market[4]['symbol'])
    get_img_lead(c1=s1,c2=s2,c3=s3,c4=s4,c5=s5)
    tweet_lead = 'Current leaderbord of #crypto :\n1rst #' + premiere_crypto + '\n2nd #' + deuxieme_crypto + '\n3rd #' + troisieme_crypto + '\n4st #' + quatrieme_crypto + '\n5st #' + cinquieme_crypto + "\n💰💰💰💰💰" 
    print(tweet_lead)
    return tweet_lead

# tweet with or without images and rt 
def Tweet(api,tweet=0,image=0,id_RT=0):
    if image == 0 :
        last_tweet = api.update_status(status=tweet)
        return last_tweet
    if image != 0 :
        image_path = "images/"+image+".jpg"
        last_tweet = api.update_with_media(image_path,tweet)
    if id_RT != 0 :
        last_retweet = api.retweet(id=id_RT)
        return last_retweet

# loop wich tweet each hour the crypto_weather and each week the crypto_leaderboard
while True:
    for i in range(168):
        Tweet(api,tweet=crypto_weather(cg),image="btc_eth")
        sleep(3600)
    Tweet(api,tweet=leaderboard(cg),image="merged")