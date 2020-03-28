# Arrays and slices
{id: arrays-and-slices}

## Arrays
{id: arrays}
{i: len}
{i: []}

![](examples/array/array.go)
![](examples/array/array.out)

* Length is part of the type!
* Two arrays with different length are also different types.

## Arrays automatic length
{id: arrays-automatic-length}
{i: [...]}

![](examples/array-auto-length/array_auto_length.go)
![](examples/array-auto-length/array_auto_length.out)


## Array: empty and fill
{id: arrays-empty-fill}

![](examples/array-fill/array-fill.go)


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

![](examples/array-assignment-pointer/array_assignment_pointer.go)
![](examples/array-assignment-pointer/array_assignment_pointer.out)

{aside}
This way br is a poiner to ar so they refer to the same data in memory.
{/aside}

## Matrix (two dimensional array)
{id: matrix}

![](examples/array-matrix/array_matrix.go)
![](examples/array-matrix/array_matrix.out)


## Slice
{id: slice}

* A slice is just a very flexible array.

![](examples/slice/slice.go)


## Slice Assign
{id: slice-assign}

![](examples/slice-assign/slice_assign.go)
![](examples/slice-assign/slice_assign.out)

## Slice of slice
{id: slice-of-slice}


![](examples/slice-of-slice/slice_of_slice.go)
![](examples/slice-of-slice/slice_of_slice.out)

* This would work on arrays as well: Slices of an array

## Slice append
{id: slice-append}

![](examples/slice-append/slice_append.go)
![](examples/slice-append/slice_append.out)

* Both the actual length and the capacity grew


* [slice internals](https://blog.golang.org/go-slices-usage-and-internals)
* [append to slice](https://tour.golang.org/moretypes/15)


## Slice remove elements from the end
{id: slice-remove-from-the-end}

![](examples/slice-remove-last/slice_remove_last_element.go)
![](examples/slice-remove-last/slice_remove_last_element.out)

* The capacity remaind the same


## Pre-allocate capacity for slice with make
{id: pre-allocate-capacity-for-slice}
{i: make}

![](examples/slice-pre-allocate/slice_pre_allocate.go)
![](examples/slice-pre-allocate/slice_pre_allocate.out)

## for loop in slice - iterate over slice
{id: for-loop}
{i: range}

![](examples/loop/loop.go)

## for loop on values of slice (no index)
{id: for-values}

![](examples/for-values/for_values.go)

## Exercise: count digits
{id: exercise-count-digits}

Skeleton:

![](examples/count-digits-exercise/count-digits-exercise.go)

Expected Output:

```
0: 0
1: 1
2: 0
3: 2
4: 0
5: 0
6: 1
7: 3
8: 0
9: 1
```

## Exercise: count digits from string
{id: exercise-count-digits-from-string}

Skeleton:

![](examples/count-digits-skeleton/skeleton.go)

## Solution: count digits
{id: solution-count-digits}

![](examples/count-digits/count-digits.go)

## Solution: count digits from string
{id: solution-count-digits-from-string}

![](examples/count-digits-again/count-digits-again.go)


TODO:  append(a, b...)
shift / pop(0)   a[1:]
pop()   [:len(a)-1]

stack

a := []int{1, 2, 3, 4, 5, 6}
b := append(a[:2], a[3:]...)
weird result in a

