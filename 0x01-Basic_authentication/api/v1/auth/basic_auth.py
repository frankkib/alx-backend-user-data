#!/usr/bin/env python3
"""Basic auth class module"""
from api.v1.auth.auth import Auth
from models.user import User
from models import db as user_db
from typing import TypeVar
import base64


class BasicAuth(Auth):
    """The basic Authentication class"""
    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """Etracts base64 Authorization headers
        """
        if authorization_header is None or not isinstance(
                authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        return authorization_header[6:]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """Decodes a Base64-encoded string and returns the decoded value
        as utf-8 string
        """
        if base64_authorization_header is None or not isinstance(
                base64_authorization_header, str):
            return None
        try:
            decoded_bytes = base64.b64decode(base64_authorization_header)
            decoded_str = decoded_bytes.decode('utf-8')
            return decoded_str
        except Exception:
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """
        Etracts user email and password from a decoded Base64-encoded
        Authorization header.
        """
        if decoded_base64_authorization_header is None or not isinstance(
                decoded_base64_authorization_header, str):
            return None, None
        if ':' not in decoded_base64_authorization_header:
            return None, None
        user_email, user_pass = decoded_base64_authorization_header.split(
                ':')
        return user_email, user_pass

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """Returns the user instance based on the provided email ad password
        """
        if user_email is None or not isinstance(user_email, str):
            return None
        if user_pwd is None or not isinstance(user_pwd, str):
            return None
        user = user_db.User.search(user_email)
        if user is None:
            return None
        if not user.is_valid_password(user_pwd):
            return None
        return user

    def current_user(self, request=None) -> TypeVar('User'):
        """Retreives the User instance for a request using Basic Authentication
        """
        authorization_header = request.headers.get('Authorization' , None)

        base64_auth_hearder = self.extract_base64_authorization_header(authorization_header)
        decoded_auth_header = self.decode_base64_authorization_header(base64_auth_hearder)
        user_email, user_pwd = self.etract_user_credentials(decoded_auth_header)
        if user_email is None or user_pwd is None:
            return Nonee
        User = self.user_object_from_credentials(user_email, user_pwd)
        return user
