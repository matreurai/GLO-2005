"""
Gestion des dictionnaires pour affichages live.
--- t_projet
1. projet_ticker
2. projet_logo
3. projet_nom_du_coin
4. projet_description
5. projet_start_date
6. projet_max_supply
7. projet_forage_possible
"""
from t_projet_import import *


def t_projet_live():
    t_projet_ticker = projet_nom_du_coin
    t_projet_logo = p_logo
    t_projet_nom_du_coin = projet_nom_du_coin
    t_projet_description = p_description
    t_projet_start_date = projet_start_date
    t_projet_max_supply = None
    t_projet_forage_possible = None
    return t_projet_ticker, t_projet_logo, t_projet_nom_du_coin, t_projet_description, t_projet_start_date, \
           t_projet_max_supply, t_projet_forage_possible


"""
--- Cryptomonnaie
1. cryptomonnaie_id
2. cryptomonnaie_ticker
3. cryptomonnaie_prix_haut
4. cryptomonnaie_prix_bas
5. cryptomonnaie_market_cap
6. cryptomonnaie_qte_circulation
7. cryptomonnaie_volume_24h
"""


def t_crypto_live():
    t_cryptomonnaie_id = None
    t_cryptomonnaie_ticker = None
    t_cryptomonnaie_prix_haut = None
    t_cryptomonnaie_prix_bas = None
    t_cryptomonnaie_market_cap = None
    t_cryptomonnaie_qte_circulation = None
    t_cryptomonnaie_volume_24h = None
    return t_cryptomonnaie_id, t_cryptomonnaie_ticker, t_cryptomonnaie_prix_haut, t_cryptomonnaie_prix_bas, \
           t_cryptomonnaie_market_cap, t_cryptomonnaie_qte_circulation, t_cryptomonnaie_volume_24h
