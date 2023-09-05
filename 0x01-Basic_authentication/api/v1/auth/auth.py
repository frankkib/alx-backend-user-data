#!/usr/bin/env python3
"""Basic authentication class
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """Authentication class defination"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Determinis if authentication is required for a give path
        """
        return False

    def authorization_header(self, request=None) -> str:
        """Etracts the authorization header from the request
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Retrieves the current user based on request
        """
        return None
