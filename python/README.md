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




