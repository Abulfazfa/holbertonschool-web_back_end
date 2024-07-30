#!/usr/bin/env python3
"""
function that a tuple
"""

from typing import Union, Tuple
import math


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """return the tuple"""
    return (k, float(math.pow(v, 2)))
