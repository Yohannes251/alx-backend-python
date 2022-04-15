#!/usr/bin/env python3
"""
    Contains a function with mixed type annotation
"""

import typing


def make_multiplier(multiplier: float) -> typing.Callable[[float], float]:
    """ Returns a function that multiplies a float by the multiplier"""
    def fn(arg: float):
        return arg * multiplier
    return fn
