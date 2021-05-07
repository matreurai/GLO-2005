import mysql.connector
from mysql.connector import errorcode

DB_NAME = '`GLO-2005-Projet`'

TABLES= {}
TABLES['t_cryptomonnaie'] = (
    'CREATE TABLE IF NOT EXISTS `t_cryptomonnaie`('
    '`cryptomonnaie_id` SMALLINT NOT NULL,'
    '`cryptomonnaie_ticker` VARCHAR(9) NOT NULL,'
    '`cryptomonnaie_prix_haut` DECIMAL(13,10),'
    '`cryptomonnaie_prix_bas` DECIMAL(13,10),'
    '`cryptomonnaie_market_cap` BIGINT,'
    '`cryptomonnaie_qte_circulation` BIGINT,'
    '`cryptomonnaie_volume_24h` BIGINT,'
    'PRIMARY KEY (`cryptomonnaie_id`),'
    'FOREIGN KEY (`cryptomonnaie_ticker`) '
    'REFERENCES `t_projet`(`projet_ticker`));'
    'ALTER TABLE `t_cryptomonnaie` ENGINE InnoDB,'
    'COLLATE utf8mb4_unicode_ci; '
    'CREATE INDEX `idx_crypto` ON `t_cryptomonnaie`(`cryptomonnaie_id`)')

db = mysql.connector.connect(user='root', password='eAXt)cdncT%Wv5}RVb!_,f]S')
cur = db.cursor()

def create_database(cur):
    try:
        cur.execute(
            "CREATE DATABASE IF NOT EXISTS {} DEFAULT CHARACTER SET 'utf8mb4'".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)

try:
    cur.execute("USE {}".format(DB_NAME))
except mysql.connector.Error as err:
    print("Database {} does not exists.".format(DB_NAME))
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        create_database(cur)
        print("Database {} created successfully.".format(DB_NAME))
        db.database = DB_NAME
    else:
        print(err)
        exit(1)

def create_table_t_project():
    for table_name in TABLES:
        table_description = TABLES[table_name]
        try:
            print("Creating table {}: ".format(table_name), end='')
            cur.execute(table_description)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("already exists.")
            else:
                print(err.msg)
        else:
            print("OK")

        cur.close()
        db.close()