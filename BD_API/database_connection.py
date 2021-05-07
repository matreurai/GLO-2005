import mysql.connector
from mysql.connector import errorcode

def db_connection():
    try:
        db = mysql.connector.connect(host='localhost', user='root', password='eAXt)cdncT%Wv5}RVb!_,f]S',
                                     db='GLO-2005-Projet', use_pure=False)

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        db.close()
    return 'GLO-2005 est connecte'





# mySql_insert_query = 'CREATE TABLE IF NOT EXISTS `t_projet` (`projet_ticker` VARCHAR(9) NOT NULL,' \
#                      '`projet_logo` VARCHAR(50),`projet_nom_du_coin` VARCHAR(50) NOT NULL,' \
#                      '`projet_description` VARCHAR(300),`projet_start_date` DATE,' \
#                      '`projet_forage_possible` BOOLEAN, PRIMARY KEY(`projet_ticker`), UNIQUE(`projet_ticker`)); ' \
#                      'ALTER TABLE `t_projet` ENGINE InnoDB, CHARACTER SET utf8mb4, COLLATE utf8mb4_unicode_ci;' \
#                      'CREATE INDEX `idx_projet` ON `t_projet`(`projet_ticker`);'

