import mysql.connector
import pymysql
import http.client
import json
import xlrd
import pandas as pd
from sqlalchemy import create_engine



# Traitement de la donner de Coinmarket
# Connection a coinmarket
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

# Creation des dictionnaires.
dict_data = json.loads(respond)['data']
dict_quote = [v['quote'] for v in dict_data if v['quote']]
dict_usd = [v['USD'] for v in dict_quote if v['USD']]
#Projet ticker coin
projet_ticker = [v['symbol'] for v in dict_data if v['symbol']]
# Nom des coins
projet_nom_du_coin = [v['name'] for v in dict_data if v['name']]
# Projet start date
projet_start_date = [v['date_added'] for v in dict_data if v['date_added']]
# print(projet_start_date)
# price = [v['price'] for v in dict_usd if v['price']]

# importation donner du fichier excel dans un dictionnaire

excel_projet = xlrd.open_workbook('Crypto.xlsx')

excel_t_proj_sheet = excel_projet.sheet_names()

p_logo = []
p_description = []
p_forage = []
p_start =[]

for v in range(0, len(excel_t_proj_sheet)):
    t_proj = excel_projet.sheet_by_index(v)

    for x in range(1, t_proj.nrows):

        projet_logo = t_proj.cell(x, 1).value
        p_logo.append(projet_logo)

        projet_description = t_proj.cell(x, 3).value
        p_description.append(projet_description)

        projet_start_date = t_proj.cell(x, 4).value
        p_start.append(projet_start_date)

        projet_forage_possible = t_proj.cell(x, 5).value
        p_forage.append(projet_forage_possible)



t_cryptomonnaie ={'cryptomonnaie_id','cryptomonnaie_ticker','cryptomonnaie_nom_du_coin','cryptomonnaie_prix_actuel',
                  'cryptomonnaie_prix_haut','cryptomonnaie_prix_bas','cryptomonnaie_Valeur_cad'}

list_t_projet = 't_projet'
t_project_frame = pd.DataFrame(data=t_projet)

sqlEngine = create_engine('mysql+pymysql://root:eAXt)cdncT%Wv5}RVb!_,f]S@localhost/GLO-2005-Projet', pool_recycle=3600)

dbConnection = sqlEngine.connect()

try:

    frame = t_project_frame.to_sql(list_t_projet, dbConnection, if_exists='append',index=False);

except ValueError as vx:

    print(vx)

except Exception as ex:

    print(ex)

else:

    print("Table %s created successfully."%t_table);

finally:

    dbConnection.close()
