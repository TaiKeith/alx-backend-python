#!/usr/bin/env python3
"""
This module contains a type-annotated function that takes a list of integers
and floats as argument and returns their sum as a float
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Type-annotated function that returns sum of a list of integers and floats
    as a float
    """
    return sum(mxd_lst)
