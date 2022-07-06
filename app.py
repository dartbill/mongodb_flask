from flask import Flask, jsonify
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://billiedartnell:Orangelemon19@cluster0.0z2m7lp.mongodb.net/?retryWrites=true&w=majority"
mongo = PyMongo(app)

@app.route("/")
def home_page():
    online_users = mongo.db.users.find({"online": True})
    return jsonify({"message": "welcome"})