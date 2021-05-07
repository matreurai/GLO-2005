import mysql.connector
from mysql.connector import errorcode


def creation_t_projet():
    DB_NAME = '`GLO-2005-Projet`'

    TABLES= {}
    TABLES['t_projet'] = (
        "CREATE TABLE IF NOT EXISTS `t_projet` ("
        "`projet_ticker` VARCHAR(9) NOT NULL,"
        "`projet_logo` VARCHAR(50),"
        "`projet_nom_du_coin` VARCHAR(50) NOT NULL,"
        "`projet_description` VARCHAR(300),"
        "`projet_start_date` DATE,"
        "`projet_forage_possible` BOOLEAN, "
        "PRIMARY KEY(`projet_ticker`), UNIQUE(`projet_ticker`)) "
        "ENGINE InnoDB")

    create_index_t_projet = (" CREATE INDEX `idx_projet` ON `t_projet`(`projet_ticker`) ")

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

    for table_name in TABLES:
        table_description = TABLES[table_name]
        try:
            print("Creating table {}: ".format(table_name), end='')
            cur.execute(table_description,create_index_t_projet)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("already exists.")
            else:
                print(err.msg)
        else:
            print("OK")

        cur.close()
        db.close()

print(creation_t_projet())