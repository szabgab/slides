# Struct
{id: struct}

## Struct andln type
{id: struct-and-type}
{i: type}
{i: struct}

![](examples/struct-person/struct_person.go)
![](examples/struct-person/struct_person.out)

## Struct with partial information (default values)
{id: struct-with-partial-information}

![](examples/partial-struct/partial_struct.go)
![](examples/partial-struct/partial_struct.out)

## Slice of structs
{id: slice-of-structs}

![](examples/slice-of-struct/slice_of_struct.go)
![](examples/slice-of-struct/slice_of_struct.out)


## Anonymous struct
{id: anonymous-struct}

![](examples/anonymous-struct/anonymous_struct.go)
![](examples/anonymous-struct/anonymous_struct.out)

## Struct in a struct
{id: struct-in-a-struct}

![](examples/struct-in-a-struct/struct_in_a_struct.go)
![](examples/struct-in-a-struct/struct_in_a_struct.out)

## composition via embedding instead of inheritance
{id: composition}

![](examples/struct-compose/struct_compose.go)
![](examples/struct-compose/struct_compose.out)

## Tags and introspection (reflect)
{id: tags}
{i: reflect}
{i: TypeOf}

* We can add "free-text" tags to the elements of the struct, but it is better to use key-value pairs in there.
* We can use introspection to look at the content of the tags.

![](examples/struct-tags/struct_tags.go)
![](examples/struct-tags/struct_tags.out)

## methods
{id: methods}

* A method is a function execution in a known context.

![](examples/struct-methods/struct_methods.go)
![](examples/struct-methods/struct_methods.out)

## method of int
{id: method-of-int}

![](examples/method-of-int/method_of_int.go)
![](examples/method-of-int/method_of_int.out)

## map keys method
{id: map-keys-method}

![](examples/map-keys-method/map_keys_method.go)
![](examples/map-keys-method/map_keys_method.out)


## method gets copy of struct
{id: method-gets-copy-of-struct}

![](examples/method-gets-copy/method_gets_copy.go)
![](examples/method-gets-copy/method_gets_copy.out)

## method pass pointer of struct
{id: method-pass-pointer-of-struct}

![](examples/method-pass-pointer/method_pass_pointer.go)
![](examples/method-pass-pointer/method_pass_pointer.out)

## Exercise: read-csv-struct
{id: exercise-read-csv-struct}

* Take the following CSV file, read in the content into structs so that the latitude and longitude values are stored in `float64`.

![](examples/csv-struct/cities.csv)

## Exercise: implement 2D point and move
{id: exercise-implement-2d-point-and-move}

* Implement a function using a struct that can store x,y values representing a point.
* Then add a function called `move` that accepts dx and dy the distances the point needs to move and update the location of the point.

## Exercise: implement 3D point and move
{id: exercise-implement-3d-point-and-move}

* Improve the previous code by creating another struct that can handle points in 3D.


## Exercise: implement wc
{id: exercise-implement-wc}

Implement the wc command of Unix/Linux: Given a name of file print out the number of lines, number of words, and number of characters in the file.

Given multiple file, print out the values for each file and then print out the totals for all the files.

![](examples/wc/a.txt)

![](examples/wc/b.txt)

```
 2   5  24 a.txt
 3  11 100 b.txt
 5  16 124 total
```

## Solution: implement wc
{id: solution-implement-wc}

TODO: finish this

![](examples/wc/wc.go)

![](examples/wc/wc_test.go)