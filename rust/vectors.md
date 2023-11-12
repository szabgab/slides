# Vectors in Rust
{id: vectors}

## Fixed vector of numbers
{id: fixed-vector-of-numbers}
{i: vec!}
{i: len}

* [Vec](https://doc.rust-lang.org/std/vec/struct.Vec.html)

![](examples/vectors/numbers/src/main.rs)
![](examples/vectors/numbers/out.out)

## Iterate over elements of vector using for-loop
{id: iterate-over-element-of-vector}

![](examples/vectors/numbers-iterate/src/main.rs)

## Mutable vector of numbers, append (push) values
{id: mutable-numbers-vector}
{i: push}
{i: append}

![](examples/vectors/mutable-numbers-vector/src/main.rs)

## Mutable empty vector for numbers (push)
{id: mutable-empty-vector-for-numbers}
{i: push}

![](examples/vectors/mutable-empty-vector-for-integers/src/main.rs)
![](examples/vectors/mutable-empty-vector-for-integers/out.out)

## Mutable empty vector for strings
{id: mutable-empty-vector-for-strings}

![](examples/vectors/mutable-empty-vector-for-strings/src/main.rs)
![](examples/vectors/mutable-empty-vector-for-strings/out.out)

## Mutable empty vector with type definition
{id: rust-vector}
{i: vec!}
{i: push}

![](examples/vectors/vector-with-type/src/main.rs)
![](examples/vectors/vector-with-type/out.out)


## Mutable vector of strings
{id: mutable-vector-of-strings}

![](examples/vectors/mutable-vector-of-strings/src/main.rs)
![](examples/vectors/mutable-vector-of-strings/out.out)


## Count words
{id: count-words}

* Given a string that consists of words and white-spaces, count how many times each word appears?

![](examples/vectors/count-words/src/main.rs)

## Vector extend (combining two vectors)
{id: vector-extend}
{i: extend}

![](examples/vectors/extend/src/main.rs)
![](examples/vectors/extend/out.out)

## Split string into vector
{id: split-string-into-vector}
{i: split}
{i: vec}

![](examples/vectors/split-string-into-vector/src/main.rs)
![](examples/vectors/split-string-into-vector/out.out)

![](examples/vectors/split-to-vector/src/main.rs)
![](examples/vectors/split-to-vector/out.out)

## Sort vector of numbers
{id: sort-vector-of-numbers}
{i: sort}

![](examples/vectors/sort-vector/src/main.rs)
![](examples/vectors/sort-vector/out.out)

## Exercise: Median
{id: exercise-median}

* Write a function that given a vector of integers it will return the median.

![](examples/vectors/median/src/main.rs)
![](examples/vectors/median/out.out)

## Exercise: ROT13
{id: rot13}

* Implement a function that given a string will return it ROT13 encrypted version.
* If we call the function again with the result we should get back the original string.

![](examples/vectors/rot13/src/main.rs)

## Chars to string
{id: chars-to-string}

![](examples/vectors/chars-to-string/src/main.rs)

## Vector of tuples
{id: vector-of-tuples}

![](examples/vectors/vector-of-tuples/src/main.rs)
![](examples/vectors/vector-of-tuples/out.out)

## Vector of structs
{id: vector-of-structs}

![](examples/vectors/vector-of-structs/src/main.rs)
![](examples/vectors/vector-of-structs/out.out)

## Vector of structs - change value
{id: vector-of-structs-change-value}


![](examples/vectors/vector-of-structs-change-value/src/main.rs)
![](examples/vectors/vector-of-structs-change-value/out.out)

## Join elements of vector into a string
{id: join-elements-of-vector}
{i: join}

![](examples/vectors/join/src/main.rs)
![](examples/vectors/join/out.out)

## Join vector of integers
{id: join-vector-of-integers}
{i: join}
{i: iter}
{i: map}
{i: collect}

![](examples/vectors/join-integers/src/main.rs)

## Maximum value of a vector
{id: maximum-vale-of-a-vector}
{i: max}
{i: match}
{i: iter}

![](examples/vectors/max-number/src/main.rs)
![](examples/vectors/max-number/out.out)


## Longest or shortest string in a vector
{id: longes-or-shortest-string-in-vector}
{i: max}
{i: min}
{i: max_by}
{i: min_by}
{i: cmp}

* max and min abc order
* max and min by length

![](examples/vectors/get-longest-string/src/main.rs)


## Change vector using map
{id: change-vector-using-map}
{i: into_iter}
{i: map}
{i: collect}

![](examples/vectors/map-on-integers/src/main.rs)

## Update values in vector of structs using map
{id: update-values-in-vector-of-structs-using-map}

![](examples/vectors/update-vector-of-structs/src/main.rs)
![](examples/vectors/update-vector-of-structs/out.out)

## map is lazy
{id: map-is-lazy}

![](examples/vectors/map1/src/main.rs)
![](examples/vectors/map1/out.out)

![](examples/vectors/map2/src/main.rs)
![](examples/vectors/map2/out.out)

![](examples/vectors/map3/src/main.rs)
![](examples/vectors/map3/out.out)

## filter numbers
{id: filter-numbers}
{i: iter}
{i: filter}
{i: cloned}
{i: collect}

* [cloned](https://doc.rust-lang.org/std/iter/trait.Iterator.html#method.cloned)

![](examples/vectors/filter-numbers/src/main.rs)
![](examples/vectors/filter-numbers/out.out)

## filter numbers iter into
{id: filter-numbers-iter-into}
{i: iter_into}

![](examples/vectors/filter-numbers-iter-into/src/main.rs)


## filter numbers by named function
{id: filter-numbers-by-named-function}

![](examples/vectors/filter-numbers-by-function/src/main.rs)

## filter string
{id: filter-string}
{i: iter}
{i: filter}
{i: cloned}
{i: collect}


![](examples/vectors/filter-strings/src/main.rs)
![](examples/vectors/filter-strings/out.out)

## Two references to the same vector
{id: two-refernces-to-the-same-vector}

![](examples/vectors/two-references-to-the-same-vector/src/main.rs)


## Filter vector of structs (cloning)
{id: filter-vector-of-structs-cloning}
{i: filter}
{i: cloned}
{i: Clone}

![](examples/vectors/filter-vector-of-structs-with-clone/src/main.rs)

## Convert vector of structs to vector of references
{id: convert-vector-of-structs-to-vector-of-references}

![](examples/vectors/convert-vector-of-structs-to-vector-of-references/src/main.rs)


## Filter vector of structs without copy
{id: filter-vector-of-structs-without-copy}

![](examples/vectors/filter-vector-of-structs/src/main.rs)

## Accessing the last element of a vector
{id: accessing-the-last-element-of-a-vector}
{i: len}
{i: last}

* Unlike Python and Perl, rust won't let us use a negative index in a vector so we won't be able to access the last element using `vector_name[-1]`
* We can either use `vector_name.len()-1` or
* We can use `vector_name.last(), but in this case we get an `Option` that can be `None` as well.

* If we access a seemingly arbitrary element that we calculated using `vector_name.len()-1` then either we get back a value or Rust will panic if we gave an index too big.
* On the other hand using `last` we are more protected. In that case we either get a value or `None` if the vector was empty.

![](examples/vectors/last-vec-index/src/main.rs)

## Insert element in vector
{id: instert-element-in-vector}
{i: insert}

![](examples/vectors/insert-element-in-vector/src/main.rs)


## Vector with optional values - None or out of range?
{id: none-or-out-of-range}
{i: get}
{i: is_none}
{i: is_some}

* If we have a vector that some of the elements can be `None` then the other elements must be `Some`-values and the whole thing must be defined using `Option`.
* If we try to access an element in a vector that is out of range we get a run-time panic.
* In order to avoid such panic we either need to check if our index is in range or we can use the `get` method.
* We can use the `get` method to access the element. It will return `None` if the index was out of range.
* Then the question arise, how do we know if the value was out of range or if it was in the range but the value was `None`?

![](examples/vectors/none-or-out-of-range/src/main.rs)
![](examples/vectors/none-or-out-of-range/out.out)


## Vector with optional values
{id: vector-with-optional-values}
{i: Option}
{i: None}
{i: Some}
{i: get}

![](examples/vectors/options/src/main.rs)
![](examples/vectors/options/out.out)


## Vector length and capacity
{id: vector-length-and-capacity}
{i: len}
{i: capacity}
{i: with_capacity}
{i: resize}

![](examples/vectors/with-capacity/src/main.rs)
![](examples/vectors/with-capacity/out.out)

## References to numbers
{id: references-to-numbers}

![](examples/other/references-to-numbers/src/main.rs)
![](examples/other/references-to-numbers/out.out)

## Queue
{id: queue}
{i: VecDeque}
{i: push_back}
{i: pop_front}
{i: len}
{i: capacity}

* [VecDeque](https://doc.rust-lang.org/std/collections/struct.VecDeque.html) provides for a fast queue
* It probably has to be mutable to make sense though we could create one from a fixed list of values and then just access the elements.
* We can add element at the end using `push_back`.
* We can fetch elements from the front using `pop_front`.
* As we add more elements Rust will automatically grow the `capacity` of the vector by a little bit more than needed to allow for faster growth.


![](examples/vectors/deque/src/main.rs)
![](examples/vectors/deque/out.out)


