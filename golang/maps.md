# Maps
{id: maps}

## Map (hash, dictionary)
{id: map}
{i: map}

A `map` is an unordered datastructur of key-value pairs.

## Empty Map
{id: empty-map}
{i: map}

![](examples/map/map.go)

## Empty Map with make
{id: map-with-make}
{i: map}

![](examples/map-with-make/map_with_make.go)
![](examples/map-with-make/map_with_make.out)

## Map type defintion without container
{id: map-type-definition-without-container}

![](examples/map-no-container/map_no_container.go)
![](examples/map-no-container/map_no_container.out)

## Create map with data in it already
{id: map-with-data}

![](examples/map-with-data/map_with_data.go)

## Delete Map element
{id: delete-map-element}

![](examples/delete-key/delete_key.go)


## Size of map (len)
{id: size-of-map}

![](examples/size-of-map/size_of_map.go)
![](examples/size-of-map/size_of_map.out)

## Access map element (that does not exist)
{id: access-map-element}

* What happens when we access an element that does not exist?
* Go returns 0.
* So we can't know if the field exists and its value is 0 or if it does not exist at all. 

![](examples/access-map-element/access_map_element.go)
![](examples/access-map-element/access_map_element.out)

## Map element exists
{id: map-element-exists}

* The variable name `ok` is not speacial. It is just a convention.

![](examples/exists/exists.go)
![](examples/exists/exists.out)

## Increment map elements
{id: increment-map-elements}

![](examples/increment-map-element/increment_map_element.go)
![](examples/increment-map-element/increment_map_element.out)


## Iterate over elements of map
{id: iterate-over-elements-of-map}

![](examples/iterate-over-map/iterate_over_map.go)
![](examples/iterate-over-map/iterate_over_map.out)


## Keys of a map
{id: keys-of-map}
{i: keys}

* There is no function to fetch the list of keys.
* We can iterate over the keys and put them in an slice with pre-allocated size.

![](examples/keys-of-map/keys_of_map.go)
![](examples/keys-of-map/keys_of_map.out)

## Sort map
{id: sort-map}

* You can't really sort a map, but you can iterate over the keys in some sorted way.
* You just need to fetch the keys, sort them, and then iterate over that slice.

![](examples/sort-map/sort_map.go)
![](examples/sort-map/sort_map.out)


## Sort map by value
{id: sort-map-by-value}

![](examples/sort-map-by-value/sort_map_by_value.go)
![](examples/sort-map-by-value/sort_map_by_value.out)

## map of slices
{id: map-of-slices}

![](examples/map-of-slices/map_of_slices.go)
![](examples/map-of-slices/map_of_slices.out)


add entry
delete(map, name) delete entry


## Mixed map
{id: mixed-map}

![](examples/mixed-map/mixed_map.go)
![](examples/mixed-map/mixed_map.out)


## Exercise: count characters
{id: exercise-count-characters}

Given a string count how many time each character appears

![](examples/count-characters-skeleton/count_characters_skeleton.go)

Expected output:

![](examples/count-characters/count_characters.out)

## Exercise: count characters - sort by frequency
{id: exercise-count-characters-sort-by-frequency}

* Given a string count how many time each character appears and list them by frequency.
* Make the count case-insensitive (so "T" and "t" will count as the same letter.)

![](examples/count-characters-by-frequency-skeleton/count_characters_by_frequency_skeleton.go)

Expected output:

![](examples/count-characters-by-frequency/count_characters_by_frequency.out)


## Exercise: count words
{id: exercise-count-words}

![](examples/count-words-skeleton/count_words_skeleton.go)

Expected output:

```
hello: 1
world: 2
how: 2
are: 2
you: 2
and: 1
```

## Exercise: count words from file
{id: exercise-count-words-from-file}

Given a text file like this one:

![](examples/count-words-from-file/words_and_spaces.txt)

* Print out a report how many times each word appears.
* Disregard case of the letters.
* Show them in order of frequency.

![](examples/count-words-from-file/count_words_from_file.out)

## Solution: count characters
{id: solution-count-characters}

![](examples/count-characters/count_characters.go)

## Solution: count characters - sort by frequency
{id: solution-count-characters-sort-by-frequency}

![](examples/count-characters-by-frequency/count_characters_by_frequency.go)


## Solution: count words
{id: solution-count-words}

![](examples/count-words/count_words.go)

## Solution: count words from file
{id: solution-count-words-from-file}

![](examples/count-words-from-file/count_words_from_file.go)
