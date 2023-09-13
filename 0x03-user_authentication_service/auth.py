#!/usr/bin/env python3
"""
The password hashing module
"""
import bcrypt
from db import DB
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError
from user import User
import uuid


def _hash_password(password: str) -> bytes:
    """
    Function that hashes the password
    """
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password


class Auth:
    """Auth class to interact with the authentication database.
    """
    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """To register a new user
        """
        try:
            existing_user = self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            hashed_password = _hash_password(password)
            new_user = self._db.add_user(
                    email=email, hashed_password=hashed_password)
            return new_user

    def valid_login(self, email: str, password: str) -> bool:
        """
        Validating password before logging in
        """
        try:
            user = self._db.find_user_by(email=email)
            if bcrypt.checkpw(password.encode('utf-8'), user.hashed_password):
                return True
        except Exception:
            pass
        return False

    def _generate_uuid() -> str:
        """
        Function that generates a unique id
        """
        new_id = uuid.uuid4()
        return str(new_id)

    def create_session(self, email: str) -> str:
        """
        Function that creates a session
        """
        try:
            user = self._db.find_user_by(email=email)
            new_session_id = _generate_uuid()
            self._db.update_user(user.id, session_id=new_session_id)
            return new_session_id
        except Exception:
            pass
        return None


if __name__ == "__main__":
    auth = Auth()
