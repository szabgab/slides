import time
import asyncio

async def count(name, end, sec):
    for i in range(end):
        print(f"{name} {i}")
        await asyncio.sleep(sec)

async def main():
    await asyncio.gather(
        count('apple', 10, 0.1),
        count('peach', 10, 0.2),
        )

start = time.time()
asyncio.run(main())
end = time.time()
print(f"Elapsed {end-start}")
