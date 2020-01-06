import time
import requests
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
from multiprocessing import Pool
import os



def get_title(url):
   resp = requests.get(url)
   if resp.status_code != 200:
       print(f"Incorrect status_code {resp.status_code} for {url}")
       return

   soup = BeautifulSoup(resp.content, 'html.parser')
   print(soup.title.string)
   return soup.title.string.encode('utf-8')


def main():
   start = time.time()
   url = 'https://code-maven.com/slides/sitemap.xml'
   resp = requests.get(url)
   if resp.status_code != 200:
       exit(f"Incorrect status_code {resp.status_code}")

   urls = []
   root = ET.fromstring(resp.content)
   for child in root:
       for ch in child:
           if ch.tag.endswith('loc'):
               urls.append(ch.text)

   #print(len(urls)) # 2653
   MAX = 20
   if len(url) > MAX:
       urls = urls[:MAX]

   titles = []
#    for url in urls:
#        titles.append(get_title(url))
#    titles = list(map(get_title, urls))
   with Pool(5) as pool:
       results = pool.map(get_title, urls)
   for r in results:
       titles.append(r)
   end = time.time()
   print("Elapsed time: {} for {} pages.".format(end-start, len(urls)))
   print(list(titles))
   print("DONE")


if __name__ == '__main__':
   main()

