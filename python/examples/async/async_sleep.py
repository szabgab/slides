import time
import asyncio

async def work(wid, sec):
    start = time.time()
    print(f"Starting {wid} that will take {sec}s")
    await asyncio.sleep(sec)
    end = time.time()
    print(f"Finishing {wid} in {end-start}s")

async def main():
    await asyncio.gather(
        work("Blue", 2),
        work("Green", 1)
    )


start = time.time()
asyncio.run(main())
end = time.time()
print(f"Elapsed {end-start}")

