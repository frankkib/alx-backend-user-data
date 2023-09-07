#!/usr/bin/env python3
"""Basic auth class module"""
from api.v1.auth.auth import Auth


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
