#!/usr/bin/env python3
"""
function that a list of ints and floats as argument and returns their sum
"""

from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """return a function that multiplies a float by the argument"""
    def multiplier_function(value: float) -> float:
        return value * multiplier
    return multiplier_function
