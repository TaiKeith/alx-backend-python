#!/usr/bin/env python3
"""
This module contains a function with integers n and max_delay as arguments
that measure the total execution time for 'wait_n(n, max_delay)', and returns
'total_time / n' (float)
"""
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int = 10) -> float:
    """
    Measures the total execution time for 'wait_n(n, max_delay)' and returns
    'total_time / n' (float value)
    """
    s = time.time()
    await wait_n(n, max_delay)
    total_time = time.time() - s
    return total_time / n
