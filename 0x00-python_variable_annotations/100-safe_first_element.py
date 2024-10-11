#!/usr/bin/env python3
"""
This module contains a type-annotated function that takes a sequence of
elements (of unknown types) and returns the first element or None if the
sequence is empty
"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Type-annotated function that returns the first element or None if the
    sequence is empty from a sequence of elements (of unknown types)
    """
    if lst:
        return lst[0]
    else:
        return None
