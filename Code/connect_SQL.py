import sys

import mysql.connector
from mysql.connector import Error


def connect():
    #Connection to databases
    conn = None
    try:
        conn = mysql.connector.connect(host='localhost',
                                        database='glo-2005-projet',
                                        user= 'root',
                                        password='christopher')
        if conn.is_connected():
            print('Connected to Project')
    except Error as e:
        print(e)
    
    finally:
        if conn is not None and conn.is_connected():
            conn.close()
if __name__ == '__main__':
    connect()