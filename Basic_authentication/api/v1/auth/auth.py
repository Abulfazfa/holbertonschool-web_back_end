#!/usr/bin/env python3
""" Auth module
"""

from flask import request
from typing import List, TypeVar


class Auth:
    """ Auth class for the API
    """

    def __init__(self):
        """ Constructor of the Auth class
        """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Method to check if a path requires authentication"""
        return False

    def authorization_header(self, request=None) -> str:
        """ Method to get the authorization header from a request"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Method to get the current user from a request """    
        return None
