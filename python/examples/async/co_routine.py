import asyncio

async def answer():
    print("start to answer")
    return 42

async def main():
    a_coroutine = answer()
    print(a_coroutine)

    await asyncio.sleep(0)
    print('before await for coroutine')

    result = await a_coroutine
    print(f"result is {result} after await")
 
asyncio.run(main())