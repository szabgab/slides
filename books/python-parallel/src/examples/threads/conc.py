import concurrent.futures
import requests
import threading
import time
import sys
from bs4 import BeautifulSoup

thread_local = threading.local()

def get_title(url):
    res = requests.get(url)
    if res.status_code:
        soup = BeautifulSoup(res.text, 'html.parser')
        return None if soup.title is None else soup.title.string
    else:
        return None


def main():
    if len(sys.argv) < 4:
        exit(f"{sys.argv[0]} LIMIT PARALLEL FILENAME")
    limit    = int(sys.argv[1])
    parallel = int(sys.argv[2])
    filename = sys.argv[3]
    with open(filename) as fh:
        urls = list(map(lambda line: line.rstrip("\n"), fh))
    if len(urls) > limit:
        urls = urls[0:limit]
    #print(urls)

    start = time.monotonic()

    #titles = list(map(get_title, urls))
    with concurrent.futures.ThreadPoolExecutor(max_workers=parallel) as exe:
        titles = list(exe.map(get_title, urls))

    for ix in range(len(urls)):
        print(f"{urls[ix]}  {titles[ix]}")
    end = time.monotonic()
    print(f"Elapsed time: {end-start}")


main()

