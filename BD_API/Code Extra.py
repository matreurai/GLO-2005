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

# @app.route('/collect', methods=['GET'])
# def collect():
#     try:
#         conn = http.client.HTTPSConnection("pro-api.coinmarketcap.com")
#         payload = ''
#         headers = {
#             'X-CMC_PRO_API_KEY': '618906da-2cdf-4e16-8356-3bd45841e5aa',
#             'Accept': 'application/json',
#             'Cookie': '__cfduid=dc40f08c990d9bb9621b3e61584f6e5951619128567'
#         }
#         conn.request("GET", "/v1/cryptocurrency/listings/latest?limit=20", payload, headers)
#         res = conn.getresponse()
#         data = res.read()
#         respond = data.decode("utf-8")
#
#         dict_data = json.loads(respond)['data']
#         dict_quote = [v['quote'] for v in dict_data if v['quote']]
#         dict_usd = [v['USD'] for v in dict_quote if v['USD']]
#
#         symbols = [v['symbol'] for v in dict_data if v['symbol']]
#         names = [v['name'] for v in dict_data if v['name']]
#         dates_added = [v['date_added'] for v in dict_data if v['date_added']]
#         price = [v['price'] for v in dict_usd if v['price']]
#
#         return symbols, names, dates_added, price
#     except Exception as e:
#         print(e)
#
#
# db = mysql.connector.connect(host="localhost", user="root",
#                              password="eAXt)cdncT%Wv5}RVb!_,f]S", db="GLO-2005-Projet")
#
# # create Student
# @app.route('/create_database', methods=['POST'])
# def create_database():
#     try:
#         excel_projet = xlrd.open_workbook('Crypto.xlsx')
#
#         excel_t_proj_sheet = excel_projet.sheet_names()
#
#         for v in range(0, len(excel_t_proj_sheet)):
#             t_proj = excel_projet.sheet_by_index(v)
#
#             for x in range(1, t_proj.nrows):
#                 proj_coin_url = t_proj.cell(x, 1).value
#
#                 proj_description = t_proj.cell(x, 3).value
#
#                 proj_forage_possible = t_proj.cell(x, 5).value
#
#         json_dict_data = dict_data
#         proj_ticker = json_dict_data['symbol']
#         proj_coins_url = proj_coin_url
#         proj_nom_du_coin = json_dict_data['name']
#         proj_descriptions = proj_description
#         proj_start_date = json_dict_data['date_added']
#         proj_forages_possible = proj_forage_possible
#
#         # insert record in database
#         insert_t_proj = 'INSERT INTO t_projet (projet_ticker, projet_logo, projet_nom_du_coin,projet_description, ' \
#                         'projet_start_date, projet_forage_possible) VALUES (%s,%s,%s,%s,%s,%s)'
#         t_proj_values = (proj_ticker, proj_coins_url, proj_nom_du_coin, proj_descriptions,
#                          proj_start_date, proj_forages_possible)
#         conn = mysql.connect()
#         cur = conn.cursor()
#         cur.execute(insert_t_proj, t_proj_values)
#         conn.commit()
#         res = jsonify('Database ready')
#         res.status_code = 200
#
#         return res
#
#     except Exception as e:
#         print(e)
#     finally:
#         cur.close()
#         conn.close()
#
#
# @app.errorhandler(404)
# def not_found():
#     message = {
#         'status': 404,
#         'message': 'There is no record: ' + request.url,
#     }
#     res = jsonify(message)
#     res.status_code = 404
#
#     return res
#
#
# # app.run(port=5000, debug=True)
# if __name__ == "__main__":
#     pass
#
#
#
# conn = http.client.HTTPSConnection("pro-api.coinmarketcap.com")
# payload = ''
# headers = {
#     'X-CMC_PRO_API_KEY': '618906da-2cdf-4e16-8356-3bd45841e5aa',
#     'Accept': 'application/json',
#     'Cookie': '__cfduid=dc40f08c990d9bb9621b3e61584f6e5951619128567'
# }
# conn.request("GET", "/v1/cryptocurrency/listings/latest?limit=20", payload, headers)
# res = conn.getresponse()
# data = res.read()
# respond = data.decode("utf-8")
#
# dict_data = json.loads(respond)['data']
# dict_quote = [v['quote'] for v in dict_data if v['quote']]
# dict_usd = [v['USD'] for v in dict_quote if v['USD']]
#
# symbols = [v['symbol'] for v in dict_data if v['symbol']]
# names = [v['name'] for v in dict_data if v['name']]
# dates_added = [v['date_added'] for v in dict_data if v['date_added']]
# price = [v['price'] for v in dict_usd if v['price']]
#
# print(price)

# try:
#     db = mysql.connector.connect(host="localhost", user="root", password="eAXt)cdncT%Wv5}RVb!_,f]S",
#                                  db="GLO-2005-Projet")
#     cursor = db.cursor()
#     # placeholders = ', '.join(['%s'] * len(dict_t_proj))
#     # columns = ', '.join(dict_t_proj.keys())
#     mySql_insert_query = 'INSERT INTO t_projet (projet_ticker, projet_logo, projet_nom_du_coin, ' \
#                          'projet_description,projet_start_date, projet_forage_possible) VALUES (%s,%s,%s,%s,%s,%s)'
#     cursor.execute(mySql_insert_query, t_projet)
#     db.commit()
#     print("Record inserted successfully into Laptop table")
#
# except mysql.connector.Error as error:
#     print("Failed to insert into MySQL table {}".format(error))
#
# finally:
#     if db.is_connected():
#         cursor.close()
#         db.close()
#         print("MySQL connection is closed")

# print(projet_start_date)
# price = [v['price'] for v in dict_usd if v['price']]


#def nom_ticker():


#print(type(ticker()))

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

markets = ['ETHBTC', 'LTCBTC', 'BNBBTC', 'NEOBTC', 'EOSETH', 'SNTETH', 'BNTETH', 'BNBETH', 'GASBTC', 'QTUMETH',
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
           'NKNUSDT', 'XRPBUSD', 'LINKETH', 'LTCBUSD', 'ETCBUSD', 'STXBNB', 'STXBTC', 'STXUSDT', 'SNGLSBTC', 'TRXBUSD',
           'EOSBUSD', 'RLCUSDT', 'XLMBUSD', 'ADABUSD', 'BCHBNB', 'BCHBTC', 'BCHUSDT', 'BCHUSDC', 'BCHTUSD', 'BCHPAX',
           'BCHBUSD', 'BQXBTC', 'DASHETH', 'XRPRUB', 'BLZBNB', 'VETBNB', 'FTTBNB', 'FTTBTC', 'FTTUSDT', 'IOTABTC',
           'THETABNB', 'VIBETH', 'XRPTRY', 'LINKBTC', 'POWRETH', 'SCBNB', 'XRPEUR', 'OGNBNB', 'OGNBTC', 'OGNUSDT',
           'WRXBNB', 'WRXBTC', 'WRXUSDT', 'ICXBUSD', 'BTSUSDT', 'LSKUSDT', 'BNTUSDT', 'BNTBUSD', 'NEOBUSD', 'XTZBUSD',
           'BATBUSD', 'ENJBUSD', 'ONTBUSD', 'RVNBUSD', 'BTTBUSD', 'XMRBUSD', 'ZECBUSD', 'SOLBNB', 'SOLBTC', 'SOLUSDT',
           'SOLBUSD', 'MDABTC', 'MFTBNB', 'MTHBTC', 'DNTBTC', 'WRXBUSD', 'ZILBUSD', 'KNCBUSD', 'KNCUSDT', 'DREPBTC',
           'LRCBUSD', 'LRCUSDT', 'ASTBTC', 'CDTETH', 'XRPGBP', 'MITHBNB', 'DGBBNB', 'DGBBTC', 'DGBBUSD', 'DASHBTC',
           'OAXBTC', 'GXSETH', 'BNBPAX', 'ZENUSDT', 'SXPBTC', 'SXPBNB', 'SXPBUSD', 'SNXBTC', 'SNXBNB', 'SNXBUSD',
           'SNXUSDT', 'QSPETH', 'MANAETH', 'ADAUPUSDT', 'ADADOWNUSDT', 'DGBUSDT', 'SXPUSDT', 'MKRBNB', 'MKRBTC',
           'MKRUSDT', 'MKRBUSD', 'ZRXBUSD', 'DCRUSDT', 'EVXBTC', 'ADXETH', 'BNBTUSD', 'BNBUSDC', 'XTZUPUSDT',
           'XTZDOWNUSDT', 'KAVABNB', 'KAVABTC', 'KAVAUSDT', 'XRPAUD', 'IOSTBNB', 'BALBTC', 'BALBUSD', 'YFIBNB',
           'YFIBTC', 'YFIBUSD', 'YFIUSDT', 'BALUSDT', 'KMDUSDT', 'REQBTC', 'WAVESETH', 'DASHBNB', 'JSTBNB', 'JSTBTC',
           'JSTBUSD', 'JSTUSDT', 'SRMBNB', 'SRMBTC', 'SRMBUSD', 'SRMUSDT', 'ANTBNB', 'ANTBTC', 'ANTBUSD', 'ANTUSDT',
           'CRVBNB', 'CRVBTC', 'CRVBUSD', 'CRVUSDT', 'NMRBNB', 'NMRBTC', 'NMRBUSD', 'NMRUSDT', 'DOTBNB', 'DOTBTC',
           'DOTBUSD', 'DOTUSDT', 'RSRBNB', 'RSRBTC', 'RSRBUSD', 'RSRUSDT', 'BTCPAX', 'ETHPAX', 'PAXGBNB', 'DOTBIDR',
           'SXPAUD', 'YFIIBNB', 'YFIIBTC', 'YFIIBUSD', 'YFIIUSDT', 'KSMBNB', 'KSMBTC', 'KSMBUSD', 'KSMUSDT', 'UMABTC',
           'UMAUSDT', 'EOSUPUSDT', 'EOSDOWNUSDT', 'TRXUPUSDT', 'TRXDOWNUSDT', 'XRPUPUSDT', 'XRPDOWNUSDT', 'DOTUPUSDT',
           'DOTDOWNUSDT', 'WINGBNB', 'WINGBTC', 'WINGBUSD', 'WINGUSDT', 'LTCUPUSDT', 'LTCDOWNUSDT', 'SXPEUR', 'UNIBNB',
           'UNIBTC', 'UNIBUSD', 'UNIUSDT', 'OXTBTC', 'OXTUSDT', 'AVABNB', 'AVABTC', 'AVABUSD', 'AVAXBNB', 'HNTBTC',
           'HNTUSDT', 'SXPBIDR', 'UNIUPUSDT', 'UNIDOWNUSDT', 'SXPTRY', 'UTKBTC', 'UTKUSDT', 'XVSBNB', 'XVSBTC',
           'XVSBUSD', 'XVSUSDT', 'VIBBTC', 'SXPUPUSDT', 'SXPDOWNUSDT', 'SXPGBP', 'FILBNB', 'FILBTC', 'FILBUSD',
           'FILUSDT', 'FILUPUSDT', 'FILDOWNUSDT', 'YFIUPUSDT', 'YFIDOWNUSDT', 'INJBNB', 'INJBTC', 'INJBUSD', 'INJUSDT',
           'ONEUSDT', 'BCHUPUSDT', 'BCHDOWNUSDT', 'OSTETH', 'DOTEUR', 'MATICBNB', 'LTCEUR', 'RENBTCBTC', 'RENBTCETH',
           'ADAEUR', 'BCHABUSD', 'AVAXBTC', 'AVAXBUSD', 'SYSBUSD', 'XEMUSDT', 'XRPBRL', 'SKLBTC', 'SKLBUSD', 'SKLUSDT',
           'BCHEUR', 'YFIEUR', 'ZILBIDR', 'GLMBTC', 'GLMETH', 'XLMUPUSDT', 'XLMDOWNUSDT', 'LTCRUB', 'TRXTRY', 'XLMEUR',
           'GRTBTC', 'GRTETH', 'GRTUSDT', 'CELOBTC', 'CELOUSDT', 'CHZTRY', 'XLMTRY', 'GRTEUR', 'POWRBTC', 'STORJBTC',
           'RCNBTC', 'EOSEUR', 'LTCBRL', 'PAXGBTC', 'DOCKBTC', 'CKBBTC', 'CKBBUSD', 'NULSBTC', 'DOTTRY', 'GRTBUSD',
           'OMGBUSD', 'DOTGBP', 'ADATRY', 'ADABRL', 'ADAGBP', 'DOTBRL', 'ADAAUD', 'HOTTRY', 'AVAXUSDT', 'BTTTRY',
           'CHZBRL', 'UNIEUR', 'CHZBUSD', 'CHZEUR', 'CHZGBP', 'ADARUB', 'ENJBRL', 'ENJEUR', 'NEOTRY', 'CFXBTC',
           'CFXBUSD', 'CFXUSDT', 'ENJGBP', 'EOSTRY', 'LTCGBP', 'RVNTRY', 'XVGBUSD', 'BTTBRL', 'BTTEUR', 'HOTEUR',
           'WINEUR', 'BTGBUSD', 'BTGUSDT', 'HOTBUSD', 'ATOMBNB', 'FRONTETH', 'VETBUSD', 'VETEUR', 'WINBRL', 'HOTBRL',
           'WRXEUR', 'TRXAUD', 'TRXEUR', 'VETGBP']