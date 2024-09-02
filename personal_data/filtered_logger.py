#!/usr/bin/env python3
""" filtered logger """

import re
from typing import List


def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    '''Filtering  fields'''
    for item in fields:
        message = re.sub(f"{item}=.*?{separator}", f"{item}={redaction}{separator}", message)
    return message
