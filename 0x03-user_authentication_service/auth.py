#!/usr/bin/env python3
"""
The password hashing module
"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """
    Function that hashes the password
    """
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password
