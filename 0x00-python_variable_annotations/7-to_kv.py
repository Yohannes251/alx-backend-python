#!/usr/bin/env python3
"""
    Contains a function with mixed type annotation
"""

import typing


def to_kv(k: str, v: typing.Union[int, float]) -> typing.Tuple[str, float]:
    """ Returns sum of ints and floats in a list"""
    return (k, v ** 2)
