# Comparison and Boolean
{id: boolean}

## if statement again
{id: if-statement-again}
{i: if}
{i: ==}

![](examples/boolean/conditionals.py)

## Comparison operators
{id: comparison-operators}
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

## Compare numbers, compare strings
{id: compare-numbers-compare-strings}


![](examples/boolean/compare_two_numbers.py)

![](examples/boolean/compare_two_strings.py)

![](examples/boolean/compare_two_values.py)

* [ASCII](https://en.wikipedia.org/wiki/ASCII)

## Do NOT Compare different types!
{id: compare-different-types}

![](examples/boolean/compare.py)

In `Python 2` please be careful and only compare the same types.
Otherwise the result will look strange.


```
Yes
No
Yes
No
```

In `Python 3`, comparing different types raises exception:

![](examples/boolean/compare.out)


## Complex if statement with boolean operators
{id: complex-if-statement}

* Boolean operators or Logical operators
* and
* or
* not

![](examples/boolean/complex_if.py)

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


## Boolean values: True and False
{id: boolean-values}
{i: True}
{i: False}

{aside}
In this chapter we are going to talk about boolean values and operations on boolean values.

Unlike in some other languages Python actually has 2 special symbols to represent True and False.

(In those languages 0 usually represents False and 1 represents True.)
{/aside}

* True
* False

## Using True and False in variables
{id: using-true-and-false-in-variables}

![](examples/boolean/true_and_false.py)


## Comparison returns True or False
{id: comparison-returns-true-or-false}

![](examples/boolean/compare_equals.py)


## Assign comparisons to variables
{id: assign-comparisons-to-variables}

* True and False are real boolean values.

{i: False}
{i: True}
![](examples/boolean/true_false.py)

## Flag
{id: flag}

![](examples/boolean/flag.py)




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

## Does this value count as True or False?
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



## Incorrect use of conditions
{id: incorrect-use-of-conditions}

{aside}
In your normal speech you could probably say something like "If status_code is 401 or 302, do something.".
Meaning status_cone can be either 401 or 302.

If you tried to translate this into code directly you would write something like this:
{/aside}

```
if status_code == 401 or 302:
    pass
```

{aside}
However, this is incorrect. This condition will always be true  as this is actually same as if you wrote: 
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
An alternative way to achieve the same results would be though probably at this point we have not learned the "in"
operator, nor lists (comma separated values in square brackets):
{/aside}

```
if status_code in [401, 302]:
    pass
```

## Exercise: compare numbers
{id: exercise-compare-numbers}

* Create a file called **bool_compare_numbers.py**
* Ask the user to enter two numbers and tell us which one is bigger.

## Exercise: compare strings
{id: exercise-compare-strings}

* Create a file called **bool_compare_strings.py**
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

![](examples/boolean/compare_numbers.py)

## Solution: compare strings
{id: solution-compare-strings}

![](examples/boolean/compare_strings.py)
