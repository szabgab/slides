import asyncio

async def answer():
    print("start to answer")
    return 42

async def main():
    a_task = asyncio.create_task(answer())
    print(a_task)

    await asyncio.sleep(0)
    print('before await for task')
    
    result = await a_task
    print(f"result is {result} after await")
 
asyncio.run(main())