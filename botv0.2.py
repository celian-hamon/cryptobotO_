from time import sleep
from pycoingecko import CoinGeckoAPI
from random import randint
from licto import lictoo,emoj
import tweepy

consumer_key = 'bgwMY7ETrRQtUJXQW50a4HFsr'
consumer_secret_key = 'gUpSnJGMTL2mTs7oEyznrT0iUvP7IGaZgXvwl2aLetu4WfFEUs'
access_token = '1382241545554948097-eQ4vy2hft8Od7kiONNG0JlzaXpTR08'
access_token_secret = 'fDQUMFFyizVKtQCmKOi5bK5QJjHyWHwkdWkeTPzijPykO'
auth=tweepy.OAuthHandler(consumer_key,consumer_secret_key)
auth.set_access_token(access_token,access_token_secret)
api = tweepy.API(auth)
cg = CoinGeckoAPI()

def bitcoin_weather(cg):
    price = cg.get_price(ids=['bitcoin','ethereum'], vs_currencies='usd')
    print(price)
    price_btc = str(price["bitcoin"]['usd'])
    price_eth = str(price["ethereum"]['usd'])
    print(price_btc,price_eth)
    tweet=emoj[randint(0,len(emoj))] + "Crypto Weather" + emoj[randint(0,len(emoj))] + "\nThe current price of #Bitcoin is " + price_btc + "$USD\nThe current price of #Ethereum is " + price_eth + "$USD\n" + lictoo[randint(0,len(lictoo))] + "\n$ETH $BTC\n" + emoj[randint(0,len(emoj))] + "End of report" + emoj[randint(0,len(emoj))] 
    print(tweet)
    return tweet

def nbelt(cg):
    nombre_de_crypto = 0
    all = cg.get_supported_vs_currencies()
    for _ in all:
        nombre_de_crypto += 1
    print("nombre de crypto :",nombre_de_crypto)
    return nombre_de_crypto

def leaderboard(cg):
    market = cg.get_coins_markets(vs_currency='usd')
    img_url = list()
    premiere_crypto = str(market[0]['id'])
    deuxieme_crypto = str(market[1]['id'])
    troisieme_crypto = str(market[2]['id'])
    quatrieme_crypto = str(market[3]['id'])
    cinquieme_crypto = str(market[4]['id'])
    for i in range(5):
        img_url.append(str(market[i]['image']))
    tweet = 'curent leaderbord of crypto :\n1rst #' + premiere_crypto + '\n2nd #' + deuxieme_crypto + '\n3rd #' + troisieme_crypto + '\n4st #' + quatrieme_crypto + '\n5st #' + cinquieme_crypto + "\n💰💰💰💰💰" 
    print(tweet)
    return tweet

def Tweet(tweet,api,image=0):
    if image == 0:
        api.update_status(status=tweet)
    else:
        api.update_status(status=tweet,media_ids=[])

while True:
    for i in range(72):
        Tweet(bitcoin_weather(cg),api)
        sleep(3600)
    Tweet(leaderboard(cg),api)