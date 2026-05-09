"""
Python Concurrency: Threading, Multiprocessing, and AsyncIO.
Covers I/O-bound vs CPU-bound tasks and asynchronous programming.
"""

import threading
import multiprocessing
import asyncio
import time
from typing import List

# 1. Threading (I/O Bound)
def io_task(name: str) -> None:
    print(f"Thread {name}: Starting I/O task...")
    time.sleep(1)
    print(f"Thread {name}: Task complete.")

# 2. Multiprocessing (CPU Bound)
def cpu_task(n: int) -> int:
    print(f"Process {multiprocessing.current_process().name}: Calculating...")
    return sum(i * i for i in range(n))

# 3. AsyncIO (Event Loop)
async def async_task(name: str) -> None:
    print(f"Async {name}: Starting...")
    await asyncio.sleep(1) # Non-blocking sleep
    print(f"Async {name}: Complete.")

async def run_async_suite():
    await asyncio.gather(
        async_task("A"),
        async_task("B"),
        async_task("C")
    )

if __name__ == "__main__":
    # Threading Demo
    print("--- Threading Demo ---")
    threads = []
    for i in range(3):
        t = threading.Thread(target=io_task, args=(f"T{i}",))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()

    # Multiprocessing Demo
    print("\n--- Multiprocessing Demo ---")
    with multiprocessing.Pool(processes=2) as pool:
        results = pool.map(cpu_task, [10**6, 10**6])
    print(f"Results: {results}")

    # AsyncIO Demo
    print("\n--- AsyncIO Demo ---")
    asyncio.run(run_async_suite())
