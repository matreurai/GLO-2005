#------------
# Stockage de mon code d'extra
# Code qui fonctionne dans certaine page qui peut etre reutiliser au besoin
#-------------


# Page Tes_binance
# Def qui retourne la liste des coins.
def name():
    exchange_info = client.get_exchange_info()['symbols']
    liste_ticker = [v['symbol'] for v in exchange_info if
                    v['symbol'] and v['status'] == 'TRADING']
    return liste_ticker

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

# import requests
os.environ['API_KEY'] = 'wSMlsBTwjkZbByuXLiL3IsgSEHIlE57HC5qHg0HTJ7zdtcYumwNu34GigRxO1OCI'
os.environ['API_SECRET'] = 'XfhicqXTykXoW3AyiBRh3NRWeZlmpU6Ku5yFB4Va0IHOJNiSgRZY8zuBfHMFiNfF'

# init
api_key = os.getenv('API_KEY')
api_secret = os.getenv('API_SECRET')

client = Client(api_key, api_secret)

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