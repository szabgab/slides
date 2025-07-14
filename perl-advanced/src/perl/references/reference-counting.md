# Reference counting

* reference counting}


As you already know perl automatically allocates memory
when you add a new element to an array or hash. It also
frees up memory (although only internally) when you
remove the element from the array or hash.

Similarly when you create an array or a hash, perl sets up a
counter (called reference counter) and sets it to 1.
When the array or hash goes out of scope the counter is reduced
by 1. If the counter reaches 0 perl frees the memory allocated
to that array. Without references this is always the case.

When you create a reference to an array and store
it in a variable perl increases the reference counter of
the original array by 1 (to 2). Now if the array goes
out of scope and the ref count is reduced by 1 it still does
not reach 0 so perl does not free up the location of the array.

Only if the reference stops referring to this memory location
will the counter reach 0 thereby freeing up the memory allocated
to the array.


