#-------------------------------
# Test API Binance
# David Bolduc
#-------------------------------

from flask import Flask, jsonify


#POST - used to receive data
#GET - used to send data

#POST /store data:(name:)
app = Flask(__name__)

stores = [
    {       
        'name': 'My Wonderful Store',
        'items': [
            {
            'name': 'My item',
            'price': 15.99
            }
        ]
    }
]

@app.route('/store', methods=['POST'])
def create_store():
    pass

#GET /store/<string:name>
@app.route('/store/<string:name>')
def get_store(name):
    pass

# GET/store
@app.route('/store/')
def get_stores():
    return jsonify(stores)

# POST /store/<string:name> (name:, price:)
@app.route('/store/<string:name>', methods=['POST'])
def create_item_in_store(name):
    pass

# GET /store/<string:name>/item
@app.route('/store/<string:name>/item')
def get_item_in_store(name):
    pass

app.run(port=5000)    
