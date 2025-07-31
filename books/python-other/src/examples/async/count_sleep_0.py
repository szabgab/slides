import asyncio

async def count(name):
    print(f"start {name}")
    for cnt in range(10):
        print(f"{name} {cnt}")
        await asyncio.sleep(0)

async def main():
    a_task = asyncio.create_task(count("A"))
    b_task = asyncio.create_task(count("B"))

    print("Before")
    #await asyncio.sleep(1)
    print("After")

    await asyncio.gather(
        a_task,
        b_task
    )

asyncio.run(main())
