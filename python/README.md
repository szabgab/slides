# The slides of the Python Progamming course

## Timing

Functional - part 1 - ~ 40 min + 30 min exercise
Functional - part 2 - 
Iterators           - ~ 50 min + 60 min exercise

https://julien.danjou.info/python-and-functional-programming/
https://stackabuse.com/functional-programming-in-python/
itertools.groupby
use reduce to group by ???

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

