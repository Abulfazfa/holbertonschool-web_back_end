#!/usr/bin/env python3
"""
function that a list of floats as argument and returns their sum
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """return the sum of floats"""
    a = 0
    for number in input_list:
        a += number
    return a
