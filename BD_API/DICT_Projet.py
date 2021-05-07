# -------------------------------
# Test API Binance
# David Bolduc
# -------------------------------

import os
from binance.client import Client
from t_crypto_import import projet_ticker

# import requests
os.environ['API_KEY'] = 'wSMlsBTwjkZbByuXLiL3IsgSEHIlE57HC5qHg0HTJ7zdtcYumwNu34GigRxO1OCI'
os.environ['API_SECRET'] = 'XfhicqXTykXoW3AyiBRh3NRWeZlmpU6Ku5yFB4Va0IHOJNiSgRZY8zuBfHMFiNfF'

# init
api_key = os.getenv('API_KEY')
api_secret = os.getenv('API_SECRET')

client = Client(api_key, api_secret)


# --- Entite projet

exchange_info = client.get_exchange_info()['symbols']
liste_ticker = [v['symbol'] for v in exchange_info if
                v['symbol'] and v['status'] == 'TRADING']


def binance_ticker():
    small_ticker = []
    for a in liste_ticker:
        x = a[0:3]
        small_ticker.append(x)
    return small_ticker

def comp_dict_binance_coin_market():
    dict_binance = []
    for a in binance_ticker():
        for b in projet_ticker:
            if a == b:
                dict_binance.append(a)
                break

    return dict_binance
