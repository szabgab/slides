# Hash
{id: hash}


## Hash intro
{id: hash-intro}
{i: has_key}
{i: has_value}
{i: each_key}
{i: size}
{i: keys}

* [Hash](https://crystal-lang.org/api/Hash.html)

![](examples/hashes/hash.cr)

## Count words
{id: count-words}
{i: each}


![](examples/hashes/count_words.cr)

## Create empty hash
{id: create-empty-hash}
{i: empty?}

![](examples/hashes/empty_hash_of_strings.cr)

![](examples/hashes/empty_hash_string_int32.cr)

![](examples/hashes/empty_hash_string_int32_bool.cr)

## Hash and types
{id: hash-and-types}

![](examples/hashes/hash_and_types.cr)
![](examples/hashes/hash_and_types.out)

## Hash get value, get default value
{id: hash-get-value}

* Get value of a key
* Get value or `nil` if the key does not exist
* Get value of a default value if the key does not exist

![](examples/hashes/get_value.cr)

## Merge hashes
{id: hash-merge}
{i: merge}
{i: merge!}

![](examples/hashes/merge.cr)
![](examples/hashes/merge.out)

## Delete - remove an element from a hash
{id: hash-delete}
{i: delete}

* `delete!` does not exist.

![](examples/hashes/delete.cr)
![](examples/hashes/delete.out)


## Reject - remove an element from a hash
{id: hash-reject}
{i: reject}
{i: reject!}

![](examples/hashes/reject.cr)
![](examples/hashes/reject.out)

## Clear - empty a hash
{id: hash-clear}
{i: clear}

![](examples/hashes/clear.cr)

## Select - keep certain key-value pairs
{id: hash-select}
{i: select}
{i: select!}

![](examples/hashes/select.cr)
![](examples/hashes/select.out)

## Multi-dimensional hash
{id: hash-multi-dimensional}

![](examples/hashes/multi_dimensional.cr)

## Dig a hash
{id: hash-dig}
{i: dig}
{i: dig?}

![](examples/hashes/dig.cr)

