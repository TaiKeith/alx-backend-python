#!/usr/bin/env python3
"""
This module contains a coroutine that will execute 'async_comprehension'
four times in parallel using asyncio.gather. The coroutine should measure
the total runtime and return it
"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Executes 'async_comprehension four times, measure the total runtime
    and returns it
    """
    start = time.time()

    await asyncio.gather(*(async_comprehension() for _ in range(4)))

    return time.time() - start
