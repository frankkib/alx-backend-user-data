#!/usr/bin/env python3
"""
The flask app module
"""
from flask import Flask, jsonify, request, abort
from auth import Auth


app = Flask(__name__)

AUTH = Auth()


@app.route("/", methods=['GET'], strict_slashes=False)
def welcome():
    """
    Returns a welcome message in JSON format.
    """
    message = {"message": "Bienvenue"}
    return message


@app.route("/users", methods=['POST'], strict_slashes=False)
def register_users():
    """
    Function that registers new users
    """
    email = request.form.get("email")
    password = request.form.get("password")
    try:
        existing_user = AUTH.register_user(email, password)
        response_data = {"email": email, "message": "User created"}
        return jsonify(response_data), 200
    except ValueError:
        error_message = {"message": "email already registered"}
        return jsonify(error_message), 400


@app.route("/sessions", methods=['POST'], strict_slashes=False)
def login():
    """
    function for logging in
    """
    email = request.form.get("email")
    password = request.form.get("password")
    if not AUTH.valid_login(email, password):
        abort(401)

    session_id = AUTH.create_session(email)
    session_id = str(session_id)
    response = jsonify({"email": email, "message": "logged in"})
    response.set_cookie("session_id", session_id)
    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
