#!/usr/bin/env python3
"""
    This script contains async_generator function
"""

import asyncio
from random import uniform
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Generates random floating numbers"""
    for i in range(10):
        await asyncio.sleep(1)
        yield uniform(0, 10)
