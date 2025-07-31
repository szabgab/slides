import time
import threading
import requests
import sys
from bs4 import BeautifulSoup

from fetch_urls import get_urls, get_title

titles = []
locker = threading.Lock()

class GetURLs(threading.Thread):
    def __init__(self, urls):
        threading.Thread.__init__(self)
        self.urls = urls

    def run(self):
        my_titles = []
        for url in self.urls:
            title, err = get_title(url)
            my_titles.append({
                'url': url,
                'title': title,
                'err': err,
            })
        locker.acquire()
        titles.extend(my_titles)
        locker.release()
        return

def main():
    if len(sys.argv) < 3:
        exit(f"Usage: {sys.argv[0]} LIMIT THREADS")
    limit = int(sys.argv[1])
    threads_count = int(sys.argv[2])

    urls = get_urls(limit)
    print(urls)
    start_time = time.time()
    batch_size = int(limit/threads_count)
    left_over = limit % threads_count
    batches = []
    end = 0
    for ix in range(threads_count):
        start = end
        end = start + batch_size
        if ix < left_over:
            end += 1
        batches.append(urls[start:end])

    threads = [ GetURLs(batches[ix]) for ix in range(threads_count) ]
    [ t.start() for t in threads ]
    [ t.join() for t in threads ]

    end_time = time.time()
    print("Elapsed time: {} for {} pages.".format(end_time-start_time, len(urls)))
    print(titles)


if __name__ == '__main__':
    main()
