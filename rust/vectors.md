# Vectors in Rust
{id: vectors}

## Fixed vector of numbers
{id: fixed-vector-of-numbers}
{i: vec!}

* [Vec](https://doc.rust-lang.org/std/vec/struct.Vec.html)

![](examples/vectors/numbers.rs)

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

