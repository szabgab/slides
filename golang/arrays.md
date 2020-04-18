# Arrays
{id: arrays}

## Arrays
{id: arrays-intro}
{i: len}
{i: []}
{i: len}

{aside}
An array can hold a series of values. Both the length and the type of the values of an array is fixed at the time we create it.
Unlike in some other languages, you cannot mix different types of values in an array.
The content can be changed.
We can access the individual elements of an array with a post-fix square-bracket indexing.
{/aside}

* Length is part of the type!
* Two arrays with different length are also different types.

![](examples/array/array.go)
![](examples/array/array.out)

## Array index out of range - compile time
{id: array-out-of-range}

![](examples/array-out-of-range/array_out_of_range.go)
![](examples/array-out-of-range/array_out_of_range.out)

## Array index out of range - run time
{id: array-out-of-range-run-time}

![](examples/array-index/array_index.go)
![](examples/array-index/array_index.out)

## Array change value
{id: array-change-value}

![](examples/array-change-value/array_change_value.go)
![](examples/array-change-value/array_change_value.out)


## Arrays automatic length
{id: arrays-automatic-length}
{i: [...]}

{aside}
There was a slight duplication of information in the above example as we could have deducted the size from the list of initial values. This happens with the 3 dots.
{/aside}

![](examples/array-auto-length/array_auto_length.go)
![](examples/array-auto-length/array_auto_length.out)




## Array: empty and fill
{id: arrays-empty-fill}

{aside}
On the other hand we could also initialize an array with only the size, without initial values. In this case the default values in the array will be the 0 values of the appropriate type.
{/aside}

![](examples/array-fill/array_fill.go)


## Empty array of strings
{id: arrays-empty-strings}

{aside}
You can also use an array of strings.
{/aside}

![](examples/array-empty-strings/array_empty_strings.go)



## Array assignment (copy)
{id: array-assignment-copy}


![](examples/array-assignment/array_assignment.go)
![](examples/array-assignment/array_assignment.out)

{aside}
Assigning an array is by default creates a copy.
Some cases this is what we want, in other cases we'd prefer to have reference / pointer to the same data in memmory.
{/aside}


## Array assignment (pointer)
{id: array-assignment-pointer}
{i: &}

![](examples/array-assignment-pointer/array_assignment_pointer.go)
![](examples/array-assignment-pointer/array_assignment_pointer.out)

{aside}
This way `br` is a poiner to `ar` so they refer to the same data in memory. Even though `br` is a pointer we can still access elements in the same way as in the original array.
We'll discuss pointers in depth later on.
{/aside}

## Matrix (two dimensional array)
{id: matrix}

![](examples/array-matrix/array_matrix.go)
![](examples/array-matrix/array_matrix.out)

## For loop on array - iterate over array
{id: for-loop-on-array}
{i: range}
{i: for}

![](examples/loop-on-array/loop_on_array.go)
![](examples/loop-on-array/loop_on_array.out)

## for loop on values of array (no index)
{id: for-array-values}

![](examples/for-array-values/for_array_values.go)
![](examples/for-array-values/for_array_values.out)


## Arrays conclusion
{id: arrays-conclusion}

```
x := [3]int{}               // 3-long arrays with default 0 values
x := [...]int{2, 7, 4}      // 3-long array with values
x := [3]int{2, 7, 4}        // same, but with unnecessary duplication of information
z := x[2]                    // access element 
x[2] = 42                   // assign to element
x[4]                        // out-of-range index: compile-time or run-time error
for i, v := range array {}  // iterator over index and value 
```

## Exercise: Language Selector
{id: exercise-language-selector}

* Create a menu where people can pick a language by selecting the number next to the language.
* You have a list of languages in an array as we have in the skeleton.

![](examples/language-selector-skeleton/language_selector_skeleton.go)

* It displays a "menu" that associates each language with a number.
* The user types in one of the numbers.
* The code checks if it is a number and if it is in the correct range.
* If it is, then we display the selected language.
* The interaction will look like this:

![](examples/language-selector/language_selector.out)


## Exercise: count digits
{id: exercise-count-digits}

* Given a list of digits, count how many time each digit appears.

Skeleton:

![](examples/count-digits-skeleton/count_digits_skeleton.go)

Expected output:

![](examples/count-digits/count_digits.out)


## Exercise: count digits from string
{id: exercise-count-digits-from-string}

* Given a string of digits, count how many times each digit appears?

Skeleton:

![](examples/count-digits-from-string-skeleton/count_digits_from_string_skeleton.go)

Expected output:

![](examples/count-digits-from-string/count_digits_from_string.out)


## Exercise: Report statistics
{id: exercise-report-statistics}

Given some numbers in an array, print out the total, the average, the minimum and the maximum values.

![](examples/statistics-skeleton/statistics_skeleton.go)

Expected output:

![](examples/statistics/statistics.out)


## Solution: Language Selector
{id: solution-language-selector}

![](examples/language-selector/language_selector.go)

## Solution: count digits
{id: solution-count-digits}

![](examples/count-digits/count_digits.go)

## Solution: count digits from string
{id: solution-count-digits-from-string}

![](examples/count-digits-from-string/count_digits_from_string.go)

## Solution: Report statistics
{id: solution-report-statistics}

![](examples/statistics/statistics.go)
