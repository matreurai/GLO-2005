import pymysql.cursors

# Connect to the database
from pymysql.connections import Connection

conn: Connection = pymysql.connect(host="localhost",
                                   user="root",
                                   password="eAXt)cdncT%Wv5}RVb!_,f]S",
                                   db="GLo-2005-Projet",
                                   cursorclass=pymysql.cursors.DictCursor)
with conn:
    with conn.cursor() as t_proj:
        # Create a new record
        proj = "INSERT INTO t_projet (projet_ticker, projet_logo, projet_nom_du_coin,projet_secteur_activite, " \
               "projet_description, projet_start_date,projet_forage_possible ) VALUES (%s, %s, %s, %s,%s, %s, %s) "
        t_proj.execute(proj, ('BTCUSD', 'LOL', 'Bitcoin', 'Movie', 'Coin du bit coins', '2002-08-21', True))

    with conn.cursor() as t_crypto:
        # Create a new record crypto = "INSERT INTO t_cryptomonnaie (cryptomonnaie_id,
        crypto = "INSERT INTO t_cryptomonnaie (cryptomonnaie_id,cryptomonnaie_ticker, cryptomonnaie_ticker,cryptomonnaie_nom_du_coin," \
                 "cryptomonnaie_prix_actuel,cryptomonnaie_prix_haut,cryptomonnaie_prix_bas,cryptomonnaie_Valeur_cad," \
                 "cryptomonnaie_market_cap,cryptomonnaie_max_supply,cryptomonnaie_qte_circulation," \
                 "cryptomonnaie_volume_24h,cryptomonnaie_logo) " \
                 "VALUES (%s, %s, %s,%s, %s, %s,%s, %s, %s, %s,%s)"
        t_crypto.execute(crypto, (1,'Bitcoin', 120.3, 120.3, 120.3, 120.3, 1234563, 123432, 12344564554533,
                                  123421123, 'lollll'))

    with conn.cursor() as t_util:
        # Create a new record util = "INSERT INTO t_utilisateur (utilisateur_id,
        util = "INSERT INTO T_utilisateur (utilisateur_id, utilisateur_username,utilisateur_password,utilisateur_email," \
               "utilisateur_phone,utilisateur_prenom, utilisateur_nom,utilisateur_date_creation) " \
               "VALUES (%s, %s, %s, %s,%s, %s, %s,%s)"
        t_util.execute(util, (1, 'jarvis', 'asedrres', 'jaime@love.com', '450-123-4567', 'Jean', 'Dujardins',
                              '2020-12-31'))

    with conn.cursor() as t_alert:
        # Create a new record alerte = "INSERT INTO t_alerte (alerte_id, alerte_user,
        alerte = "INSERT INTO t_alerte (alerte_ticker, alerte_user, alerte_ticker, alerte_below_price, alerte_above_price,alerte_end_date) " \
                 "VALUES (%s, %s, %s, %s, %s, %s)"
        t_alert.execute(alerte, (1, 9, 'Bitcoin', 120.3, 119.3, '2021-06-01'))

    # connection is not autocommit by default. So you must commit to save
    # your changes.
    conn.commit()

    with conn.cursor() as t_proj:
        # Read a single record
        proj = "SELECT projet_ticker FROM t_projet WHERE projet_secteur_activite=%s"
        t_proj.execute(proj, ('Movie',))
        result = t_proj.fetchone()
        print(result)
