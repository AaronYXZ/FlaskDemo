## https://www.udemy.com/rest-api-flask-and-python/learn/v4/t/lecture/5960110?start=585
## https://www.udemy.com/rest-api-flask-and-python/learn/v4/t/lecture/5960120?start=34

from flask import Flask, jsonify, request
## package starts with lower case letter f, Class starts with upper case letter F

app = Flask(__name__)

# @app.route("/") ## decorator 'http://www.google.com/' forward slash is home page

stores = [
    {
        'name': 'My Wonderful Store',
        'item':[
            {
                'name': 'My Item',
                'price': 15.99
            }
        ]
    }
]

# def home():
#     return "Hello World!"
# POST - used to receive data
# GET - used to send data back only

# POST /store data:{name:} create a new store with a given name
@app.route('/store', methods = ['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name':request_data['name'],
        'items':[]
    }
    stores.append(new_store)
    return jsonify({"stores":new_store}) ##

# GET /store/<string:name> get a store given a name and return some data about it
@app.route('/store/<string:name>')
# 'http://127.0.0.1:5000/store/some_name some_name will be the name passed to func get_score
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({"message": "store not found"})


# GET /store return a list of all the stores
@app.route('/store')
def get_stores():
    return jsonify({'stores': stores}) ## convert stores to json

# POST /store/<string:name>/item {name:, price: } create an item inside a store with a given name
@app.route('/store/<string:name>/item', methods = ['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name': request_data['name'],
                'price':request_data['price']
            }
        stores['items'].append(new_item)
        return jsonify(new_item)
    return jsonify({'stores': stores})

# GET /store/<string:name>/item get a list of all the items inside a specific store
@app.route('/store/<string:name>/item')
def get_item_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({"items": store['items']})
    return jsonify({"message": "store not found"})
app.run(port = 5001)