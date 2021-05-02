# ----------
# Test respond Biannce
# -------------

import os
from binance.client import Client
import http.client
import json

# import requests
os.environ['API_KEY'] = 'wSMlsBTwjkZbByuXLiL3IsgSEHIlE57HC5qHg0HTJ7zdtcYumwNu34GigRxO1OCI'
os.environ['API_SECRET'] = 'XfhicqXTykXoW3AyiBRh3NRWeZlmpU6Ku5yFB4Va0IHOJNiSgRZY8zuBfHMFiNfF'

# init
api_key = os.getenv('API_KEY')
api_secret = os.getenv('API_SECRET')

client = Client(api_key, api_secret)

# asset_details = client.get_margin_asset(asset='BNB')
# print (asset_details)

# -----
# Binance_info: Liste des informations de biannce.
# exchange_info est la liste complete des symbole de binance
# liste_ticker est la liste des Symbol qui on la mention Trading dans Biannce

exchange_info = client.get_exchange_info()
# print (exchange_info)


exchange_ticker = client.get_exchange_info()['symbols']
liste_ticker = [v['symbol'] for v in exchange_ticker if
                v['symbol'] and v['status'] == 'TRADING']


def list_ticker(liste_ticker):
    return liste_ticker


# print(liste_ticker)


# Creation d'un dictionnaire des 3 premiere lettre des ticker
# Servira a comparer entre Biannce et Coinmarket pour les nom des coins

def binance_ticker():
    len_tick_list = len(liste_ticker)
    i = 0
    small_ticker = []
    while i <= len_tick_list:
        for a in liste_ticker:
            x = a[0:3]
            i += 1
            small_ticker.append(x)
    return small_ticker


# print(binance_ticker())

# Coin market request
# Sert a avoir les informations sur tous les coins.
# ne dois pas etre utiliser souvent
conn = http.client.HTTPSConnection("pro-api.coinmarketcap.com")
payload = ''
headers = {
    'X-CMC_PRO_API_KEY': '618906da-2cdf-4e16-8356-3bd45841e5aa',
    'Accept': 'application/json',
    'Cookie': '__cfduid=dc40f08c990d9bb9621b3e61584f6e5951619128567'
}
conn.request("GET", "/v1/cryptocurrency/listings/latest?limit=20", payload, headers)
res = conn.getresponse()
data = res.read()
respond = data.decode("utf-8")
dict = json.loads(respond)['data']
symbol = [v['symbol'] for v in dict if v['symbol']]
name = [v['name'] for v in dict if v['name']]
date_added = [v['date_added'] for v in dict if v['date_added']]
minable = [v['tags'] for v in dict if v['tags'] == 'minable']
print(symbol,name,date_added,minable)


# def name_ticker():
#     bin_tick_simple = binance_ticker()
#     for r in bin_tick_simple and c in symbol:
#         if r == c:
#
#         return
# print(name_ticker())


# for i in range (len(name)):
#     print('Nom:' + name[i]+'\t'+'Symbol:' + symbol[i])
# print(exchange_info)
# print(Binance_info)
