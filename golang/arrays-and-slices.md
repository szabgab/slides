# Arrays and slices
{id: arrays-and-slices}

## Arrays
{id: arrays}
{i: len}
{i: []}

![](examples/array/array.go)

* Length is part of the type!
* Two arrays with different length are also different types

## Arrays automatic length
{id: arrays-automatic-length}

![](examples/array2/array2.go)

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


## Slice
{id: slice}

![](examples/slice/slice.go)

## Slice append
{id: slice-append}

![](examples/slice_append/slice_append.go)

* [slice internals](https://blog.golang.org/go-slices-usage-and-internals)
