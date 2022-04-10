# Lists
{id: lists}

## Anything can be a list
{id: any-lists}

* Comma separated values
* In square brackets
* Can be any value, and a mix of values: Integer, Float, Boolean, None, String, List, Dictionary, ...
* But usually they are of the same type:
* Distances of astronomical objects
* Chemical Formulas
* Filenames
* Names of devices
* Objects describing attributes of a network device.
* Actions to do on your data.

![](examples/lists/any_list.py)
![](examples/lists/any_list.out)


## Any layout
{id: any-lists2}

* Layout is flexible
* Trailing comma is optional. It does not disturb us. Nor Python.

![](examples/lists/any_list2.py)
![](examples/lists/any_list2.out)


## Access elements of a list
{id: access-elements-of-lists}
{i: []}
{i: len}

* Access single element: **[index]**
* Access a sublist: **[start:end]**
* Creates a copy of that sublist

![](examples/lists/simple.py)


## List slice with steps
{id: list-slice}

* List slice with step: **[start:end:step]**

![](examples/lists/slice.py)


## Change a List
{id: list-change}
{i: :}

![](examples/lists/change.py)

* Unlike strings, lists are mutable. You can change the content of a list by assigning values to its elements.
* You can use the slice notation to change several elements at once.
* You can even have different number of elements in the slice and in the replacement. This will also change the length of the array.

## Change sublist vs change element of a list
{id: change-sublist-vs-change-element}

![](examples/lists/change_sublist.py)

![](examples/lists/change_element.py)


## Change with steps
{id: list-change-steps}

![](examples/lists/change_steps.py)


## List assignment and list copy
{id: list-copy}
{i: [:]}

![](examples/lists/not_copy.py)

* There is one list in the memory and two pointers to it.
* If you really want to make a copy the pythonic way is to use the slice syntax.
* It creates a shallow copy.

![](examples/lists/real_copy.py)

## Shallow vs. Deep copy of lists
{id: deep-copy-of-lists}
{i: copy}
{i: deepcopy}

[copy](https://docs.python.org/library/copy.html)

```
copy.copy()     # shallow copy
copy.deepcopy() # deep copy
```

![](examples/lists/shallow_copy.py)


![](examples/lists/deep_copy.py)


## join
{id: join}
{i: join}

![](examples/lists/join.py)

* For real CSV use: [csv](https://docs.python.org/library/csv.html)

## join list of numbers
{id: join-mixed-list}
![](examples/lists/joining_integers.py)


## split
{id: split}
{i: split}
{i: list}

* Special case: To split a string to its characters: Use the **list()** function.
* Split using more than one splitter: use **re.split**

![](examples/lists/split.py)


## for loop on lists
{id: for-loop-on-list}
{i: for}
{i: in}

![](examples/lists/for.py)
![](examples/lists/for.out)


## in list
{id: in-syntax-on-list}
{i: in}

Check if the value is in the list?

![](examples/lists/in.py)


## Where is the element in the list
{id: where-is-the-element-in-the-list}
{i: index}
![](examples/lists/index.py)
![](examples/lists/index.py.out)


## Index improved
{id: index-improved}
{i: index}
![](examples/lists/index_improved.py)


## [].insert
{id: list-insert}
{i: insert}
{i: unshift}
![](examples/lists/insert.py)


## [].append
{id: list-append}
{i: append}
![](examples/lists/append.py)



## [].remove
{id: list-remove}
{i: remove}
![](examples/lists/remove.py)

{aside}

Remove **first** element from a list given by its value.
Throws an exception if there is no such element in the list.
{/aside}


## Remove element by index [].pop
{id: list-pop}
{i: pop}
![](examples/lists/pop.py)

{aside}
Remove and return the last element of a list. Throws an exception if the list was empty.
{/aside}



## Remove first element of list
{id: list-shift}
{i: pop}
{i: shift}

{aside}
To remove an element by its index, use the slice syntax:
{/aside}

![](examples/lists/remove_first_element.py)


## Remove several elements of list by index
{id: list-remove-by-index}
{i: slice}

{aside}
To remove an element by its index, use the slice syntax:
{/aside}

![](examples/lists/remove_by_slice.py)



## Use list as a queue - FIFO
{id: list-as-a-queue}

![](examples/lists/list_as_a_queue.py)
![](examples/lists/list_as_a_queue.out)


## Queue using deque from collections
{id: dequeue}
{i: collections}
{i: deque}
{i: append}
{i: popleft}

![](examples/lists/queue_with_deque.py)

![](examples/lists/queue_with_deque.out)

* .append
* .popleft
* len()  number of elements
* if q:  to see if it has elements or if it is empty
* [dequeue](https://docs.python.org/library/collections.html#collections.deque)



## Fixed size queue
{id: fixed-size-dequeue}
{i: maxlen}
![](examples/lists/fixed_size_queue.py)


## List as a stack - LIFO
{id: list-as-a-stack}

![](examples/lists/stack.py)
![](examples/lists/stack.out)


## stack with deque
{id: stack-with-deque}
![](examples/lists/stack_with_deque.py)



## Exercies: Queue
{id: exercise-queue}


* Create file called **queue_of_people.py**

* The application should manage a queue of people.

* It will prompt the user for a new name by printing **:**, the user can type in a name and press ENTER. The app will add the name to the queue.
* If the user types in "n" then the application will remove the first name from the queue and print it.
* If the user types in "x" then the application will print the list of users who were left in the queue and it will exit.
* If the user types in "s" then the application will show the current number of elements in the queue.


```
$ python queue_of_people.py

: Joe
: Jane
: Mary
: s
  3
: n
  next is Joe
: n
  next is Jane
: Peter
: n
  next is Mary
: n
  next is Peter
: n
  the queue is empty
: Bar
: Tal
: x
  Left in the queue: Bar, Tal
$
```


## Exercise: Stack
{id: exercise-stack}


* Create file called **reverse_polish_calculator.py**
* Implement a Reverse Polish Calculator

```
2
3
4
+
*
=
14
```

```
x = eXit, s = Show, [+-*/=]
:23
:19
:7
:8
:+
:3
:-
:/
:s
[23.0, -0.631578947368421]
:+
:=
22.36842105263158
:s
[]
:x
```

## Exercise: MasterMind
{id: exercise-mastermind}

* Create file called **mastermind.py**

* Implement the MasterMind game.

The computer "thinks" a number with 4 different digits.
You guess which digits. For every digit that matched both
in value, and in location the computer gives you a `*`. For every
digit that matches in value, but not in space the computer gives
you a `+`. Try to guess the given number in as few guesses as possible.


```
Computer: 2153
You:      2467  *
You:      2715  *++
```


## Solution: Queue with list
{id: solution-queue}

![](examples/lists/queue_people.py)

## Solution: Queue with deque
{id: solution-queue-deque}

![](examples/lists/deque_people.py)

## Solution: Reverse Polish calculator (stack) with lists
{id: solution-stack}

![](examples/lists/reverse_polish_calculator.py)

## Solution: Reverse Polish calculator (stack) with deque
{id: solution-stack-deque}

![](examples/lists/reverse_polish_calculator_deque.py)

## Solution: MasterMind
{id: solution-mastermind}

![](examples/lists/master_mind.py)

## MasterMind to debug
{id: mastermind-to-debug}

Debug the following version of the MasterMind game.

![](examples/lists/MasterMind_to_debug.py)

## Debugging Queue
{id: debugging-queue}


The following implementation has a bug. (Even though the n was supposed to remove the element
and the code seems to mean that it does, we still see two items after we removed the first.)

The question is how to debug this?



![](examples/lists/queue_with_bug.py)

```
your name: Foo
your name: Bar
your name: n
Foo
your name: s
2
```



## sort
{id: sort}
{i: sort}
![](examples/lists/sort.py)


## sort numbers
{id: sort-numbers}
{i: sort}
{i: key}
{i: abs}

![](examples/lists/sort_numbers.py)

## key sort of strings
{id: key-sort}
{i: key}
{i: len}

* Another example for using a **key**.
* To sort the list according to length

![](examples/lists/sort_key.py)
![](examples/lists/sort_key.out)


## sort mixed values
{id: sort-mixed}

![](examples/lists/sort_mixed.py)

In Python 3 it throws an exception.

![](examples/lists/sort_mixed.out)

Python 2 puts the numbers first in numerical order and then the strings in ASCII order.

```
[100, 'foo', 42, 'bar']
[42, 100, 'bar', 'foo']
```

## sorting with sorted
{id: sorted}
{i: sorted}

![](examples/lists/sorted.py)


## sort vs. sorted
{id: sort-vs-sorted}

The sort() method will sort a list in-place and return None.
The built-in sorted() function will return the sorted list and leave the original list intact.

## Sorted and change - shallow copy
{id: sorted-and-change}

* Sorted creates a shallow copy of the original list

* If the list elements are simple values that creates a copy

![](examples/lists/sorted_and_change.py)
![](examples/lists/sorted_and_change.out)

* If some of the elements are complex structures (list, dictionaries, etc.) then the internal structures are not copied.
* One can use `copy.deepcopy` to make sure the whole structure is separated, if that's needed.

![](examples/lists/sorted_and_change_deep.py)
![](examples/lists/sorted_and_change_deep.out)


## Sorting characters of a string
{id: sorting-characters}

![](examples/lists/sorting-characters.py)


## range
{id: range}
{i: range}

![](examples/lists/range.py)


## Looping over index
{id: looping-over-index}

![](examples/lists/loop.py)
![](examples/lists/loop.out)

![](examples/lists/loop_index.py)
![](examples/lists/loop_index.out)


## Enumerate lists
{id: enumerate-lists}
{i: enumerate}

![](examples/lists/enumerate.py)
![](examples/lists/enumerate.out)


## List operators
{id: list-operators}

![](examples/lists/operators.py)


## List of lists
{id: list-of-lists}
![](examples/lists/list_of_lists.py)


## List assignment
{id: list-assignment}

{aside}

List assignment works in "parallel" in Python.
{/aside}
![](examples/lists/list_assignment.py)

```
x,y = f()  # works if f returns a list of 2 elements
```


It will throw a run-time ValueError exception if the number
of values in the returned list is not 2. (Both for fewer and for more return values).




## List documentation
{id: list-documentation}

* [datastructures](http://docs.python.org/tutorial/datastructures.html)



## tuple
{id: tuple}
{i: tuple}
{i: ()}

Tuple

* A tuple is a fixed-length immutable list. It cannot change its size or content.
* Can be accessed by **index**, using the **slice** notation.
* A tuple is denoted with parentheses: (1,2,3)

![](examples/lists/tuple.py)
![](examples/lists/tuple.out)

List


* Elements of a list can be changed via their index or via the list slice notation.
* A list can grow and shrink using **append** and **pop** methods or using the **slice** notation.
* A list is denoted with square brackets:   [1, 2, 3]

![](examples/lists/list.py)
![](examples/lists/list.out)


{aside}
Tuples are rarely used. There are certain places where Python or some module require tuple (instead of list) or return a tuple (instead of a list)
and in each place it will be explained. Otherwise you don't need to use tuples.

e.g. keys of dictionaries can be tuple (but not lists).
{/aside}

## Convert list to tuple and tuple to list
{id: convert-list-to-tuple}

![](examples/lists/totuple.py)
![](examples/lists/totuple.out)

## Enumerate returns tuples
{id: enumerate-lists-tuples}
{i: enumerate}
{i: tuple}

![](examples/lists/enumerate_tuple.py)
![](examples/lists/enumerate_tuple.out)


## Change a tuple
{id: change-a-tuple}

![](examples/lists/change_tuple.py)


## Sort tuples
{id: sort-tuples}

![](examples/lists/sort_tuples.py)

## Sort tuples by specific elements
{id: sort-tuples-by-specific-element}

Sorting tuples or list, or other complex structures

![](examples/lists/sort_tuples_by_specific_elements.py)

## Sort and secondary sort
{id: sort-and-secondary-sort}

{aside}
We have a list of words. It is easy to sort them by length, but what will be the order among the words
that have the same length?

A sort using a lambda-function that returns a tuple can provide the secondary sort order.
{/aside}

![](examples/lists/sort_by_two_keys.py)



## Exercise: color selector menu
{id: exercise-menu}

* In a script called **color_selector_menu.py** have a list of colors. Write a script that will display a menu (a list of numbers and the corresponding color) and prompts the user for a number. The user needs to type in one of the numbers. That's the selected color.


1. blue
1. green
1. yellow
1. white


* For extra credit make sure the system is user-proof and it won't blow up on various incorrect input values. (e.g Floating point number. Number that is out of range, non-number)
* For more credit allow the user to supply the number of the color on the command line. **python color_selector_menu.py 3**. If that is available, don't prompt.
* For further credit allow the user to provide the name of the color on the command line: **python color_selector_menu.py yellow** Can you handle color names that are not in the expected case (e.g. YelloW)?
* Any more ideas for improvement?


## Exercise: count digits
{id: exercise-count-digits}

Create a script called **count_digits_in_lists.py** that given a list of numbers count how many times each digit appears? The output will look like this:


```
0  1
1  3
2  3
3  2
4  1
5  2
6  2
7  0
8  1
9  1
```

* Use this skeleton

![](examples/lists/count_digits_skeleton.py)


## Exercise: Create list
{id: exercise-create-list}

* Create a script called **create_list.py** that given a list of strings with words separated by spaces, create a single list of all the words.

* Skeleton:

![](examples/lists/create_list_skeleton.py)

* Expected result:

```
['grape', 'banana', 'mango', 'nut', 'orange', 'peach', 'apple', 'nut', 'banana', 'apple', 'mango']
```

Then create a list of unique values sorted in alphabetical order.

Expected result:

```
['apple', 'banana', 'grape', 'mango', 'nut', 'orange', 'peach']
```


## Exercise: Count words
{id: exercise-count-words-in-list}

* Create a script called **count_words_in_lists.py** that given a list of words (for now embedded in the program itself) will count how many times each word appears.

![](examples/lists/count_words_skeleton.py)

Expected output:

```
Moon        2
Gas         1
Asteroid    3
Dwarf       1
```


## Exercise: Check if number is prime
{id: exercise-is-prime}

Write a program called **is_prime.py** that gets a number on the command line a prints "True" if the number is a prime
number or "False" if it isn't.

```
python is_prime.py 42
False
python is_prime.py 19
True
```


## Exercise: DNA sequencing
{id: exercise-dna-sequencing}

* Create a file called **dna_sequencing.py**
* A, C, T, G are called bases or nucleotides
* Given a sequence like **'ACCGXXCXXGTTACTGGGCXTTGTXX'** (nucleotides mixed up with other elements)
* First return the sequences containing only ACTG. The above string can will be changed to **['ACCG', 'C', 'GTTACTGGGC', 'TTGT']**.
* Then sort them by lenght. Expected result: **['GTTACTGGGC', 'ACCG', 'TTGT', 'C']**

* What if the original string contains more than on type of foreign elements? e.g. **'ACCGXXTXXYYGTTQRACQQTGGGCXTTGTXX'**. Can you do the same?
* Expected output: **['TGGGC', 'ACCG', 'TTGT', 'GTT', 'AC', 'T']**


## Solution: menu
{id: solution-menu}

![](examples/lists/colors.py)

* We would like to show a menu where each number corresponds to one element of the list so this is one of the places where we need to iterate over the indexes of a list.
* `len(colors)` gives us the length of the list (in our case 4)
* `range(len(colors))` is the range of numbers between 0 and 4 (in our case), meaning 0, 1, 2, 3.
* (Sometimes people explicitly write 4 in this solution, but if later we change the list and include another color we'll have to remember updating this number as well. This is error prone and it is very easy to deduct this number from the data we already have. (The list.))
* We start the list from 0, but when we display the menu we would like to show the numbers 1-4 to make it more human friendly. Therefore we show `ix+1` and the color from locations `ix`.
* We ask for input and save it in a variable.

* We use the `isdecimal` method to check if the user typed in a decimal number. We give an error and exit if not.
* Then we check if the users provided a number in the correct range of values. We give an error and exit if not.
* then we convert the value to the correct range of numbers (remember, the user sees and selects numbers between 1-4 and we need them between 0-3).



## Solution: count digits
{id: solution-count-digits}


![](examples/lists/count_digits.py)


First we have to decide where are we going to store the counts. A 10 element long list seems to fit our requirements so if we have 3 0s and 2 8s we would have `[3, 0, 0, 0, 0, 0, 0, 0, 2, 0]`.


* We have a list of numbers.
* We need a place to store the counters. For this we create a variable called counter which is a list of 10 0s. We are going to count the number of times the digit 3 appears in `counters[3]`.
* We iterate over the numbers so `num` is the current number. (e.g. 1203)
* We would like to iterate over the digits in the current number now, but if we write `for var in num` we will get an error `TypeError: 'int' object is not iterable` because `num` is a number, but numbers are not iterables, so we we cannot iterate over them. So we need to convert it to a string using `str`.
* On each iteration `char` will be one character (which in or case we assume that will be a digit, but still stored as a string).
* `int(char)` will convert the string to a number so for example "2" will be converted to 2.
* `count[int(char)]` is going to be `char[2]` if `char` is "2". That's the location in the list where we count how many times the digit 2 appears in our numbers.
* We increment it by one as we have just encountered a new copy of the given digit.
* That finished the data collection.

* The second for-loop iterates over all the "possible digits" that is from 0-9, prints out the digit and the counter in the respective place.

## Solution: Create list
{id: solution-create-list}
{i: unique}
{i: sorted}
{i: set}

![](examples/lists/create_list.py)

## Solution: Count words
{id: solution-count-words-in-list}

![](examples/lists/count_words_two_lists.py)

![](examples/lists/count_words_two_lists_one_loop.py)


## Solution: Check if number is prime
{id: solution-is-prime}

![](examples/lists/is_prime.py)


## Solution: DNA sequencing
{id: solution-dna-sequencing}

![](examples/lists/dna_sequencing.py)

## Solution: DNA sequencing other
{id: solution-dna-sequencing-using-other}

![](examples/lists/dna_sequencing_other.py)

## Solution: DNA sequencing using replace
{id: solution-dna-sequencing-using-replace}

![](examples/lists/dna_sequencing_replace.py)

## Solution: DNA sequencing using regex
{id: solution-dna-sequencing-using-regex}

![](examples/lists/dna_sequencing_regex.py)

## Solution: DNA sequencing with filter
{id: solution-dna-sequencing-filter}

![](examples/lists/dna_sequencing_filter.py)


## Solution: DNA sequencing with filter and lambda
{id: solution-dna-sequencing-filter-lambda}

![](examples/lists/dna_sequencing_filter_lambda.py)


## [].extend
{id: list-extend}
{i: extend}

![](examples/lists/extend.py)


## append vs. extend
{id: list-append-vs-extend}

{aside}

What is the difference between [].append and [].extend ?
The method **append** adds its parameter as a single element to the list, while **extend** gets a list and adds its content.
{/aside}

![](examples/lists/append_extend.py)


## split and extend
{id: split-extend}

{aside}
When collecting data which is received from a string via splitting,
we would like to add the new elements to the existing list:
{/aside}

![](examples/lists/split_extend.py)



