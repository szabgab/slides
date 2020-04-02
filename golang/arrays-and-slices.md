# Arrays and slices
{id: arrays-and-slices}

## Arrays
{id: arrays}
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


## Array change value
{id: array-change-value}

![](examples/array-change-value/array_change_value.go)
![](examples/array-change-value/array_change_value.out)


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

## Slice of an array
{id: slice-on-an-array}
{i: len}
{i: cap}

![](examples/slice-of-array/slice_of_array.go)
![](examples/slice-of-array/slice_of_array.out)

## Slice
{id: slice}
{i: slice}
{i: len}
{i: cap}

* You can view a slice to be just a very flexible array.
* Actually it is a slice of an array. A view on a section of the array.
* len - length
* cal - capacity

{aside}
The only difference you can see when we create a slice is that we don't explicitely say its size and we also don't put the 3 dots `...` in the square bracket.

There is also a `cap` function that returns the size of the underlying array.

We can access the elements of a slice using the postfix square-bracket notation. Just as with arrays.
{/aside}

![](examples/slice/slice.go)
![](examples/slice/slice.out)

## Change value in slice 
{id: slice-change-value}

![](examples/slice-change-value/slice_change_value.go)
![](examples/slice-change-value/slice_change_value.out)

## Slice Assign
{id: slice-assign}

* It is an alias to the other slice, same place in memory

{aside}
Unlike with arrays, when we assign a slice, we only assign the location of the slice in the memory. So if we change the content of one of the slices then the other one also sees the change. 
{/aside}

![](examples/slice-assign/slice_assign.go)
![](examples/slice-assign/slice_assign.out)


## Slice of a slice
{id: slice-of-slice}


![](examples/slice-of-slice/slice_of_slice.go)
![](examples/slice-of-slice/slice_of_slice.out)

* This would work on arrays as well: Slices of an array

## Slice append
{id: slice-append}
{i: append}

![](examples/slice-append/slice_append.go)
![](examples/slice-append/slice_append.out)

* Both the actual length and the capacity grew


* [slice internals](https://blog.golang.org/go-slices-usage-and-internals)
* [append to slice](https://tour.golang.org/moretypes/15)


## Remove last element of slice (pop)
{id: slice-remove-from-the-end}
{i: pop}

![](examples/slice-remove-last/slice_remove_last_element.go)
![](examples/slice-remove-last/slice_remove_last_element.out)

* The capacity remaind the same


## Remove first element of slice (shift, pop(0))
{id: remove-first-element-of-slice}
{i: shift}

![](examples/slice-shift/slice_shift.go)
![](examples/slice-shift/slice_shift.out)


## Pre-allocate capacity for slice with make
{id: pre-allocate-capacity-for-slice}
{i: make}

![](examples/slice-pre-allocate/slice_pre_allocate.go)
![](examples/slice-pre-allocate/slice_pre_allocate.out)

## For loop in slice - iterate over slice
{id: for-loop}
{i: range}
{i: for}

![](examples/loop-on-slice/loop_on_slice.go)
![](examples/loop-on-slice/loop_on_slice.out)

## for loop on values of slice (no index)
{id: for-values}

![](examples/for-values/for_values.go)


## Merge two slices
{id: merge-two-slices}
{i: ...}

![](examples/merge-slices/merge_slices.go)


## Find element in array or slice
{id: find-element-in-slice}

![](examples/find-element-in-slice/find_element_in_slice.go)
![](examples/find-element-in-slice/find_element_in_slice.out)

## Remove element of slice
{id: slice-remove-element}

![](examples/remove-element-from-slice/remove_element_from_slice.go)
![](examples/remove-element-from-slice/remove_element_from_slice.out)

## Weird merge slices
{id: weird-merge-slices}

* When we try to remove an element in the middle but assign to a new name.
* Avoid this mess!

![](examples/weird-merge-slices/weird_merge_slices.go)
![](examples/weird-merge-slices/weird_merge_slices.out)


## TODO: stack
{id: stack}

* see [lists](https://golang.org/pkg/container/list/)

## TODO: queue
{id: queue}

* see [lists](https://golang.org/pkg/container/list/)


## Exercise: count digits
{id: exercise-count-digits}

Skeleton:

![](examples/count-digits-exercise/count_digits_exercise.go)

Expected output:

![](examples/count-digits/count_digits.out)


## Exercise: count digits from string
{id: exercise-count-digits-from-string}

Skeleton:

![](examples/count-digits-from-string-skeleton/count_digits_from_string_skeleton.go)

Expected output:

![](examples/count-digits-from-string/count_digits_from_string.out)

## TODO: Exercise: count words
{id: exercise-count-words-slices}


## Solution: count digits
{id: solution-count-digits}

![](examples/count-digits/count_digits.go)

## Solution: count digits from string
{id: solution-count-digits-from-string}

![](examples/count-digits-from-string/count_digits_from_string.go)


## Solution: count words
{id: solution-count-words-slices}
