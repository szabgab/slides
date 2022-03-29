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

Examples:

* [OpenWeatherMap](https://openweathermap.org/api)
* [Using the Open Weather Map API with curl](https://code-maven.com/openweathermap-api-using-curl)
* [Using the Open Weather Map API with Python](https://code-maven.com/openweathermap-api-using-python)

* [Libretranslate](https://libretranslate.com/)

![](examples/json/data.json)


## JSON dumps
{id: json-dumps}
{i: dumps}

* Dictionaries and lists are handles
* Tuples are indistinguishable from lists
* Always Double-quotes
* `null` instead of `None`
* No trailing comma

![](examples/json/dumps.py)
![](examples/json/dumps.out)

`dumps` can be used to take a Python data structure and generate a string in JSON format. That string can then be saved in a file,
inserted in a database, or sent over the wire.



## JSON loads
{id: json-loads}
{i: loads}

![](examples/json/loads.py)
![](examples/json/loads.out)


## dump
{id: json-dump}
{i: dump}

![](examples/json/dump.py)

As a special case `dump` will save the string in a file or in other stream.

## load
{id: json-load}
{i: load}

![](examples/json/load.py)


## Round trip
{id: json-round-trip}
{i: loads}
{i: dumps}
![](examples/json/round_trip.py)


## Pretty print JSON
{id: pretty-print-json}

![](examples/json/pretty_print.py)
![](examples/json/pretty_print.out)

## Serialize Datetime objects in JSON
{id: serialize-datetime-objects-in-json}

* [Serialize datetime objects in JSON](https://code-maven.com/serialize-datetime-object-as-json-in-python)


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




