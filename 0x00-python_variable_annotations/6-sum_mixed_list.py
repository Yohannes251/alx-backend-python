#!/usr/bin/env python3
"""
    Contains summing function with mixed type annotation
"""

import typing


def sum_mixed_list(mxd_lst: typing.List[typing.Union[int, float]]) -> float:
    """ Returns sum of ints and floats in a list"""
    return sum(num for num in mxd_lst)
