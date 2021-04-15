import tweepy
from time import sleep
from pycoingecko import CoinGeckoAPI

consumer_key = 'bgwMY7ETrRQtUJXQW50a4HFsr'
consumer_secret_key = 'gUpSnJGMTL2mTs7oEyznrT0iUvP7IGaZgXvwl2aLetu4WfFEUs'
access_token = '1382241545554948097-eQ4vy2hft8Od7kiONNG0JlzaXpTR08'
access_token_secret = 'fDQUMFFyizVKtQCmKOi5bK5QJjHyWHwkdWkeTPzijPykO'

auth=tweepy.OAuthHandler(consumer_key,consumer_secret_key)
auth.set_access_token(access_token,access_token_secret)
api=tweepy.API(auth)

cg = CoinGeckoAPI()
while True:
    price = cg.get_price(ids=['bitcoin','ethereum'], vs_currencies='usd')
    print(price)
    price_btc = str(price["bitcoin"]['usd'])
    price_eth = str(price["ethereum"]['usd'])
    print(price_btc,price_eth)

    tweet="the current price of #Bitcoin is " + price_btc + "$\nAnd the price of #Ethereum is " + price_eth + "$\n$ETH $BTC"
    api.update_status(tweet)
    sleep(7200)
    
