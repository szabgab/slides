# Boolean
{id: python-boolean}

## if statement again
{id: if-statement-again}
![](examples/boolean/conditionals.py)


## True and False
{id: boolean-values}

* True and False are real boolean values.

{i: False}
{i: True}
![](examples/boolean/true_false.py)


## Boolean
{id: any-boolean-value}
![](examples/boolean/boolean.py)


## True and False values in Python
{id: false-values}
{i: None}

* None
* 0
* "" (empty string)
* False
* []
* {}


Everything else is true.

![](examples/boolean/boolean_values.py)


<b>None</b> is like undef or Null or Nill in other languages.




## Comparision operators
{id: comparision-operators}
{i: ==}
{i: !=}

```
==                        equal
!=                        not equal

&lt;                      less than
&lt;=                     less than or equal
&gt;                      greater than
&gt;=                     greater than or equal
```
![](examples/other/compare_equals.py)


## Do NOT Compare different types
{id: compare-different-types}
![](examples/other/compare.py)


In <b>Python 2</b> please be careful and only compare the same types.
Otherwise the result will look strange.



```
True
False
True
False
```



In <b>Python 3</b>, comparing different types raises exception:


![](examples/other/compare.out)



## Boolean operators
{id: boolean-operators}
{i: and}
{i: or}
{i: not}

* and
* or
* not


```
if COND:
   do something
else:
   do something other

if not COND:
    do something other

if COND1 and COND2:
    do something

if COND1 or COND2:
    do something

if COND1 and not COND2:
    do something
```


## Boolean truth tables
{id: boolean-truth-tables}

```
COND1 and COND2     Result
True      True      True
True      False     False
False     True      False
False     False     False
```

```
COND1 or COND2      Result
True      True      True
True      False     True
False     True      True
False     False     False
```

```
not COND     Result
True         False
False        True
```


## Short circuit
{id: short-circuit}
![](examples/boolean/short_circuit.py)


## Short circuit fixed
{id: short-circuit-fixed}
![](examples/boolean/short_circuit_fixed.py)


## Incorrect use of conditions
{id: incorrect-use-of-conditions}


```
if status_code == 401 or 302:
    pass
```



Probably meant this:




```
if status_code == 401 or status_code == 302:
    pass
```



That can be written like this as well:




```
if status_code in [401, 302]
    pass
```


## Exercise: compare values
{id: exercise-compare-values}

* Ask the user to enter two numbers and tell us which one is bigger.
* Ask the user to enter two strings and tell us which one is bigger.





