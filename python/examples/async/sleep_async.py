import time
import asyncio

async def say(wid, sec):
    start = time.monotonic()
    print(f"Starting {wid} that will take {sec}s")
    await asyncio.sleep(sec)
    end = time.monotonic()
    print(f"Finishing {wid} in {end-start}s")

async def main():
    start = time.monotonic()
    await asyncio.gather(
        say("First", 2),
        say("Second", 1)
    )
    end = time.monotonic()
    print(f"Elapsed: {end-start}")


asyncio.run(main())

