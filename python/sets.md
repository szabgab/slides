# Sets
{id: python-sets}

## sets
{id: sets}
{i: set}


* Sets in Python are used when we are primarily interested in operations that we know from [sets in mathematics](https://en.wikipedia.org/wiki/Set_(mathematics)).
* In day to day speach we often use the word "group" instead of "set" even though they are not the same.
* What are the common elements of two set (two groups)
* Is one group (set) the subset of the other?
* What are all the elements that exist in both groups (sets)?
* What are the elements that exist in exactly one of the groups (sets)?


![](examples/sets/try_set.py)
![](examples/sets/try_set.out)



## defining an empty set
{id: defining-an-empty-set}
![](examples/sets/empty.py)
![](examples/sets/empty.out)
![](examples/sets/empty2.out)


## Adding an element to a set (add)
{id: adding-an-element-to-a-set}
![](examples/sets/add_elements.py)
![](examples/sets/add_elements.out)


In Python 2:


![](examples/sets/add_elements2.out)


## Merging one set into another set (update)
{id: merging-one-set-into-another-set}
![](examples/sets/merge_sets.py)
![](examples/sets/merge_sets.out)



## set operations
{id: set-operations}
{i: set}
{i: issubset}
{i: intersection}
{i: difference}
![](examples/lists/languages.py)

```
english:  set(['car', 'door', 'lunar', 'era'])
spanish:  set(['era', 'hola', 'lunar'])
intersection:  set(['era', 'lunar'])
issubset:  True
symmetric_difference:  set(['car', 'door', 'hola'])
```


<a href="http://docs.python.org/3/library/stdtypes.html#set">stdtypes: set</a>





