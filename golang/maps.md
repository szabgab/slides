# Maps
{id: maps}

## Map (hash, dictionary)
{id: map}

![](examples/map/map.go)

* [Mutating maps](https://tour.golang.org/moretypes/22)


## Iterate over elements of map
{id: iterate-over-elements-of-map}

![](examples/iterate-over-map/iterate_over_map.go)

## Map with data
{id: map-with-data}

![](examples/map-with-data/map_with_data.go)

## Delete Map element
{id: delete-map-element}

![](examples/delete-key/delete_key.go)

## Size of map (len)
{id: size-of-map}

![](examples/size-of-map/size_of_map.go)
![](examples/size-of-map/size_of_map.out)


## Sort map
{id: sort-map}

![](examples/sort-map/sort_map.go)
![](examples/sort-map/sort_map.out)

## Map element exists
{id: map-element-exists}

![](examples/exists/exists.go)

## Exercise: count characters
{id: exercise-count-characters}

Given a string count how many time each character appears

![](examples/count-characters-skeleton/count_characters_skeleton.go)

Expected output:

![](examples/count-characters/count_characters.out)

## Exercise: count characters - sort by frequency
{id: exercise-count-characters-sort-by-frequency}

Given a string count how many time each character appears and list them by frequency:

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


## Solution: count characters
{id: solution-count-characters}

![](examples/count-characters/count_characters.go)

## Solution: count characters - sort by frequency
{id: solution-count-characters-sort-by-frequency}

![](examples/count-characters-by-frequency/count_characters_by_frequency.go)


## Solution: count words
{id: solution-count-words}

![](examples/count-words/count_words.go)

## map of slices
{id: map-of-slices}

![](examples/map-of-slices/map_of_slices.go)
![](examples/map-of-slices/map_of_slices.out)


create with content
create empty, with without make
add entry
delete(map, name) delete entry
what happens when we access an element that does not exist?
pop = mymap[name]
pop, ok = mymap[name]
len(mymap)
