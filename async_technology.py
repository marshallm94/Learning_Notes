import time
import asyncio
import numpy as np
import aiohttp

async def get_url():
    async with aiohttp.ClientSession() as session:
        async with session.get('http://www.randomnumberapi.com/api/v1.0/random') as response:
            out = await response.json()
            return out[0]

async def main():
    start = time.process_time_ns()

    task_1 = asyncio.create_task(get_url())
    task_2 = asyncio.create_task(get_url())
    task_3 = asyncio.create_task(get_url())
    task_4 = asyncio.create_task(get_url())
    task_5 = asyncio.create_task(get_url())
    task_6 = asyncio.create_task(get_url())
    task_7 = asyncio.create_task(get_url())
    task_8 = asyncio.create_task(get_url())
    task_9 = asyncio.create_task(get_url())
    task_10 = asyncio.create_task(get_url())
    out = await asyncio.gather( task_1, task_2, task_3, task_4, task_5, task_6, task_7, task_8, task_9, task_10)
    sum(out)

    stop = time.process_time_ns()
    total_time = stop - start
    return total_time


if __name__ == '__main__':
    times = [asyncio.run(main()) for _ in range(10**3)]
    print(f"Average runtime (nanoseconds): {np.mean(times)}")
    print(f"Runtime deciles (nanoseconds): {np.quantile(times, np.arange(0,1,0.1))}")

