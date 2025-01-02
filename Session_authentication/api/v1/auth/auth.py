#!/usr/bin/env python3
""" Auth module
"""

from flask import request
from typing import List, TypeVar
from os import getenv


class Auth:
    """ Auth class for the API
    """

    def __init__(self):
        """ Constructor of the Auth class
        """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ require_auth method that returns
        True if the path is not in the list
        """

        if path is None or excluded_paths is None or excluded_paths == []:
            return True

        for exclude_path in excluded_paths:
            if path.strip("/") in exclude_path.strip("/"):
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """ authorization_header method that returns None
        """
        if request is None:
            return None

        return request.headers.get('Authorization', None)

    def current_user(self, request=None) -> TypeVar('User'):
        """ current_user method that returns None
        """
        return request

    def session_cookie(self, request=None):
        """ session_cookie method that returns None
        """
        if request is None:
            return None

        session_env = getenv('SESSION_NAME', None)
        cookie = request.cookies.get(session_env, None)

        return cookie
