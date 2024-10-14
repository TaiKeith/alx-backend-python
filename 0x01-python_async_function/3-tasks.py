#!/usr/bin/env python3
"""
This module contains a function that takes an integer 'max_delay' and
returns a 'asyncio.Task'
"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int = 10) -> asyncio.Task:
    """
    Creates and returns an asyncio.Task that runs the wait_random coroutine.

    Args:
        max_delay (int): The maximum delay in seconds for the wait_random
        coroutine.

    Returns:
        asyncio.Task: A task object that can be awaited.
    """
    return asyncio.create_task(wait_random(max_delay))
