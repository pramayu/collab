from os import getenv
from flask import Flask
from pymongo import MongoClient
from app.configure.basic import Development
from dotenv import load_dotenv
from app.controller.blueprint.home import homepage

app = Flask(__name__)
app.config.from_object(Development)
client = MongoClient(getenv('MONGODB_URI'))
app.register_blueprint(homepage)
db = client.db_collab