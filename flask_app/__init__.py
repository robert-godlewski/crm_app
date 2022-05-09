from flask import Flask
from flask_app.config.project_key import flask_key


app = Flask(__name__)
app.secret_key = flask_key
