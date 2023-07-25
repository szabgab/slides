# Hashes in Rust
{id: hash}

## Create empty HashMap, insert key-value pairs
{id: create-emptty-hash}
{i: HashMap}
{i: new}
{i: insert}
{i: len}

* [std::collections](https://doc.rust-lang.org/std/collections/index.html)
* [HashMap](https://doc.rust-lang.org/std/collections/hash_map/struct.HashMap.html)

![](examples/hashes/create_empty_hash.rs)
![](examples/hashes/create_empty_hash.out)

## Create immutable hash with data
{id: create-hash-with-data}
{i: HashMap}
{i: from}

![](examples/hashes/create_hash_with_data.rs)
![](examples/hashes/create_hash_with_data.out)

## Check if hash contains key (key exists)
{id: hash-containes-key}
{i: contains}
{i exists}

![](examples/hashes/contains_key.rs)
![](examples/hashes/contains_key.out)

## Get value from hash
{id: get-value-from-hash}
{i: get}

* `get` returns a reference to the value corresponding to the key.

![](examples/hashes/get_value_from_hash.rs)
![](examples/hashes/get_value_from_hash.out)


## Iterate over keys of a hash
{id: iterate-over-keys-of-hash}
{i: keys}

![](examples/hashes/iterate_over_keys.rs)
![](examples/hashes/iterate_over_keys.out)

## Iterate over key-value pairs in a Hash
{id: iterate-over-key-value-pairs-of-hash}
{i: iter}

* Use the `iter` method to get the iterator
* Though you can iterate over the hash directly. It does the same.

![](examples/hashes/iterate_over_pairs.rs)
![](examples/hashes/iterate_over_pairs.out)


## Rust hash update value
{id: rust-hashmap-update-value}
{i: entry}
{i: or_insert}

![](examples/hashes/update_hash.rs)
![](examples/hashes/updating_values.rs)

## Rust update values in a hash - count words
{id: rust-update-values-in-a-hash}

![](examples/hashes/count_words.rs)

## Remove element from hash
{id: remove-element-from-hash}
{i: remove}

![](examples/hashes/remove_from_hash.rs)
![](examples/hashes/remove_from_hash.out)

## Accessing values
{id: accessing-values}

* unwrap_or(0)  sets a default value to 0

![](examples/hashes/accessing_values.rs)
![](examples/hashes/accessing_values.out)


## Split string create hash
{id: spplit-string-create-hash}

![](examples/hashes/split_string_create_hash.rs)

## Create hash from key-value pairs after split
{id: create-hash-from-key-value-pairs}

![](examples/hashes/hash_from_key_value_pairs.rs)
![](examples/hashes/hash_from_key_value_pairs.out)

## Read key-value pairs from file
{id: read-key-value-pairs-from-file}

![](examples/hashes/key_value_pairs.txt)

![](examples/hashes/read_key_value_pairs.rs)
![](examples/hashes/read_key_value_pairs.out)

## Sort vector of hashes
{id: sort-vector-of-hashes}
{i: sort_by}

![](examples/hashes/sort_vector_of_hashes.rs)
![](examples/hashes/sort_vector_of_hashes.out)
