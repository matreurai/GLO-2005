#-------------------------------
# Test API Binance
# David Bolduc
#-------------------------------

from flask import Flask, jsonify, request, render_template


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
        request_data = request.get_json()
        new_store = {
            'name': request_data['name'],
            'items':[]
        }
        stores.append(new_store)
        return jsonify(new_store)

#GET /store/<string:name>
@app.route('/store/<string:name>')
def get_store(name):
    # Iterate over stores
    for store in stores:
    # if the store name matches , return it
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'message':'store not found'})
    # if none match, return error message

# GET/store
@app.route('/store')
def get_stores():
    return jsonify({'stores':stores})

# POST /store/<string:name> (name:, price:)
@app.route('/store/<string:name>', methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name':request_data['name'],
                'price':request_data['price']
            }
        store['items'].append(new_item)
        return jsonify(new_item)
    return jsonify({'message': 'store not found'})    

# GET /store/<string:name>/item
@app.route('/store/<string:name>/item')
def get_item_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items':store['items']})
    return jsonify({'message': 'store not found'})

app.run(port=5000)    
