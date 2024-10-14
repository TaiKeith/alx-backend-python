#!/usr/bin/env python3
"""
This module contains an asynchronous coroutine that takes an int argument
'max_delay' and waits for a random delay between 0 and 'max_delay' seconds
and eventually returns it
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    An asynchronous coroutine that waits for a random delay between 0 and
    max_delay (defaulting to 10), seconds and then returns the delay
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
