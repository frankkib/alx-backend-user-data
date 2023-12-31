#!/usr/bin/env python3
"""Basic authentication class
"""
from flask import request
from typing import List, TypeVar
import os


class Auth:
    """Authentication class defination"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Determinis if authentication is required for a give path
        """
        if path is None:
            return True
        if excluded_paths is None or not excluded_paths:
            return True
        slash = path + '/'

        return path not in excluded_paths and slash not in excluded_paths

    def authorization_header(self, request=None) -> str:
        """Etracts the authorization header from the request
        """
        if request is None:
            return None
        if 'Authorization' not in request.headers:
            return None
        return request.headers['Authorization']

    def current_user(self, request=None) -> TypeVar('User'):
        """Retrieves the current user based on request
        """
        return None

    def session_cookie(self, request=None):
        """Get the value of the session cookie from a request.
        """
        if request is None:
            return None
        cookie_name = os.environ.get("SESSION_NAME")
        session_cookie_value = request.cookies.get(cookie_name)
        return session_cookie_value
