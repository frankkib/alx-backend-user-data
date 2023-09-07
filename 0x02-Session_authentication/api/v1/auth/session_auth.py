#!/usr/bin/env python3
"""Session module"""
from .auth import Auth
import uuid


class SessionAuth(Auth):
    """class session"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """
        Create a new session and associate it with user_id
        """
        if user_id is None or not isinstance(user_id, str):
            return None
        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """Get the user ID associated with a given Session ID.
        """
        if session_id is None or not isinstance(session_id, str):
            return None
        user_id = self.user_id_by_session_id.get(session_id)
        return user_id

    def current_user(self, request=None):
        """Gets the user instance based oon session cookie value.
        """
        if request is None:
            return None
        session_cookie_value = self.session_cookie(request)
        if session_cookie_value is None:
            return None
        user_id = self.user_id_for_session_id(session_cookie_value)
        if user_id is None:
            return None
        user = User.get(user_id)
        return user
