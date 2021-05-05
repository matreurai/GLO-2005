# -------------------------------
# Test API Binance
# David Bolduc
# -------------------------------

import os
from binance.client import Client

# import requests
os.environ['API_KEY'] = 'wSMlsBTwjkZbByuXLiL3IsgSEHIlE57HC5qHg0HTJ7zdtcYumwNu34GigRxO1OCI'
os.environ['API_SECRET'] = 'XfhicqXTykXoW3AyiBRh3NRWeZlmpU6Ku5yFB4Va0IHOJNiSgRZY8zuBfHMFiNfF'

# init
api_key = os.getenv('API_KEY')
api_secret = os.getenv('API_SECRET')

client = Client(api_key, api_secret)


# --- Entite projet

def ticker():
    exchange_info = client.get_exchange_info()['symbols']
    liste_ticker = [v['symbol'] for v in exchange_info if
                    v['symbol'] and v['status'] == 'TRADING']
    return liste_ticker

#def nom_ticker():


print(type(ticker()))

# conn = http.client.HTTPSConnection("api.binance.com")
# payload = ''
# headers = {
#     'Content-Type': 'application/json'
# }
# conn.request("GET", "/api/v3/exchangeInfo", payload, headers)
# res = conn.getresponse()
# data = res.read()
# transfor = data.decode("utf-8")
# exchange_dictionary = loads(transfor)
# print(type(exchange_dictionary['symbols']))

#
# client = Client("", "")
#
#
# def get_paires(client):
#     exchange_info = client.get_exchange_info()['symbols']
#
#     liste_paires_binance = [v['symbol'] for v in exchange_info if
#                             v['symbol'].endswith('USD') and v['status'] == 'TRADING']
#
#     return liste_paires_binance
#
#
# print(get_paires(client))