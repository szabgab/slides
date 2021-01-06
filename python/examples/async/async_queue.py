import time
import asyncio
import sys

#queue = [4, 3, 1, 2, 1, 7, 3, 4, 5, 1, 2, 1, 2, 3, 4]
queue = [1] * 10
print(f"Total: {sum(queue)}")

parallel = 1
if len(sys.argv) == 2:
    parallel = int(sys.argv[1])

async def worker(wid):
    while queue:
        job = queue.pop(0)

        ts = time.monotonic()
        print(f"Worker {wid} starting job {job} {ts}")
        await asyncio.sleep(job)
        print(f"Worker {wid} finished job {job}")

async def main():
    tasks = []
    for wid in range(parallel):
        tasks.append( asyncio.create_task(worker(wid)) )
    await asyncio.gather(*tasks) 


start = time.monotonic()
print(f"Start {start}")
asyncio.run(main())
end = time.monotonic()
print(f"Elapsed: {end-start}")
