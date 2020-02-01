import time
import requests
import sys
from bs4 import BeautifulSoup

def get_urls(limit):
    with open('urls.txt') as fh:
        urls = list(map(lambda line: line.rstrip("\n"), fh))
    if len(urls) > limit:
        urls = urls[:limit]

    return urls

def get_title(url):
    try:
        resp = requests.get(url)
        if resp.status_code != 200:
            return None, f"Incorrect status_code {resp.status_code} for {url}"
    except Exception as err:
        return None, f"Error: {err} for {url}"

    soup = BeautifulSoup(resp.content, 'html.parser')
    return soup.title.string, None

def main():
    if len(sys.argv) < 2:
        exit(f"Usage: {sys.argv[0]} LIMIT")
    limit = int(sys.argv[1])
    urls = get_urls(limit)
    print(urls)
    start = time.time()

    titles = []
    for url in urls:
        #print(f"Processing {url}")
        title, err = get_title(url)
        if err:
            print(err)
        else:
            print(title)
        titles.append({
            "url": url,
            "title": title,
            "err": err,
        })
    end = time.time()
    print("Elapsed time: {} for {} pages.".format(end-start, len(urls)))
    print(titles)


if __name__ == '__main__':
    main()
