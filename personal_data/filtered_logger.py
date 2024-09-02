#!/usr/bin/env python3
""" Filtered logger """

import re
from typing import List

def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    """Filtering fields"""
    pattern = '|'.join(f"{field}=" for field in fields)
    return re.sub(fr'(?<={pattern})(.*?)(?={separator})', redaction, message)
