from os import remove
from requests import get 
from time import sleep
from pycoingecko import CoinGeckoAPI
import json
import tweepy
import pprint
cg = CoinGeckoAPI()

def twitter_api():
    consumer_key = ''
    consumer_secret_key = ''
    access_token = ''
    access_token_secret = ''

    auth=tweepy.OAuthHandler(consumer_key,consumer_secret_key)
    auth.set_access_token(access_token,access_token_secret)
    api=tweepy.API(auth)
    return api

def hourly(cg,api):
    price = cg.get_price(ids=['bitcoin','ethereum'], vs_currencies='usd')
    print(price)
    price_btc = str(price["bitcoin"]['usd'])
    price_eth = str(price["ethereum"]['usd'])
    print(price_btc,price_eth)
    tweet="The current price of #Bitcoin is " + price_btc + "$\nThe current price of #Ethereum is " + price_eth + "$\nhave a good day\n$ETH $BTC" 
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
    tweet = 'curent leaderbord of crypto :\n#' + premiere_crypto + '\n#' + deuxieme_crypto + '\n#' + troisieme_crypto + '\n#' + quatrieme_crypto + '\n#' + cinquieme_crypto
    print(tweet)
    return tweet,img_url

# def tweet_image(img_url ,tweet ,api):
#     for c,url in enumerate(img_url):
#         filename = 'temp'+ c +'.jpg'
#         request = requests.get(url, stream=True)
#         if request.status_code == 200:
#             with open(filename, 'wb') as image:
#                 for chunk in request:
#                     image.write(chunk)
            
#         api.update_status(status=tweet , media)
#         os.remove(filename)
#     else:
#         print("Unable to download image")

leaderboard(cg)
# api.update_status(status=tweet , media)
