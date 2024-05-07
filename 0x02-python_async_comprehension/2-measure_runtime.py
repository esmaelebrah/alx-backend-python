#!/usr/bin/env python3

import time
import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension

async def measure_runtime():
    start_time = time.time()
    await asyncio.gather(async_comprehension(), async_comprehension(), async_comprehension(), async_comprehension())
    last_time = time.time()
    return (last_time - start_time)
