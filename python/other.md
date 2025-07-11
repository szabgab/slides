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
![](examples/other/hello_ex.py)

* The first line staring with # is needed if you want to have a file that can be executed without explicitly typing in python as well.
* Make your file executable: **chmod u+x hello_ex.py**
* Run like: **./hello_ex.py**
* In order to run it as **hello_ex.py** in needs to be located in one of the directories listed in the **PATH** environment variable.




## pydoc
{id: pydoc}


If you really want it, you can also read some of the documentation on the command line, but unless you are locked up some place without Internet connection,
I don't recommend this.




Type `pydoc`. On Windows, you might need to create the following file and put it in a directory in your PATH. (see `echo %PATH%`)


![](examples/other/pydoc.bat)



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
![](examples/other/parameter_passing.py)

```
Hello Foo!!!!
```


## Command line arguments and main
{id: command-line-arguments-and-main}
![](examples/other/argv_main.py)

Run as **python argv.py Foo**



Later we'll see the `argparse` module that can handle command line arguments in a better way.




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

![](examples/other/xrange.py)

In Python 2 `range` creates a list of values `range(from, to, step)` and `xrnage` creates and iterator.
In Python 3 `range` creates the iterator and if really necesary then `list(range())` can create the list.

[range vs. xrange in Python](http://code-maven.com/range-vs-xrange-in-python)


## profile (with hotshot) slow code
{id: hotshot-slow-code}

It was experimental and dropped from Python 3

* [](https://docs.python.org/2/library/hotshot.html)

![](examples/advanced/slow_hotshot.py)
![](examples/advanced/slow_hotshot.out)

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

![](examples/other/sorted_key.py)
![](examples/other/sorted_key.out)

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

