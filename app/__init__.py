from os import getenv
from flask import Flask
from pymongo import MongoClient
from flask_graphql import GraphQLView
from app.configure.basic import Development
from dotenv import load_dotenv
from app.controller.blueprint.home import homepage
from app.controller import schema

app = Flask(__name__)
app.config.from_object(Development)
client = MongoClient(getenv('MONGODB_URI'))
app.register_blueprint(homepage)
db = client.db_collab
app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))