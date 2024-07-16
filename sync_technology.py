import time
import asyncio
import numpy as np
import requests

def get_url():
    response = requests.get('http://www.randomnumberapi.com/api/v1.0/random')
    out = response.json()
    return out[0]

def main():
    start = time.process_time_ns()

    out = []
    for i in range(10):
        response = get_url()
        out.append(response)
    sum(out)

    stop = time.process_time_ns()
    total_time = stop - start
    return total_time


if __name__ == '__main__':
    times = [main() for _ in range(10**3)]
    print(f"Average runtime (nanoseconds): {np.mean(times)}")
    print(f"Runtime deciles (nanoseconds): {np.quantile(times, np.arange(0,1,0.1))}")

