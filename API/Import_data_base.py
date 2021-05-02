
import pymysql.cursors
import xlrd

db = pymysql.connect(host="localhost", user="root",
                     password="eAXt)cdncT%Wv5}RVb!_,f]S", db="GLO-2005-Projet")
cur = db.cursor()

peuple_table_t_projet = 'CREATE TABLE IF NOT EXISTS `t_projet`(projet_ticker VARCHAR(9) NOT NULL,' \
                        'projet_logo VARCHAR(60),projet_nom_du_coin VARCHAR(20) NOT NULL,' \
                        'projet_description VARCHAR(300), projet_start_date DATE,' \
                        'projet_forage_possible BOOLEAN, PRIMARY KEY(projet_ticker),UNIQUE(projet_ticker))'

cur.execute(peuple_table_t_projet)

excel_projet = xlrd.open_workbook()
excel_t_proj_sheet =