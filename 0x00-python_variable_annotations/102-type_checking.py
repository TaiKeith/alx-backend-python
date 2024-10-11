#!/usr/bin/env python3
"""
This module contains a type-annotated function that takes a Sequence and integer
'factor' arguments and returns a list
"""
from typing import List, Tuple, Sequence


def zoom_array(lst: Sequence, factor: int = 2) -> List:
    """
    Type-annotated function that zooms in by repeating each element in the
    list/tuple a specified number of times
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
