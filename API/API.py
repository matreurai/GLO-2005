#-------------------------------
# Test API Binance
# David Bolduc
#-------------------------------

import json
import http.client
from flask import Flask ,render_template , request
from flask_mysqldb import MySQL
import MySQLdb
from API.time_stamp import *

# Init App
app = Flask(__name__)
# Init Server
db = MySQLdb.connect("localhost","root","eAXt)cdncT%Wv5}RVb!_,f]S","GLO-2005-Projet")

# Def du cursor
cur = db.cursor()

#Route de la page home
@app.route('/Home')
# time stamp

def mise_a_jour():
      return None

if __name__ == '__main__':
      app.run(debug=True)

def exchange_dict ():
  conn = http.client.HTTPSConnection("api.binance.com")
  payload = ''
  headers = {
    'Content-Type': 'application/json'
  }
  conn.request("GET", "/api/v3/exchangeInfo", payload, headers)
  res = conn.getresponse()
  data = res.read()
  transfor = data.decode("utf-8")
  exchange_dict = json.loads(transfor)
  print (type(exchange_dict['symbols']))
  
  for stocks in exchange_dict['symbols']:
    return (stocks['symbol'])