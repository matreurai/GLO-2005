# -------------------------------
# Test API Binance
# David Bolduc
# -------------------------------

from json import loads
import http.client


# import requests


# --- Entite projet


def exchange_dict():
    conn = http.client.HTTPSConnection("api.binance.com")
    payload = ''
    headers = {
        'Content-Type': 'application/json'
    }
    conn.request("GET", "/api/v3/exchangeInfo", payload, headers)
    res = conn.getresponse()
    data = res.read()
    transfor = data.decode("utf-8")
    exchange_dictionnaire = loads(transfor)
    print(type(exchange_dictionnaire['symbols']))

    for stock in exchange_dictionnaire['symbols'] == :
        return stock['symbol']


print(exchange_dict())
