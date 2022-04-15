#!/usr/bin/env python3
"""
    Contains a function that implement duck-typed annotations
"""

import typing


# The types of the elements of the input are not know
def safe_first_element(lst: typing.Sequence[typing.Any]) -> \
        typing.Union[typing.Any, None]:
    """Returns first element of iterable or None"""
    if lst:
        return lst[0]
    else:
        return None
