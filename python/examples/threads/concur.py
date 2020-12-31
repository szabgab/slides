import sys
import concurrent.futures
import requests
import time

def download_all(urls):
    for url in urls:
        res = requests.get(url)
        print(f"{url} - {len(res.text)}")
        return



if __name__ == '__main__':
    if len(sys.argv) != 2:
        exit(f"Usage: {sys.argv[0]} FILENAME (examples/parallel/urls.txt)")
    filename = sys.argv[1]
    with open(filename) as fh:
        urls = list(map(lambda s: s.rstrip("\n"), fh.readlines()))
    start = time.time()
    download_all(urls)
    end = time.time()
    elapsed = end-start
    print(f"Elapsed time : {elapsed:2f}")
