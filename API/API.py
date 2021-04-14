#-------------------------------
# Test API Binance
# David Bolduc
#-------------------------------

import requests
import json
import http.client
import API.connect_SQL
from flask import Flask ,
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'GLO-2005-projet'

mysql = MySQL(app)

@approute('/')
def index():
      return render_template('home.html')

if __name__ == '__main__':
      app.run(debug=True)


url = "https://api.binance.com/wapi/v3/systemStatus.html"

payload={}
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)



conn = http.client.HTTPSConnection("api.binance.com")
payload = ''
headers = {
  'Content-Type': 'application/json'
}
conn.request("GET", "/api/v3/ticker/24hr?symbol=BTCUSDT", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))

url = "https://api.binance.com/api/v3/exchangeInfo"

payload={}
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)