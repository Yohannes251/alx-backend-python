#!/usr/bin/env python3
"""
    Contains summing function with type annotation
"""

import typing


def sum_list(input_list: typing.List[float]) -> float:
    """ Returns sum of floats in a list"""
    return sum(num for num in input_list)
