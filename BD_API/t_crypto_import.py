import http.client
import json
import pandas as pd
from sqlalchemy import create_engine
import pymysql
from t_projet_import import projet_ticker


markets_values = []

markets = ['ETHBTC', 'LTCBTC', 'BNBBTC', 'NEOBTC', 'EOSETH']

for a in markets:
    conn = http.client.HTTPSConnection("api.binance.com")
    payload = ''
    headers = {
        'Content-Type': 'application/json'
    }
    conn.request("GET", "/api/v3/ticker/24hr?symbol={}".format(a), payload, headers)
    res = conn.getresponse()
    data = res.read()
    deecode = data.decode("utf-8")
    dict_data = json.loads(deecode)
    markets_values.append(dict_data)

    crypto_ticker = [v['symbol'] for v in markets_values if v['symbol']]
    crypto_p_haut = [v['highPrice'] for v in markets_values if v['highPrice']]
    crypto_p_bas = [v['lowPrice'] for v in markets_values if v['lowPrice']]
    crypto_volume = [v['volume'] for v in markets_values if v['volume']]

# Traitement de la donner de Coinmarket
# Connection a coinmarket
conn = http.client.HTTPSConnection("pro-api.coinmarketcap.com")
payload = ''
headers = {
    'X-CMC_PRO_API_KEY': '618906da-2cdf-4e16-8356-3bd45841e5aa',
    'Accept': 'application/json',
    'Cookie': '__cfduid=dc40f08c990d9bb9621b3e61584f6e5951619128567'
}
conn.request("GET", "/v1/cryptocurrency/listings/latest?limit=200", payload, headers)
res = conn.getresponse()
data = res.read()
respond = data.decode("utf-8")

# Creation des dictionnaires.
dict_data = json.loads(respond)['data']
dict_quote = [v['quote'] for v in dict_data if v['quote']]
dict_usd = [v['USD'] for v in dict_quote if v['USD']]

# Projet ticker coin
crypto_market_cap = [v['market_cap'] for v in dict_usd if v['market_cap']]
# Crypto 24h
crypto_volume_24h = [v['volume_24h'] for v in dict_usd if v['volume_24h']]
#
crypto_circulating_sup = [v['circulating_supply'] for v in dict_data if v['circulating_supply']]

# Price
# price = [v['price'] for v in dict_usd if v['price']]
a = 0
t_cryptomonnaie = {'cryptomonnaie_id':++a ,'cryptomonnaie_ticker':projet_ticker,
                   'cryptomonnaie_prix_haut': crypto_p_haut, 'cryptomonnaie_prix_bas': crypto_p_bas,
                   'cryptomonnaie_market_cap': crypto_market_cap,
                   'cryptomonnaie_qte_circulation': crypto_circulating_sup,
                   'cryptomonnaie_volume_24h': crypto_volume_24h}

list_t_crypto = 't_cryptomonnaie'
t_crypto_frame = pd.DataFrame(data=t_cryptomonnaie)

sqlEngine = create_engine('mysql+pymysql://root:eAXt)cdncT%Wv5}RVb!_,f]S@localhost/GLO-2005-Projet', pool_recycle=3600)

dbConnection = sqlEngine.connect()

try:

    t_crypto_frame.to_sql(list_t_crypto, dbConnection, if_exists='append', index=False)

except ValueError as vx:

    print(vx)

except Exception as ex:

    print(ex)

else:

    print("Table %s created successfully." % t_cryptomonnaie)

finally:

    dbConnection.close()
