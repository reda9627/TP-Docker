import os

from flask import Flask
from pymongo import MongoClient
from pymongo.errors import PyMongoError

app = Flask(__name__)


MONGO_URI = os.environ.get("MONGO_URI", "mongodb://localhost:27017")
client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)


@app.route("/")
def hello_world():
    return "Hello, World!  <br> <a href='/db-check'>Check MongoDB Connection</a>"


@app.route("/db-check")
def db_check():
    try:
        client.admin.command("ping")
        return "Connexion a MongoDB reussie !"
    except PyMongoError as e:
        return f"Echec de connexion a MongoDB : {e}", 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3500, debug=True)
