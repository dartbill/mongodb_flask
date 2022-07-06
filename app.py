from flask import Flask, jsonify
from flask_cors import CORS
import pymongo
  
# Replace your URL here. Don't forget to replace the password.
connection_url = 'mongodb+srv://billiedartnell:Orangelemon19@cluster0.0z2m7lp.mongodb.net/?retryWrites=true&w=majority'
app = Flask(__name__)
client = pymongo.MongoClient(connection_url)
  
# Database
Database = client.get_database('sample_restaurants')
# Table
SampleTable = Database.sample_restaurants


@app.route('/')
def hello():
    return jsonify({"hello": "world"}),200

if __name__ == '__main__':
    app.run(debug=True)
