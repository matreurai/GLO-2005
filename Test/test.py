from flask import Flask, request
from flask_restful import Resource, Api
from flask_jwt import JWT

from security import authenticate, identity


app = Flask(__name__)
app.secret_key = 'glo-project'
api = Api(app)

items =[]

#list will return a list of all name found in the list item 
#next will return only the first item of the list

class Item(Resource):
    def get(self,name):
        item = next(filter(lambda x: x['name'] == name,items))
        return {'item':None}, 200 if item else 404
    
    def post(self,name):
        if next(filter(lambda x: x['name'] == name,items)) is not None:
            return {'message': "An item with'{}' already exists.".format(name)}, 400

        data = request.get_json()
        item = {'name': name, 'price':data['price']}
        items.append(item)
        return item, 201
    
class ItemList(Resource):
    def get(self):
        return {'items': items}


api.add_resource(Item,'/item/<string:name>')
api.add_resource(ItemList, '/items')

app.run(port=5000, debug=True)

