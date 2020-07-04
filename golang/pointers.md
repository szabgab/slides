# Pointers
{id: pointers}

## Integer assignment is copying (not pointer)
{id: no-pointer}

{aside}
Normally, that is without the use of pointers if we assign a variable that contains a number, we create a copy of the value in
a new place in the memory. Then if we change the value of the original variable (in this case if we increment it by one),
then only the content of that variable changes.

The same happens if we change the new variable (in this case assigning 3 to it), only the content of that variable changes.

Normally this is what you want in regular assignment.
{/aside}

![](examples/no-pointer/no_pointer.go)
![](examples/no-pointer/no_pointer.out)

## Pointer to integer
{id: int-pointer}
{i: &}
{i: *}

{aside}
We can use the & prefix during the assignment that means: take the pointer to this variable and copy the pointer.
This means that the new variable (b in our case) will point to the same place in memory where the value of the original
variable is. The content was not copied.

If at this point you print out the content of the new variable, you'll see the hexadecimal value of the pointer.
In order to print out the real value you need to prefix the variable by a *.

If you now change the original variable, you'll see both are incremented.
If you change the new variable (you'll have to use the * prefix for this)  both are incremented.

Maybe it is better to say that there is only one value jut two ways to access it.

I think you would rarely do this in such code, but it is important to understand the concept for when
we will want to pass a variable by reference to a function.
{/aside}

* `&amp;` get pointer to
* `*` get value behind pointer

![](examples/int-pointer/int_pointer.go)
![](examples/int-pointer/int_pointer.out)

## Array Pointer
{id: array-pointer}

{aside}
Just as with variables holding integers, variables holding arrays are also copied dirng assignment. Here too you can use
a pointer to have two ways to access the same array.
{/aside}

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

