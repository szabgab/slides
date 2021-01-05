import time
import asyncio

async def say(text, sec):
    await asyncio.sleep(sec)
    print(text)

async def main():
    start = time.monotonic()
    await asyncio.gather(
        say("First", 2),
        say("Second", 1),
    )
    end = time.monotonic()   
    print(f"Elapsed: {end-start}")


asyncio.run(main())

