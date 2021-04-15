from time import sleep
from pycoingecko import CoinGeckoAPI
from random import randint
from licto import licto_ as licto
import tweepy

consumer_key = ''
consumer_secret_key = ''
access_token = ''
access_token_secret = ''
auth=tweepy.OAuthHandler(consumer_key,consumer_secret_key)
auth.set_access_token(access_token,access_token_secret)
api = tweepy.API(auth)
cg = CoinGeckoAPI()

def hourly(cg):
    price = cg.get_price(ids=['bitcoin','ethereum'], vs_currencies='usd')
    price_btc = str(price["bitcoin"]['usd'])
    price_eth = str(price["ethereum"]['usd'])
    print(price)
    print(price_btc,price_eth)
    x = randint(0,len(licto))
    tweet="The current price of #Bitcoin is " + price_btc + "$USD\nThe current price of #Ethereum is " + price_eth + "$USD\n" + licto[x] + "\n$ETH $BTC" 
    print(tweet)
    return tweet

def nbelt(cg):
    nombre_de_crypto = 0
    all = cg.get_supported_vs_currencies()
    for i in all:
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
    tweet = 'curent leaderbord of crypto :\n#' + premiere_crypto + '\n#' + deuxieme_crypto + '\n#' + troisieme_crypto + '\n#' + quatrieme_crypto + '\n#' + cinquieme_crypto + "\n maybe invest ¯\_(ツ)_/¯" 
    print(tweet)
    return tweet,img_url

def Tweet(tweet,api,image=0):
    if image == 0:
        api.update_status(status=tweet)
    else:
        api.update_status(status=tweet,media_ids=[])

while True:
    for i in range(168):
        Tweet(hourly(cg),api)
        sleep(3600)
    Tweet(leaderboard(cg),api)