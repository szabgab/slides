import asyncio

async def say(text, sec):
    await asyncio.sleep(sec)
    print(text)

async def main():
    await asyncio.gather(
        say("First", 2),
        say("Second", 1),
    )


asyncio.run(main())

