# Arrays in JavaScript
{id: arrays}

## for-loop
{id: for-loop}
{i: for}

```
for (INITIALIZE;   CONDITION;   STEP) {

}
```
![](examples/js/for_loop.js)


## while loop
{id: while-loop}
{i: while}

```
while (CONDITION) {

}
```
![](examples/js/while.js)

```
2
3
4
5
6
7
```


## Break out from while loop in JavaScript
{id: break-out-from-while-javascript}
{i: break}
![](examples/js/break_while.js)

```
2
3
4
```


## An infinite while loop
{id: infinite-while-loop}
![](examples/js/infinite_loop.js)



## Continue to next in while loop in JavaScript
{id: continue-next-while-javascript}
{i: continue}
![](examples/js/continue_while.js)

```
2
3
4
5
6
7
```


## do-while loop in JavaScript
{id: do-while-loop-javascript}
{i: do while}

The loop is executed at least once.

![](examples/js/do_while.js)

For example you ask a question and let the user guess. Every time you compare
  the answer to the expected answer. You will need to
  get the value from the user before the first compare, and then if it fails,
  ask the user again. If you use plain "while" then you'll have to read from the user
  once before the while-loop and then inside the loop too. OTOH if you use the "do-while"
  loop, it is enought to ask in the do-block.




## new Array
{id: new-array}
{i: new}
{i: Array}
{i: for}
{i: length}
![](examples/js/new_array.js)


## Literal array: []
{id: new-array-square-brackets}
{i: []}
![](examples/js/new_array_brackets.js)


## Enlarge array with elements
{id: array-elements}
![](examples/js/array_elements.js)


## JavaScript Arrays - pop - push
{id: pop-push-shift-unshift}
{i: pop}
{i: push}
![](examples/js/pop_push.js)


## JavaScript Arrays - shift - unshift
{id: shift-unshift}
{i: shift}
{i: unshift}
![](examples/js/shift_unshift.js)


## Two dimensional array (matrix)
{id: two-dimensional-array}
{i: matrix}
![](examples/js/two_dimensional_array.js)



## For-in loop on array
{id: for-in-loop-on-array}
{i: for}
{i: in}

{aside}

We don't have to use the C-style for-loop on arrays. We can use the simpler, for-in construct.
It will iterate over the index of the array.
{/aside}
![](examples/js/for_in_loop_on_array.js)


## ForEach loop on array
{id: foreach-loop-on-array}
{i: forEach}

{aside}

Another way to iterate over the elements of an array is to use the forEach method of the array.
It gets a function as an argument and it will call that function with each one of the values of the array.
{/aside}
![](examples/js/foreach_loop_on_array.js)


## Reverse array
{id: reverse-arrays}
{i: reverse}
![](examples/arrays/reverse.js)


## Concatenate arrays
{id: concatenate-arrays}
{i: concat}
![](examples/arrays/concat.js)


## Concatenate array with object
{id: concatenate-arrays-with-object}
![](examples/arrays/concat_other.js)


## Concatenate array is shallow
{id: shallow-concatenate-arrays}
![](examples/arrays/concat_shallow.js)


## Array indexOf lastIndexOf
{id: array-index}
{i: indexOf}
{i: lastIndexOf}
![](examples/arrays/index.js)


## Array slice (range) or splice
{id: array-slice}
{i: slice}
{i: splice}

slice(from, to) - shallow copy of a range defined by its end points.


splice(from, length) - shallow copy of a range defined by the number of elements in it

![](examples/arrays/slice.js)


## Split string, join array
{id: split-join}
{i: split}
{i: join}
![](examples/arrays/split_join.js)


## Deep copy with JSON
{id: deep-copy-json}
{i: JSON}

```
JSON.parse(JSON.stringify(o));
```


## Exercise: Count digits
{id: exercise-count-digits}


Given an array of strings in which every string contains numbers separated by spaces,
count how many times each digit appears?


![](examples/arrays/count_digits_skeleton.js)

Expected output:


```
0 0
1 2
2 3
3 2
4 1
5 1
6 2
7 0
8 1
9 0
```


## Solution: Count digits
{id: solution-count-digits}
![](examples/arrays/count_digits.js)


## Exercise: Count characters
{id: exercise-count-character}

Given a string count how many time each character appears. See this skeleton:

![](examples/arrays/count_characters_skeleton.js)


## Solution: Count characters
{id: solution-count-character}
![](examples/arrays/count_characters.js)


## Exercise: Number guessing - history
{id: exercise-number-guessing}


In the previous chapter we had an exercise in which the computer "thought"
a number, and the user had to guess it.

* Show the  history of guesses.
* Show if we are getting closer (warm) or farther away (cold) relative to the previous guess.





## Solution: Number guessing - history
{id: solution-number-guessing}
![](examples/arrays/guess_number_history.html)
![](examples/arrays/guess_number_history.js)


## Exercise: Number guessing
{id: exercise-number-guessing-start-new-game}


Once that works, add a new button allowing the user to start a new game once one was finished.




Once that works allow the user to "give up" the current game and start a new one.




## Exercise: Reverse the number guessing game
{id: exercise-reversed-number-guessing-game}


In this version you think about a number between 1-200 and press the "start" button.
Then the computer guesses and you have to tell it if the guessed number is the one
you thought about, or if it is smaller or larger than what you thought about.
For this you might need to add 3 new buttons.
If your answer was "smaller" or "bigger", the computer guesses again.
How many guesses does your program need?




## Solution: Reverse the number guessing game
{id: solution-reversed-number-guessing-game}
![](examples/arrays/reverse_number_guessing.html)
![](examples/arrays/reverse_number_guessing.js)




