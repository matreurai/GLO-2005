# Connect to the database
import mysql.connector
from Dict_projet import *

# Login base de donnee
conn = mysql.connector.connect(host="localhost", user="root",
                               password="eAXt)cdncT%Wv5}RVb!_,f]S", db="GLo-2005-Projet")
# Creation d'un curseur
cursor = conn.cursor()

# ajout du chemin entre notre table t_projet dans base de donne et les informations de binance.
proj = "INSERT INTO t_projet (projet_ticker, projet_logo, projet_nom_du_coin, projet_description, " \
       "projet_start_date,projet_forage_possible) VALUES (%(projet_ticker)s, %(projet_logo)s, " \
       "%(projet_nom_du_coin)s,%(projet_description)s,%(projet_start_date)s, %(projet_forage_possible)s) "

# ajout du chemin entre notre table t_cryptomonaie dans base de donne et les informations de binance.
crypto = "INSERT INTO t_cryptomonnaie (cryptomonnaie_id,cryptomonnaie_ticker,cryptomonnaie_nom_du_coin," \
         "cryptomonnaie_prix_actuel,cryptomonnaie_prix_haut,cryptomonnaie_prix_bas,cryptomonnaie_Valeur_cad," \
         "cryptomonnaie_market_cap,cryptomonnaie_max_supply,cryptomonnaie_qte_circulation," \
         "cryptomonnaie_volume_24h,cryptomonnaie_logo) VALUES (%(cryptomonnaie_id)s, %(cryptomonnaie_ticker)s," \
         "%(cryptomonnaie_nom_du_coin)s, %(cryptomonnaie_prix_actuel)s, %(cryptomonnaie_prix_haut)s," \
         "%(cryptomonnaie_prix_bas)s, %(cryptomonnaie_Valeur_cad)s, %(cryptomonnaie_market_cap)s," \
         "%(cryptomonnaie_max_supply)s, %(cryptomonnaie_qte_circulation)s,%(cryptomonnaie_volume_24h)s," \
         "%(cryptomonnaie_logo)s)"

# ajout du chemin entre notre table t_utilisateur dans base de donne et les informations de binance.
util = "INSERT INTO t_utilisateur (utilisateur_id, utilisateur_username,utilisateur_email, " \
       "utilisateur_phone,utilisateur_prenom, utilisateur_nom,utilisateur_date_creation) VALUES (%(utilisateur_id)s, " \
       "%(utilisateur_username)s, %(utilisateur_email)s, %(utilisateur_phone)s,%(utilisateur_prenom)s, " \
       "%(utilisateur_nom)s, %(utilisateur_date_creation)s)"

# ajout du chemin entre notre table t_alerte dans base de donne et les informations de binance.
alerte = "INSERT INTO t_alerte (alerte_id, alerte_user, alerte_ticker, alerte_below_price, alerte_above_price," \
         "alerte_end_date) VALUES (%(alerte_id)s, %(alerte_user)s, %(alerte_ticker)s, %(alerte_below_price)s, " \
         "%(alerte_above_price)s,%(alerte_end_date)s)"

portfolio = "INSERT INTO t_portfolio (portfolio_id,portfolio_user,portfolio_balance,portfolio_profit_total," \
            "portfolio_cout_total,portfolio_qte_coin_diff,portfolio_ratio) VALUES(%(portfolio_id)s," \
            "%(portfolio_user)s, %(portfolio_balance)s,%(portfolio_profit_total)s,%(portfolio_qte_coin_diff)s," \
            "%(portfolio_qte_coin_diff)s, %(portfolio_ratio)s)"

titre = "INSERT INTO t_titre (titre_crypto_id,titre_portfolio_id,titre_qte,titre_valeur_courante," \
        "titre_prix_moyen_paye,titre_ratio) VALUES (%(titre_crypto_id)s,%(titre_portfolio_id)s,%(titre_qte)s," \
        "%(titre_valeur_courante)s,%(titre_prix_moyen_paye)s,%(titre_ratio)s)"

data_proj = {'projet_ticker': 'BTCUSD', 'projet_logo': 'LOL', 'projet_nom_du_coin': 'BITCOIN',
             'projet_description': 'MOVIE', 'projet_start_date': '2002-08-21', 'projet_forage_possible': True}
cursor.execute(proj, data_proj)
cryptomonnaie_id = cursor.lastrowid

data_crypto = {'cryptomonnaie_id': cryptomonnaie_id, 'cryptomonnaie_ticker': 'BTCUSD',
               'cryptomonnaie_nom_du_coin': 120.3, 'cryptomonnaie_prix_actuel': 120.3, 'cryptomonnaie_prix_haut': 120.3,
               'cryptomonnaie_prix_bas': 120.3, 'cryptomonnaie_Valeur_cad': 1234563, 'cryptomonnaie_market_cap': 123432,
               'cryptomonnaie_max_supply': 12344564554533, 'cryptomonnaie_qte_circulation': 123421123,
               'cryptomonnaie_volume_24h': 1234.56, 'cryptomonnaie_logo': 'lollll'}
cursor.execute(crypto, data_crypto)

data_util = {'utilisateur_id': '1', 'utilisateur_username': 'javapist', 'utilisateur_email': 'imnice@bool.com',
             'utilisateur_phone': '514-445-4108', 'utilisateur_prenom': 'Jean', 'utilisateur_nom': 'Du Jardin',
             'utilisateur_date_creation': '2004-04-20'}
cursor.execute(util, data_util)

alerte_id = cursor.lastrowid
data_alerte = {'alerte_id': alerte_id, 'alerte_user': '1', 'alerte_ticker': 'BTCUSD', 'alerte_below_price': '1.090',
               'alerte_above_price': '3.45', 'alerte_end_date': '2020-04-19'}
cursor.execute(alerte, data_alerte)

data_portfolio = {'portfolio_id': '1', 'portfolio_user': '1', 'portfolio_balance': '1000.00',
                  'portfolio_profit_total': '100.00', 'portfolio_cout_total': '134.03',
                  'portfolio_qte_coin_diff': '20', 'portfolio_ratio': '30'}
cursor.execute(portfolio, data_portfolio)

data_titre = {'titre_crypto_id': cryptomonnaie_id, 'titre_portfolio_id': '1', 'titre_qte': '30',
              'titre_valeur_courante': '134.4', 'titre_prix_moyen_paye': '130.09', 'titre_ratio': '20'}
cursor.execute(titre, data_titre)

conn.commit()
cursor.close()
conn.close()
