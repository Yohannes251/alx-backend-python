#!/usr/bin/env python3
"""
    This script contains async_comprehension function
"""

import asyncio
from time import time

asy_comp = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Returns the total runtime of four async_comprehension functions"""
    start = time()
    tasks = [asy_comp() for i in range(4)]
    await asyncio.gather(*tasks)
    finish = time()
    return finish - start
