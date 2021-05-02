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
