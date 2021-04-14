#-------------------------------
# Test API Binance
# David Bolduc
#-------------------------------

import requests
import json
import http.client




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