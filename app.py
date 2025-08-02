import flask
from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to the Flask App!"  


rednder_template = flask.render_template