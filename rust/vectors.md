# Vectors in Rust
{id: vectors}

## Fixed vector of numbers
{id: fixed-vector-of-numbers}
{i: vec!}
{i: len}

* [Vec](https://doc.rust-lang.org/std/vec/struct.Vec.html)

![](examples/vectors/numbers.rs)
![](examples/vectors/numbers.out)

## Iterate over elements of vector using for-loop
{id: iterate-over-element-of-vector}

![](examples/vectors/numbers_iterate.rs)

## Mutable vector of numbers, append (push) values
{id: mutable-numbers-vector}
{i: push}
{i: append}

![](examples/vectors/mutable_numbers_vector.rs)

## Mutable empty vector for numbers (push)
{id: mutable-empty-vector-for-numbers}
{i: push}

![](examples/vectors/mutable_empty_vector_for_integers.rs)
![](examples/vectors/mutable_empty_vector_for_integers.out)

## Mutable empty vector for strings
{id: mutable-empty-vector-for-strings}

![](examples/vectors/mutable_empty_vector_for_strings.rs)
![](examples/vectors/mutable_empty_vector_for_strings.out)

## Mutable empty vector with type definition
{id: rust-vector}
{i: vec!}
{i: push}

![](examples/vectors/vector_with_type.rs)
![](examples/vectors/vector_with_type.out)


## Mutable vector of strings
{id: mutable-vector-of-strings}

![](examples/vectors/mutable_vector_of_strings_one.rs)
![](examples/vectors/mutable_vector_of_strings_one.out)



## Count words
{id: count-words}

* Given a string that consists of words and white-spaces, count how many times each word appears?

![](examples/vectors/count_words.rs)

## Vector extend (combining two vectors)
{id: vector-extend}
{i: extend}

![](examples/vectors/extend.rs)

## Split string into vector
{id: split-string-into-vector}
{i: split}
{i: vec}

![](examples/vectors/split_string_into_vector.rs)
![](examples/vectors/split_to_vector.rs)

## Sort vector of numbers
{id: sort-vector-of-numbers}
{i: sort}

![](examples/vectors/sort_vector.rs)
![](examples/vectors/sort_vector.out)

## Exercise: Median
{id: exercise-median}

* Write a function that given a vector of integers it will return the median.

![](examples/vectors/median.rs)
![](examples/vectors/median.out)

## Exercise: ROT13
{id: rot13}

* Implement a function that given a string will return it ROT13 encrypted version.
* If we call the function again with the result we should get back the original string.

![](examples/vectors/rot13.rs)

## Chars to string
{id: chars-to-string}

![](examples/vectors/chars_to_string.rs)

## Vector of tuples
{id: vector-of-tuples}

![](examples/vectors/vector_of_tuples.rs)
![](examples/vectors/vector_of_tuples.out)

## Vector of structs
{id: vector-of-structs}

![](examples/vectors/vector_of_structs.rs)
![](examples/vectors/vector_of_structs.out)

## Vector of structs - change value
{id: vector-of-structs-change-value}


![](examples/vectors/vector_of_structs_change_value.rs)
![](examples/vectors/vector_of_structs_change_value.out)

## Join elements of vector into a string
{id: join-elements-of-vector}
{i: join}

![](examples/vectors/join.rs)
![](examples/vectors/join.out)

## Join vector of integers
{id: join-vector-of-integers}
{i: join}
{i: iter}
{i: map}
{i: collect}

![](examples/vectors/join_integers.rs)

## Maximum value of a vector
{id: maximum-vale-of-a-vector}
{i: match}

![](examples/vectors/max_number.rs)
![](examples/vectors/max_number.out)

## Change vector using map
{id: change-vector-using-map}
{i: into_iter}
{i: map}
{i: collect}

![](examples/vectors/map_on_integers.rs)

## Update values in vector of structs using map
{id: update-values-in-vector-of-structs-using-map}

![](examples/vectors/update_vector_of_structs.rs)
![](examples/vectors/update_vector_of_structs.out)

## map is lazy
{id: map-is-lazy}

![](examples/vectors/map1.rs)
![](examples/vectors/map1.out)

![](examples/vectors/map2.rs)
![](examples/vectors/map2.out)

![](examples/vectors/map3.rs)
![](examples/vectors/map3.out)

## filter numbers
{id: filter-numbers}
{i: iter}
{i: filter}
{i: cloned}
{i: collect}

* [cloned](https://doc.rust-lang.org/std/iter/trait.Iterator.html#method.cloned)

![](examples/vectors/filter_numbers.rs)
![](examples/vectors/filter_numbers.out)

## filter numbers iter into
{id: filter-numbers-iter-into}
{i: iter_into}

![](examples/vectors/filter_numbers_iter_into.rs)


## filter numbers by named function
{id: filter-numbers-by-named-function}

![](examples/vectors/filter_numbers_by_function.rs)

## filter string
{id: filter-string}
{i: iter}
{i: filter}
{i: cloned}
{i: collect}


![](examples/vectors/filter_strings.rs)
![](examples/vectors/filter_strings.out)

## Two references to the same vector
{id: two-refernces-to-the-same-vector}

![](examples/vectors/two_references_to_the_same_vector.rs)


## Filter vector of structs (cloning)
{id: filter-vector-of-structs-cloning}
{i: filter}
{i: cloned}
{i: Clone}

![](examples/vectors/filter_vector_of_structs_with_clone.rs)

## Convert vector of structs to vector of references
{id: convert-vector-of-structs-to-vector-of-references}

![](examples/vectors/convert_vector_of_structs_to_vector_of_references.rs)


## Filter vector of structs without copy
{id: filter-vector-of-structs-without-copy}

![](examples/vectors/filter_vector_of_structs.rs)

## Accessing the last element of a vector
{id: accessing-the-last-element-of-a-vector}
{i: len}
{i: last}

* Unlike Python and Perl, rust won't let us use a negative index in a vector so we won't be able to access the last element using `vector_name[-1]`
* We can either use `vector_name.len()-1` or
* We can use `vector_name.last(), but in this case we get an `Option` that can be `None` as well.

* If we access a seemingly arbitrary element that we calculated using `vector_name.len()-1` then either we get back a value or Rust will panic if we gave an index too big.
* On the other hand using `last` we are more protected. In that case we either get a value or `None` if the vector was empty.

![](examples/vectors/last_vec_index.rs)

## Insert element in vector
{id: instert-element-in-vector}
{i: insert}

![](examples/vectors/insert_element_in_vector.rs)

