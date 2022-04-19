#!/usr/bin/env python3
"""
    This script contains an async function which executes multi coroutines
"""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Returns a sorted list of random await delays"""

    collector: List[float] = []
    for i in range(n):
        collector.append(task_wait_random(max_delay))
    return [await delay for delay in asyncio.as_completed(collector)]
