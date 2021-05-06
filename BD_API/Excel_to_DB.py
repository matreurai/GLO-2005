
import mysql.connector
import xlrd

db = mysql.connector.connect(host="localhost", user="root",
                             password="eAXt)cdncT%Wv5}RVb!_,f]S", db="GLO-2005-Projet")
cur = db.cursor()

# peuple_table_t_projet = 'CREATE TABLE IF NOT EXISTS `t_projet`(projet_ticker VARCHAR(9) NOT NULL,' \
#                         'projet_logo VARCHAR(60),projet_nom_du_coin VARCHAR(20) NOT NULL,' \
#                         'projet_description VARCHAR(300),projet_start_date DATE, projet_forage_possible BOOLEAN,' \
#                         'PRIMARY KEY(projet_ticker),UNIQUE(projet_ticker))'
#
# cur.execute(peuple_table_t_projet)

excel_projet = xlrd.open_workbook('Crypto.xlsx')

excel_t_proj_sheet = excel_projet.sheet_names()

insert_proj = 'INSERT INTO t_projet (projet_ticker, projet_logo, projet_nom_du_coin, ' \
              'projet_description, projet_start_date, projet_forage_possible) VALUES (%s,%s,%s,%s,%s,%s)'

insert_t_crypto = 'INSERT INTO t_cryptomonnaie(cryptomonnaie_id, cryptomonnaie_ticker, ' \
                  'cryptomonnaie_nom_du_coin, cryptomonnaie_prix_actuel, cryptomonnaie_prix_haut, ' \
                  'cryptomonnaie_prix_bas, cryptomonnaie_valeur_usd, cryptomonnaie_market_cap, ' \
                  'cryptomonnaie_max_supply, cryptomonnaie_qte_circulation, cryptomonnaie_volume_24h, ' \
                  'cryptomonnaie_logo) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'



for v in range(0, len(excel_t_proj_sheet)):
    t_proj = excel_projet.sheet_by_index(v)

    for x in range(1, t_proj.nrows):
        proj_ticker = symbols

        proj_coin_url = t_proj.cell(x, 1).value

        proj_nom_du_coin = t_proj.cell(x, 2).value

        proj_description = t_proj.cell(x, 3).value

        proj_start_date = t_proj.cell(x, 4).value

        proj_forage_possible = t_proj.cell(x, 5).value

        t_proj_values = (proj_ticker, proj_coin_url, proj_nom_du_coin, proj_description, proj_start_date,
                         proj_forage_possible)

        # crypto_id = cursor.lastrowid
        #
        # crypto_ticker = proj_ticker
        #
        # crypto_nom_du_coin = proj_nom_du_coin
        #
        # crypto_prix_actuel = t_proj.cell(x, 7).value
        #
        # crypto_prix_haut = t_proj.cell(x, 8).value
        #
        # crypto_prix_bas = t_proj.cell(x, 9).value
        #
        # crypto_valeur_usd = t_proj.cell(x, 10).value
        #
        # crypto_market_cap = t_proj.cell(x, 11).value
        #
        # crypto_max_supply = t_proj.cell(x, 12).value
        #
        # crypto_qte_circulation = t_proj.cell(x, 13).value
        #
        # crypto_volume_24h = t_proj.cell(x, 14).value
        #
        # crypto_logo = proj_coin_url
        #
        # crypto_values = (crypto_id, crypto_ticker, crypto_nom_du_coin, crypto_prix_actuel,crypto_prix_haut,
        #                  crypto_prix_bas, crypto_valeur_usd, crypto_market_cap,crypto_max_supply,
        #                  crypto_qte_circulation, crypto_volume_24h, crypto_logo)

        cur.execute(insert_proj, t_proj_values)
        # cur.execute(insert_t_cryptoj, crypto_values)
        db.commit()