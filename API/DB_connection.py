import mysql.connector
from mysql.connector import errorcode


def connection():
    conn = mysql.connector.connect(host="localhost", user="root", password="eAXt)cdncT%Wv5}RVb!_,f]S",
                                   db="GLo-2005-Projet")
    return conn

