import requests
import sys
from bs4 import BeautifulSoup

def fetch(url):
    response = requests.get(url)
    content = response.text
    return content

def main():
    if len(sys.argv) < 2:
        exit(f"Usage: {sys.argv[0]} FILENAME") # examples/parallel/url.txt
    filename = sys.argv[1]
    with open(filename) as fh:
        urls = list(map(lambda url: url.rstrip('\n'), fh.readlines()))
    #urls = urls[0:10]
    #urls = ['https://httpbin.org/get']
    #print(urls)

    tasks = []
    for url in urls:
#        tasks.append([url, fetch(url)])
#    for task in tasks:
#        url, content = task
        content = fetch(url)
        print(url)
        #print(content)
        soup = BeautifulSoup(content, 'html.parser')
        print('Missing' if soup.title is None else soup.title.string)

        #print(task)


main()

