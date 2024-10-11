#!/usr/bin/env python3
"""
This module contains a type-annotated function that takes a float as an
argument and returns the floor of the float
"""
import math


def floor(n: float) -> int:
    """
    Type-annotated function that returns the floor of a float argument
    """
    return math.floor(n)
