#!/usr/bin/env python3
"""
The flask app module
"""
from flask import Flask, jsonify


app = Flask(__name__)


@app.route("/", methods=['GET'], strict_slashes=False)
def welcome():
    """
    Returns a welcome message in JSON format.
    """
    message = {"message": "Bienvenue"}
    return message


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
