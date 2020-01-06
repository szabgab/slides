import time
import requests
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup


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
   for url in urls:
       resp = requests.get(url)
       if resp.status_code != 200:
           print(f"Incorrect status_code {resp.status_code} for {url}")
           continue

       soup = BeautifulSoup(resp.content, 'html.parser')
       print(soup.title.string)
       titles.append(soup.title.string)
   end = time.time()
   print("Elapsed time: {} for {} pages.".format(end-start, len(urls)))
   print(titles)


if __name__ == '__main__':
   main()
