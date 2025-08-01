import aiohttp
import asyncio
import sys
from bs4 import BeautifulSoup

async def fetch(session, url):
    async with session.get(url) as response:
        content = await response.text()
        return [url, content]

async def main():
    if len(sys.argv) < 2:
        exit(f"Usage: {sys.argv[0]} FILENAME") # examples/parallel/url.txt
    filename = sys.argv[1]
    with open(filename) as fh:
        urls = list(map(lambda url: url.rstrip('\n'), fh.readlines()))
    #urls = urls[0:6]
    #urls = ['https://httpbin.org/get']
    #print(urls)

    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in urls:
            tasks.append(asyncio.create_task(fetch(session, url)))
        await asyncio.gather(*tasks)
        for task in tasks:
            url, content = task.result()
            print(url)
            #print(content)
            soup = BeautifulSoup(content, 'html.parser')
            print('Missing' if soup.title is None else soup.title.string)

            #print(task)


asyncio.run(main())

