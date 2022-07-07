from flask import Flask, jsonify, request
from flask_cors import CORS
import pymongo

# Replace your URL here. Don't forget to replace the password.
connection_url = 'mongodb+srv://billiedartnell:<password>@cluster0.0z2m7lp.mongodb.net/?retryWrites=true&w=majority'
app = Flask(__name__)
client = pymongo.MongoClient(connection_url)

# Database
Database = client.get_database('example')
# Table
SampleTable = Database.sample


@app.route('/')
def hello():
    return jsonify({"hello": "world"}), 200


@app.route('/db', methods=["GET", "POST"])
def get_db():
    if request.method == 'GET':

        query = SampleTable.find()
        output = {}
        i = 0
        for x in query:
            output[i] = x
            output[i].pop('_id')
            i += 1
        return jsonify(output)
    elif request.method == 'POST':
        return jsonify('message: hello')


if __name__ == '__main__':
    app.run(debug=True)
