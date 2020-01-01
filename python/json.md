# JSON
{id: python-json}

## JSON - JavaScript Object Notation
{id: json}
{i: json}

<a href="http://www.json.org/">JSON</a> is basically the data format used by JavaScript. Because its universal availability it became the de-facto standard for data
communication between many different languages. Most dynamic languages have an fairly good mapping between JSON and their own data structures.
Lists and dictionaries in the case of Python.




Documentation of the
<a href="http://docs.python.org/library/json.html">Python json library</a>.


![](examples/json/data.json)



## dumps
{id: json-dumps}
{i: dumps}
![](examples/json/dumps.py)

```
{'lname': 'Bar', 'email': None, 'fname': 'Foo',
  'children': ['Moo', 'Koo', 'Roo']}

{"lname": "Bar", "email": null, "fname": "Foo",
  "children": ["Moo", "Koo", "Roo"]}
```

(lines were broken for readability on the slides)


<emp>dumps</emp> can be used to take a Python data structure and generate a string in JSON format. That string can then be saved in a file,
inserted in a database, or sent over the wire.



## loads
{id: json-loads}
{i: loads}
![](examples/json/loads.py)

```
{"lname": "Bar", "email": null, "fname": "Foo",
    "children": ["Moo", "Koo", "Roo"]}

{u'lname': u'Bar', u'email': None, u'fname': u'Foo',
    u'children': [u'Moo', u'Koo', u'Roo']}
```

u is the Unicode prefix used in Python 2. In Python 3 it won't appear as Unicode is the default there.




## dump
{id: json-dump}
{i: dump}
![](examples/json/dump.py)

```
{'lname': 'Bar', 'email': None, 'fname': 'Foo',
  'children': ['Moo', 'Koo', 'Roo']}

{"lname": "Bar", "email": null, "fname": "Foo",
  "children": ["Moo", "Koo", "Roo"]}
```

(lines were broken for readability on the slides)


As a special case **dump** will save the string in a file or in other stream.



## load
{id: json-load}
{i: load}
![](examples/json/load.py)

```
{u'lname': u'Bar', u'email': None, u'fname': u'Foo',
    u'children': [u'Moo', u'Koo', u'Roo']}
```


## Round trip
{id: json-round-trip}
{i: loads}
{i: dumps}
![](examples/json/round_trip.py)


## Exercise: Counter in JSON
{id: exercise-json-counter}

Write a script that will provide several counters. The user can provide an argument on the command
line and the script will increment and display that counter.
Keep the current values of the counters in a single JSON file.
The script should behave like this:



```
$ python counter.py foo
1

$ python counter.py foo
2

$ python counter.py bar
1

$ python counter.py foo
3
```


## Exercise: Phone book
{id: exercise-json-phonebook}

Write a script that acts as a phonebook. As "database" use a file in JSON format.


```
$ python phone.py Foo 123
Foo added

$ python phone.py Bar
Bar is not in the phnebook

$ python phone.py Bar 456
Bar added

$ python phone.py Bar
456

$ python phone.py Foo
123
```


Can it handle changes in phone numbers?
Can it remove a name from the "database"?




## Exercise: Processes
{id: exercise-processes}

Write a program that will do "some work" that can be run in parallel
and collect the data. Make the code work in a single process by default
and allow the user to pass a number that will be the number of child processes
to be used. When the child process exits it should save the results in
a file and the parent process should read them in.




The "some work" can be accessing 10-20 machines using "ssh machine uptime"
and creating a report from the results.



It can be fetching 10-20 URLs and reporting the size of each page.


It can be any other network intensive task.


Measure the time in both cases




## Solution: Counter in JSON
{id: solution-json-counter}
![](examples/json/counter.py)


## Solution: Phone book
{id: solution-json-phonebook}
![](examples/json/phonebook.py)




