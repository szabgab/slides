# Boolean
{id: python-boolean}

## Boolean values: True and False
{id: boolean-values}
{i: True}
{i: False}

{aside}
In this chapter we are going to talk about boolean values and operations on boolean values.

Unlike in some other languages Python actually has 2 special symbols to represent True and False.

(In ther languages 0 usuall represents False and 1 represents True.
{/aside}

* True
* False

![](examples/boolean/true_and_false.py)

## if statement again
{id: if-statement-again}

![](examples/boolean/conditionals.py)


## Assign comparisions to variables
{id: assign-comparisions-to-variables}

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
* ()

Everything else is true.

![](examples/boolean/boolean_values.py)

`None` is like undef or Null or Nill in other languages.


## Comparision operators
{id: comparision-operators}
{i: ==}
{i: !=}
{i: <}
{i: <=}
{i: >=}
{i: >}

```
==             equal
!=             not equal

<              less than
<=             less than or equal
>              greater than
>=             greater than or equal
```
![](examples/other/compare_equals.py)


## Do NOT Compare different types
{id: compare-different-types}
![](examples/other/compare.py)


In `Python 2` please be careful and only compare the same types.
Otherwise the result will look strange.



```
True
False
True
False
```



In `Python 3`, comparing different types raises exception:


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

## Toggle
{id: toggle}
{i: not}

![](examples/boolean/toggle.py)

## Short circuit
{id: short-circuit}

![](examples/boolean/short_circuit.py)


## Short circuit fixed
{id: short-circuit-fixed}
![](examples/boolean/short_circuit_fixed.py)


## Incorrect use of conditions
{id: incorrect-use-of-conditions}

{aside}
In your normal speach you could probably say something like "If status_code is 401 or 302, do something.".
Meaning status_cone can be either 401 or 302.

If you tried to translate this into code directly you would write something like this:
{/aside}

```
if status_code == 401 or 302:
    pass
```

{aside}
However this is incorrect. This condition will be always true  as this is actually same as if you wrote: 
`if (status_code == 401) or (302)` so it will compare status_code to 401, and it will separately check if
302 is True, but any number different from 0 is considered to be True so the above expression will always be True.
{/aside}

What you probably meant is this:

```
if status_code == 401 or status_code == 302:
    pass
```

Alternative way:

{aside}
An alternative way to achieve the same results would be though probbaly at this point we have not learned the "in"
operator, nor lists (comma separated values in square brackets):
{/aside}

```
if status_code in [401, 302]
    pass
```

## Exercise: compare numbers
{id: exercise-compare-numbers}

* Ask the user to enter two numbers and tell us which one is bigger.

## Exercise: compare strings
{id: exercise-compare-strings}

* Ask the user to enter two strings
* Then ask the user to select if she wants to compare them based on ASCII or based on their length
* Then tell us which one is bigger.

```
Input a string: (user types string and ENTER)
Input another string: (user types string and ENTER) 
How to compare:
1) ASCII
2) Length
(user types 1 or 2 and ENTER)
```


## Solution: compare numbers
{id: solution-compare-numbers}

![](examples/boolean/compare_strings.py)

## Solution: compare strings
{id: solution-compare-strings}

![](examples/boolean/compare_strings.py)
