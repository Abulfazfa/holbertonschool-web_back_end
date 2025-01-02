#!/usr/bin/env python3
""" Module of Session Expiration Authentication
"""

from flask import request
from api.v1.auth.session_auth import SessionAuth
from os import getenv
from datetime import datetime, timedelta
from typing import Dict


class SessionExpAuth(SessionAuth):
    """ Session Expiration Authentication Class inherited from SessionAuth
    """

    def __init__(self):
        """ Constructor
        """
        super().__init__()
        SESSION_DURATION = getenv('SESSION_DURATION', 0)

        try:
            SESSION_DURATION = int(SESSION_DURATION)
        except Exception:
            SESSION_DURATION = 0

        self.session_duration = SESSION_DURATION

    def create_session(self, user_id=None):
        """ Create a Session ID
        """
        session_id = super().create_session(user_id)
        if session_id is None:
            return None

        session_dict: Dict = {
            "user_id": user_id,
            "created_at": datetime.now()
        }

        self.user_id_by_session_id[session_id] = session_dict

        return session_id

    def user_id_for_session_id(self, session_id=None):
        """ Return a User ID based on a Session ID
        """
        if session_id is None or session_id not in self.user_id_by_session_id:
            return None

        session_dictionary = self.user_id_by_session_id.get(session_id)

        if self.session_duration <= 0 or session_dictionary is None:
            return session_dictionary.get('user_id', None)

        created_by = session_dictionary.get('created_at', None)
        if created_by is None:
            return None

        expired_session = created_by + timedelta(seconds=self.session_duration)

        if expired_session < datetime.now():
            return None

        return session_dictionary.get('user_id', None)
