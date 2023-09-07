#!/usr/bin/env python3
"""Basic auth class module"""
from api.v1.auth.auth import Auth
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
