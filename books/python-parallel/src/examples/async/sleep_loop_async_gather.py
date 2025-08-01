import time
import asyncio

async def sleep(cnt, sec):
    print(f"Start {cnt}")
    await asyncio.sleep(sec)
    print(f"End {cnt}")

async def main():
    co_routines = []
    for i in range(4):
        co_routines.append(sleep(i, 1))

    await asyncio.gather(*co_routines)

start = time.monotonic()
asyncio.run(main())
end = time.monotonic()
print(f"Elapsed {end-start}")

