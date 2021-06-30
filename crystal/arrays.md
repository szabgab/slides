# Arrays
{id: arrays}


## Arrays intro
{id: arrays-intro}

* [Array API](https://crystal-lang.org/api/Array.html)
* [Array reference](https://crystal-lang.org/reference/syntax_and_semantics/literals/array.html)

![](examples/arrays/array.cr)

## Array elements - indexing
{id: array-elements}

![](examples/arrays/elements.cr)

## Array iterate over (each, each_with_index)
{id: array-iterate}
{i: each}
{i: each_with_index}

![](examples/arrays/array_iterate.cr)

## Array push, append, <<
{id: arrays-push}
{i: push}
{i: append}
{i: <<}

![](examples/arrays/array_push.cr)

## Empty array
{id: array-empty}

* Empty array must come with a type definition

![](examples/arrays/empty_array.cr)

## Count digitis
{id: count-digits}

![](examples/arrays/count_digits.cr)

## Operations on arrays
{id: operations-on-arrays}

* add +
* repeat *

## Add arrays
{id: add-arrays}

![](examples/arrays/add.cr)
![](examples/arrays/add.out)

## Repeat arrays
{id: repeat-arrays}

![](examples/arrays/repeat.cr)
![](examples/arrays/repeat.out)

## Select (filter, grep)
{id: select}
{i: select}
{i: select!}
{i: filter}
{i: grep}

![](examples/arrays/select.cr)
![](examples/arrays/select.out)


## Reject (negative filter, grep)
{id: reject}
{i: reject}
{i: reject!}
{i: filter}
{i: grep}

* the `reject!` with the exlamation mark will modify the array
* the `reject` without the exlamation mark will only return the filtered array

![](examples/arrays/reject.cr)
![](examples/arrays/reject.out)


## Transform with map
{id: transform-with-map}
{i: map}

![](examples/arrays/map.cr)
![](examples/arrays/map.out)

## Sample from array
{id: arrays-sample}
{i: sample}

* Using [Random](random) behind the scenes.


![](examples/arrays/sample.cr)
![](examples/arrays/sample.out)


## Shuffle array
{id: arrays-shuffle}
{i: shuffle}

* Using [Random](random) behind the scenes.


![](examples/arrays/shuffle.cr)
![](examples/arrays/shuffle.out)


## join
{id: arrays-join}

![](examples/arrays/join.cr)
