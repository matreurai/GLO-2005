import mysql.connector
import http.client
import json
import xlrd

usage = """%prog"""

# Traitement de la donner de Coinmarket
conn = http.client.HTTPSConnection("pro-api.coinmarketcap.com")
payload = ''
headers = {
    'X-CMC_PRO_API_KEY': '618906da-2cdf-4e16-8356-3bd45841e5aa',
    'Accept': 'application/json',
    'Cookie': '__cfduid=dc40f08c990d9bb9621b3e61584f6e5951619128567'
}
conn.request("GET", "/v1/cryptocurrency/listings/latest?limit=2", payload, headers)
res = conn.getresponse()
data = res.read()
respond = data.decode("utf-8")

dict_data = json.loads(respond)['data']
dict_quote = [v['quote'] for v in dict_data if v['quote']]
dict_usd = [v['USD'] for v in dict_quote if v['USD']]

p_ticker=[]
projet_ticker = [v['symbol'] for v in dict_data if v['symbol']]
for i in projet_ticker:
    p_ticker.append(i.split(','))

p_nom_du_coin = []
projet_nom_du_coin = [v['name'] for v in dict_data if v['name']]
for i in projet_nom_du_coin:
    p_nom_du_coin.append(i.split(','))


p_start_date = []
projet_start_date = [v['date_added'] for v in dict_data if v['date_added']]
for i in projet_start_date:
    p_start_date.append(i.split(','))

# importation donner du fichier excel dans un dictionnaire

excel_projet = xlrd.open_workbook('Crypto.xlsx')

excel_t_proj_sheet = excel_projet.sheet_names()


p_logo = []
p_description = []
p_forage = []

for v in range(0, len(excel_t_proj_sheet)):
    t_proj = excel_projet.sheet_by_index(v)

    # for x in range(1, t_proj.nrows):
    for x in range(1, 2):

        projet_logo = t_proj.cell(x, 1).value
        p_logo.append(projet_logo)

        projet_description = t_proj.cell(x, 3).value
        p_description.append(projet_description)

        projet_forage_possible = t_proj.cell(x, 5).value
        p_forage.append(projet_forage_possible)
#
# # price = [v['price'] for v in dict_usd if v['price']]
# # dict_price = {'price': price}
#
dict_t_proj = []
list_t_proj = {"projet_ticker": p_ticker, "projet_logo": p_logo, "projet_nom_du_coin":p_nom_du_coin,
               "projet_description": p_description, "projet_start_date":p_start_date,
               "projet_forage_possible":projet_forage_possible}
dict_t_proj.append(list_t_proj)

with open("t_projet.json", "w") as outfile:
    json.dump(dict_t_proj, outfile)

with open("t_projet.json") as json_file:
    t_projet = json.load(json_file)



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