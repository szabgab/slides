# Other slides
{id: other}

## Other slides
{id: other-slides}


Some slides that used to be part of the material and they might return to be there, but for now they were parked here.


## Atom for Python
{id: atom-for-python}

{aside}

Some details about the Atom editor. You can freely skip this part. Personally I don't use it now.
{/aside}

* [Atom](https://atom.io/)


Autocomplete


* apm install autocomplete-python


Autocomplete


* easy_install jedi
* apm install autocomplete-plus-python-jedi


Linter


* easy_install flake8
* easy_install flake8-docstrings
* apm install linter
* apm install linter-flake8


[source](http://www.marinamele.com/install-and-configure-atom-editor-for-python)



## IDLE - Integrated DeveLopment Environment
{id: idle}
{i: IDLE}

* Python shell
* Better editing
* Limited debugger
* `c:\Python27\Lib\idlelib\idle.bat`
* `C:\Users\Gabor\AppData\Local\Programs\Python\Python35\Lib\idlelib\idle.bat`



## sh-bang - executable on Linux/Apple
{id: sh-bang}
![](examples/basics/hello_ex.py)

* The first line staring with # is needed if you want to have a file that can be executed without explicitly typing in python as well.
* Make your file executable: **chmod u+x hello_ex.py**
* Run like: **./hello_ex.py**
* In order to run it as **hello_ex.py** in needs to be located in one of the directories listed in the **PATH** environment variable.



## Strings as Comments
{id: strings-as-comments}
{i: '''}

{aside}

# marks single line comments.
There are no real multi-line comments in Python, but we can use triple-quots to
create multi-line strings and if they are not part of another statement,  they will be
disregarded by the Python interpreter. Effectively creating multi-line comments.
{/aside}
![](examples/basics/string_comments.py)


## pydoc
{id: pydoc}


If you really want it, you can also read some of the documentation on the command line, but unless you are locked up some place without Internet connection,
I don't recommend this.




Type `pydoc`. On Windows, you might need to create the following file and put it in a directory in your PATH. (see `echo %PATH%`)


![](examples/basics/pydoc.bat)



## Spyder Intro
{id: spyder-intro}

* iPython console (bottom right)
* Spyder-Py2 / Preferences / Console / Advanced Settings
* Save the file (Ctrl-S / Command-S)
* Run/Run  (F5)
* F9   - execute selected text (e.g. we can eecute a function definition after we've changed it)
* TAB for autocomple names of already existing variables.


```
print("abc")
"abc".          shows the available methods.
"abc".center    Command-I will explain what is "center"
```


## Interactive Debugging
{id: interactive-debugging}
![](examples/other/interact.py)


## Parameter passing
{id: parameter-passing}
![](examples/basics/parameter_passing.py)

```
Hello Foo!!!!
```


## Command line arguments and main
{id: command-line-arguments-and-main}
![](examples/basics/argv_main.py)

Run as **python argv.py Foo**



Later we'll see the `argparse` module that can handle command line arguments in a better way.




## Infinite loop
{id: infinite-loop}
![](examples/strings/infinite_loop.py)


## break
{id: break}
{i: break}
![](examples/strings/break.py)

```
0
1
2
3
4
5
6
done
```


## continue
{id: continue}
{i: continue}
![](examples/strings/continue.py)

```
1
2
3
8
9
10
```


## While with many conditions
{id: while-many-conditions}
![](examples/strings/while_many_conditions.py)


## while loop with many conditions
{id: infinite-while-many-conditions}
![](examples/strings/infinite_while_many_conditions.py)


## Format with conversion (stringifiation with str or repr)
{id: format-with-conversion}

Adding !s or !r in the place-holder we tell it to cal the str or repr
method of the object, respectively.



* repr (__repr__) Its goal is to be unambiguous
* str (__str__) Its goal is to be readable
* The default implementation of both are useless
* Suggestion
* [Difference between __str__ and __repr__](http://stackoverflow.com/questions/1436703/difference-between-str-and-repr-in-python)

![](examples/format/format_no_conversion.py)
![](examples/format/format_conversions.py)


## Name of the current function in Python
{id: name-of-the-current-function}
{i: inspect}
{i: currentframe}
{i: stack}
![](examples/advanced/name_of_current_function.py)


## Name of the caller function in Python
{id: name-of-the-caller-function}
{i: inspect}
{i: stack}
![](examples/advanced/name_of_caller_function.py)


## Stack trace in Python using inspect
{id: stack-trace-using-inspect}
{i: inspect}
{i: stack}
![](examples/advanced/stack_trace.py)
![](examples/advanced/stack_trace.out)



## SAX with coroutine
{id: sax-coroutine}
![](examples/xml/sax_coroutine.py)


copied from [Stack Overflow](http://stackoverflow.com/questions/8873643/how-to-return-data-from-a-python-sax-parser)
based on [coroutines](http://www.dabeaz.com/coroutines/)

![](examples/xml/cosax.py)


## Getting the class name of an object
{id: class-name}
{i: __class__}
{i: __name__}
{i: type}

How to find out which class an object (instance) belongs to?

![](examples/other/class.py)


## Inheritance - super
{id: inheritance-call-super}

{aside}
We can also call super() passing a different class name
{/aside}

![](examples/oop/inheritance/ball_shape2.py)


## Inheritance - super - other class
{id: inheritance-bad-super}

{aside}
We cannot pass any class name to super()
{/aside}

![](examples/oop/inheritance/bad_shapes.py)



## iterator - pairwise
{id: iterator-pairwise}

![](examples/iterators/pairwise_manual.py)


## iterator - grouped
{id: iterator-grouped}

![](examples/iterators/grouped_manual.py)
![](examples/iterators/grouped_manual.out)


## itertools - groupby
{id: itertools-groupby}

Group elements

![](examples/iterators/groupby.py)

## Circular references
{id: circular-references}

circular references are cleaned up the by the garbage collector
but maybe not all the memory is given back to the OS, and it can take some time to clean them up.

![](examples/advanced/circular.py)

but weakref might expedite the cleanup. See also the gc module and if I can show it
http://stackoverflow.com/questions/2428301/should-i-worry-about-circular-references-in-python

## Context managers: with (file) experiments
{id: context-managers-with-file-experiments}

![](examples/advanced/with_file_write.py)

```
f = open('out.txt', 'w')
f.write("hello\n")
f.close()

# for line in open("myfile.txt"):
#    print line,
# the file is closed only when script ends
```

## itertools - izip
{id: itertools-izip}
{i: izip}

Python 3 does not need this any more as the built-in zip is already an iterator.

Combine two unbounded lists

![](examples/iterators/izip.py)


## mixing iterators
{id: iterators-mixer}
{i: izip}

Combine three unbounded lists

![](examples/iterators/mixer.py)


## mixing iterators
{id: iterators-mixer-iterators}

![](examples/iterators/my_iterators.py)

## itertools - pairwise
{id: itertools-pairwise}
{i: iter}
{i: izip}

![](examples/iterators/pairwise.py)


Every 2 element from a list. We are using the exact same iterator object in both places of the izip() call,
so very time izip() wants to return a tuple, it will fetch two elements from the same iterator.

[Iterating over every two elements in a list](http://stackoverflow.com/questions/5389507/iterating-over-every-two-elements-in-a-list)

## itertools - grouped
{id: itertools-grouped}

Every N element from a list

![](examples/iterators/grouped.py)


## range vs xrange in Python
{id: range-vs-xrange}
{i: range}
{i: xrange}

![](examples/lists/xrange.py)

In Python 2 `range` creates a list of values `range(from, to, step)` and `xrnage` creates and iterator.
In Python 3 `range` creates the iterator and if really necesary then `list(range())` can create the list.

[range vs. xrange in Python](http://code-maven.com/range-vs-xrange-in-python)


## profile (with hotshot) slow code
{id: hotshot-slow-code}

It was experimental and dropped from Python 3

* [](https://docs.python.org/2/library/hotshot.html)

![](examples/advanced/slow_hotshot.py)
![](examples/advanced/slow_hotshot.out)

## Abstract Base Class without abc
{id: abstract-base-class-without-abc-python-2}

Only works in Python 2?

![](examples/oop/abc/without_abc.py)

## Abstract Base Class with abc Python 2 ?
{id: abstract-base-class-with-abc-python2}
{i: abc}

![](examples/oop/abc/with_abc.py)

* [Abstract Base Classes in Python](https://dbader.org/blog/abstract-base-classes-in-python)
* [abc](https://docs.python.org/library/abc.html)


## Abstract Base Class with metaclass
{id: abstract-base-class-with-metaclass}
{i: __metaclass__}

![](examples/oop/abc/abc_meta.py)


## Create class with metaclass
{id: create-class-with-metaclass}

![](examples/classes/meta.py)
![](examples/classes/create_class.py)

* [what is a metaclass](http://stackoverflow.com/questions/100003/what-is-a-metaclass-in-python)

## Python Descriptors
{id: descriptors}
{i: __init__}
{i: __get__}
{i: __set__}
{i: __delete__}

A more manual way to implement the property() functionality we have just seen.
Use cases:


* Implement type-checking and/or value checking for attribute setters ()


* [Descriptors](http://intermediatepythonista.com/classes-and-objects-ii-descriptors)
* [Descriptor HowTo Guide](https://docs.python.org/howto/descriptor.html)

## alter iterator
{id: iterators-alter}

Is this interesting at all ?

![](examples/iterators/alter.py)


## Create a counter queue
{id: class-counter-queue}
{i: Queue}

![](examples/threads/counter_queue.py)

## A Queue of tasks
{id: class-tasks}

![](examples/threads/run_tasks.py)



## Python from .NET
{id: python-from-dotnet}

TODO and add to dotnet

TODO: example with async call in .NET getting back to python


## assert to verify values
{id: assert}
{i: assert}
{i: raise}
{i: Exception}

![](examples/modules/raise_exception.py)
![](examples/modules/raise_exception.out)

![](examples/modules/assert.py)
![](examples/modules/assert.out)


## mycalc as a self testing module
{id: self-testing-module}
{i: __file__}

![](examples/modules/use_mycalc.py)

```
$ python use_mycalc.py
42
```
![](examples/modules/mycalc.py)

```
$ python mycalc.py
Self testing  mycalc.py
```


## doctest
{id: doctest}
{i: doctest}

![](examples/modules/fibonacci_doctest.py)

```
python -m doctest fibonacci_doctest.py
python examples/modules/fibonacci_doctest.py

```

![](examples/modules/fibonacci_doctest.out)

[doctest](https://docs.python.org/library/doctest.html)


## Export import
{id: export-import}
{i: __all__}
{i: import}
{i: from}

* from mod import a,b,_c  - import 'a', 'b', and '_c' from 'mod'
* from mod import *  - import every name listed in __all__ of 'mod' if __all__ is available.
* from mod import *  - import every name that does NOT start with _ (if __all__ is not available)
* import mod - import 'mod' and make every name in 'mod' accessible as 'mod.a', and 'mod._c'

![](examples/modules/my_module.py)
![](examples/modules/x.py)
![](examples/modules/y.py)


## Export import with __all__
{id: import-with-all}
{i: __all__}

![](examples/modules/my_module2.py)
![](examples/modules/z.py)


## import module
{id: import-module}

![](examples/modules/q.py)


## deep copy list
{id: deep-copy-list}

![](examples/modules/copy_list.py)

```
[{'name': 'Jane', 'email': 'joe@examples.com', 'phone': '1234'}, {'name': 'Mary', 'email': 'mary@examples.com'}, {'name': 'George'}]
[{'name': 'Jane', 'email': 'joe@examples.com', 'phone': '1234'}, {'name': 'Mary', 'email': 'mary@examples.com'}, {'name': 'George'}]
```

![](examples/modules/shallow_copy_list.py)

```
[{'name': 'Jane', 'email': 'joe@examples.com', 'phone': '1234'}, {'name': 'Mary', 'email': 'mary@examples.com'}, {'name': 'George'}]
[{'name': 'Jane', 'email': 'joe@examples.com', 'phone': '1234'}, {'name': 'Mary', 'email': 'mary@examples.com'}]
```


![](examples/modules/deep_copy_list.py)

```
[{'name': 'Jane', 'email': 'joe@examples.com', 'phone': '1234'}, {'name': 'Mary', 'email': 'mary@examples.com'}, {'name': 'George'}]
[{'name': 'Joe', 'email': 'joe@examples.com'}, {'name': 'Mary', 'email': 'mary@examples.com'}]
```


## deep copy dictionary
{id: deep-copy-dictionary}

![](examples/modules/copy_dictionary.py)

```
{'name': 'Foo Bar', 'grades': {'math': 90, 'art': 100}, 'friends': ['Mary', 'John', 'Jane', 'George'], 'email': 'foo@bar.com'}
{'name': 'Foo Bar', 'grades': {'math': 90, 'art': 100}, 'friends': ['Mary', 'John', 'Jane', 'George'], 'email': 'foo@bar.com'}
```

* [deepcopy](https://docs.python.org/library/copy.html#copy.deepcopy)


![](examples/modules/deep_copy_dictionary.py)

```
{'name': 'Foo Bar', 'grades': {'math': 90, 'art': 100}, 'friends': ['Mary', 'John', 'Jane', 'George'], 'email': 'foo@bar.com'}
{'name': 'Foo Bar', 'grades': {'math': 70, 'art': 100}, 'friends': ['Mary', 'John', 'Jane', 'George']}
```


## Pandas Stocks
{id: pandas-stocks}

![](examples/pandas/stocks.py)


## Pandas Stocks
{id: pandas-read-csv-stocks}

![](examples/pandas/read_csv_stocks.py)


## Merge Dataframes
{id: merge-dataframes}
![](examples/pandas/merge_dataframes.py)


## Analyze Alerts
{id: analyze-alerts}
![](examples/pandas/alerts.py)


## Analyze IFMetrics
{id: analyze-ifmetrics}
![](examples/pandas/ifmetrics.py)

## Calculate Genome metrics - add columns
{id: calculate-genome-metrics-add-columns}

![](examples/pandas/genome_calculation_add_columns.py)


## Calculate Genome metrics - vectorized
{id: calculate-genome-metrics-vecorized}

![](examples/pandas/genome_calculation_vectorized.py)


## Calculate Genome metrics - vectorized numpy
{id: calculate-genome-metrics-vecorized-numpy}

![](examples/pandas/genome_calculation_vectorized_numpy.py)

## Pandas more
{id: pandas-more}

```
df.iloc[:, 4:10].sum(axis=1)

# rearrange order of columns
cols = list(df.columns)
df = df[ cols[0:4], cols[-1], cols[4:20] ]

to_csv('file.csv', index=False)

read_csv(filename, delimiter='\t')
to_csv(filename, sep='\t')


# after filtering out some rows:
df = df.reset_index()
df.reset_index(drop=True, inplace=True)


filter with
df.loc[ ~df['Name'].str.contains('substring') ]

can also have regex=True parameter

# replace values
df[ df['Name'] == 'old', 'Name' ] = 'new'
```


## Pandas Series
{id: pandas-series}
{i: Series}
{i: values}
{i: index}
{i: RangeIndex}

![](examples/pandas/series.py)


## Pandas Series with names
{id: pandas-series-with-names}

![](examples/pandas/series_with_names.py)

## Matplotlib subplot
{id: matplotlib-subplot}

* Generates a separate graph, but when saving to disk, the image is blank

fig, ax = plt.subplots()
ax.plot(
    [ 1,  2,   3,  4 ],
    [ 10, 3, 45, 5 ],
)

## Jupyter StackOverflow - historgram
{id: jupyter-stackoverflow-histogram}

```
# Historgram of the top 20 countries
first20.hist(bins = 20)

# Plot using Seaborn
plot = sns.relplot(data = first20)
plot.set_xticklabels(rotation=90)
```

## Jupyter StackOverflow - OpenSourcer
{id: jupyter-stackoverflow-opensourcer}

```
df['OpenSourcer'].value_counts()

df['OpenSourcer'].unique()
```



## Jupyter StackOverflow - cross tabulation
{id: jupyter-stackoverflow-cross-tabulation}

```
# Crosstabulation
first10 = country_count.head(10)
subset = df[ df['Country'].isin( first10.keys() ) ]
# subset.count()

# subset['OpenSourcer'].value_counts()
grouped = subset.groupby('Country')['OpenSourcer'].value_counts()
# grouped.plot.bar(figsize=(15,15))

pd.crosstab(subset['Country'], df['OpenSourcer'])

ct = pd.crosstab(subset['Country'], df['OpenSourcer']).apply(lambda r: 100 * r/r.sum(), axis=1)
ct

ct.transpose().hist(figsize=(15, 15))
```



## Jupyter StackOverflow - salaries
{id: jupyter-stackoverflow-salaries}

```
# Try to show the average salary by country
grp = df.groupby('Country').mean().round({'CompTotal' : 0})
#grp['CompTotal']
pd.set_option('display.float_format', lambda x: '{:,}'.format(x))
grp.sort_values('CompTotal', ascending=False)
```



## Jupyter StackOverflow - replace values
{id: jupyter-stackoverflow-replace-values}

```
nd = df.replace({'OpenSourcer' : {
        'Never' : 0,
        'Less than once per year' : 1,
        'Less than once a month but more than once per year' : 2,
        'Once a month or more often' : 3,
       } })
nd
nd.describe()
nd.groupby('Country').mean().sort_values('OpenSourcer', ascending=False)
```


## ord in a file
{id: ord-in-file}
{i: ord}

![](examples/strings/ord.py)

## NameError
{id: name-error}

```
python common_error.py 42
```

![](examples/other/common_error.py)

## UnboundLocalError
{id: unbound-local-error}

```
python common_error_in_function.py 42
```

![](examples/other/common_error_in_function.py)

## Insert element in sorted list using bisect
{id: instert-element-in-sorted-list-using-bisect}
{i: bisect}

![](examples/other/find_insert_location_bisect.py)

## Insert element in sorted list using insort
{id: instert-element-in-sorted-list-using-insort}
{i: insort}

![](examples/other/find_insert_location_insort.py)


![](examples/decorators/dir_tree.py)
![](examples/decorators/dir_tree_return.py)
![](examples/decorators/dir_tree_with_callback.py)
![](examples/other/deco.py)

## Classes
{id: old-oop-examples}

![](examples/classes/ppl.py)
![](examples/classes/ppl.out)

## Create a class inherit from object
{id: class-creation-inherit-from-object}

* In Python 2.x classes had to inherit from `object` in order to become 'new style' classes.

![](examples/classes/with_object.py)
![](examples/classes/with_object.out)


## Abstract Base Class without ABC
{id: abstract-base-class-without-abc}

![](examples/oop/abc/no_abc.py)
![](examples/oop/abc/no_abc.out)


## Gravatar in Python
{id: gravatar}

![](examples/gravatar.py)

## Debug with ptpython
{id: debug-with-ptpython}

```
pip install ptpython
```

* Then either use it as a REPL to explore code or make your application fall back into this REPL to debug your code.

![](examples/other/debug_with_ptpython.py)

## REPL - Interactive debugging with ptpython
{id: interactive-debugging-with-ptpython}

![](examples/other/interactive_debugging_with_ptpython.py)

## Print in color on the CLI
{id: print-in-color}
{i: colorama}

![](examples/other/colored_text.py)

* [colorama](https://pypi.org/project/colorama/)

## Easy Install
{id: easy-install}

* [setuptools](http://pypi.python.org/pypi/setuptools)

```
$ easy_install module_name
```

* Intsalling pip on Windows as well: `easy_install pip` Will work on Windows as well.


```
easy_install -d ~/python Genshi
```

## sorting with sorted using a key
{id: key-sorted}

To sort the list according to length using sorted

![](examples/lists/sorted_key.py)
![](examples/lists/sorted_key.out)

## get and set locale
{id: get-and-set-locale}
{i: locale}
{i: LC_CTYPE}
{i: getlocale}
{i: setlocale}

![](examples/other/set_locale.py)


## Modify time anomality
{id: modify-time-anomality}

{aside}
Without calling flush the modify-time of the two files will be the same. Even if we sleep 0.001 seconds.
Despite the fact that the filesystem provide more accurate values.

If we we wait a bit between calls, or if we flush the buffer of the file, then the timestamps will be different.
{/aside}

![](examples/other/modify_time_is_the_same.py)

## Some strange code
{id: some-strange-code}

![](examples/other/bad_code.py)

## is vs ==
{id: is-vs-equal-equal}

![](examples/other/is_vs_equal.py)

