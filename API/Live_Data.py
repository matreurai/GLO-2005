#-------------------------------
# API
# David Bolduc
#-------------------------------

import os
from binance.client import Client
from binance.websockets import BinanceSocketManager
from twisted.internet import reactor

#init API key

os.environ['API_KEY']= 'wSMlsBTwjkZbByuXLiL3IsgSEHIlE57HC5qHg0HTJ7zdtcYumwNu34GigRxO1OCI'
os.environ['API_SECRET'] = 'XfhicqXTykXoW3AyiBRh3NRWeZlmpU6Ku5yFB4Va0IHOJNiSgRZY8zuBfHMFiNfF'
#init
# api_key = 
api_key = os.getenv('API_KEY')
api_secret = os.getenv('API_SECRET')
client = Client(api_key,api_secret)
btc_price = {'error':False}

def btc_trade_history(msg):
    #Define how to process incoming WebSockt message
    if msg['e'] != 'error':
        print ('symbol:',msg['s'], 'Stas_open:',msg['o'], 'High price:',msg['h'])
        btc_price['symbol'] = msg['s']
        btc_price['stats_open'] = msg['o']
        btc_price['High price'] = msg['h']
    else:
        btc_price['error'] = True

# init and start the WebSocket
bsm = BinanceSocketManager(client)
conn_key = bsm.start_symbol_ticker_socket('ETHUSDT', btc_trade_history)
bsm.start()
