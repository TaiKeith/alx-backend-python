#!/usr/bin/env python3
"""
This module contains an asynchronous function that spawns the function
'wait_random' n times with a specified max_delay and returns a list of
delays (float values) in ascending order
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """
    Spawns 'wait_random' n times with a specified max_delay.

    Args:
        n (int): Number of times to call the 'wait_random' coroutine.
        max_delay (int): Maximum delay in seconds for each 'wait_random' call.

    Returns:
        List[float]: A list of delays (float values) in ascending order.
    """
    # Create a list of tasks by calling wait_random n times
    tasks = [wait_random(max_delay) for _ in range(n)]

    # Use asyncio.gather to run all tasks concurrently and get the results
    delays = await asyncio.gather(*tasks)

    return sorted(delays)
