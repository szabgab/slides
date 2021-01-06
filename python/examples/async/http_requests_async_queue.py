import aiohttp
import asyncio
import sys
from bs4 import BeautifulSoup

async def fetch(session, urls, results):
    while urls:
        url = urls.pop(0)
        async with session.get(url) as response:
            content = await response.text()
            soup = BeautifulSoup(content, 'html.parser')
            results[url] = None if soup.title is None else soup.title.string


async def main(parallel, urls):
    results = {}
    async with aiohttp.ClientSession() as session:
        tasks = []
        for _ in range(parallel):
            tasks.append(asyncio.create_task(fetch(session, urls, results)))
        await asyncio.gather(*tasks)
    return results

def setup():
    if len(sys.argv) < 4:
        exit(f"Usage: {sys.argv[0]} LIMIT PARALLEL FILENAME") # examples/parallel/url.txt or wikipedia.txt
    limit = int(sys.argv[1])
    parallel = int(sys.argv[2])
    filename = sys.argv[3]

    with open(filename) as fh:
        urls = list(map(lambda url: url.rstrip('\n'), fh.readlines()))
    if len(urls) > limit:
        urls = urls[0:limit]
    # use asyncio.Queue instead

    results = asyncio.run(main(parallel, urls))

    for url, title in results.items():
        print(f"{url} - {title}")

setup()
