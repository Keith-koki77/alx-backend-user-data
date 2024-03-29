#!/usr/bin/env python3
"""
Python script for SessionAuth
"""

from api.v1.auth.auth import Auth
from typing import TypeVar
from uuid import uuid4
from models.user import User
from flask import request

class SessionAuth(Auth):
    """
    Class for Session auth class
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """
        Function that creates a Session ID for a user_id
        """
        if not user_id or type(user_id) != str:
            return
        session_id = str(uuid4())
        SessionAuth.user_id_by_session_id[user_id] = session_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """
        Returns a User ID based on a Session ID
        """
        if not session_id or type(session_id) != str:
            return
        return SessionAuth.user_id_by_session_id.get(session_id, None)

    def session_cookie(self, request) -> str:
        """
        Extracts the session cookie from the request
        """
        return request.cookies.get("session_id")

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Returns current_user
        """
        if request:
            session_cookie = self.session_cookie(request)
            if session_cookie:
                user_id = self.user_id_for_session_id(session_cookie)
                return User.get(user_id)
