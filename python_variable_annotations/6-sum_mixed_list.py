#!/usr/bin/env python3
"""
function that a list of ints and floats as argument and returns their sum
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """return the sum of ints and floats"""
    return sum(mxd_lst)
