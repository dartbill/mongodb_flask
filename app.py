import json
from random import sample
from flask import Flask, jsonify, request
from flask_cors import CORS
from bson.json_util import dumps
import pymongo

# Replace your URL here. Don't forget to replace the password.
connection_url = 'mongodb+srv://billiedartnell:Orangelemon19@cluster0.0z2m7lp.mongodb.net/?retryWrites=true&w=majority'
app = Flask(__name__)
client = pymongo.MongoClient(connection_url)

# Database
Database = client.get_database('example')
# Table
SampleTable = Database.sample
CORS(app)


@app.route('/')
def hello():
    return jsonify({"hello": "world"}), 200


@app.route('/db', methods=["GET"])
def get_db():
    query = SampleTable.find()
    output = {}
    i = 0
    for x in query:
        output[i] = x
        output[i].pop('_id')
        i += 1
    return jsonify(output)


@app.route('/db/<name>', methods=["GET"])
def get_db_by_name(name):
    query = SampleTable.find_one({"name": name})

    output = {'name': query['name'], 'age': query['age']}
    # i = 0
    # for x in query:
    #     output[i] = x
    #     # output[i].pop('_id')
    #     i += 1
    return jsonify(output)


@ app.route('/db', methods=["POST"])
def post_db():
    new_user = request.get_json()
    SampleTable.insert_one(new_user)
    return jsonify('a new user has been added')


@ app.route('/db/:<id>', methods=["PATCH"])
def update_db():
    update_user = SampleTable.find_one({"name": id})
    data = request.get_json()
    SampleTable.update_one(update_user, data)
    return jsonify('a new user has been updated')


if __name__ == '__main__':
    app.run(debug=True)
