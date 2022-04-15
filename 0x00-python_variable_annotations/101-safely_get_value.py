#!/usr/bin/env python3
"""
    Contains a function that implements annotations
"""

import typing


def safely_get_value(dct: typing.Mapping, key: typing.Any,
                     default: typing.Union[typing.TypeVar('T'), None] = None)\
                    -> typing.Union[typing.Any, typing.TypeVar('T')]:
    """Returns value of a given key from a dictionary-like type"""
    if key in dct:
        return dct[key]
    else:
        return default
