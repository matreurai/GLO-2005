# -------------------------------
# API
# David Bolduc
# -------------------------------

import os
import gzip
import threading
import ujson as json

from binance.client import Client
from binance.websockets import BinanceSocketManager
# from binance.enums import *
from twisted.internet import reactor

from autobahn.twisted.websocket import WebSocketClientFactory, \
    WebSocketClientProtocol, connectWS
from twisted.internet import reactor, ssl
from twisted.internet.protocol import ReconnectingClientFactory
from twisted.internet.error import ReactorAlreadyRunning

# init API key

os.environ['API_KEY'] = 'wSMlsBTwjkZbByuXLiL3IsgSEHIlE57HC5qHg0HTJ7zdtcYumwNu34GigRxO1OCI'
os.environ['API_SECRET'] = 'XfhicqXTykXoW3AyiBRh3NRWeZlmpU6Ku5yFB4Va0IHOJNiSgRZY8zuBfHMFiNfF'

# init
api_key = os.getenv('API_KEY')
api_secret = os.getenv('API_SECRET')

client = Client(api_key, api_secret)
btc_price = {'error': False}

# exchange_ticker = client.get_exchange_info()['symbols']
# liste_ticker = [v['symbol'] for v in exchange_ticker if
#                 v['symbol'] and v['status'] == 'TRADING']

# def btc_trade_history(msg):
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
#
#
# # init and start the WebSocket
# bsm = BinanceSocketManager(client, user_timeout=10)
# conn_key = bsm.start_symbol_ticker_socket('BNBBTC', btc_trade_history)
# bsm.start()


class BinanceClientProtocol(WebSocketClientProtocol):
    def __init__(self):
        super(WebSocketClientProtocol, self).__init__()

    def onConnect(self, response):
        # reset the delay after reconnecting
        self.factory.resetDelay()

    def onMessage(self, payload, isBinary):
        if isBinary:
            try:
                payload = gzip.decompress(payload)
            except:
                print('Could not interpret binary response payload')
                return

        try:
            payload_obj = json.loads(payload.decode('utf8'))
        except ValueError:
            pass
        else:
            self.factory.callback(payload_obj)


class BinanceReconnectingClientFactory(ReconnectingClientFactory):
    # set initial delay to a short time
    initialDelay = 0.1

    maxDelay = 10

    maxRetries = 5


class BinanceClientFactory(WebSocketClientFactory, BinanceReconnectingClientFactory):
    protocol = BinanceClientProtocol
    _reconnect_error_payload = {
        'e': 'error',
        'm': 'Max reconnect retries reached'
    }

    def clientConnectionFailed(self, connector, reason):
        self.retry(connector)
        if self.retries > self.maxRetries:
            self.callback(self._reconnect_error_payload)

    def clientConnectionLost(self, connector, reason):
        self.retry(connector)
        if self.retries > self.maxRetries:
            self.callback(self._reconnect_error_payload)

class BinanceSocketManager(threading.Thread):

    STREAM_URL = 'wss://stream.binance.com:9443/'
    FSTREAM_URL = 'wss://fstream.binance.com/'
    VSTREAM_URL = 'wss://vstream.binance.com/'
    VSTREAM_TESTNET_URL = 'wss://testnetws.binanceops.com/'

    WEBSOCKET_DEPTH_5 = '5'
    WEBSOCKET_DEPTH_10 = '10'
    WEBSOCKET_DEPTH_20 = '20'

    DEFAULT_USER_TIMEOUT = 30 * 60  # 30 minutes

    def __init__(self, client, user_timeout=DEFAULT_USER_TIMEOUT):
        """Initialise the BinanceSocketManager

        :param client: Binance API client
        :type client: binance.Client
        :param user_timeout: Custom websocket timeout
        :type user_timeout: int

        """
        threading.Thread.__init__(self)
        self._conns = {}
        self._client = client
        self._user_timeout = user_timeout
        self._timers = {'user': None, 'margin': None}
        self._listen_keys = {'user': None, 'margin': None}
        self._account_callbacks = {'user': None, 'margin': None}
        # Isolated margin sockets will be opened under the 'symbol' name

        self.testnet = self._client.testnet

# def start_symbol_ticker_socket(self, symbol, callback):j