# -------------------------------
# API
# David Bolduc
# -------------------------------

import os
from binance.client import Client
from binance import AsyncClient, BinanceSocketManager
import asyncio
from binance.enums import *

# init API key

os.environ['API_KEY'] = 'wSMlsBTwjkZbByuXLiL3IsgSEHIlE57HC5qHg0HTJ7zdtcYumwNu34GigRxO1OCI'
os.environ['API_SECRET'] = 'XfhicqXTykXoW3AyiBRh3NRWeZlmpU6Ku5yFB4Va0IHOJNiSgRZY8zuBfHMFiNfF'

# init
api_key = os.getenv('API_KEY')
api_secret = os.getenv('API_SECRET')

client = Client(api_key, api_secret)
# btc_price = {'error': False}

# exchange_ticker = client.get_exchange_info()['symbols']
# liste_ticker = [v['symbol'] for v in exchange_ticker if
#                 v['symbol'] and v['status'] == 'TRADING']

# def trade_history(msg):
#     # Define how to process incoming WebSockt message
#     if msg['e'] != 'error':
#         print('Symbol:', msg['s'], 'Quantity:', msg['q'], 'Price:', msg['c'],
#               'Open Price:', msg['o'], 'Close Price:', msg['c'], 'High Price:',
#               msg['h'])
#         btc_price['symbol'] = msg['s']
#         btc_price['Quantity'] = msg['q']
#         btc_price['Price'] = msg['c']
#         btc_price['Open Price'] = msg['o']
#         btc_price['Close Price'] = msg['c']
#         btc_price['High price'] = msg['h']
#
#     else:
#         btc_price['error'] = True
#         bsm.stop_socket(conn_key)
#         reactor.stop()
# #
# #
# # init and start the WebSocket
# bsm = BinanceSocketManager(client, user_timeout=1)
# conn_key = bsm.start_symbol_ticker_socket('BNBBTC', btc_trade_history)
# bsm.start()


async def main():
    client = await AsyncClient.create()
    # initialise socket manager
    bsm = BinanceSocketManager(client, loop)

    # setup async callback handler for socket messages
    async def handle_evt(msg):
        pair = msg['s']
        print(f'{pair} : {msg}')

    # create listener, can use the `ethkey` value to close the socket later
    key = await bsm.start_aggtrade_socket('BTCUSDT', handle_evt)

    while True:
        print("doing a sleep")
        await asyncio.sleep(20, loop=loop)

if __name__ == "__main__":

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())


