#!/usr/bin/env python3
"""
This module contains a type-annotated function that takes an iterable of
sequences and returns a list of tuples.
Each tuple contains a sequence and its corresponding length.
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Type-annotated function that returns a list of tuples from an iterable of
    sequences. Each tuple contains a sequence and its corresponding length.
    """
    return [(i, len(i)) for i in lst]
