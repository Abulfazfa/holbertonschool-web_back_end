#!/usr/bin/env python3
""" filtered logger """

import re
from typing import List


def filter_datum(fields: List[str], redaction: str, message: str, seperator: str) -> str:
    """ function that returns a string with certain fields redacted """
    for field in fields:
        regex = rf'{field}=([^;]+){seperator}'
        message = re.sub(regex, f"{field}={redaction};", message)

    return message
