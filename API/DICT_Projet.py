





import json
import http.client

#--- Entite projet


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