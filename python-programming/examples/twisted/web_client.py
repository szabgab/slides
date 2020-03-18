from twisted.internet import reactor
from twisted.web.client import getPage
import sys
import re
import time

queue = [
  'http://docs.python.org/3/',
  'http://docs.python.org/3/whatsnew/3.3.html',
  'http://docs.python.org/3/tutorial/index.html',
  'http://docs.python.org/3/library/index.html',
  'http://docs.python.org/3/reference/index.html'
  'http://docs.python.org/3/howto/index.html',
  'http://docs.python.org/3/howto/pyporting.html',
  'http://docs.python.org/3/howto/cporting.html',
  'http://docs.python.org/3/howto/curses.html',
  'http://docs.python.org/3/howto/descriptor.html',
  'http://docs.python.org/3/howto/functional.html',
  'http://docs.python.org/3/howto/logging.html',
  'http://docs.python.org/3/howto/logging-cookbook.html',
  'http://docs.python.org/3/howto/regex.html',
  'http://docs.python.org/3/howto/sockets.html',
  'http://docs.python.org/3/howto/sorting.html',
  'http://docs.python.org/3/howto/unicode.html',
  'http://docs.python.org/3/howto/urllib2.html',
  'http://docs.python.org/3/howto/webservers.html',
  'http://docs.python.org/3/howto/argparse.html',
  'http://docs.python.org/3/howto/ipaddress.html',
]

max_parallel = 3
current_parallel = 0
if len(sys.argv) == 2:
  max_parallel = int(sys.argv[1])

def printPage(result):
  print(f"page size: ", len(result))
  global current_parallel
  current_parallel -= 1
  print("current_parallel: ", current_parallel)
  #urls = re.findall(r'href="([^"]+)"', result)
  #for u in urls:
  #  queue.append(u)
  #queue.extend(urls)
  process_queue()

def printError(error):
  print("Error: ", error)
  global current_parallel
  current_parallel -= 1
  process_queue()


def stop(result):
  reactor.stop()

def process_queue():
  global current_parallel, max_parallel,queue
  print("process_queue cs: {} max: {}".format(current_parallel, max_parallel))
  while True:
    if current_parallel >= max_parallel:
      print("No empty slot")
      return
    if len(queue) == 0:
      print("queue is empty")
      if current_parallel == 0:
        reactor.stop()
      return
    url = queue[0] + '?' + str(time.time())
    queue[0:1] = []
    current_parallel += 1
    d = getPage(url)
    d.addCallbacks(printPage, printError)

process_queue()
reactor.run()
print("----done ---")

