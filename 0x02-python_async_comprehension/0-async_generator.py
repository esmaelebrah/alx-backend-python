#!/usr/bin/env python3
import random
import asyncio
from typing import Generator
async def async_generator() -> Generator[int, None, None]:
    for i in range(10):
        num = random.uniform(0, 10)
        yield num
        await asyncio.sleep(1)
