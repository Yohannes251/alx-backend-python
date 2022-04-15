#!/usr/bin/env python3
"""
    Contains a function with mixed type annotation
"""

import typing


def element_length(lst: typing.Iterable[typing.Sequence]) -> \
        typing.List[typing.Tuple[typing.Sequence, int]]:
    """Returns a list of tuples which contain elements with their length"""
    return [(i, len(i)) for i in lst]
