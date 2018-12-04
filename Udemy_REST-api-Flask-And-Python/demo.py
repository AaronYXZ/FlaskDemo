## https://www.udemy.com/rest-api-flask-and-python/learn/v4/t/lecture/5960110?start=585

from flask import Flask
## package starts with lower case letter f, Class starts with upper case letter F

app = Flask(__name__)

# @app.route("/") ## decorator 'http://www.google.com/' forward slash is home page


# def home():
#     return "Hello World!"
# POST - used to receive data
# GET - used to send data back only

# POST /store data:{name} create a new store with a given name
# GET /store/<string:name> get a store given a name and return some data about it
# GET /store return a list of all the stores
# POST /store/<string:name>/item create an item inside a store with a given name
# GET /store/<string:name>/item get a list of all the items inside a specific store

app.run(port = 5001)