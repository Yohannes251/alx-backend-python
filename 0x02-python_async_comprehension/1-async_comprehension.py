#!/usr/bin/env python3
"""
    This script contains async_comprehension function
"""

import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Generates a list of random floating numbers using async comprehension"""
    return [num async for num in async_generator()]
