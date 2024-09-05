#!/usr/bin/env python3
""" BasicAuth module for the API
"""

from api.v1.auth.auth import Auth, TypeVar
from typing import Tuple, List
import base64
from models.user import User


class BasicAuth(Auth):
    """ BasicAuth class
    """

    def __init__(self):
        """ Constructor of the BasicAuth class
        """