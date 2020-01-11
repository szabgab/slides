import aiohttp
import asyncio
#from aiohttp import ClientSession


urls = ['https://code-maven.com/', 'https://code-maven.com/slides']

async def fetch():
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in urls:
            resp = await session.request(method="GET", url=url)
            html = await resp.text()
            print("got it")
        await asyncio.gather(*tasks)

asyncio.run(fetch())

