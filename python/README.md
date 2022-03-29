# The slides of the Python Progamming course


REPL: ptpython

## Scapy

# TODO: send between two other machines HTTP traffic on some arbitrary port
# TODO: set the source IP

ScapyTrafficGenerator -X http -r "-i $interface -s $ip -d 8.8.8.8 -D 80 -m $mac:$prefix:22:$postfix -U '$http_scapy' -u http://google.com"
ScapyTrafficGenerator -X http -r "-i $target_interface -s $ip -d 8.8.8.8 -D 80 -m $mac:$target_prefix:22:$postfix -U $httpscapy -u http://google.com"
ScapyTrafficGenerator -X http -r "-i $target_interface -s 8.8.8.8 -d $ip -D 80 -M $mac:$target_prefix:22:$postfix -k 'Server: $server'"
ScapyTrafficGenerator -X http -r "-i eno192 -s 10.162.130.20 -d $ip -D 80 -m 50:ec:50:22:22:02 -M $host"

cdp = cisco discovery protocol

https://en.wikipedia.org/wiki/Cisco_Discovery_Protocol

ipv4 / dhcp 

ipv6 / ping
ipv6 / dhcp


## Functional

Immutable datastructures
functions without side-effects
collections.namedtuple is it like an immutable dictionary with fixed keys.

replace zip by itertools.product

## Timing

Functional - part 1 - ~ 40 min + 30 min exercise
Functional - part 2 -
Iterators           - ~ 50 min + 60 min exercise

https://julien.danjou.info/python-and-functional-programming/
https://stackabuse.com/functional-programming-in-python/
itertools.groupby
use reduce to group by ???


## Dictionaries - defaultdict

Defaultdict
Counting
Grouping items - list
Grouping unique items - set
Accumulating items - int or float, adding values togetber

defaultdict()
defaultdict (None)
It also creates the key/value pair if I only try to access the field reading it.

## Parallel

Patterns:
  Pipes
  N-workers
  Broadcast


* import colorama
colorama.Fore.YELLOW + "text"


* Why parallel programming:
  cooking example - you won't want to stand next to thewashing machine till it finishes its job, right?
  IO intensive example: web access, reading from disk and processing files
  CPU intensive: lots of number crunching, image processing, video erndering etc.
  Interactive - UI make sure you can click buttons while it does its job.
  Scalability

async def  get_html(url):
  #resp = request.get(url)
    resp.raise_for_status()
  #return resp.text

  async with aiohttp.ClientSession() as session:
      async with session.get(url) as resp:
        resp.raise_for_status()
        return await resp.text


* glances (like htop for mac)


## Async

* download urls
* read several big files and process them.

loop = asyncio.get_event_loop()
queue = asyncio.Queue()
loop.run_until_complete()

Async sniffer https://scapy.readthedocs.io/en/latest/usage.html?highlight=capture#sniffing
Asynch pulsar

## Flask

* configuration of development vs testing vs productions deployment in external configuration files
* Session with cookies
* Session with JWT JSON Web Token
* Show Debug mode vs not debug mode (security code when looking at the source code)
* Use {{ url_for('static', filename='some.png') }}  in the templates


def connect_db():
    sql = sqlite3.connect('abc.db')
    sql.row_factory = sqlite3.Row
    return sql

def get_db():
    if not hasattr(g, 'db')
       g.db = connect_db() 
    return g.db

@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'db'):
        g.db.close()

@app.route('/list')
def list_entries():
    db = get_db()
    cur = db.execute('SELECT * FROM  some_tabel')
    results = cur.fetchall()

FLASK_ENV=development


## TODO

Extracting extension from filename in Python
filename, extension = os.path.splitext('/path/to/some/file.ext')


* What do we do if we need better floating point calculation precision that what Pyhton has?


## Example
{id: example-with-files}


![](examples/files/sample.txt)
![](examples/files/example.py)



## More TODO

Add http://rosalind.info/problems/locations/

How to use ImageJ  (stand alone and from Python) https://imagej.nih.gov/ij/download.html

- http://hs2.proteome.ca/SSRCalc/SSRCalc.html

- http://hlathena.tools, using the 'predict' tab

- https://neonmhc2.org/neonmhc2/neonmhc2_main/



https://genome.ucsc.edu/cgi-bin/hgTracks?db=hg38&lastVirtModeType=default&lastVirtModeExtraState=&virtModeType=default&virtMode=0&nonVirtPosition=&position=chrX%3A15560138%2D15602945&hgsid=925046977_4JJvooQub4aKDYio81R6NELN0vnH
https://www.danielecook.com/fetch-data-from-ucsc-genome-browser/
https://pypi.org/project/pygbrowse/
https://github.com/brentp/cruzdb


Weizmann Cluster
wexac
mobax
module list
module avail
module load python/3.5.2
module unload python/2.7

Take the codon exercise, solve it with 3 loops and solve it with a pre-calculated look-up table.
see the time difference.

## Pytest

* parametrized tests
* fork -disregard one of the report from the child process
* https://code-maven.com/slides/python/pytest-flask-app-sending-mail
  create a test case in which we mock the random string generation as well (maybe add this as an exercise and put the solution in a separate file)
  https://code-maven.com/slides/python/pytest-mocking-collecting-stats
    really implement the code behind it using request and other tools (and also update the database at the end) and then give the testing of it as an exercise.


* Can we protect our test from infinite (or too long) process? e.g. what if we get in an infinite loop? Can we set a max run time for the tests?
(API testing meaning (exceptions?) meaning of 500 400 errors?

https://stribny.name/blog/pytest/


Benchmarking, timing:
timeit library
time.perf_counter_ns


## Other

https://github.com/pypa/pipfile  a replacement for requirements.txt

## Algorithms

The bisect module for binary search to find where to insert an element



## OOP

isinstance(p, Person)


class attributes - no need to mark it specifically
static attributes  ??

class method for Point - e.g. number of points ever created

Is there a reliable destructor in Python?

def __del__(self):


@classmethod
class method to hold all the instances, but then they will never be destructed (well, unless we have a manual destroy call) but we can mark them as weak references.

https://docs.python.org/library/weakref.html


Abstract Base Class
  a blueprint
  you want to avoid people creating instances of it
  you want to make sure a subclass defines all the necessary methods
from abc import ABC, abstractmethod

class Main(ABC):
   pass

   @abstractmethod
   def method(self):
      pass



Multiple inheritance
not really recommended
Show call order when each one has an `__init__`
Show what happens if it becomes diamond shaped inheritance?

MRO - Method Resolution Order ?
`Classname.__mro__`

Interfaces - Python does not support them, but you can define other ABC-es
and use multiple inheritance to say that your class provides that method.


Composition (e.g. a line has 2 Points)


How to compare two points?  Compare both coordinates using `__eq__`
Which point is bigger?  the one where both coordinates are bigger (what to do when one is bigger and the other is smaller? Raise a ValueError, our own Error that inherits from Value error?)  In circles we
might say one is bigger than the other purely based on their area.
What happens if we implement `__eq__` for Point and compare two instances of Circle(Point) ?

```
def __eq__(self, value):
   if not isintsnace(value, Point):
       raise ValueError("Cannot compare Point to non-Pont {value.__class__.__name__}")

def __lt__(self, value):
   return ...

This also makes the object sortable


def __getattribute__(self, name):
    if name == "age":
       real = super().__getattribute__(name)


def __call__(self, ...):   to make the instances callable (when would we need it?)



__setattr__
__getattr__
```

## Data Science

Machine Learning

Data points show by a scatter plot
Clusters


Usupervised machine learning
cluster analyzis
K-means algorithm

## Jupyer Notebook


* Header type is legacy - use Markdown instead

* What other Kernels can I install?


## Machine learning

* Reinforcement learning
* Recommender system


## python speed improvement

* replace by a faster module (Levinshtein example)
* better algorithm with lower complexity,
* better data structure (dictioanry instead of list when that is better)
* profile the code and find the slow parts.
* concurrent execution (forking, threading, asynchronous)


## TODO

examples/types/fixed_literal_values.py
examples/types/type_of_dict.py
examples/other/network_example.py
examples/fork/a.py
examples/fork/frk.py
examples/fork/mem.py
examples/fork/pl.py
examples/dictionary/default_dict_for_list.py


Add exercises to each regex chapter
how to add color to log messages
