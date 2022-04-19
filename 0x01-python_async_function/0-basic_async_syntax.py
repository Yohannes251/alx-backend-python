#!/usr/bin/env python3
"""
    Implements an asynchronous coroutine
"""

import asyncio
from random import uniform


async def wait_random(max_delay=10):
    """Waits for random delay and returns it"""
    delay = uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
