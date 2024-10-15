#!/usr/bin/env python3
"""
This module contains a coroutine that collects 10 random numbers using an
async comprehension over async_generator, then returns the 10 random numbers
"""
import asyncio
import random
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collects 10 random numbers using async comprehension then returns
    the 10 random numbers
    """
    return [num async for num in async_generator()]
