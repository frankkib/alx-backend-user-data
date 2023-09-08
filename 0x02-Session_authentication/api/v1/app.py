#!/usr/bin/env python3
"""
Route module for the API
"""
from os import getenv
from api.v1.views.__init__ import app_views
from flask import Flask, jsonify, abort, request
from flask_cors import (CORS, cross_origin)
import os
from api.v1.auth.auth import Auth
from api.v1.auth.session_auth import SessionAuth


app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})
auth = None
if 'AUTH_TYPE' in os.environ:
    auth_type = os.environ['AUTH_TYPE']
    if auth_type == 'session_auth':
        auth = SessionAuth()
    else:
        auth = Auth()


@app.before_request
def before_request():
    """Executes this function before processing each request"""
    excluded_paths = [
            '/api/v1/status',
            '/api/v1/unauthorized/', '/api/v1/auth_session/login/']
    if request.path not in excluded_paths:
        auth_header = auth.authorization_header(request)
        session_cookie = auth.session_cookie(request)
        if auth_header is None and session_cookie is None:
            abort(401)

    request.current_user = auth.current_user(request)


@app.errorhandler(404)
def not_found(error) -> str:
    """ Not found handler
    """
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(401)
def unauthorized_error(error) -> str:
    """Unauthorized handler
    """
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def forbidden_error(error) -> str:
    """forbidden error handler
    """
    return jsonify({"error": "Forbidden"})


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
