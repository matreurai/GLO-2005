# ----------
# Test respond Biannce
# -------------

import os
import http.client
import json


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

dict_data = json.loads(respond)['data']
dict_quote = [v['quote'] for v in dict_data if v['quote']]
dict_usd = [v['USD'] for v in dict_quote if v['USD']]

symbols = [v['symbol'] for v in dict_data if v['symbol']]
names = [v['name'] for v in dict_data if v['name']]
dates_added = [v['date_added'] for v in dict_data if v['date_added']]
price = [v['price'] for v in dict_usd if v['price']]

print (price)

