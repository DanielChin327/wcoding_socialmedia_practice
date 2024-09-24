from app import app, db
from flask import jsonify, request


@app.route("/hello", methods = ["GET"])
def hello_world():
    return "Hello People"
