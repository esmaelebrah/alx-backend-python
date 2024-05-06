#!/usr/bin/env python3

import asyncio

task_wait_random = __import__('3-tasks').task_wait_random
async def task_wait_n(n: int, max_delay: int) -> list[float]:
    responses = [task_wait_random(max_delay) for _ in range(n)]
    return [await res for res in asyncio.as_completed(responses)]
