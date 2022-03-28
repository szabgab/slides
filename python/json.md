# JSON
{id: python-json}

## JSON - JavaScript Object Notation
{id: json}
{i: json}

[JSON](http://www.json.org/) is basically the data format used by JavaScript. Because its universal availability it became the de-facto standard for data
communication between many different languages. Most dynamic languages have an fairly good mapping between JSON and their own data structures.
Lists and dictionaries in the case of Python.

Documentation of the
[Python json library](http://docs.python.org/library/json.html).

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


`dumps` can be used to take a Python data structure and generate a string in JSON format. That string can then be saved in a file,
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


## Pretty print JSON
{id: pretty-print-json}

![](examples/json/pretty_print.py)
![](examples/json/pretty_print.out)


## Sort keys in JSON
{id: sort-keys-in-json}

![](examples/json/sort_keys.py)
![](examples/json/sort_keys.out)


## Set order of keys in JSON - OrderedDict
{id: set-order-of-keys-in-json}
{i: collections}
{i: OrderedDict}

![](examples/dictionary/set_order.py)
![](examples/dictionary/set_order.out)


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

* Extend the exercise so if the user provides the `--list` flag then all the indexes are listed (and no counting is done).
* Extend the exercise so if the user provides the `--delete foo` parameter then the counter `foo` is removed.


## Exercise: Phone book in JSON
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

* If the user provides `Bar 123` save 123 for Bar.
* If the user provides `Bar 456` tell the user Bar already has a phone number.
* To update a phone-number the user must provide `--update Bar 456`
* To remove a name the user must provide `--delete Bar`
* To list all the names the user can provide `--list`


## Solution: Counter in JSON
{id: solution-json-counter}

![](examples/json/counter.py)


## Solution: Phone book
{id: solution-json-phonebook}

![](examples/json/phonebook.py)




