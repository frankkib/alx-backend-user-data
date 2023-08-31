#!/usr/bin/env python3
"""Implementing a hash_password function"""
import bcrypt


def hash_password(password: str) -> bytes:
    """
    Hash a password using bcrypt with salt.
    """
    salt = bcrypt.gensalt()

    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password

def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Validates the password against a hashed using bcrypt.
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
