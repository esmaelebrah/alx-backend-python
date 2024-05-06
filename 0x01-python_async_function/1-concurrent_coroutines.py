#!/usr/bin/env python3

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay: int) -> list[float]:
    responses = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    return [await res for res in asyncio.as_completed(responses)]
