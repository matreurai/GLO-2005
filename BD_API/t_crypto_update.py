import http.client
import json
import pandas as pd
from sqlalchemy import create_engine
import pymysql
from BD_API.t_projet_import import projet_ticker


markets_values_update = []

markets_update = ['ETHBTC', 'LTCBTC', 'BNBBTC', 'NEOBTC', 'EOSETH', 'SNTETH', 'BNTETH', 'BNBETH', 'GASBTC', 'QTUMETH',
           'LRCBTC', 'LRCETH', 'OMGBTC', 'OMGETH', 'ZRXBTC', 'ZRXETH', 'KNCBTC', 'KNCETH', 'FUNBTC', 'FUNETH',
           'SNMBTC', 'NEOETH', 'XVGBTC', 'XVGETH', 'MTLBTC', 'MTLETH', 'EOSBTC', 'SNTBTC', 'ETCETH', 'ETCBTC',
           'ZECBTC', 'ZECETH', 'BNTBTC', 'BTGBTC', 'TRXBTC', 'TRXETH', 'ARKBTC', 'XRPBTC', 'XRPETH', 'ENJBTC',
           'ENJETH', 'BNBUSDT', 'KMDBTC', 'KMDETH', 'XMRBTC', 'XMRETH', 'BATBTC', 'BATETH', 'BATBNB', 'NEOUSDT',
           'NEOBNB', 'BTSBTC', 'LSKBTC', 'LSKETH', 'BCDBTC', 'ADABTC', 'ADAETH', 'PPTBTC', 'XLMBTC', 'XLMETH', 'XLMBNB',
           'LTCETH', 'LTCUSDT', 'LTCBNB', 'ICXBTC', 'ICXETH', 'ICXBNB', 'ELFBTC', 'ELFETH', 'RLCBTC', 'RLCETH',
           'ZILBTC', 'ZILETH', 'ZILBNB', 'ONTBTC', 'ONTETH', 'ONTBNB', 'XEMBTC', 'XEMETH', 'WANBTC', 'WANETH',
           'WANBNB', 'SYSBTC', 'ADAUSDT', 'ADABNB', 'XRPUSDT', 'REPBTC', 'REPETH', 'BTCUSDT', 'ETHUSDT', 'ZENBTC',
           'ZENETH', 'ZENBNB', 'EOSUSDT', 'EOSBNB', 'CVCBTC', 'CVCETH', 'XRPBNB', 'XLMUSDT', 'AGIBTC', 'ENJBNB',
           'ONTUSDT', 'TRXBNB', 'TRXUSDT', 'ETCUSDT', 'ETCBNB', 'ICXUSDT', 'HOTETH', 'NAVETH', 'VETBTC', 'VETETH',
           'VETUSDT', 'PAXUSDT', 'RVNBTC', 'RVNBNB', 'DCRBTC', 'WTCBNB', 'WTCBTC', 'BQXETH', 'XRPPAX', 'RENBTC',
           'IOTABNB', 'XRPTUSD', 'EOSTUSD', 'WABIBNB', 'QTUMBTC', 'IOTAETH', 'XRPUSDC', 'EOSUSDC', 'ADATUSD',
           'TRXTUSD', 'TRXXRP', 'LTCTUSD', 'LTCPAX', 'LTCUSDC', 'TRXPAX', 'TRXUSDC', 'BTTBNB', 'BTTUSDT', 'BTTTUSD',
           'BTTUSDC', 'ONGBTC', 'ONGUSDT', 'HOTBNB', 'HOTUSDT', 'ZILUSDT', 'ZRXUSDT', 'FETBNB', 'FETBTC', 'FETUSDT',
           'BATUSDT', 'XMRBNB', 'XMRUSDT', 'ZECBNB', 'ZECUSDT', 'ZECUSDC', 'CELRBNB', 'CELRBTC', 'CELRUSDT', 'ADAUSDC',
           'NEOUSDC', 'OMGUSDT', 'ENJUSDT', 'BATUSDC', 'AIONETH', 'ONEBNB', 'ONEBTC', 'FTMBNB', 'FTMBTC', 'FTMUSDT',
           'WINBNB', 'WINUSDT', 'WINUSDC', 'MTLUSDT', 'WANUSDT', 'FUNUSDT', 'CVCUSDT', 'BTTTRX', 'WINTRX', 'CHZBNB',
           'CHZBTC', 'CHZUSDT', 'WAVESBNB', 'YOYOBTC', 'XTZBNB', 'XTZBTC', 'XTZUSDT', 'RENUSDT', 'RVNUSDT', 'NKNBTC',
           'NKNUSDT', 'XRPBUSD', 'LINKETH', 'LTCBUSD', 'ETCBUSD', 'STXBNB', 'STXBTC', 'STXUSDT', 'SNGLSBTC', 'TRXBUSD']

for a in markets_update:
    conn = http.client.HTTPSConnection("api.binance.com")
    payload = ''
    headers = {
        'Content-Type': 'application/json'
    }
    conn.request("GET", "/api/v3/ticker/24hr?symbol={}".format(a), payload, headers)
    res_update = conn.getresponse()
    data_update = res_update.read()
    deecode_update = data_update.decode("utf-8")
    dict_data_update = json.loads(deecode_update)
    markets_values_update.append(dict_data_update)

    crypto_ticker_update = [v['symbol'] for v in markets_values_update if v['symbol']]
    crypto_p_haut_update = [v['highPrice'] for v in markets_values_update if v['highPrice']]
    crypto_p_bas_update = [v['lowPrice'] for v in markets_values_update if v['lowPrice']]
    crypto_volume_update = [v['volume'] for v in markets_values_update if v['volume']]

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
dict_data_update = json.loads(respond)['data']
dict_quote_update = [v['quote'] for v in dict_data_update if v['quote']]
dict_usd_update = [v['USD'] for v in dict_quote_update if v['USD']]

# Projet ticker coin
crypto_market_cap_update = [v['market_cap'] for v in dict_usd_update if v['market_cap']]
# Crypto 24h
crypto_volume_24h_update = [v['volume_24h'] for v in dict_usd_update if v['volume_24h']]
#
crypto_circulating_sup_update = [v['circulating_supply'] for v in dict_data_update if v['circulating_supply']]

# Price
# price = [v['price'] for v in dict_usd if v['price']]
def crypto_id_update():
    incremente = []
    a = -1
    for b in markets_update:
        a = a + 1
        incremente.append(a)
    return incremente

t_cryptomonnaie_update = {'cryptomonnaie_prix_haut': crypto_p_haut_update,'cryptomonnaie_prix_bas': crypto_p_bas_update,
                          'cryptomonnaie_market_cap': crypto_market_cap_update,
                          'cryptomonnaie_qte_circulation': crypto_circulating_sup_update,
                          'cryptomonnaie_volume_24h': crypto_volume_24h_update}

def insert_t_cryptomonnaie_update():

    list_t_crypto_update = 't_cryptomonnaie'
    t_crypto_frame_update = pd.DataFrame(data=t_cryptomonnaie_update)

    sqlEngine_update = create_engine('mysql+pymysql://root:eAXt)cdncT%Wv5}RVb!_,f]S@localhost/GLO-2005-Projet',
                              pool_recycle=3600)

    dbConnection_update = sqlEngine_update.connect()

    try:

        t_crypto_frame_update.to_sql(list_t_crypto_update, dbConnection_update, if_exists='update', index=False)

    except ValueError as vx:

        print(vx)

    except Exception as ex:

        print(ex)

    else:

        return("Table {} was filled successfully.".format(list_t_crypto_update))

    finally:

        dbConnection_update.close()

print(insert_t_cryptomonnaie_update())