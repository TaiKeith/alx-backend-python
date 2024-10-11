#!/usr/bin/env python3
"""
This module contains a type-annotated function that safely retrieves a value
from a dictionary.
If the key is not present, it returns the default value (if provided).
"""
from typing import Mapping, Any, TypeVar, Union


T = TypeVar('T')


def safely_get_value(dct: Mapping,
                     key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """
    Type-annotated function that safely retrieves a value from a dictionary.
    If the key is not present, it returns the default value (if provided).
    """
    if key in dct:
        return dct[key]
    else:
        return default
