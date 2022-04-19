#!/usr/bin/env python3
"""
    This script contains a function that computes runtime
"""

import asyncio
from time import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Computes total execution time and returns its value divided by n"""
    start = time()
    asyncio.run(wait_n(n, max_delay))
    finish = time()
    return (finish - start) / n
