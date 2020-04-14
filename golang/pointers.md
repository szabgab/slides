# Pointers
{id: pointers}

## No Pointer
{id: no-pointer}

![](examples/no-pointer/no_pointer.go)
![](examples/no-pointer/no_pointer.out)

## Int Pointer
{id: int-pointer}
{i: &}
{i: *}

![](examples/int-pointer/int_pointer.go)
![](examples/int-pointer/int_pointer.out)

## Array Pointer
{id: array-pointer}

* Assigning an array creates a copy of the data.
* One can assign a pointer and then both variables access the same place in memory. 

![](examples/array-pointer/array_pointer.go)
![](examples/array-pointer/array_pointer.out)

## Slice Pointer and copy slice
{id: slice-pointer}
{i: copy}

* Assigning a slices assigns the reference to the slice, to the same place in memory.
* However if we then change one of the variables (e.g. enlarge it), it might be moved to another array and then the two get separated.
* If we assign a pointer to the slices, that pointer goes to the "head of the slice" which is moved when we move the slice.  

![](examples/slice-pointer/slice_pointer.go)
![](examples/slice-pointer/slice_pointer.out)

## Pointer
{id: pointer}

* [video](https://youtu.be/YS4e4q9oBaU?t=14813)

