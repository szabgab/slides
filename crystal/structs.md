# Structs
{id: structs}

## Empty struct
{id: empty-struct}
{i: struct}

{aside}
Structs are very powerful constructs in Crystal. Very similar to classes, but they are usually faster.

In the first example we create an empty struct. It does not give as a lot, but we have to start somewhere.
{/aside}

* [Struct API](https://crystal-lang.org/api/Struct.html)
* [Struct reference](https://crystal-lang.org/reference/syntax_and_semantics/structs.html)
* [use structs when possible](https://crystal-lang.org/reference/guides/performance.html#use-structs-when-possible)

![](examples/struct/empty_struct.cr)
![](examples/struct/empty_struct.out)

## Initialize immutable struct
{id: struct-initialize}
{i: initialize}

{aside}
A more realistic example is a struct that has a method called `initialize` that can be used to set the
attributes of the struct. Each variable with a single `@` sign in-front of it is an attribute.

We can initialize some of the attributes by values received from the user and some attributes by generating
the value ourseves. e.g. by using a Time object, a Random value or generating or computing it in any other way.

We can print the content of the Struct, but we have no way to access the attributes and no way to change them.
Hence this struct is immutable.
{/aside}

* There is no way to change this struct
* There is no way to access the individual attributes as there are no getters

![](examples/struct/initialize_struct.cr)
![](examples/struct/initialize_struct.out)

## Initialize immutable struct - shorthand
{id: struct-initialize-shorthand}

{aside}
Writing each attribute name 3 times is quite annoying, luckily Crystal provides a shorthand writing mode.
{/aside}

![](examples/struct/initialize_struct_shorthand.cr)
![](examples/struct/initialize_struct_shorthand.out)

## Immutable struct with getters
{id: struct-immutable-with-getters}

{aside}
We can defined methods in the struct to become the getters of the attributes, but this too is boring.
{/aside}

![](examples/struct/immutable_struct_with_getter.cr)
![](examples/struct/immutable_struct_with_getter.out)

## Immutable struct with getter macro
{id: struct-immutable-with-getter-macro}

{aside}
We can use the `getter` macro to create getters to all of the attributes.
{/aside}

* [macros on Object](https://crystal-lang.org/api/Object.html)

![](examples/struct/immutable_struct_with_getter_macro.cr)
![](examples/struct/immutable_struct_with_getter_macro.out)

## Mutable Struct with setter
{id: struct-mutable-with-setter}

![](examples/struct/mutable_struct_with_setter.cr)
![](examples/struct/mutable_struct_with_setter.out)

## Mutable Struct with propery macro
{id: struct-mutable-with-property-macro}

* [macros on Object](https://crystal-lang.org/api/Object.html)

![](examples/struct/mutable_struct_with_property_macro.cr)
![](examples/struct/mutable_struct_with_property_macro.out)

## Struct with optional attributes
{id: struct-optional}

![](examples/struct/struct_optional.cr)
![](examples/struct/struct_optional.out)

## Struct with default value
{id: struct-with-deefault}

![](examples/struct/with_default_value.cr)
![](examples/struct/with_default_value.out)

## Struct pass-by-value
{id: struct-pass-by-value}

{aside}
For immutable structs this is not relevant but when the struct is mutable you have to remember that it is passed by value to functions.
That is, the function receives a copy of the external struct. Any changes made to the struct inside the function will be lost
when you leave the function.
{/aside}

![](examples/struct/struct_pass_by_value.cr)
![](examples/struct/struct_pass_by_value.out)

## Struct from JSON
{id: struct-from-json}
{i: JSON::Serializable}

* [JSON::Serializable](https://crystal-lang.org/api/JSON/Serializable.html)

![](examples/struct/struct_from_json.cr)
![](examples/struct/struct_from_json.out)

## Struct both from JSON and initialize
{id: struct-from-json-and-initialize}
{i: initialize}

![](examples/struct/struct_initialize_and_from_json.cr)
![](examples/struct/struct_initialize_and_from_json.out)

## Struct from JSON - manual parsing
{id: struct-from-json-manual-parsing}
{i: include}
{i: JSON::PullParser}

* [JSON::PullParser](https://crystal-lang.org/api/JSON/PullParser.html)

![](examples/struct/struct_from_json_pull_parser.cr)
![](examples/struct/struct_from_json_pull_parser.out)

## Multi-level struct manually
{id: struct-multi-level-manually}

![](examples/struct/multi_level_struct_manually.cr)
![](examples/struct/multi_level_struct_manually.out)

## Multi-level struct from JSON
{id: struct-multi-level-from-json}

![](examples/struct/multi_level_struct_from_json.cr)
![](examples/struct/multi_level_struct_from_json.out)

## Struct from JSON with extra data
{id: struct-from-json-with-extra-data}

![](examples/struct/struct_from_json_extra_data.cr)
![](examples/struct/struct_from_json_extra_data.out)

## Struct from JSON missing data (optionl fields)
{id: struct-from-json-missing-data}

![](examples/struct/struct_from_json_missing_data.cr)
![](examples/struct/struct_from_json_missing_data.out)


## Extend struct
{id: struct-extend-struct}

![](examples/struct/extend_struct.cr)
![](examples/struct/extend_struct.out)

## Extend other structs
{id: struct-extend-other-structs}

![](examples/struct/integers.cr)


